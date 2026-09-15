"""Generate an image and save it to ./output/generated.png."""

from __future__ import annotations

import base64
import os
import sys
from pathlib import Path

import httpx
from openai import OpenAI


def main() -> None:
    api_key = os.environ.get("TOKENAAS_API_KEY")
    if not api_key:
        print("Set TOKENAAS_API_KEY first.", file=sys.stderr)
        sys.exit(1)

    client = OpenAI(
        api_key=api_key,
        base_url=os.environ.get("TOKENAAS_BASE_URL", "https://tokenaas.ai/v1"),
        timeout=120.0,
        max_retries=1,
    )

    model = os.environ.get("TOKENAAS_IMAGE_MODEL", "Doubao-Seedream-4.5")
    result = client.images.generate(
        model=model,
        prompt="A quiet tropical beach at sunset, realistic photography",
        size="2048x2048",
        n=1,
    )

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "generated.png"

    item = result.data[0]
    b64 = getattr(item, "b64_json", None)
    url = getattr(item, "url", None)

    if b64:
        out_path.write_bytes(base64.b64decode(b64))
    elif url:
        with httpx.Client(timeout=120.0) as http:
            response = http.get(url)
            response.raise_for_status()
            out_path.write_bytes(response.content)
    else:
        print("No image payload in response.", file=sys.stderr)
        sys.exit(1)

    print(f"Saved {out_path.resolve()}")


if __name__ == "__main__":
    main()
