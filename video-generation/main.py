"""Create a video task, poll status, and download the result."""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import httpx


def main() -> None:
    api_key = os.environ.get("TOKENAAS_API_KEY")
    if not api_key:
        print("Set TOKENAAS_API_KEY first.", file=sys.stderr)
        sys.exit(1)

    base = os.environ.get("TOKENAAS_BASE_URL", "https://tokenaas.ai/v1").rstrip("/")
    model = os.environ.get("TOKENAAS_VIDEO_MODEL", "Doubao-Seedance-2.0")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    with httpx.Client(timeout=120.0) as http:
        create = http.post(
            f"{base}/videos/generations",
            headers=headers,
            json={
                "model": model,
                "prompt": "A cinematic sunset over a calm ocean",
                "duration": 5,
                "resolution": "480p",
                "ratio": "16:9",
                "generate_audio": False,
                "watermark": False,
            },
        )
        create.raise_for_status()
        payload = create.json()
        task_id = payload.get("id") or payload.get("task_id")
        if not task_id:
            print(f"Unexpected create response: {payload}", file=sys.stderr)
            sys.exit(1)

        print(f"Created task {task_id}")

        status = "pending"
        for _ in range(120):
            time.sleep(5)
            poll = http.get(f"{base}/videos/generations/{task_id}", headers=headers)
            poll.raise_for_status()
            body = poll.json()
            status = body.get("status") or body.get("data", {}).get("status")
            print(f"status={status}")
            if status in {"succeeded", "failed", "canceled", "expired"}:
                break

        if status != "succeeded":
            print(f"Task ended with status={status}", file=sys.stderr)
            sys.exit(1)

        out_dir = Path("output")
        out_dir.mkdir(exist_ok=True)
        out_path = out_dir / "result.mp4"
        download = http.get(
            f"{base}/videos/generations/{task_id}/content",
            headers={"Authorization": f"Bearer {api_key}"},
            follow_redirects=True,
        )
        download.raise_for_status()
        out_path.write_bytes(download.content)
        print(f"Saved {out_path.resolve()}")


if __name__ == "__main__":
    main()
