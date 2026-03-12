"""MACHINE-1.0 transpiler CLI.

Environment:
  MODEL_PROVIDER      gemini (default) | claude | openai
  CLAUDE_MODEL  default: claude-sonnet-4-6
  OPENAI_MODEL  default: gpt-4o
  GEMINI_MODEL  default: gemini-2.0-flash
  GEMINI_API_KEY  required for gemini provider
"""

import asyncio
from enum import Enum
from pathlib import Path
from typing import Annotated, Literal

import langcodes
import tenacity
import typer

from .. import util
from ..providers import DEFAULT_PROVIDER, PROVIDERS, RETRYABLE_ERRORS
from ..spec import LANGUAGE_CODES, NodeType


def prompt(node_type: str, lang: str, text: str) -> str:
    lang_name = langcodes.get(lang).display_name()
    peer_warning = (
        "\n- Prepend a [!WARNING] callout stating that lossless parity cannot be "
        "guaranteed in non-English output at Peer density."
        if node_type == "peer" and lang != "en"
        else ""
    )

    return f"""
{util.package_text("machine.md")}

---

You are a transpiler for Machine 1.0 (MACHINE-1.0).

Transpile the below for a **{node_type}** node in **{lang_name}**.

Universal rules (normative):
- Output entirely in {lang_name}. All prose MUST be translated.
- Technical keywords (MUST, MAY, ASSERT, IRQ, SYN, DAMP, etc.) MUST NOT be translated.
- Structural syntax and keywords inside code blocks MUST NOT be translated.
- Mermaid diagram strings MUST be translated; node IDs and arrows MUST NOT.
- Crude language MUST NOT be softened for subject, student, or peer outputs.{peer_warning}

Output a complete Markdown document. No preamble or commentary outside the document.

---

{text}
"""


@tenacity.retry(
    wait=tenacity.wait_exponential(multiplier=1, min=2, max=60),
    stop=tenacity.stop_after_attempt(5),
    retry=tenacity.retry_if_exception_type(RETRYABLE_ERRORS),
)
async def transpile(
    target_node: str, lang: str, source: str, *, provider=DEFAULT_PROVIDER
):
    async with util.MODEL_SEMAPHORE:
        return await PROVIDERS[provider](prompt(target_node, lang, source))


def _languages_callback(value: bool) -> None:
    if value:
        typer.echo(" ".join(LANGUAGE_CODES))
        raise typer.Exit()


def _node_types_callback(value: bool) -> None:
    if value:
        typer.echo(" ".join((node.value for node in NodeType)))
        raise typer.Exit()


main = typer.Typer(help=__doc__)


@main.command()
def _main(
    node_type: Annotated[NodeType, typer.Argument(help="Target node type")],
    lang: Annotated[
        Literal[*LANGUAGE_CODES], typer.Argument(help="ISO 639-1/3 language code")
    ],
    source: Annotated[Path, typer.Argument(help="Source")],
    provider: Annotated[
        Literal[*PROVIDERS.keys()], typer.Argument(help="Provider name")
    ] = DEFAULT_PROVIDER,
    languages: Annotated[
        bool,
        typer.Option(
            "--languages",
            help="Print supported language codes and exit.",
            callback=_languages_callback,
            is_eager=True,
        ),
    ] = False,
    node_types: Annotated[
        bool,
        typer.Option(
            "--node-types",
            help="Print supported node types and exit.",
            callback=_node_types_callback,
            is_eager=True,
        ),
    ] = False,
) -> None:
    if node_type is NodeType.newborn:
        # newborn: L1 signal only — no L3 text output.
        typer.echo("N/A")
    else:
        typer.echo(
            asyncio.run(
                transpile(
                    node_type.value,
                    lang,
                    source,
                    provider=provider,
                )
            )
        )


if __name__ == "__main__":
    main()
