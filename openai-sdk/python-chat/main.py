"""Non-streaming chat completion via the OpenAI Python SDK."""

from __future__ import annotations

import os
import sys

from openai import OpenAI


def main() -> None:
    api_key = os.environ.get("TOKENAAS_API_KEY")
    if not api_key:
        print("Set TOKENAAS_API_KEY first.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(
        api_key=api_key,
        base_url=os.environ.get("TOKENAAS_BASE_URL", "https://tokenaas.ai/v1"),
        timeout=60.0,
        max_retries=2,
    )

    model = os.environ.get("TOKENAAS_TEXT_MODEL", "deepseek-v4-flash")
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Explain large language models in three sentences."}],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
