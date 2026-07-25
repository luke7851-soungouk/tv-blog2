from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from openai import OpenAI


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output"
PROMPT_FILE = ROOT / "prompt.txt"


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY GitHub Secret가 설정되지 않았습니다.")

    model = os.getenv("OPENAI_MODEL", "gpt-5.5")
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    today = now.strftime("%Y년 %m월 %d일 %A")
    base_prompt = PROMPT_FILE.read_text(encoding="utf-8")

    request = f"""{base_prompt}

오늘은 {today}입니다.
현재 한국 시간은 {now.strftime('%H:%M')}입니다.
오늘 실제 방송 정보를 다시 검색해서 글을 작성하세요.
"""

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        tools=[
            {
                "type": "web_search",
                "user_location": {
                    "type": "approximate",
                    "country": "KR",
                    "timezone": "Asia/Seoul",
                },
            }
        ],
        input=request,
    )

    article = response.output_text.strip()
    if not article:
        raise RuntimeError("생성된 블로그 글이 비어 있습니다.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    dated_file = OUTPUT_DIR / f"tv-blog-{now.strftime('%Y-%m-%d')}.md"
    latest_file = OUTPUT_DIR / "latest.md"

    header = (
        f"<!-- 자동 생성: {now.isoformat()} / 모델: {model} -->\n\n"
    )
    dated_file.write_text(header + article + "\n", encoding="utf-8")
    latest_file.write_text(header + article + "\n", encoding="utf-8")

    print(f"작성 완료: {dated_file}")


if __name__ == "__main__":
    main()
