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

import yaml

import jsonschema


def _literal_str_representer(dumper: yaml.Dumper, data: str) -> yaml.ScalarNode:
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


yaml.add_representer(str, _literal_str_representer)
import tenacity
import typer

from .. import util
from ..providers import DEFAULT_PROVIDER, PROVIDERS, RETRYABLE_ERRORS


def prompt(text: str) -> str:
    schema = util.package_text("standard.schema.json")
    return f"""
{util.package_text("machine.md")}

---

You are a compiler for Machine 1.0 (MACHINE-1.0). Extract a structured engineering standard from the document below and output a JSON object that strictly conforms to the following JSON Schema:

{schema}

Key constraints:
- Output raw JSON only — no markdown fences, no preamble, no commentary.
- `metadata.status` must be one of: COMMITTED, DEPRECATED, DRAFT, IMMUTABLE
- `standard.base_class` must be one of: Apostolic_Engineering, Universal_Law
- `standard.uid` must match ^[A-Z]+-[0-9]+$
- `standard.version` must match ^[0-9]+\\.[0-9]+\\.[0-9]+
- `machine_session` MUST be present. Write a Machine IR session using the MACHINE-1.0 spec above:
  - Open with BEGIN_SESSION: and close with END_SESSION
  - Include TRANSPILATION_ID, SOURCE_NODE, TARGET_NODE, LOGIC_STRATEGY comments
  - Express the standard's core logic as ASSERT, REQUIRE, LOG, EXECUTE, PUSH_STRING, SET, and TERMINATE_SESSION statements
  - Semicolons are statement separators, not terminators: only use `;` when two statements appear on the same line
- `compliance_matrix` fields MUST have Machine IR values, not plain text:
  - l1_physical.requirement: an ASSERT or REQUIRE IR statement (e.g. "ASSERT: Transparency == MANDATORY")
  - l1_physical.status: a compliance keyword (e.g. "MANDATORY")
  - l1_physical.forbidden: array of IR token identifiers (e.g. ["Binary_Blobs", "Secret_Silicon"])
  - l2_data_link.interrupt: an IRQ token (e.g. "IRQ_0")
  - l2_data_link.trigger: the condition that fires the interrupt (e.g. "Obfuscation_Detected")
  - l2_data_link.action: an EXECUTE IR statement (e.g. "HALT_AND_CATCH_FIRE")
  - l3_network.protocol: a protocol token (e.g. "RFC_2119_STRICT")
  - l3_network.integrity: an integrity assertion (e.g. "Lossless_Transpilation")

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
    data = json.loads(raw)
    jsonschema.validate(data, json.loads(util.package_text("standard.schema.json")))
    typer.echo(yaml.dump(data, allow_unicode=True, sort_keys=False), nl=False)


if __name__ == "__main__":
    main()
