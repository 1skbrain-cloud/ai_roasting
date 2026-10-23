# 에이전트 도구 안내: 헤르메스·Aside·Orca·Buzz·Instinct

원본: https://bizroasting.com/agents-tools.html

---

에이전트 도구 안내: 헤르메스·Aside·Orca·Buzz·Instinct | AI ROASTING          [본문으로 건너뛰기](https://bizroasting.com#main)

한눈에 보기

## 에이전트가 일하는 자리를 채팅창 밖으로 옮깁니다

Claude와 ChatGPT를 채팅창에서만 쓰면 대화를 닫는 순간 작업도 멈춥니다. 아래 다섯 도구는 에이전트가 일하는 자리를 각각 서버, 브라우저, 멀티 모델 토론 작업대, 팀 메신저, 문자 메시지로 옮깁니다. 지금 하는 작업과 가장 가까운 자리 하나를 고르면 됩니다.

 [

01

헤르메스

상주 에이전트

늘 켜 둔 컴퓨터나 서버에서 실행
 ](https://bizroasting.com#sec2) [

02

Aside

AI 브라우저

로그인해 둔 웹사이트에서 실행
 ](https://bizroasting.com#sec3) [

03

Orca

멀티 모델 토론 작업대

여러 모델이 같은 문제를 나란히 실행
 ](https://bizroasting.com#sec4) [

04

Buzz

사람과 에이전트의 팀 메신저

팀 채널 안에서 실행
 ](https://bizroasting.com#sec5) [

05

Instinct

문자로 부르는 개인 비서

문자 메시지와 전화로 지시
 ](https://bizroasting.com#sec6)

다섯 가운데 넷은 모델을 따로 팔지 않습니다. 이미 쓰는 Claude·ChatGPT 구독이나 API 키를 연결합니다.

 Instinct만 자체 서비스로 운영되고, 지금은 미국에서 초대받은 사람만 쓸 수 있습니다.

헤르메스

TOOL 01

헤르메스 에이전트
 상주 에이전트

컴퓨터 한 대를 24시간 일하는 에이전트로 만듭니다

Nous Research가 공개한 오픈소스 자율 에이전트입니다. 늘 켜 두는 맥이나 윈도우 컴퓨터, 또는 빌린 서버에 설치하고 Claude나 ChatGPT 같은 모델을 연결합니다. 터미널에서 지시할 수도 있고, 텔레그램이나 슬랙에서 메시지로 지시할 수도 있습니다.

만든 곳

Nous Research

2026년 3월 첫 공개

프로그램 비용

무료

MIT 라이선스

매달 드는 돈

모델 사용료

서버를 빌리면 서버 비용 추가

지원 환경

macOS · Windows

임대 서버에도 설치

#### 꺼지지 않습니다

게이트웨이 프로그램이 실행 중이면 메신저로 지시를 받고, 예약한 작업을 정해진 시각에 실행합니다.

#### 모델을 바꿔 끼웁니다

명령 한 줄로 Claude, ChatGPT, 제미나이, 내 컴퓨터에 설치한 로컬 모델 사이를 옮깁니다.

#### 기억이 누적됩니다

대화, 기억, 스스로 만든 스킬이 한 폴더에 남아 세션이 바뀌어도 이어집니다.

이럴 때메신저로 지시해 두고 결과만 받고 싶을 때, 예약 작업을 내 컴퓨터나 서버에서 실행하고 싶을 때 적합합니다.

 [다운로드 페이지

hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/) [사용 사례](https://bizroasting.com/hermes-cases.html)

Aside

TOOL 02

Aside
 AI 브라우저

로그인해 둔 웹사이트에서 에이전트가 대신 작업합니다

Y Combinator 2025년 가을 배치 출신 스타트업 Aside Computer가 2026년 6월에 공개한 브라우저입니다. 웹을 보는 브라우저 안에 에이전트가 들어 있습니다. 이미 로그인한 사이트를 그대로 쓰므로 별도의 연결 설정 없이 조사, 메시지 답장, 스프레드시트 작업을 맡길 수 있습니다.

만든 곳

Aside Computer

2026년 6월 공개

프로그램 비용

내려받기 무료

공식 가격표 미공개

연결하는 모델

내 구독 또는 API 키

Claude·ChatGPT 구독 연결

지원 환경

macOS · Windows

브라우저 앱

#### 연결 설정이 필요 없습니다

로그인해 둔 사이트에서 에이전트가 직접 클릭하고 입력합니다. API가 없는 사이트에도 작동합니다.

#### 비밀번호를 에이전트에게 보여 주지 않습니다

전용 비밀번호 관리자 Vault가 로그인 칸에 직접 채우고, 접근할 때마다 기록을 남깁니다.

#### 기억은 내 기기에 남습니다

작업 맥락을 기억하지만, 작업과 기억과 데이터는 기기 밖으로 보내지 않는다고 공식 사이트가 밝힙니다.

이럴 때API가 없는 사내 시스템이나 웹사이트에서 반복 클릭 작업을 줄이고 싶을 때 적합합니다.

쓰기 전에 확인할 점

- 에이전트가 내 계정으로 로그인한 사이트에서 결제와 메시지 발송까지 할 수 있습니다. 회사 계정에 쓰기 전에 사내 보안 정책을 확인합니다.

- 공식 가격표는 아직 공개되지 않았습니다. 지금은 내려받아 쓰던 구독을 연결하는 방식입니다.

 [다운로드 페이지

aside.com/download](https://aside.com/download) [공식 사이트](https://aside.com)

Orca

TOOL 03

Orca
 멀티 모델 토론 작업대

여러 모델에게 같은 문제를 맡기고, 서로의 답을 검토하게 합니다

Stably AI가 만든 오픈소스 데스크톱 앱입니다. Claude Code(Claude), Codex(GPT), Cursor CLI처럼 서로 다른 모델의 에이전트를 작업마다 별도의 git 워크트리(같은 저장소를 한 벌 더 펼쳐 둔 작업 폴더)에서 동시에 실행합니다. 같은 문제에 대한 모델별 답을 한 화면에 나란히 놓고, 한 모델의 결과를 다른 모델에게 넘겨 반론과 검토를 받습니다. 한 모델의 답만 볼 때 놓치는 허점을 다른 모델이 지적하게 만드는 용도입니다.

만든 곳

Stably AI

2026년 3월 저장소 공개

프로그램 비용

무료

MIT 라이선스

매달 드는 돈

모델별 구독료

모델 수만큼 사용량 증가

지원 환경

macOS · Windows · Linux

Git 저장소 필요

#### 같은 문제를 여러 모델에게

작업마다 워크트리가 따로 생겨 Claude Code, Codex, Cursor CLI가 같은 문제를 서로 간섭 없이 동시에 풉니다.

#### 답을 나란히 놓고 비교합니다

분할 화면과 변경 내용 비교 화면에서 모델별 답이 어디서 다른지 바로 확인합니다.

#### 반론과 검토를 주고받습니다

한 모델의 결과에 단 의견을 받을 모델을 골라 보냅니다. 오케스트레이션 기능을 쓰면 조율 에이전트가 이 순서를 진행합니다.

이럴 때중요한 설계안이나 판단을 한 모델의 답만으로 정하기 어려울 때, Claude와 GPT의 답을 맞대어 차이와 허점을 확인하고 싶을 때 적합합니다.

토론 진행 순서

- 같은 문제를 워크트리 셋에 만들어 Claude Code, Codex, Cursor CLI에게 각각 맡깁니다.

- 세 답을 나란히 놓고 서로 다른 부분을 찾습니다.

- 한 모델의 답에 의견을 달아 다른 모델에게 보내 반론과 검토를 받습니다.

- 최종안을 고른 워크트리만 남기고 나머지는 지웁니다.

에이전트끼리 직접 메시지를 주고받지는 않습니다. 사람이나 조율 에이전트가 결과를 전달합니다. 모델 수만큼 사용량도 늘어나므로 비교가 필요한 작업에만 씁니다.

 [다운로드 페이지

onorca.dev](https://www.onorca.dev/docs/install)

Buzz

TOOL 04

Buzz
 사람과 에이전트의 팀 메신저

에이전트를 봇이 아니라 동료로 채널에 들입니다

Square와 Cash App을 운영하는 Block이 2026년 7월 21일 공개한 오픈소스 팀 메신저입니다. 슬랙처럼 채널과 스레드가 있고, 에이전트가 자기 키를 가진 멤버로 들어와 사람과 같은 자격으로 대화하고 작업합니다. Block의 에이전트 goose와 Claude Code, Codex를 채널에 추가할 수 있습니다.

만든 곳

Block

2026년 7월 21일 공개

프로그램 비용

무료

Apache 2.0 라이선스

서버

릴레이 하나

직접 운영 또는 Block 호스팅

지원 환경

macOS · Windows · Linux

초기 버전

#### 에이전트도 멤버입니다

자기 키를 가진 멤버로 채널에 들어와 대화를 읽고, 답하고, 다른 사람을 부릅니다.

#### 코드 작업도 채널에서

작업 브랜치 하나가 채널 하나가 되어 수정 제안, 검사 결과, 검토 의견이 한곳에 남습니다.

#### 모든 행동에 서명이 붙습니다

메시지, 승인, 코드 수정이 서명된 기록으로 쌓여 누가 무엇을 했는지 같은 방식으로 추적합니다.

이럴 때팀 대화와 에이전트의 작업 기록을 한곳에 모으고, 사람이 마지막 결정을 내리는 구조로 일하고 싶을 때 적합합니다.

쓰기 전에 확인할 점

- 아직 초기 버전입니다. 공개 저장소가 되는 기능과 안 되는 기능을 따로 표시합니다.

- Windows 설치 파일은 코드 서명 전 알파 단계입니다.

 [다운로드 페이지

github.com/block/buzz](https://github.com/block/buzz/releases/latest)

Instinct

TOOL 05

Instinct
 문자로 부르는 개인 비서

별도 앱 없이 문자와 전화로 개인 업무를 맡깁니다

Spear Street Technology가 2026년 8월에 공개한 개인 비서 에이전트입니다. iMessage나 WhatsApp으로 문자를 보내거나 전화를 걸어 지시합니다. 에이전트가 자기 컴퓨터와 전화를 사람처럼 써서 예약, 구독 해지, 서류 작성을 처리합니다. 연결 계정과 설정은 웹 작업 공간에서 관리합니다.

만든 곳

Spear Street Technology

2026년 8월 공개

비용

베타 기간 무료

공식 가격 미정

지시 방법

문자 · 전화

iMessage · WhatsApp

이용 조건

미국 · 초대제

만 18세 이상

#### 문자로 지시합니다

새 앱을 익힐 필요 없이 평소 쓰는 메신저로 일을 맡기고 결과를 받습니다.

#### 먼저 연락합니다

처리하지 못한 일을 챙겨 사용자에게 먼저 문자나 전화를 겁니다.

#### 웹과 전화를 직접 다룹니다

브라우저를 조작하고 전화를 걸어 예약, 해지, 일정 조율을 처리합니다.

이럴 때예약, 구독 해지, 일정 조율처럼 연락이 여러 번 오가는 개인 업무를 맡기고 싶을 때 적합합니다.

쓰기 전에 확인할 점

- 2026년 9월 말 기준으로 미국 거주자 대상 초대제로 운영됩니다. 한국에서는 바로 쓸 수 없습니다.

- 연결한 메일과 메시지를 수집해 색인하고, 모델 학습 활용이 기본으로 켜져 있습니다. 설정에서 직접 꺼야 합니다.

- 계정 연결을 끊어도 이미 색인된 데이터는 삭제를 따로 요청해야 지워집니다.

 [초대 신청 페이지

instinct.com](https://instinct.com)

선택 기준

## 다섯 도구 비교

차이가 가장 큰 항목은 에이전트가 일하는 자리와 지시하는 방법입니다.

도구일하는 자리지시 방법모델비용지원 환경받는 곳

헤르메스늘 켜 둔 컴퓨터, 임대 서버터미널, 텔레그램, 슬랙API 키 연결무료, 모델 사용료 별도macOS · Windows · 서버[공식 사이트](https://hermes-agent.nousresearch.com/)

Aside로그인해 둔 웹사이트브라우저 화면Claude·ChatGPT 구독, API 키내려받기 무료macOS · Windows[다운로드](https://aside.com/download)

Orca내 컴퓨터의 Git 저장소앱 화면, 조율 에이전트Claude Code·Codex·Cursor CLI 구독무료, 구독료 별도macOS · Windows · Linux[설치 문서](https://www.onorca.dev/docs/install)

Buzz팀 채널채널 메시지goose·Claude Code·Codex무료, 릴레이 운영 별도macOS · Windows · Linux[릴리스](https://github.com/block/buzz/releases/latest)

InstinctInstinct의 컴퓨터와 전화문자, 전화자체 서비스베타 기간 무료미국 · 초대제[초대 신청](https://instinct.com)

1상황별 선택 기준

 [메신저로 지시하고, 내가 자리를 비워도 에이전트가 계속 실행되면 좋겠다헤르메스 →](https://bizroasting.com#sec2) [API가 없는 웹사이트에서 반복하는 클릭 작업을 줄이고 싶다Aside →](https://bizroasting.com#sec3) [중요한 판단을 여러 모델에게 동시에 맡기고, 서로의 답을 검토하게 하고 싶다Orca →](https://bizroasting.com#sec4) [팀원과 에이전트가 같은 채널에서 함께 일하는 구조를 시험하고 싶다Buzz →](https://bizroasting.com#sec5) [예약과 해지 같은 개인 업무를 문자로 맡기고 싶다 (미국 거주자)Instinct →](https://bizroasting.com#sec6)

한 번에 하나씩 설치합니다

다섯 도구 모두 에이전트에게 내 컴퓨터나 계정의 권한을 넘깁니다. 지금 하는 작업과 가장 가까운 도구 하나를 먼저 설치하고, 작은 작업 하나로 결과를 확인한 다음 범위를 넓힙니다.

참고

 [  Hermes Agent 공식 문서

Nous Research 문서 ](https://hermes-agent.nousresearch.com/docs/) [  Aside 공식 사이트

Aside Computer · 기능, 개인정보 처리 방식 공식 ](https://aside.com) [  Orca 공식 문서

Stably AI 문서 ](https://www.onorca.dev/docs) [  Orca 오케스트레이션 문서

조율 에이전트와 작업 배분 문서 ](https://www.onorca.dev/docs/cli/orchestration) [  block / buzz

공개 저장소 · Apache 2.0 라이선스 저장소 ](https://github.com/block/buzz) [  Instinct 공식 사이트

Spear Street Technology 공식 ](https://instinct.com)

### 실행 순서

위 선택 기준에서 지금 작업과 가장 가까운 도구 하나를 고릅니다. 다운로드 페이지에서 설치한 뒤, 작은 작업 하나로 결과를 확인하고 범위를 넓힙니다.

 [← 목록으로](https://bizroasting.com/index.html#section-hermes) [헤르메스 사용 사례 →](https://bizroasting.com/hermes-cases.html)

 [ ←목록으로 ](https://bizroasting.com/index.html#section-hermes)
