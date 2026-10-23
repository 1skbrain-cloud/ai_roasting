# 에이전트의 도구: MCP·커넥터·스킬·플러그인 한눈에

원본: https://bizroasting.com/agent-tools.html

---

에이전트의 도구: MCP·커넥터·스킬·플러그인 한눈에 | AI ROASTING           [본문으로 건너뛰기](https://bizroasting.com#main)

다섯 종류의 도구

## 각 도구가 맡는 일

도구는 에이전트가 말 대신 실제로 행동하게 해 주는 수단입니다. 아래 다섯 가지는 Claude Code와 Codex가 함께 쓰며, 부르는 방법만 다릅니다

 1

#### 내장 도구

Built-in · 기본기

설치 없이 처음부터 갖춘 능력입니다. 파일 읽기와 쓰기, 터미널 실행, 웹 검색이 여기에 해당합니다.
 [치트시트 →](https://bizroasting.com/cheatsheet.html)

 2

#### MCP

Model Context Protocol

외부 시스템을 에이전트의 도구로 붙이는 표준 규약입니다. 두 도구가 같은 MCP 서버를 그대로 씁니다.
 [PlayMCP 예제 →](https://bizroasting.com/mcp-examples.html#mcp-kakao)

 3

#### 커넥터

Connectors · 클릭 연결

MCP를 코드 없이 클릭으로 쓰게 만든 버전입니다. Gmail, 드라이브, 노션을 메뉴에서 골라 켭니다.
 설정 화면에서 클릭으로 연결

 4

#### 스킬

Skills · 절차 도구

자주 쓰는 절차를 한 번 정리해 두고 다시 부르는 도구입니다. 한 번 등록하면 부를 때마다 같은 품질이 나옵니다.
 [나만의 Skill →](https://bizroasting.com/skills.html)

 5

#### 플러그인

Plugins · 묶음 패키지

스킬과 MCP를 한 묶음으로 포장해 한 번에 설치합니다. 앞의 네 종류를 담는 그릇입니다.

 도구별 차이

- 내장 도구. 파일 읽기와 쓰기, 터미널 실행, 웹 검색을 설치 없이 바로 씁니다.

- MCP. 설정 · 커넥터 화면에서 서버 주소를 넣어 추가합니다.

- 커넥터. 데스크톱 앱과 웹의 설정에 커넥터 메뉴가 따로 있습니다.

- 스킬. .claude/skills 폴더에 두면 Claude Code가 설명을 읽고 필요할 때 스스로 실행합니다.

- 플러그인. 마켓플레이스에서 골라 설치하면 스킬과 MCP가 한 번에 붙습니다.

- 내장 도구. 파일과 터미널은 바로 씁니다. 웹 검색은 기본값이 캐시라, 실시간 검색은 따로 켜야 합니다.

- MCP. 플러그인에 포함된 서버가 함께 붙고, 없으면 주소를 직접 넣어 추가합니다.

- 커넥터. CLI에는 커넥터 메뉴가 없습니다. ChatGPT 데스크톱 앱과 웹에서 플러그인을 설치할 때 함께 붙습니다.

- 스킬. .agents/skills 폴더에 둡니다. Codex가 스스로 쓰기도 하고, $스킬이름으로 직접 부를 수도 있습니다.

- 플러그인. 플러그인 디렉터리에서 설치합니다. 설치한 뒤 새 대화를 시작해야 반영됩니다.

MCP와 커넥터

## MCP는 규약, 커넥터는 그 규약의 포장

MCP는 외부 시스템을 잇는 약속된 방식입니다. 서비스마다 연결 방법이 제각각이면 매번 새로 만들어야 하니, 방식을 하나로 정해 둔 것입니다. 커넥터는 그 방식을 클릭 한 번으로 쓰게 만든 포장입니다. 콘센트 규격과 멀티탭의 관계입니다.

#### MCP · 규약 (개발자 쪽)

- 외부 시스템을 도구로 잇는 약속된 방식

- 서버 주소를 직접 입력해 등록

- 목록에 없는 서비스도 연결 가능

- 설정과 권한을 직접 지정

#### 커넥터 · 포장 (누구나)

- 같은 MCP를 메뉴에서 클릭으로 연결

- 데스크톱 앱과 웹의 설정에서 관리

- Gmail, 드라이브, 노션 등 준비된 서비스만

- 코드나 터미널 없이 사용

 도구별 연결 경로

둘 다 Claude 데스크톱과 웹의 설정 · 커넥터 한 화면에 있습니다.

둘 다 ChatGPT 데스크톱과 웹의 플러그인에서 다룹니다. 플러그인을 설치하면 그 안의 커넥터와 MCP 서버가 함께 붙습니다. Codex CLI 자체에는 커넥터 메뉴가 없습니다.

## 한 표로 비교

구분MCP커넥터

무엇인가연결하는 방식 자체그 방식을 입힌 클릭 버전

쓰는 사람직접 연결하는 사람누구나

연결 방법서버 주소를 직접 입력목록에서 클릭으로 켜기

붙일 수 있는 범위어떤 서비스든목록에 있는 것만

비유콘센트 규격완제품 멀티탭

그래서 "MCP를 쓴다"와 "커넥터를 붙인다"는 대개 같은 일을 가리킵니다.

Claude Code

## Claude에서 도구 추가하기

터미널을 열지 않아도 됩니다. 세 가지 모두 앱 화면에서 클릭으로 끝납니다

#### 커넥터 켜기

설정 화면에서

준비된 목록에서 Gmail, 드라이브, 노션 같은 서비스를 고릅니다. 로그인 한 번으로 끝납니다.

#### MCP 서버 추가

주소 붙여넣기

목록에 없는 서비스는 같은 화면에서 직접 추가합니다. 서버를 만든 쪽이 안내한 주소를 붙여넣습니다.

#### 플러그인 설치

묶음으로

스킬과 MCP를 한 벌로 묶은 플러그인을 설치하면 도구 여러 개가 한 번에 붙습니다.

 Claude 데스크톱 앱 · 설정

검색

설정

일반

계정

개인정보보호

결제

사용량

기능

Claude Code

Cowork

Chrome용 Claude

데스크톱 앱

일반

확장 프로그램

개발자

사용자 지정

스킬

커넥터

플러그인

 커넥터  추가

전체연결됨연결되지 않음

인기

MGmail연결

SSlack연결

31Calendar연결

커넥터유형상태

GGitHub 연동웹✓

DGoogle Drive웹✓

KPlayMCP웹✓

Kkorean-law웹사용자 정의연결

AAdobe for creativity플러그인에서 제공됨웹플러그인세션에서 연결됨

- 1

사용자 지정

설정 왼쪽 맨 아래 묶음입니다. 스킬 · 커넥터 · 플러그인이 나란히 있습니다. 앞에서 본 다섯 종류 중 셋이 여기 모여 있습니다.

- 2

추가 버튼

목록에 없는 서비스를 직접 붙입니다. 여기서 주소를 넣는 순간이 MCP를 쓰는 때입니다.

- 3

전체 · 연결됨 · 연결되지 않음

지금 무엇이 붙어 있는지 거르는 탭입니다. 연결됨만 보면 현재 상태가 한눈에 들어옵니다.

- 4

상태 열의 체크

이미 붙은 커넥터입니다. 체크가 있는 것만 Claude가 읽고 씁니다.

- 5

유형 열의 꼬리표

사용자 정의는 직접 붙인 것, 플러그인은 플러그인에 딸려 온 것입니다. 어디서 왔는지가 여기 적힙니다.

실습 예제

붙이는 과정 전체는 실전 예제에서 단계별로 따라갈 수 있습니다. 카카오 도구 연결은 [PlayMCP 카카오 예제](https://bizroasting.com/mcp-examples.html#mcp-kakao), 법제처 커넥터 추가는 [법제처 MCP 예제](https://bizroasting.com/mcp-examples.html#mcp-law)를 보세요.

Codex

## ChatGPT에서 도구 추가하기

Codex CLI에는 커넥터 화면이 없습니다. 도구는 ChatGPT 쪽 플러그인에서 붙입니다

ChatGPT 데스크톱 앱이나 chatgpt.com에서 왼쪽 플러그인을 엽니다. 디렉터리에서 플러그인을 고르면 그 안의 커넥터와 MCP 서버가 함께 붙습니다.
 ChatGPT 데스크톱 앱 · 플러그인

  플러그인스킬

 Codex ▾

새 채팅

풀 리퀘스트

사이트

예약

플러그인

프로젝트

사내 가이드

표지 이미지 교체

주간 보고

워드 파일 HTML 변환

U사용자 계정

플러그인

즐겨 쓰는 도구 어디서나 ChatGPT와 함께 작업하세요

플러그인 검색

설치됨

WPXPSAGM

공개개인용

Featured

CComputer UseControl Mac apps···

CChromeControl Chrome···

XSpreadsheetsCreate and edit files···

PPresentationsCreate presentations···

GGitHubTriage PRs, issues, CI···

DGoogle DriveWork across Drive, Docs설치

MSNGmail, Slack 외 22개 더 보기

- 1

플러그인 메뉴

왼쪽 사이드바에 있습니다. 위쪽 탭에서 스킬로도 넘어갑니다. Codex CLI에는 이 화면이 없습니다.

- 2

설치됨

지금 붙어 있는 플러그인이 아이콘으로 늘어섭니다. 여기 있는 것만 대화에서 씁니다.

- 3

공개 · 개인용

누구나 받는 디렉터리와, 우리 조직만 쓰는 것을 나눠 봅니다.

- 4

디렉터리 목록

플러그인 하나에 커넥터와 스킬이 함께 들어 있습니다. ChatGPT와 Codex가 같은 목록을 씁니다.

- 5

설치 버튼

누르면 그 서비스 로그인을 요구합니다. 설치한 뒤에는 새 대화를 시작해야 도구가 붙습니다.

 [   스킬 라이브러리 비즈니스 리더를 위해 검증한 실무 스킬만 모았습니다  → ](https://skill.airoasting.com/) [   MCP 허브 AI에 연결할 수 있는 오픈소스 MCP를 한 곳에 모은 카탈로그입니다  → ](https://mcp.airoasting.com/)

참고 자료

 [   Model Context Protocol 공식 문서

 MCP 규약 소개와 연결 방법  원문 ](https://modelcontextprotocol.io) [   Anthropic | Claude Code의 MCP 연결 안내

 MCP 서버 연결과 커넥터 관리  원문 ](https://docs.claude.com/en/docs/claude-code/mcp) [   OpenAI | Codex CLI 레퍼런스

 MCP와 플러그인 관리 방법  원문 ](https://learn.chatgpt.com/docs/cli/reference) [   OpenAI | Codex 스킬 만들기

 .agents/skills 위치와 SKILL.md 형식  원문 ](https://learn.chatgpt.com/docs/build-skills)

### 도구를 갖췄다면 다음은 팀입니다

도구는 에이전트에게 손발을 줍니다. 그 손발로 일할 팀을 꾸리는 방법은 멀티 에이전트 소환에서 다룹니다.

 [← 하네스 엔지니어링이란?](https://bizroasting.com/harness-engineering.html) [멀티 에이전트 소환 →](https://bizroasting.com/harness-workflows.html)

 [ ←목록으로 ](https://bizroasting.com/index.html#section-3)
