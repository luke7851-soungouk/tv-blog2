# tv-blog2

매일 한국시간 오전 8시에 오늘 방송되는 지상파 TV 프로그램 정보를 웹에서 확인하고, 네이버 블로그용 글을 자동으로 만드는 저장소입니다.

## 들어 있는 파일

- `main.py`: OpenAI 웹 검색을 사용해 오늘의 방송 정보를 확인하고 글을 생성합니다.
- `prompt.txt`: 네이버 블로그 글 작성 기준입니다.
- `.github/workflows/tv-blog.yml`: 매일 자동 실행하는 GitHub Actions입니다.
- `output/latest.md`: 가장 최근에 생성된 글입니다.

## 처음 한 번만 해야 하는 설정

1. 저장소에서 `Settings`를 누릅니다.
2. `Secrets and variables` → `Actions`로 들어갑니다.
3. `New repository secret`을 누릅니다.
4. 이름은 `OPENAI_API_KEY`로 입력합니다.
5. 값에는 본인의 OpenAI API 키를 붙여 넣고 저장합니다.

## 직접 실행하기

저장소의 `Actions` 탭에서 `오늘의 TV 네이버 블로그 글 만들기`를 선택한 뒤 `Run workflow`를 누릅니다.

생성된 글은 `output/latest.md`에서 확인할 수 있습니다.

> 이 자동화는 네이버에 직접 게시하지 않고, 복사해서 붙여 넣을 수 있는 글을 생성합니다.
