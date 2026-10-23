# MCP 연결 실전

원본: https://bizroasting.com/mcp-examples.html

---

MCP 연결 실전 | AI ROASTING           [본문으로 건너뛰기](https://bizroasting.com#main)

## 먼저, MCP가 뭔가요

3분개념

MCP(Model Context Protocol)는 AI 앱이 외부 도구에 접속하는 공용 규격입니다. 노트북에 USB-C 단자 하나만 있으면 충전기도 모니터도 꽂히듯, AI 앱은 MCP 하나로 여러 도구를 붙입니다.

MCP

AI에 끼우는 USB-C

Model Context Protocol

2024년 11월 Anthropic이 공개한 개방형 연결 규격. AI 앱과 외부 도구를 한 가지 방식으로 잇습니다.

 AI 앱Claude · ChatGPT
  꽂으면 바로 연결

MCP
 하나의 공용 규격

Google

카카오톡

DART 공시

한국 법령

텔레그램

Higgsfield

Liner 검색

예제 일곱 개모두 MCP

 어느 앱으로 따라 할까요

구글 지메일, 캘린더, 드라이브 연결하기

10분입문

 ▼

Gmail, Google Calendar, Google Drive 세 커넥터를 Claude에 붙여, 받은편지함의 메일, 캘린더의 일정, 드라이브의 문서·스프레드시트·PDF를 Claude가 직접 찾아 읽습니다.


① 사용자 지정 열기
 Claude Desktop을 열고 왼쪽 사이드바에서 사용자 지정(Customize)을 누릅니다.

- 새로 생성

- Artifacts

- 루틴

- 발송베타

- 사용자 지정1

- 더보기


② 커넥터 탭에서 탐색 누르기
 위쪽 탭에서 커넥터를 고르고, 옆의 탐색을 누릅니다. 아래 인기 커넥터에 Google Drive, Gmail, Google Calendar가 보입니다. 안 보이면 오른쪽 검색창에 이름을 입력합니다.

사용자 지정

 스킬 커넥터2 플러그인

내 항목탐색

커넥터 검색

인기 커넥터

  Google DriveSearch, read, and upload files제작: Google +3

  GmailDraft replies, summarize threads제작: Google +3

  Google CalendarManage your schedule제작: Google +3

  NotionSearch and update your workspace제작: Notion +

연결이 끝나면 + 자리가 초록 체크로 바뀝니다

 ② 커넥터 → 탐색을 고르고, ③ 세 카드의 +를 누릅니다


④ Google 계정 로그인과 권한 동의
 열린 창에서 Google 계정으로 로그인하고 접근 권한에 동의합니다. 세 커넥터 모두 같은 계정으로 로그인합니다. 회사 구글 계정이면 관리자가 커넥터를 열어두어야 이 화면이 끝까지 넘어갑니다.


⑤ 연결 확인
 오늘 내 구글 캘린더 일정을 알려주고, 일정마다 관련된 최근 Gmail 메일과 구글 드라이브 문서를 찾아 한 줄씩 정리해줘. 새 대화에서 위 질문을 그대로 보냅니다. 일정, 메일, 문서가 함께 나오면 세 커넥터가 모두 연결된 것입니다.


① 왼쪽 네 번째 버튼 누르기
 Codex 앱 왼쪽 세로 버튼 줄의 네 번째 버튼을 누르면 맞춤 설정이 열립니다.

  1

맞춤 설정

- 플러그인2

- 스킬

설치됨

- Google Contacts

- Google Drive

- Google Calendar

- Gmail

- Plugin Creator

 ① 왼쪽 네 번째 버튼을 누르고 ② 플러그인을 고릅니다. 설치한 플러그인은 설치됨 아래에 보입니다


② 플러그인 고르기
 맞춤 설정 맨 위의 플러그인을 누릅니다. 플러그인 화면이 열립니다.


③ Gmail, Google Drive, Google Calendar 추가
 인기 목록의 Gmail과 Google Drive 오른쪽 +를 누릅니다. Google Calendar는 플러그인 검색에 입력해 찾아 같은 방법으로 추가합니다.

플러그인

플러그인 검색3
 추가 ▾

사용 중인 여러 도구에서 Codex가 작업할 수 있도록 플러그인을 연결하세요

공개개인용

인기 ›

GmailRead and manage Gmail+3

Remote Desktop CommanderBuild and automate, anywhere+

Google DriveDrive, Docs, Sheets or Slides+3

GitHubTriage PRs, issues, CI, and publish flows···

Outlook EmailTriage Outlook inboxes+

WPVibeAI WordPress tools+

 ③ Gmail과 Google Drive의 +를 누르고, Google Calendar는 검색창에 입력해 찾습니다


④ Google 계정 로그인과 권한 동의
 열린 창에서 Google 계정으로 로그인하고 접근 권한에 동의합니다. 세 플러그인 모두 같은 계정으로 로그인합니다.


⑤ 연결 확인
 오늘 내 구글 캘린더 일정을 알려주고, 일정마다 관련된 최근 Gmail 메일과 구글 드라이브 문서를 찾아 한 줄씩 정리해줘. Codex 앱에서 새 스레드를 열고 위 질문을 보냅니다. 일정, 메일, 문서가 함께 나오면 세 플러그인이 모두 연결된 것입니다.

카카오톡 PlayMCP 연결하기

12분중급

 ▼

먼저 playmcp.kakao.com에서 회원가입하고 도구함에 쓸 도구를 담은 다음, Claude Desktop에 PlayMCP 커넥터를 붙입니다.


① PlayMCP에 카카오 계정으로 로그인
 [playmcp.kakao.com](https://playmcp.kakao.com)에 접속해 카카오 계정으로 로그인합니다. 카카오톡을 쓰는 계정이면 회원가입 없이 바로 들어갑니다.


② 도구함에 쓸 도구 담기
 로그인하면 도구함이 보입니다. 여기에 쓸 도구를 먼저 담아 둡니다. 아래 카카오톡 나챗방은 반드시 담습니다.

 카카오톡 나챗방 + 도구함에 추가2


③ 사용자 지정 열기
 Claude Desktop을 열고 왼쪽 사이드바에서 사용자 지정(Customize)을 누릅니다.

- 새로 생성

- Artifacts

- 루틴

- 발송베타

- 사용자 지정3

- 더보기


④ 커넥터에서 playmcp 검색해 추가
 위쪽 탭에서 커넥터를 고르고, 오른쪽 검색창에 playmcp를 입력합니다. 나온 PlayMCP 카드의 +를 누르고 연결을 누릅니다.

사용자 지정

 스킬 커넥터4 플러그인

내 항목탐색

playmcp×4

  PlayMCPConnect and use PlayMCP servers in your toolbox제작: KAKAO +4

연결이 끝나면 + 자리가 초록 체크로 바뀝니다

 ④ 커넥터를 고르고 검색창에 playmcp를 입력한 뒤, 카드의 +를 누릅니다


⑤ 카카오 계정 로그인과 권한 동의
 연결 창에서 카카오 계정으로 로그인하고 권한에 모두 동의합니다. 이러면 준비가 끝납니다.


⑥ 연결 확인
 카톡으로 "MCP 연결 완료"라고 보내줘. 새 대화에서 위 메시지를 보냅니다. 카카오톡 나와의 채팅방에 그대로 도착하면 연결된 것입니다.

Liner 검색 MCP 연결하기

8분입문

 ▼

Liner의 원격 MCP 서버를 붙여, AI가 출처가 달린 웹 검색과 논문 검색, 딥 리서치를 Liner로 돌립니다. 법률·금융·의료·기업 분야 검색도 따로 부를 수 있습니다. 답마다 근거 링크가 따라오므로 보고서에 옮기기 전에 원문을 바로 확인합니다. 키를 붙여넣지 않고 Liner 계정으로 로그인만 하면 연결됩니다.
 [Liner MCP 공식 문서 · liner.com/ko/developers/docs/mcp ›](https://liner.com/ko/developers/docs/mcp)

MCP로 부른 검색도 Liner API를 직접 부를 때와 똑같이 사용량이 과금됩니다. 크레딧이 모자라면 검색이 실패하니 platform.liner.com/billing에서 잔액을 먼저 확인합니다.

Webvs.Liner

기본 웹서치와 Liner, 무엇이 다른가

웹 검색 없는 모델 정확도SimpleQA Verified · 1,000문항 · 2026.10.10

GPT-6 AstraOpenAI75.8%

Gemini 4 ArgonGoogle75.6%

GPT-6.1 SolOpenAI73.8%

Claude Opus 5Anthropic63.3%

Grok 4.7xAI59.4%

Claude Sonnet 5.5Anthropic44.7%

Claude Haiku 5.5Anthropic23.9%

Claude + 기본 웹서치원본 SimpleQA 기준90.5%

맨 아래 줄은 문항 세트가 달라 직접 비교용이 아닌 참고값입니다(Firecrawl 측정, 2026.07). Claude Opus 5.5·Fable 5.1은 리더보드 미등재.

기본 웹서치Liner MCP

검색 범위일반 웹 검색웹 검색 + 논문 전용 검색search_scholar

분야별 검색별도 도구 없음법률·금융·의료·기업 전용 4종search_legal 등

심층 리서치기본 검색 기능다단계 딥 리서치 에이전트deep_research_agent

앱 간 일관성앱마다 다른 검색 엔진Claude·Codex·Cursor에서 동일

비용·설정구독에 포함, 설정 불필요사용량 과금, 커넥터 1회 설정

정리단순 사실 확인은 기본 웹서치로 충분합니다. 논문, 분야별 자료, 출처 목록이 필요한 리서치에서 Liner를 연결합니다.


① 커넥터 화면에서 추가 누르기
 사용자 지정 → 커넥터 → 오른쪽 위 + 추가 Claude Desktop 왼쪽 사이드바에서 사용자 지정을 열고 위쪽 탭에서 커넥터를 고릅니다. 오른쪽 위 + 추가를 눌러 커스텀 커넥터 추가 창을 엽니다.


② 이름과 MCP 서버 URL 넣고 계속
 이름 liner MCP 서버 URL https://platform.liner.com/api/v1/mcp 이름 칸과 MCP 서버 URL 칸에 위 값을 그대로 붙이고 계속을 누릅니다. 주소 뒤에 키를 붙이지 않습니다. 인증은 다음 단계의 로그인이 맡습니다.

커스텀 커넥터 추가×

Claude를 데이터와 도구에 연결하세요.

liner1

커넥터 목록에 표시됩니다.

https://platform.liner.com/api/v1/mcp2

서버가 MCP 요청을 수락하는 HTTPS 주소입니다.

신뢰할 수 있는 개발자의 커넥터만 사용하세요.

취소계속3

 1 이름과 2 MCP 서버 URL을 넣고 3 계속을 누릅니다


③ Liner 로그인
 계속을 누르면 브라우저에 Liner 로그인 창이 열립니다. 바로 열리지 않으면 커넥터 목록의 liner에서 연결을 누릅니다. 로그인하고 동의한 뒤, 이 연결에 쓸 API 키를 고르고 접근을 허용합니다. 키가 아직 없으면 그 화면에서 바로 만들면 됩니다. 키나 토큰을 채팅에 붙이지 않습니다. 연결 정보는 로그인 과정에서 Claude가 받아 보관합니다. 처음부터 있는 Default 키는 Playground 전용이라 목록에 나오지 않습니다. 고른 키를 나중에 폐기하면 연결도 바로 끊깁니다.


④ 도구 확인
 연결되면 search_web(웹 검색), search_scholar(논문 검색), search_legal, search_finance, search_medical, search_business(법률·금융·의료·기업 분야 검색), quick_answer_agent(짧은 사실 확인), search_agent(출처를 단 종합 답), deep_research_agent(여러 단계 리서치) 같은 도구가 보입니다. 바로 안 보이면 Claude Desktop을 다시 열거나 잠시 뒤 확인합니다.


⑤ 첫 검색 테스트
 Liner로 최근 AI 검색 서비스 동향을 찾아서, 출처 링크를 단 5줄 요약으로 정리해줘. Claude Desktop에서 새 대화를 열고 위 질문을 보냅니다. 문장마다 출처 링크가 달려 나오면 연결된 것입니다. 논문이 필요하면 "Liner 논문 검색으로"라고 덧붙입니다.


① 플러그인 화면에서 추가 누르기
 왼쪽 네 번째 버튼 → 맞춤 설정 → 플러그인 → 오른쪽 위 추가 Codex 앱 왼쪽 세로 버튼 줄의 네 번째 버튼으로 맞춤 설정을 열고 플러그인을 고릅니다. 오른쪽 위 추가를 눌러 사용자 지정 MCP 서버 만들기 창을 엽니다.


② 이름과 서버 URL 넣고 플러그인으로 만들기
 이름 liner 연결 · 서버 URL https://platform.liner.com/api/v1/mcp 이름 칸과, 연결의 서버 URL 탭 주소 칸에 위 값을 그대로 붙입니다. 설명은 비워 둬도 되고, 인증은 기본값 OAuth 그대로 둡니다. 이해했으며 계속 진행하겠습니다에 체크하고 플러그인으로 만들기를 누릅니다.

사용자 지정 MCP 서버 만들기×

이름

liner1

설명(선택 사항)

앱의 기능을 간단히 설명하세요

연결

서버 URL터널

https://platform.liner.com/api/v1/mcp2

인증

OAuth

⚠︎ 사용자 지정 MCP 서버에는 위험이 따릅니다.

이해했으며 계속 진행하겠습니다3

취소플러그인으로 만들기4

 1 이름과 2 서버 URL을 넣고, 3 체크한 뒤 4 플러그인으로 만들기를 누릅니다


③ Liner 로그인
 브라우저에 Liner 로그인 창이 열립니다. 바로 열리지 않으면 Liner를 처음 쓸 때 열립니다. 로그인하고 동의한 뒤, 이 연결에 쓸 API 키를 고르고 접근을 허용합니다. 키가 아직 없으면 그 화면에서 바로 만들면 됩니다. 키나 토큰을 채팅에 붙이지 않습니다. 처음부터 있는 Default 키는 Playground 전용이라 목록에 나오지 않습니다. 고른 키를 나중에 폐기하면 연결도 바로 끊깁니다. 맞춤 설정의 설치됨 아래에 liner가 보이면 연결된 것입니다. search_web(웹 검색), search_scholar(논문 검색), search_legal, search_finance, search_medical, search_business(법률·금융·의료·기업 분야 검색), quick_answer_agent(짧은 사실 확인), search_agent(출처를 단 종합 답), deep_research_agent(여러 단계 리서치) 같은 도구를 쓸 수 있습니다.


④ 첫 검색 테스트
 Liner로 최근 AI 검색 서비스 동향을 찾아서, 출처 링크를 단 5줄 요약으로 정리해줘. Codex 앱에서 새 스레드를 열고 위 질문을 보냅니다. 문장마다 출처 링크가 달려 나오면 연결된 것입니다. 논문이 필요하면 "Liner 논문 검색으로"라고 덧붙입니다.

기업 공시 데이터 분석

12분중급

 ▼

GitHub에서 DART 공시 분석 스킬을 내려받아 Claude Code에 설치하면, /dart 종목명 한 줄로 그 기업의 재무와 공시를 분석한 HTML 리포트를 받습니다. 13인 투자자 페르소나 평가까지 담깁니다.
 [dart 스킬 · github.com/airoasting/dart ›](https://github.com/airoasting/dart)

이 예제는 터미널에서 claude로 켠 Claude Code 안에서 진행합니다. 설치는 자연어로 부탁하면 Claude가 알아서 받아 설치합니다.


① DART 스킬 설치
 https://github.com/airoasting/dart 다운로드 받은 다음, 클로드 스킬로 설치해주세요. Claude Code에 위 문장을 그대로 입력합니다. GitHub 주소를 받아 Claude가 알아서 내려받고 설치합니다.


② OpenDART API 키 받아 Claude에 알려주기
 [opendart.fss.or.kr](https://opendart.fss.or.kr)에 접속해 인증키 신청/관리 메뉴에서 인증키 신청을 눌러 신청합니다. 발급되면 오픈API 이용현황을 눌러 40자 키 값을 복사합니다.

인증키 신청/관리

- 인증키 신청1

- 인증키 관리

- 오픈API 이용현황2

 1 인증키 신청으로 신청하고, 2 오픈API 이용현황에서 키 값을 복사합니다
 이건 opendart API 값이야. 복사한_키_붙여넣기 Claude Code 채팅 창에 위 문장을 넣고, 복사한_키_붙여넣기 자리에 방금 복사한 키 값을 붙여 보냅니다. Claude가 키를 받아 프로젝트 .env에 저장합니다.


③ 리포트 생성
 /dart 카카오 Claude Code에서 /dart 종목명을 실행하면 output/ 폴더에 HTML 리포트가 만들어집니다.

GitHub에서 DART 공시 분석 스킬을 내려받아 Codex에 설치하면, $dart 종목명 한 줄로 그 기업의 재무와 공시를 분석한 HTML 리포트를 받습니다. 13인 투자자 페르소나 평가까지 담깁니다.
 [dart 스킬 · github.com/airoasting/dart ›](https://github.com/airoasting/dart)

이 예제는 Codex 앱에서 진행합니다. 설치는 자연어로 부탁하면 Codex가 알아서 받아 설치합니다.


① DART 스킬 설치
 https://github.com/airoasting/dart 다운로드 받은 다음, Codex 스킬로 설치해주세요. Codex 앱 새 스레드에 위 문장을 그대로 입력합니다. GitHub 주소를 받아 Codex가 알아서 내려받고 설치합니다. 승인 요청이 뜨면 허용합니다.


② OpenDART API 키 받아 Codex에 알려주기
 [opendart.fss.or.kr](https://opendart.fss.or.kr)에 접속해 인증키 신청/관리 메뉴에서 인증키 신청을 눌러 신청합니다. 발급되면 오픈API 이용현황을 눌러 40자 키 값을 복사합니다.

인증키 신청/관리

- 인증키 신청1

- 인증키 관리

- 오픈API 이용현황2

 1 인증키 신청으로 신청하고, 2 오픈API 이용현황에서 키 값을 복사합니다
 이건 opendart API 값이야. 복사한_키_붙여넣기 Codex 채팅 창에 위 문장을 넣고, 복사한_키_붙여넣기 자리에 방금 복사한 키 값을 붙여 보냅니다. Codex가 키를 받아 프로젝트 .env에 저장합니다.


③ 리포트 생성
 $dart 카카오 Codex에서 $dart 종목명을 입력하면 output/ 폴더에 HTML 리포트가 만들어집니다.

한국 법령 MCP 연결하기

15분중급

 ▼

korean-law 스킬과 MCP 서버를 내 컴퓨터에 설치해, AI가 쓴 계약서 검토 메모나 의견서의 조문·판례 인용을 법제처 원문과 대조합니다. 인용마다 실제로 있는지, 지금도 시행 중인지, 제목과 선고일이 맞는지 확인해 법률 근거 검증표와 통과·반려 판정을 냅니다. 법령과 판례를 찾아 읽는 도구도 함께 들어 있습니다.
 [korean-law 스킬·MCP · github.com/airoasting/korean-law ›](https://github.com/airoasting/korean-law)

내 컴퓨터에 Node.js 20.19 이상과 Python 3.9 이상이 있어야 합니다.


① 법제처 OC 키 발급
 [open.law.go.kr](https://open.law.go.kr)에 접속해 회원가입한 뒤 활용 신청을 하고, 마이페이지에서 OC 키를 확인합니다. OC 키는 사용자가 직접 입력한 값입니다. open.law.go.kr → OPEN API → 활용 신청 → 마이페이지


② Claude Desktop의 Code 탭 열기
 Claude Desktop → Code 탭 → 작업 폴더 선택


③ 설치 부탁하기
 https://github.com/airoasting/korean-law 를 설치해줘. 위 문장을 그대로 보냅니다. Claude가 저장소를 받고, 서버를 빌드하고, claude mcp add로 등록합니다. 명령 실행 허락을 물으면 허용합니다. 이건 법제처 OC 값이야. 복사한_키_붙여넣기 이어서 위 문장의 복사한_키_붙여넣기 자리에 ①에서 확인한 OC 키를 넣어 보냅니다. Claude가 키를 mcp/.env에 저장합니다.


④ 새 세션에서 연결 확인
 korean-law MCP 도구 목록을 보여줘. 등록한 서버는 새 세션부터 붙습니다. Code 탭에서 새 세션을 열고 위 질문을 보냅니다. find_law, read_law, find_decision, read_decision, check_precedent 같은 도구가 나오면 연결된 것입니다.


⑤ 첫 검증 테스트
 korean-law 스킬로 아래 두 문장의 법률 인용을 검증해줘. 1. 근로기준법 제60조(연차 유급휴가)에 따라 1년간 80퍼센트 이상 출근한 근로자에게 15일의 유급휴가를 주어야 한다. 2. 민사소송법 제272조(준비서면)에 따라 준비서면을 제출한다. 2번 인용이 조문 제목 불일치로 걸려 판정이 FAIL(반려)로 나오면 제대로 작동하는 것입니다. 민사소송법 제272조의 실제 제목은 '변론의 집중과 준비'입니다.


① 법제처 OC 키 발급
 [open.law.go.kr](https://open.law.go.kr)에 접속해 회원가입한 뒤 활용 신청을 하고, 마이페이지에서 OC 키를 확인합니다. OC 키는 사용자가 직접 입력한 값입니다. open.law.go.kr → OPEN API → 활용 신청 → 마이페이지


② Codex 앱에서 새 스레드 열기
 Codex 앱 → 작업 폴더 선택 → 새 스레드 Codex 데스크탑 앱을 열고 아무 작업 폴더나 고른 뒤 새 스레드를 엽니다.


③ 설치 부탁하기
 https://github.com/airoasting/korean-law 를 설치해줘. 위 문장을 그대로 보냅니다. Codex가 저장소를 받고, 서버를 빌드하고, ~/.codex/config.toml에 서버를 등록합니다. 승인 요청이 뜨면 허용합니다. 이건 법제처 OC 값이야. 복사한_키_붙여넣기 이어서 위 문장의 복사한_키_붙여넣기 자리에 ①에서 확인한 OC 키를 넣어 보냅니다. Codex가 키를 mcp/.env에 저장합니다. Codex 앱은 Codex CLI와 같은 설정 파일을 읽습니다. 그래서 여기서 등록한 서버가 앱에도 그대로 적용됩니다.


④ 앱을 다시 열고 연결 확인
 설정(Settings) → MCP servers → korean_law 켜짐 확인 Codex 앱을 완전히 종료했다가 다시 엽니다. 설정의 MCP servers 목록에 korean_law가 켜져 있으면 연결된 것입니다.


⑤ 첫 검증 테스트
 korean-law 스킬로 아래 두 문장의 법률 인용을 검증해줘. 1. 근로기준법 제60조(연차 유급휴가)에 따라 1년간 80퍼센트 이상 출근한 근로자에게 15일의 유급휴가를 주어야 한다. 2. 민사소송법 제272조(준비서면)에 따라 준비서면을 제출한다. 새 스레드에서 위 문장을 보냅니다. 2번 인용이 조문 제목 불일치로 걸려 판정이 FAIL(반려)로 나오면 제대로 작동하는 것입니다. 민사소송법 제272조의 실제 제목은 '변론의 집중과 준비'입니다.

Higgsfield 연결하기

8분입문

 ▼

Higgsfield의 원격 MCP 서버를 붙여, 대화창에서 바로 이미지와 영상을 만듭니다. 생성 말고도 업스케일과 배경 제거를 같은 계정으로 부릅니다. API 키 없이 Higgsfield 계정 로그인으로 인증합니다.
 [Higgsfield MCP 연결 페이지 · higgsfield.ai/mcp ›](https://higgsfield.ai/mcp)

Higgsfield 유료 구독이 있어야 연결되고, 이미지나 영상을 만들 때마다 Higgsfield 크레딧이 차감됩니다.


① Higgsfield 상단 메뉴에서 MCP 누르기
 [higgsfield.ai](https://higgsfield.ai/mcp)에 접속해 맨 위 메뉴에서 MCP를 누릅니다.


② Claude 탭에서 Higgsfield 연결하기 누르기
 Claude 탭을 고르고 Higgsfield 연결하기(영어 화면은 Connect Higgsfield)를 누릅니다.

둘러보기이미지비디오오디오MCP1API

ChatGPT 확장 프로그램ChatGPT 플러그인Claude2Claude CodeCLI··· 기타

이미지 & 비디오 생성하기CLAUDE 안에서 HIGGSFIELD와 함께

Higgsfield 연결하기2어떻게 연결하나요?

https://mcp.higgsfield.ai/mcp


③ 연결을 누르고 Higgsfield 로그인
 추가한 커넥터의 연결을 누르면 Higgsfield 로그인 창이 열립니다. Higgsfield 계정으로 로그인하고 접근을 허용합니다.


④ 연결 확인
 내 Higgsfield 크레딧 잔액이 얼마야? Claude Desktop에서 새 대화를 열고 위 질문을 보냅니다. 잔액이 숫자로 나오면 연결된 것입니다. 이 확인에는 크레딧이 들지 않습니다.


⑤ 첫 생성 테스트
 Higgsfield로 비 내리는 서울 골목의 작은 카페 이미지를 한 장 만들어줘. 만들기 전에 드는 크레딧을 먼저 알려주고 내 확인을 기다려. 크레딧 안내를 보고 확인하면 이미지가 만들어집니다. 비용을 먼저 알려 달라고 붙여 두면 크레딧이 모르는 사이에 빠지지 않습니다.


① Higgsfield 상단 메뉴에서 MCP 누르기
 [higgsfield.ai](https://higgsfield.ai/mcp)에 접속해 맨 위 메뉴에서 MCP를 누릅니다.


② ChatGPT 플러그인 탭에서 플러그인 설치
 ChatGPT 플러그인(영어 화면은 ChatGPT Plugin) 탭을 고르고 Higgsfield 플러그인 설치하기를 누릅니다. 플러그인 화면이 열리면 설치하고, Higgsfield 계정으로 로그인해 접근을 허용합니다. Codex 앱은 ChatGPT 계정으로 로그인합니다. 같은 계정에 설치한 플러그인을 Codex에서 그대로 부릅니다.

둘러보기이미지비디오오디오MCP1API

ChatGPT 확장 프로그램ChatGPT 플러그인2ClaudeClaude CodeCLI··· 기타

HIGGSFIELD 앱을CHATGPT 안에서 바로 사용해 보세요

Higgsfield 플러그인 설치하기2어떻게 연결하나요?

https://mcp.higgsfield.ai/mcp


③ 연결 확인
 내 Higgsfield 크레딧 잔액이 얼마야? Codex 앱에서 새 스레드를 열고 위 질문을 보냅니다. 잔액이 숫자로 나오면 연결된 것입니다. 이 확인에는 크레딧이 들지 않습니다.


④ 첫 생성 테스트
 Higgsfield로 비 내리는 서울 골목의 작은 카페 이미지를 한 장 만들어줘. 만들기 전에 드는 크레딧을 먼저 알려주고 내 확인을 기다려. 크레딧 안내를 보고 확인하면 이미지가 만들어집니다. 비용을 먼저 알려 달라고 붙여 두면 크레딧이 모르는 사이에 빠지지 않습니다.

텔레그램으로 메시지 주고 받기

15분중급터미널 전용

 ▼

자리를 비운 사이에도 휴대폰 텔레그램으로 지시를 보내고 결과를 받습니다. 일은 내 컴퓨터의 Claude Code가 하고, 텔레그램 봇은 그 사이를 오가는 창구 역할만 합니다. 그래서 컴퓨터를 켜 두고 Claude Code를 실행해 둔 동안에만 작동합니다.

⚠️ 이 예제만 Claude Desktop 앱이 아니라 터미널에서 합니다


① Claude Code 설치 확인
 터미널을 열어 claude를 입력했을 때 명령을 찾을 수 없다고 나오면 아직 설치되지 않은 것입니다. 체크리스트 1단계에서 Node.js와 Claude Code를 설치하고 돌아옵니다. [체크리스트 1단계 · Claude Code 설치하기 ›](https://bizroasting.com/checklist.html#tip1)


② Bun 설치
 Bun은 Claude Code를 설치할 때 쓴 npm 대신 자체 설치 명령을 씁니다. 그 명령이 맥과 윈도우에서 다르므로, 아래에서 내 컴퓨터에 맞는 쪽을 골라 씁니다. 이 명령은 Claude Code 안이 아니라 터미널에 바로 넣습니다. 1번에서 claude를 켜 두었다면 /exit로 나오거나 새 창을 엽니다. 윈도우 · 시작 메뉴에서 Windows PowerShell을 열고 아래 명령어를 붙여넣습니다 irm bun.sh/install.ps1 | iex 맥 · 터미널을 열고 아래 명령어를 붙여넣습니다 curl -fsSL https://bun.sh/install | bash 설치가 끝나면 창을 껐다 켜고 bun --version을 입력해 봅니다. 버전 숫자가 나오면 성공입니다. 윈도우에서 붙여넣기가 Ctrl+V로 안 되면 마우스 우클릭을 쓰세요.


③ BotFather로 봇 만들고 토큰 받기
 텔레그램 앱에서 @BotFather를 찾아 대화를 엽니다. /newbot을 보내고 안내에 따라 봇 이름과 봇 아이디(my_assistant_bot처럼 bot으로 끝나야 합니다)를 정하면, 숫자로 시작하는 긴 문자열을 줍니다. 이것이 토큰, 즉 내 컴퓨터가 이 봇을 움직일 때 쓰는 비밀번호입니다. 통째로 복사해 둡니다.  텔레그램에서 BotFather로 검색하면 이름이 비슷한 가짜 봇이 여럿 나옵니다. 이름 옆에 파란 인증 마크가 붙은 계정을 골라야 합니다. [@BotFather 열기 ›](https://t.me/BotFather)


④ 텔레그램 플러그인 설치 (최초 1회)
 /plugin install telegram@claude-plugins-official 터미널에서 claude를 입력해 Claude Code를 켭니다. 그 안에서 위 명령으로 텔레그램 플러그인을 설치합니다. 이 설치는 한 번만 하면 됩니다. 설치가 끝나면 Claude Code를 한 번 껐다 켭니다. 그래야 Claude Code가 다음 단계의 /telegram: 명령과 --channels 옵션을 알아봅니다.

 회사 계정이면 이 설치가 막혀 있을 수 있습니다. 팀 요금제나 엔터프라이즈 요금제는 관리자가 설치 가능한 플러그인 목록을 미리 정해 둘 수 있습니다. 그러면 위 명령을 실행해도 설치가 거부되거나, /plugin 목록에 텔레그램이 아예 보이지 않습니다. 회사 노트북에 IT가 배포한 설정이 걸려 있는 경우도 같습니다.

 이 경우, 사내 IT나 Claude 관리자에게 telegram 플러그인 허용을 요청하거나, 회사 자산이 아닌 개인 계정과 개인 컴퓨터에서 사용합니다.


⑤ 토큰을 Claude Code에 등록
 /telegram:configure <토큰> Claude Code를 켜고 위 명령을 붙여넣습니다. <토큰> 부분을 지우고 그 자리에 3번에서 복사해 둔 토큰을 붙여 실행합니다. 제대로 된 토큰은 숫자로 시작해 콜론(:)이 하나 있고, 그 뒤로 영문과 숫자가 길게 이어집니다.

봇 토큰은 비밀번호와 같습니다. 공개된 곳에 올리지 않습니다. 토큰은 내 컴퓨터의 ~/.claude/ 안에만 저장됩니다. 혹시 노출되면 BotFather에서 /revoke로 새 토큰을 다시 받습니다.


⑥ 텔레그램과 연결한 상태로 Claude Code 실행
 claude --channels plugin:telegram@claude-plugins-official 터미널을 새로 열고 위 명령으로 Claude Code를 켭니다. 뒤에 붙은 --channels가 텔레그램과 이어 주는 통로를 함께 엽니다. 텔레그램을 쓰려면 Claude Code를 켤 때마다 이 명령으로 실행합니다. claude만 입력하면 텔레그램과 연결되지 않습니다.


⑦ 봇에게 메시지를 보내 확인 코드 받기
 내 텔레그램에서 방금 만든 봇을 찾아 아무 메시지나 보냅니다. 봇은 아직 내가 주인인지 모르기 때문에 메시지를 Claude Code로 넘기지 않고, 6자리 확인 코드부터 보내 줍니다. 숫자와 a부터 f까지의 영문이 섞인 코드입니다.봇은 다음 단계에 붙여 넣을 명령까지 통째로 적어 답장합니다. 그대로 복사해 쓰면 됩니다. 코드는 1시간 뒤 만료되고, 지났으면 메시지를 다시 보내 새로 받습니다.


⑧ 내가 주인이라고 알려 주기
 /telegram:access pair <확인코드> Claude Code 화면으로 돌아와 위 명령을 붙여넣고, <확인코드> 자리에 방금 받은 6자리 코드를 넣어 실행합니다. 이제 봇이 내 메시지를 Claude Code로 넘겨 줍니다. 이 코드를 넣은 사람만 봇을 쓸 수 있습니다. 다른 사람이 봇 주소를 알아내 말을 걸어도 내 Claude Code에는 닿지 않습니다.


⑨ 봇 대화창에서 연결 확인하기
 테스트 텔레그램 봇 대화창에 위 메시지를 보냅니다. Claude Code 화면에 그 메시지가 그대로 도착하면 연결에 성공한 것입니다.

메시지가 도착하지 않는다면6번 명령(--channels)으로 Claude Code를 켰는지, 8번 확인 코드를 제대로 넣었는지 확인해 봅니다. 그래도 안 되면 터미널에서 bun --version을 입력해서 Bun이 설치되었는지 확인합니다.


⑩ 모르는 사람에게 코드가 나가지 않게 막기
 /telegram:access policy allowlist 지금까지의 설정에서는 낯선 사람이 봇에게 말을 걸면 봇이 그 사람에게도 확인 코드를 보내 줍니다. 7번에서 내가 받은 것과 같은 코드입니다. 내 연결은 9번에서 이미 확인했으니 더는 필요 없습니다. 위 명령을 실행하면 코드 발급이 멈추고, 등록해 둔 나만 봇을 쓰게 됩니다.

주의 사항

각 도구의 화면 구성과 메뉴 이름은 업데이트에 따라 바뀔 수 있습니다. 외부로 메시지나 데이터를 보내는 연결은 되돌리기 어려우니, 민감한 정보를 다룰 때는 사람이 한 번 확인하는 절차를 두고 사내 보안 정책을 함께 확인하시기 바랍니다.

### 하나만 골라 작게 시작해 보세요

일곱 예제 모두 10~15분이면 첫 연결을 만들 수 있습니다. 지금 가장 끌리는 카드를 펼쳐 그 자리에서 따라가면 됩니다.

 [가장 쉬운 구글 연결부터 →](https://bizroasting.com#mcp-drive)

API

서비스마다 다른 전용 창구
 Application Programming Interface · 프로그램끼리 정해 둔 창구 AI 앱 외부 도구와 그 API

Claude

ChatGPT

사내 챗봇

구글 드라이브규칙 A

슬랙규칙 B

DART 공시규칙 C

3 × 3연결 9개

#### 그래서 생기는 일

- 서비스마다 문서·인증·데이터 모양이 다릅니다

- 앱마다 개발자가 연결 코드를 별도로 작성합니다

- 한쪽이 바뀌면 그 연결을 다시 고칩니다

  앱과 도구가 늘수록 연결은 곱하기로 늘어납니다

API 키 예시서비스마다 따로 발급받아 코드에 넣는 비밀번호

 구글AIzaSyA3kX•••••••• 슬랙xoxb-1234-••••-•••• DART7c1e0f••••••(40자리)

API키

DART로 보는 API 요청 한 줄
 개발자가 문서를 참고해 직접 입력하는 값

1인증키 crtfc_key · 40자리opendart.fss.or.kr에서 발급받는 비밀번호

 7c1e0f3a9b1~10 24d85e6f0111~20 c7a3b9d24e21~30 8f5a6c0b1731~40

숫자 0~9와 영문 a~f로 된 무작위 40자입니다. 앞쪽 몇 자리가 회사나 날짜를 뜻하지 않고, 40자 전체가 한 덩어리로 “누가 묻는가”를 증명합니다. 한 글자만 틀려도 거절됩니다.

https://opendart.fss.or.kr/api/fnlttSinglAcnt.json

?crtfc_key=7c1e0f3a9b…0b171&corp_code=001263802&bsns_year=20243&reprt_code=110114

 삼성전자 2024년 사업보고서의 주요 재무 항목을 달라는 요청

1 crtfc_key · 40자리
7c1e…0b17

내 인증키. 하루 조회 한도도 이 키에 걸립니다

2 corp_code · 8자리
00126380

DART 고유번호, 삼성전자. 6자리 종목코드 005930과 다른 번호입니다

3 bsns_year · 4자리
2024

사업연도. 보고서가 다루는 해입니다

4 reprt_code · 5자리
11011

보고서 종류. 11013 1분기, 11012 반기, 11014 3분기, 11011 사업보고서

MCP

한 번 만들면 어디서나 사용하는 규격
 Model Context Protocol · AI와 도구 사이의 공용 플러그 MCP 클라이언트 · AI 앱 MCP 서버 · 도구

Claude

ChatGPT

사내 챗봇

  MCP 공용 규격

구글 드라이브

슬랙

DART 공시

3 + 3연결 6개

#### 이렇게 움직입니다

- 서버가 자기가 할 수 있는 일의 목록을 알려 줍니다

- AI가 목록을 읽고 필요한 것을 골라 부릅니다

- 서버 하나를 더하면 모든 앱에서 씁니다

  USB-C처럼, 단자 모양 하나에 무엇이든 꽂습니다

APIvs.MCP

이름부터 풀어 보면

APIApplication Programming Interface

MCPModel Context Protocol
  이름의 유래

1968년 한 컴퓨터 그래픽 논문에 처음 등장한 말입니다. 응용 프로그램(Application)이 다른 프로그램을 부를 때 쓰는, 미리 약속해 둔 접점(Interface)이라는 뜻입니다.

Anthropic 개발자 데이비드 소리아 파라는 Claude와 코드 편집기 사이에서 코드를 복사해 붙이다 지쳤습니다. 개발 도구의 공용 규격 LSP를 본떠, 모델(Model)에 맥락(Context)을 건네는 약속(Protocol)을 만들었습니다.
 누가 부르나 연결 규칙 도구를 늘릴 때 무엇을 할지

개발자가 작성한 프로그램코드가 정해 둔 순서대로 부름

서비스마다 제각각문서·인증·데이터 모양이 다름

앱마다 연결 코드를 새로앱이 3개면 3번 개발

개발자가 미리 정해 둠사전에 구현한 기능만 실행

AI 모델Claude, ChatGPT 같은 AI 앱이 부름

모두 같은 규격 하나목록 보기, 부르기, 결과 받기

서버 하나 연결하면 끝호환되는 AI 앱 어디서나 씀

AI가 목록을 읽고 고름요청에 맞는 도구를 스스로 선택
   MCP 연표

2024.11.25

Anthropic 공개
개방형 규격으로 첫 공개

2025.03.26

OpenAI 채택
Agents SDK부터 지원

2025.04.09

구글 채택
Gemini 모델·SDK 지원 발표

2025.12.09

리눅스 재단에 기부
Agentic AI Foundation으로 이관

핵심MCP는 API를 없애지 않습니다. MCP 서버 대부분이 안에서 그 서비스의 API를 부르고, MCP는 AI가 쓰기 쉽게 감싼 공용 포장입니다.

LSPLanguage Server Protocol. 2016년 Microsoft가 공개한, 코드 편집기와 프로그래밍 언어 기능(자동 완성, 오류 표시)을 잇는 공용 규격입니다. MCP는 이 구조를 AI 앱과 도구 사이로 옮겨 왔습니다.

{ }JSON

MCP의 메시지 포맷, JSON-RPC 2.0
 MCP 공식 규격은 모든 메시지를 이 포맷으로 기술합니다

JSON
JavaScript Object Notation

“키(key)”: 값(value) 구조로 데이터를 표기하는 텍스트 포맷. 사람과 프로그램 모두 판독할 수 있습니다.

RPC
Remote Procedure Call

원격 프로그램의 기능을 함수명과 인자만 전송해 로컬 함수처럼 호출하는 방식.

2.0
version

규격의 버전 번호. 모든 메시지 첫 줄에 "jsonrpc": "2.0"을 명시합니다.

   요청(Request) · AI 앱 → Liner 서버

{ "jsonrpc": "2.0", ← 규격 버전 "id": 2, ← 요청 ID "method": "tools/call", ← 메서드: 도구 호출 "params": { ← 파라미터 "name": "search_web", "arguments": { "query": "AI 검색 동향" } } }
 응답(Response) · Liner 서버 → AI 앱

{ "jsonrpc": "2.0", "id": 2, ← 동일 ID로 요청과 매칭 "result": { ← 결과값 "content": [ { "type": "text", "text": "검색 결과 …" } ] } }

흐름initialize 연결 개시와 기능 협상 → tools/list 도구 목록 조회 → tools/call 선택한 도구 호출 → result 결과 수신

참고JSON은 데이터 포맷이며 프로그래밍 언어가 아닙니다. 서버는 Python, TypeScript 등 어떤 언어로 구현해도 이 포맷만 준수하면 됩니다. LSP도 동일한 JSON-RPC를 사용합니다.

휴대폰을 가로로 돌리면 크게 보입니다

휴대폰을 가로로 돌리면 크게 보입니다

 [ ←목록으로 ](https://bizroasting.com/index.html#section-3)
