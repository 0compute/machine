"""LLM provider backends for transpilation."""

import os
from functools import cache, partial

from google import genai
from google.api_core import exceptions as google_exceptions
import anthropic
import openai


RETRYABLE_ERRORS = (
    anthropic.RateLimitError,
    anthropic.InternalServerError,
    anthropic.APITimeoutError,
    google_exceptions.TooManyRequests,
    google_exceptions.InternalServerError,
    google_exceptions.ServiceUnavailable,
    openai.RateLimitError,
    openai.InternalServerError,
    openai.APITimeoutError,
)

DEFAULT_PROVIDER = "gemini"

MODELS = dict(
    claude=os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5"),
    gemini=os.environ.get("GEMINI_MODEL", "gemini-3.0-flash"),
    openai=os.environ.get("OPENAI_MODEL", "gpt-5-mini"),
)

CLIENTS = dict(
    claude=cache(anthropic.AsyncAnthropic),
    gemini=cache(partial(genai.Client, api_key=os.environ["GEMINI_API_KEY"])),
    openai=cache(openai.AsyncOpenAI),
)


async def _claude(prompt: str) -> str:
    return (
        (
            await CLIENTS["claude"]().messages.create(
                model=MODELS["claude"],
                max_tokens=8096,
                messages=[{"role": "user", "content": prompt}],
            )
        )
        .content[0]
        .text
    )


async def _gemini(prompt: str) -> str:
    return (
        await CLIENTS["gemini"]().aio.models.generate_content(
            model=MODELS["gemini"],
            contents=prompt,
        )
    ).text


async def _openai(prompt: str) -> str:
    return (
        (
            await CLIENTS["openai"]().chat.completions.create(
                model=MODELS["openai"],
                messages=[{"role": "user", "content": prompt}],
            )
        )
        .choices[0]
        .message.content
    )


PROVIDERS = dict(
    claude=_claude,
    gemini=_gemini,
    openai=_openai,
)
