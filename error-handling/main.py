"""Call TokenAAS with bounded retries and safe error reporting."""

from __future__ import annotations

import os
import sys
import time

from openai import APIConnectionError, APIStatusError, OpenAI, RateLimitError


def redact(value: str | None) -> str:
    if not value:
        return ""
    if len(value) <= 8:
        return "***"
    return f"{value[:4]}...{value[-4:]}"


def main() -> None:
    api_key = os.environ.get("TOKENAAS_API_KEY")
    if not api_key:
        print("Set TOKENAAS_API_KEY first.", file=sys.stderr)
        sys.exit(1)

    print(f"Using key {redact(api_key)}")

    client = OpenAI(
        api_key=api_key,
        base_url=os.environ.get("TOKENAAS_BASE_URL", "https://tokenaas.ai/v1"),
        timeout=60.0,
        max_retries=0,
    )
    model = os.environ.get("TOKENAAS_TEXT_MODEL", "deepseek-v4-flash")

    delays = (1, 2, 4)
    for attempt, delay in enumerate([0, *delays], start=1):
        if delay:
            time.sleep(delay)
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Reply with the word ok."}],
            )
            print(response.choices[0].message.content)
            return
        except RateLimitError as exc:
            print(f"attempt={attempt} rate_limited status={exc.status_code}", file=sys.stderr)
        except APIConnectionError as exc:
            print(f"attempt={attempt} connection_error={exc.__class__.__name__}", file=sys.stderr)
        except APIStatusError as exc:
            request_id = None
            if exc.response is not None:
                request_id = exc.response.headers.get("x-request-id") or exc.response.headers.get(
                    "x-oneapi-request-id"
                )
            print(
                f"attempt={attempt} status={exc.status_code} request_id={request_id} "
                f"body={exc.message}",
                file=sys.stderr,
            )
            if exc.status_code and 400 <= exc.status_code < 500 and exc.status_code != 429:
                sys.exit(1)

    print("Exhausted retries.", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
