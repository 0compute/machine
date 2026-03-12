"""MACHINE-1.0 standard compiler CLI.

Compiles a text document to a JSON object conforming to standard.schema.json.

Environment:
  MODEL_PROVIDER      gemini (default) | claude | openai
  CLAUDE_MODEL        default: claude-haiku-4-5
  OPENAI_MODEL        default: gpt-5-mini
  GEMINI_MODEL        default: gemini-3.0-flash
  GEMINI_API_KEY      required for gemini provider
"""

import asyncio
import json
from pathlib import Path
from typing import Annotated, Literal

import jsonschema
import tenacity
import typer

from .. import util
from ..providers import DEFAULT_PROVIDER, PROVIDERS, RETRYABLE_ERRORS


def prompt(text: str) -> str:
    schema = util.package_text("standard.schema.json")
    return f"""
{util.package_text("machine.md")}

---

You are a compiler for Machine 1.0 (MACHINE-1.0) extracts a structured engineering standard from a document.

Given the document below, output a YAML document that strictly conforms to the following JSON Schema:

{schema}

Key constraints:
- Output raw JSON only — no markdown fences, no preamble, no commentary.

---

{text}
"""


def _strip_fences(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[-1]
        text = text.rsplit("```", 1)[0]
    return text.strip()


@tenacity.retry(
    wait=tenacity.wait_exponential(multiplier=1, min=2, max=60),
    stop=tenacity.stop_after_attempt(5),
    retry=tenacity.retry_if_exception_type(RETRYABLE_ERRORS),
)
async def compile(text: str, *, provider=DEFAULT_PROVIDER) -> str:
    async with util.MODEL_SEMAPHORE:
        raw = await PROVIDERS[provider](prompt(text))
        return _strip_fences(raw)


main = typer.Typer(help=__doc__)


@main.command()
def _main(
    source: Annotated[Path, typer.Argument(help="Source document")],
    provider: Annotated[
        Literal[*PROVIDERS.keys()], typer.Argument(help="Provider name")
    ] = DEFAULT_PROVIDER,
) -> None:
    text = source.read_text()
    raw = asyncio.run(compile(text, provider=provider))
    typer.echo(raw)
    data = json.loads(raw)
    jsonschema.validate(data, json.loads(util.package_text("standard.schema.json")))
    typer.echo(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
