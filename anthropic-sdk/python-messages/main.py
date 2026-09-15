"""Anthropic SDK pointed at TokenAAS /v1/messages."""

from __future__ import annotations

import os
import sys

from anthropic import Anthropic


def main() -> None:
    api_key = os.environ.get("TOKENAAS_API_KEY")
    if not api_key:
        print("Set TOKENAAS_API_KEY first.", file=sys.stderr)
        sys.exit(1)

    model = os.environ.get("TOKENAAS_ANTHROPIC_MODEL")
    if not model:
        print(
            "Set TOKENAAS_ANTHROPIC_MODEL to a model ID from GET /v1/models "
            "that supports the Anthropic protocol for your key.",
            file=sys.stderr,
        )
        sys.exit(1)

    client = Anthropic(
        api_key=api_key,
        base_url=os.environ.get("TOKENAAS_ANTHROPIC_BASE_URL", "https://tokenaas.ai"),
    )

    message = client.messages.create(
        model=model,
        max_tokens=512,
        messages=[{"role": "user", "content": "Hello"}],
    )

    block = message.content[0]
    print(getattr(block, "text", block))


if __name__ == "__main__":
    main()
