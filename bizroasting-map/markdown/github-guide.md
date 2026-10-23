# GitHub · Vercel · Netlify 가이드

원본: https://bizroasting.com/github-guide.html

---

GitHub · Vercel · Netlify 가이드 | AI ROASTING              [본문으로 건너뛰기](https://bizroasting.com#main)

## 개념 설명

Git과 GitHub, 슬라이드 열한 장으로 먼저 보기

 처음 만나는 개발 도구

Git과

GitHub

이름은 닮았지만,

Git은 도구이고 GitHub는 서비스입니다

Git · 도구

GitHub · 서비스

5분이면

충분합니다

01 / 11 · AI ROASTING

이 파일들, 어느 것이 최신인가요?

사업계획서_최종.pptx

사업계획서_최종_수정.pptx

사업계획서_진짜최종.pptx

사업계획서_최종_팀장님검토.pptx

사업계획서_최종(2)_0928.pptx

파일 이름으로는 알 수 없는 것

누가 고쳤나

언제 고쳤나

무엇이 바뀌었나

어제 버전은 어디 있나

최종의 최종의 최종

02 / 11

git[ɡɪt]
 명사 · 영국 속어

꼴통, 고집불통,

밥맛없는 녀석

좋게 풀면

Global

Information

Tracker

"나는 자아도취적인 놈이라 내 프로젝트엔 전부 내 이름을 붙인다. 먼저 리눅스, 이번엔 깃."

리누스 토르발스 · 리눅스라는 이름은 그의 이름(Linus)에서 왔습니다. git이라는 이름도 고집불통인 자신을 빗댄 농담입니다

 왜 만들었나

2000년 5월

래리 맥보이가 상용 버전 관리 도구 BitKeeper를 출시했습니다

맥보이 · 썬 마이크로시스템즈 출신 엔지니어, BitMover 창업자

2002년 2월

리눅스 개발자들이 BitKeeper를 무료로 쓰기 시작했습니다. 조건은 경쟁 도구를 만들지 않고 내부를 뜯어보지 않는 것이었습니다

2005년 4월

한 개발자가 통신 방식을 분석하자, BitMover는 무료 제공을 중단했습니다

같은 달

토르발스는 열흘 만에 Git의 기본 구조를 만들어 공개했습니다

03 / 11

Git

바뀐 순간을 저장해 두는 도구

Git은 내가 기록할 때마다 그 순간을 사진처럼 한 장씩 남깁니다.

이 한 장을 커밋(commit)이라고 부릅니다.

9월 1일초안 작성

9월 3일표 추가

9월 5일색 변경

누가, 언제,

무엇을 바꿨는지

Git이 기억합니다

인터넷 없이도

내 컴퓨터에서

돌아갑니다

무료 · 오픈소스

Git으로

어제 버전도

되살릴 수 있습니다

04 / 11

이 기록을 인터넷에 올려 두는 곳이 GitHub입니다 →

GitHub

그 기록을 인터넷에 보관하는 서비스

 내 노트북

Git 기록

● 9월 5일 · 색 변경● 9월 3일 · 표 추가● 9월 1일 · 초안 작성

  푸시GitHub에 올리기

저장소 · repository

내-프로젝트

github.com/내아이디/…

백업

공유

협업

공개

코드용 구글 드라이브라고 생각하면 쉽습니다

05 / 11

GitHub 로고의 고양이는 왜 문어 다리를 가졌을까요

GitHub 로고Octocat · 이름은 Mona

다리는

8개가 아니라

5개

출발은 스톡 그림

원본은 영국 디자이너 사이먼 옥슬리가 스톡 이미지 사이트에 올린 그림 'Octopuss'입니다

옥슬리는 초기 트위터 새 로고를 그린 디자이너입니다

왜 골랐나

Git에는 브랜치 셋 이상을 한 번에 합치는 '문어 병합(octopus merge)' 기능이 있습니다. 창업자들은 이 기능에 빗대어 문어 다리 고양이를 골랐습니다

이름을 바꾸다

창업자들은 오류 페이지에 넣으려고 이 그림을 샀습니다. 이후 이름을 Octocat으로 바꾸고 상표로 등록했습니다

담긴 의미

GitHub 디자이너 캐머런 맥피는 Octocat을 사용자 누구나 자기 모습을 볼 수 있는 캐릭터라고 설명했습니다

06 / 11

한 장으로 비교하면

Git

정체도구 (프로그램)

어디서내 노트북 안

무엇에저장 · 되돌리기 · 브랜치 나누기

비용무료 · 오픈소스

용량내 디스크만큼

GitHub

정체서비스 (웹사이트)

어디서인터넷

무엇에백업 · 공유 · 협업 · 공개

비용개인 사용자는 무료

용량파일당 100MB까지

VS

07 / 11

용량 제한을 자세히 살펴봅니다 →

무료지만, 크기 제한은 있습니다

 파일 하나

100MB

이보다 크면 올라가지 않습니다

50MB부터는 경고가 뜹니다

 웹 화면에서 올릴 때

25MB

브라우저로 끌어다 놓는

파일은 더 작아야 합니다

 저장소 하나

1GB

GitHub가 권하는 저장소 크기입니다

5GB를 넘기지 말라고 안내합니다

업로드 차단

동영상처럼 큰 파일은 저장소 밖에 따로 보관합니다

08 / 11

그렇다면 무료로 쓰는 GitHub의 몸값은 얼마였을까요 →

개발자 넷이 만든 GitHub는 10년 뒤 75억 달러에 팔렸습니다

한때 리눅스를 '암'이라 불렀던 마이크로소프트가, 리눅스를 위해 만든 Git을 쓰는 GitHub를 샀습니다

 만든 사람

크리스 완스트래스톰 프레스턴워너PJ 하이엇스콧 차콘

네 사람은 2007년 10월 개발을 시작해 2008년 4월 10일 정식으로 출시했습니다

 2018년 6월 4일 발표

75억 달러

마이크로소프트가 자사 주식으로 인수했습니다

당시 GitHub 사용자는 2,800만 명이 넘었습니다

 마이크로소프트는 왜 샀을까

① 오픈소스와 화해 업계 분석

발머 CEO는 리눅스를 적으로 봤지만,

나델라 CEO는

오픈소스를 끌어안았습니다

② 개발자 공식 발표

나델라 CEO는 "마이크로소프트는

개발자 우선 회사"라고 밝혔습니다

③ 클라우드 업계 분석

GitHub는 개발자를 MS 클라우드(Azure)로 이끄는 통로입니다

09 / 11

그 뒤 GitHub의 공개 코드는 AI의 학습 자료가 되었습니다 →

GitHub 코드를 배운 AI, 출처를 밝히지 않아도 될까요

2021년 6월

코딩 AI 비서

Copilot 공개

공개 저장소의 코드로 학습한 AI가 코드를 대신 써 줍니다

2022년 11월

개발자들의 소송

개발자들은 Copilot이 원작자 이름과 사용 조건을 빼고 자신들의 코드를 내놓는다고 주장했습니다

피고 · GitHub, MS, OpenAI

2024년 6월

1심, 출처 표시

청구 기각

법원은 Copilot이 내놓은 코드가 원본과 똑같은 복사본은 아니라고 봤습니다

2026년 9월

2심(항소심)도

개발자 측 패소

법원은 AI가 내놓은 코드를 새 결과물로 보고, 출처를 지운 것이 아니라고 판단했습니다

 아직 열린 쟁점

법원은 저작권 침해 여부를 판단하지 않았습니다

계약 위반 청구 2건은 1심에서 계속 심리 중입니다

 우리의 선택

공개 코드는 이미 AI 학습에 쓰였습니다

그래서 회사 코드는 비공개(Private)로 올립니다

10 / 11

이제 Git과 GitHub가 어떻게 이어지는지 정리합니다 →

Git과 GitHub는 이렇게 이어집니다

내 컴퓨터

작업 폴더

지금 만들고 고치는 파일이 있는 곳

내 컴퓨터

Git 기록

커밋한 기록이 순서대로 쌓입니다

인터넷

GitHub 저장소

프로젝트가 통째로 올라가는 곳

회사 코드는 비공개로

인터넷

웹 주소

저장소는 비공개로 남고, Vercel·Netlify가 띄운 사이트는 기본적으로 누구나 볼 수 있습니다

 커밋한 장 저장 푸시GitHub에 올리기 자동 배포

Git으로 기록하고 GitHub에 올리면, Vercel·Netlify가 웹사이트로 띄워 줍니다

11 / 11

5분 정리는 여기까지, 이제 직접 올려 봅니다 →

  1 / 11

  +

### GitHub에 올린 코드를 Vercel·Netlify가 자동으로 웹 주소로 띄워줍니다

  GitHub Pages https://내아이디.github.io/프로젝트이름/  →   Vercel https://내프로젝트.vercel.app/   Netlify https://내프로젝트.netlify.app/

이 네 가지만 기억하면 됩니다

① Git = 내 컴퓨터에서 파일이 바뀐 과정을 시점마다 저장해 두는 도구입니다. 문서의 버전 기록이라고 생각하면 됩니다.

② GitHub = 그 기록을 안전하게 보관하는 창고입니다. 코드용 구글 드라이브라고 보면 됩니다.

③ Vercel · Netlify = 창고에 있는 코드를 실제 웹사이트 주소로 띄워주는 배포 서비스입니다.

④ 내가 할 일 = 명령어를 외울 필요 없이 AI에게 자연어로 말하는 것뿐입니다. Claude Code든 Codex든 방법은 같습니다. 내가 만든 랜딩페이지와 대시보드, 데모를 개발자 없이 바로 공개할 수 있습니다.

Git과 GitHub, 이름이 비슷한데 무엇이 다른가요?

항목Git[바로가기 ↗](https://git-scm.com)GitHub[바로가기 ↗](https://github.com)

 최초 공개 시점 2005년 4월 2008년 4월 (정식 출시)

 어디에서 작동하나 내 노트북 안. 인터넷이 없어도 씁니다 인터넷. 접속해야 씁니다

 무엇에 쓰나 저장 · 되돌리기 · 브랜치 나누기 백업 · 공유 · 협업 · 공개

 비용이 드나 무료입니다. 오픈소스입니다 개인 사용자는 무료입니다. Team 요금제는 사용자당 월 4달러, 기업용 Enterprise 요금제는 사용자당 월 21달러입니다

 용량 제한이 있나 없습니다. 내 컴퓨터 저장 공간만큼 씁니다 있습니다. 무료여도 파일 하나가 100MB를 넘으면 올라가지 않습니다(웹 화면에서 직접 올릴 때는 25MB). 저장소 하나는 1GB 이하를 권장하고, 5GB를 넘기지 말라고 안내합니다. 동영상처럼 큰 파일은 따로 보관하는 편이 안전합니다

 내 코드가 보이나 내 컴퓨터에만 저장되어 외부에 공개되지 않습니다 공개(Public)와 비공개(Private)를 직접 고를 수 있습니다

 없으면 버전 관리가 되지 않습니다 노트북이 고장 나면 함께 사라집니다

  GitHub Team과 Enterprise 요금제, 무엇이 다른가요

Team · 사용자당 월 4달러

- 여러 명이 한 저장소를 함께 쓸 때 필요한 통제 수단이 Team부터 제공됩니다. 검토를 통과한 코드만 반영하는 PR 리뷰 필수 지정(PR은 "이 변경을 반영해 달라"는 요청서입니다), 정해진 사람만 고칠 수 있게 잠그는 브랜치 보호, 파일마다 책임자를 두는 코드 오너가 대표적입니다.

- 자동화 실행 시간(Actions)은 월 3,000분까지, 패키지 저장소는 2GB까지 쓸 수 있습니다. 기술 지원은 이메일로 받습니다.

Enterprise · 사용자당 월 21달러

- Team의 모든 기능에 전사 계정 관리가 더해집니다. 회사 계정으로 한 번에 로그인하는 SAML SSO와 퇴사 시 접근 권한이 자동 회수되는 SCIM 연동, 이 둘이 실무에서 가장 크게 체감되는 차이입니다.

- 계열사나 사업부별로 조직이 분산돼 있어도 엔터프라이즈 계정 하나로 통합해 관리할 수 있습니다.

- 감사 기록을 외부 보안 시스템으로 실시간 전송하는 감사 로그 스트리밍, 허용한 IP에서만 접속하게 막는 IP 허용 목록, 데이터를 저장할 국가를 고르는 기능이 들어갑니다. 금융·공공 부문이 요구하는 규제 대응 항목입니다. 가동률 99.9% 보장(SLA)도 이 등급부터 적용됩니다.

- 자동화 실행 시간은 월 50,000분, 패키지 저장소는 50GB로 늘어납니다. 각각 Team의 약 17배와 25배입니다.

선택 기준

- 소수 인원이 코드를 함께 관리하는 수준이라면 Team으로 충분합니다.

- 정보보안팀이 접근 권한 회수 기록과 감사 로그를 요구하는 단계라면 Enterprise가 필요합니다.

   왜 archive가 아니라 repository인가

- 어원이 다릅니다. repository는 라틴어 reponere(다시 놓다, 보관하다)에서 파생된 repositorium이 어원이며, 창고를 의미합니다. archive는 그리스어 arkheion(관청, 공문서 보관소)이 어원이며, 완결된 공식 기록을 보존하는 장소라는 의미를 처음부터 내포합니다.

- 버전 관리 도구의 오랜 관행입니다. 1990년 전후에 등장한 버전 관리 도구 CVS(Concurrent Versions System, 동시 버전 시스템)가 저장소를 repository라고 명명했고, 2000년의 후속 도구 Subversion(약칭 SVN)이 이 용어를 계승했으며, 2005년의 Git도 그대로 이어받았습니다. 같은 시기의 상용 도구인 Perforce는 depot(창고), SourceGear 사의 Vault는 vault(금고)라는 명칭을 사용했습니다. 명칭은 다르지만 모두 물건을 넣고 꺼내는 창고를 비유한 것입니다.

- archive는 이미 다른 의미로 사용되고 있었습니다. 유닉스에서 archive는 여러 파일을 하나로 묶은 파일을 지칭합니다. tar는 tape archive의 약어이고, zip 파일 역시 archive라고 부릅니다.

- 그래서 Git에서는 두 용어의 역할이 구분됩니다. git archive는 특정 시점의 파일을 tar나 zip 하나로 묶어 이력 없이 내보내는 명령이고, GitHub의 Archive repository는 저장소를 읽기 전용으로 동결하는 기능입니다. repository는 도서관처럼 대출과 반납이 반복되는 공간이고, archive는 서고에 봉인한 상자입니다. 버전 관리의 본질은 check in과 check out, 즉 반복되는 출입이므로 repository라는 이름이 채택되었습니다.

   만든이와 이름의 유래

항목Git[바로가기 ↗](https://git-scm.com)GitHub[바로가기 ↗](https://github.com)

만든이리누스 토르발스

핀란드 헬싱키 출신. 1991년 헬싱키대학교 21살 학생 때 취미로 리눅스 커널을 만들었습니다. 여기에 리처드 스톨먼이 1983년에 시작한 GNU 프로젝트의 프로그램들이 합쳐져 GNU/Linux 운영체제가 됐습니다.톰 프레스턴 워너 · 크리스 완스트라스 · PJ 하이엇 · 스콧 샤콘

네 사람 모두 샌프란시스코의 소프트웨어 엔지니어였습니다. 프레스턴 워너는 아바타 서비스 그라바타를 만들어 오토매틱에 매각했고, 하이엇은 CNET을 거쳐 컨설팅 회사를 세웠습니다. 마지막에 합류한 샤콘은 Git 대표 교재 Pro Git의 저자입니다.

출시 시점2005년 4월 첫 공개

2005년 12월 정식 버전 1.02008년 4월 정식 출시

탄생 배경리눅스 커널 개발자들은 2002년부터 상용 도구 BitKeeper를 무료 라이선스로 썼습니다. 조건은 경쟁 도구를 만들지 않고 통신 방식을 역분석하지 않는 것이었습니다. 2005년 개발자 앤드루 트리젤이 통신 방식을 분석하는 도구를 만들자 무료 제공이 끊겼습니다. 토르발스는 직접 개발에 착수해 열흘 만에 기본 구조를 완성했습니다. 수천 명이 동시에 코드를 주고받아도 빠르고, 기록이 손상되지 않는 데 집중했습니다.2007년 가을 샌프란시스코의 한 술집에서 프레스턴 워너가 친구 완스트라스에게 Git을 웹에서 쉽게 쓸 수 있는 서비스를 만들자고 제안했습니다. Git은 강력하지만 다루기가 너무 번거로웠기 때문입니다. 두 사람은 다음 날 아침 첫 코드를 올렸고, 석 달 동안 매주 토요일에 만나 기능을 개발하고 요금제를 정했습니다.

이름의 뜻영국 속어로 "고집불통", "밥맛" 정도의 뜻입니다. 토르발스는 "나는 자아도취적인 놈이라 내가 만드는 프로젝트에는 전부 내 이름을 붙인다. 먼저 리눅스, 이번엔 깃"이라고 농담했습니다.Git(버전 관리 도구) + Hub(중심). Git 저장소를 한곳에 모은다는 뜻입니다.

그 뒤 이야기지금도 리눅스 커널을 비롯해 가장 널리 쓰이는 버전 관리 도구입니다. 무료 오픈소스로 남아 있습니다.2018년 마이크로소프트가 75억 달러에 인수했습니다. 스티브 발머 시절 리눅스를 "암 같은 존재"라 부르던 회사가 사티아 나델라 체제에서 애저 클라우드 확장을 위해 오픈소스를 택한 결과입니다. 당시 개발자 3천만 명이 모여 있었습니다.

다른 선택지Mercurial, SubversionGitLab, Bitbucket

AI 학습 데이터와 코파일럿 소송

- 2021년 6월 깃허브는 오픈AI와 함께 만든 코드 자동완성 도구 코파일럿을 시험 공개했습니다. 공개된 수십억 줄의 코드를 학습한 도구입니다. 2022년 11월 개발자들은 코파일럿이 원저작자와 라이선스 표시를 누락해 오픈소스 라이선스를 위반한다며 깃허브·마이크로소프트·오픈AI를 상대로 집단소송을 제기했습니다.

- 2024년 6월 미국 캘리포니아 북부 연방지방법원은 저작권 관리정보를 제거했다는 DMCA(디지털 밀레니엄 저작권법) 청구를 기각했습니다. 원본과 동일한 복제물 사례를 원고가 충분히 제시하지 못했다는 판단입니다. 오픈소스 라이선스를 어겼다는 계약 위반 청구는 살아남아 소송이 이어집니다. AI 학습이나 코드 사용 전반이 적법하다고 판결한 것은 아닙니다.

- 원고는 DMCA 기각에 항소했고, 2026년 2월 11일 제9연방항소법원에서 구두변론이 열렸습니다. 쟁점은 저작권 관리정보 제거를 문제 삼으려면 코드가 원본과 반드시 같아야 하는지입니다.

그래서 둘은 어떻게 이어지나요?

내 컴퓨터

작업 폴더

지금 만들고 고치는 파일이 있는 곳입니다.

 커밋 Commit →↓ 지금 상태를 저장

내 컴퓨터

Git 기록

저장한 시점이 순서대로 쌓입니다. 인터넷이 없어도 됩니다.

 푸시 Push →↓ 인터넷으로 올리기

인터넷

GitHub 저장소

프로젝트 하나가 통째로 올라가는 폴더입니다. 줄여서 레포라고 부릅니다.

## GitHub 가입하기

이 단계의 목표

GitHub 계정을 만들고 첫 번째 저장소를 생성합니다

1

### github.com 접속 → Sign up

[github.com](https://github.com)에 접속해서 Sign up 버튼을 클릭합니다. 이메일, 비밀번호, 사용자명을 입력하면 끝입니다.

사용자명은 나중에 URL에 포함됩니다. 기억하기 쉬운 영문으로 만드세요. (예: honggildong → hong.github.io)

2

### 새 저장소 만들기

로그인 후 왼쪽 상단 New 버튼을 클릭합니다.

 # 저장소 설정 Repository name: my-project ← 프로젝트 이름 입력 Public / Private 선택 ← 공개 or 비공개 [Create repository] 클릭

※ Private(비공개)으로 만들면 나만 볼 수 있습니다.

3

### AI 코딩 도구와 GitHub 연결하기

AI가 내 저장소에 접근하려면 인증이 필요합니다. 컴퓨터에 한 번만 해 두면 되고, Claude Code와 Codex가 그 인증을 함께 씁니다. 명령어를 외울 필요는 없습니다. 폴더 이동과 설치는 AI에게 시키고, 로그인 질문 몇 개와 브라우저 승인만 직접 하면 됩니다.

 방법 A GitHub CLI로 로그인 권장

GitHub가 공식으로 만든 gh 명령어를 설치하고 한 번 로그인하면 끝납니다. 인증 키는 GitHub가 알아서 발급해 윈도우 자격 증명 관리자(맥은 키체인)에 넣어 줍니다.

 # AI에게 이렇게 말하세요 > 터미널을 열어서 이 프로젝트 폴더로 이동한 다음 GitHub CLI(gh)를 설치해 줘 > 설치가 끝나면 gh auth login을 실행해 줘

※ 폴더 이동과 설치는 AI가 자동으로 실행합니다. 아래 명령어는 AI가 무엇을 실행하는지 확인하는 참고용입니다. 로그인 단계만 다릅니다. gh auth login은 질문에 답을 골라야 하므로 AI가 터미널 창에 띄워 주면 아래 순서대로 직접 고릅니다.

윈도우 Windows

 # PowerShell에 입력 winget install --id GitHub.cli

winget은 Windows 10·11에 기본으로 들어 있습니다. "winget을 찾을 수 없다"고 나오면 Microsoft Store에서 앱 설치 관리자를 업데이트한 뒤 다시 실행하세요. 설치한 뒤에는 터미널을 껐다 켜야 명령어가 잡힙니다.

맥 macOS

 # Homebrew가 없다면 먼저 (한 번만) /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

 # 터미널에 입력 brew install gh

맥에는 Homebrew가 기본 탑재되어 있지 않으므로 첫 번째 명령어로 먼저 설치합니다. 설치 중에 맥 로그인 비밀번호를 요구하면 입력하고 Enter를 누릅니다. Homebrew가 이미 설치되어 있다면 첫 번째 명령어는 생략하고 brew install gh만 실행합니다. brew -v를 입력해 버전 번호가 출력되면 설치된 상태입니다.

 # 윈도우·맥 모두 같은 명령어 gh auth login

※ 질문이 차례로 나옵니다. 방향키로 고르고 Enter를 누르세요. 버전에 따라 문구가 조금 다를 수 있습니다.

- What account do you want to log into? → GitHub.com

- What is your preferred protocol for Git operations? → HTTPS

- Authenticate Git with your GitHub credentials? → Yes

- How would you like to authenticate? → Login with a web browser

- 화면에 XXXX-XXXX 형태의 여덟 자리 코드가 뜹니다. 그대로 복사하고 Enter를 누르면 브라우저가 열립니다.

- 브라우저에 코드를 붙여넣고 Authorize github 버튼을 누르면 연결이 끝납니다.

 # 잘 됐는지 확인 gh auth status

※ ✓ Logged in to github.com account 내아이디가 보이면 연결된 것입니다.

 연결을 끊고 싶다면 · 터미널에 gh auth logout을 입력하면 됩니다. GitHub 웹에서 지우려면 Settings → Applications → Authorized OAuth Apps → GitHub CLI → Revoke를 누르세요.

   방법 B Personal Access Token 발급 까다로운 방법

설치 없이 브라우저만으로 인증 키를 직접 만드는 방법입니다. 화면 위치가 자주 바뀌니 천천히 따라가세요.

1

#### 프로필 클릭

우측 상단 프로필 사진 → Settings

2

#### Developer Settings

왼쪽 맨 하단 Developer settings 클릭

3

#### 토큰 생성

Personal access tokens → Tokens (classic) → Generate new token

 # 토큰 설정 Note: claude-code-access ← 이름 (자유롭게) Expiration: 30 days ← 짧을수록 안전합니다 Scopes: repo 만 체크 ← 나머지는 그대로 두세요 [Generate token] → 토큰 복사 ← 벗어나면 다시 못 봅니다

토큰을 다룰 때 지킬 네 가지

- 유효기간은 30일로 짧게 잡으세요. 만료되면 같은 방법으로 다시 만들면 됩니다.

- 권한은 repo 하나만 체크하세요. 목록에 체크박스가 수십 개 보여도 나머지는 손대지 않습니다. 권한이 적을수록 새어 나갔을 때 피해가 작습니다.

- 메신저·메일·메모 앱에 붙여넣지 마세요. 바로 쓰는 것이 원칙입니다.

- 조금이라도 이상하면 지우세요. Settings → Developer settings → Tokens (classic)에서 해당 토큰을 Delete하면 그 즉시 폐기됩니다.

## AI로 올리기

이 단계의 목표

AI 코딩 도구에서 프로젝트를 GitHub에 올립니다

 시작 전 확인: Claude Code나 Codex가 실행 중이어야 하고, 작업할 프로젝트 폴더가 열려 있어야 합니다. 인증은 앞의 가입하기에서 이미 끝났으니 따로 준비할 것은 없습니다.
  앞에서 방법 B(토큰)를 골랐다면 · 토큰을 AI에게 전달하기

방법 A(gh auth login)로 연결했다면 이 칸은 볼 필요가 없습니다. 토큰을 직접 만들었다면, AI가 GitHub에 처음 접근할 때 이렇게 말하세요.

 # AI에게 이렇게 말하세요 > GitHub Personal Access Token은 ghp_xxxxxxxxxxxx야 > 이 키는 절대 메모리나 파일에 저장하지 마

※ ghp_로 시작하는 긴 문자열이 토큰입니다. 위 예시 자리에 복사한 값을 그대로 붙여넣으세요.

 여기서 꼭 지킬 것 · 토큰은 이 대화에서만 쓰고, 코드나 파일에 저장하지 마세요. 오늘 작업이 끝나면 GitHub에서 토큰을 지워도 됩니다. 다음에 필요하면 다시 만들면 됩니다. 남겨 둔 채 잊는 것보다 그 편이 안전합니다.

1

### 처음 올릴 때

이미 내 컴퓨터에 프로젝트가 있다면 AI에게 말하세요:

 # AI에게 이렇게 말하세요 > 이 프로젝트를 GitHub에 올려줘 > GitHub 주소는 https://github.com/내아이디/my-project 야

GitHub에 있는 프로젝트를 내려받고 싶다면:

 # AI에게 이렇게 말하세요 > https://github.com/내아이디/my-project 클론해줘

2

### 이후에 수정할 때

하고 싶은 것AI에게 이렇게 말하세요

변경사항 저장하기"지금까지 바꾼 거 커밋해줘"

GitHub에 올리기"GitHub에 푸시해줘"

최신 코드 받기"GitHub에서 최신 코드 받아줘"

이전 버전으로 돌리기"마지막 커밋 전으로 되돌려줘"

## 저장소 메뉴

### 저장소 메뉴, 어디에 무엇이 있나요?

화면 속 메뉴나 아래 설명에 마우스를 올려 보세요. 해당 메뉴에 빨간 테두리가 표시됩니다. 모바일에서는 설명을 누르면 해당 위치로 화면이 이동합니다.

 ![airoasting의 blog 저장소 화면. Code, Issues, Pull requests, Agents, Actions, Projects, Wiki, Security and quality, Insights, Settings 메뉴가 순서대로 있습니다.](https://bizroasting.com/assets/img/github-repository-menu.png)

실제 화면: airoasting / blog · 메뉴는 저장소 설정과 접근 권한에 따라 달라질 수 있습니다.

## GitHub Pages로 공개하기

이 단계의 목표

GitHub의 무료 호스팅 기능을 켜서 내 URL로 사이트가 열리는 것을 확인합니다

GitHub Pages 활성화 3단계

1

#### Settings 클릭

해당 저장소 상단 탭에서 Settings 선택

2

#### Pages 메뉴

왼쪽 사이드바에서 Pages 클릭

3

#### branch 선택 후 Save

main 또는 master 브랜치 선택 → Save

1~2분 후 공개됩니다

저장소에 올린 HTML/CSS/JS 파일이 그대로 웹사이트로 공개됩니다. 주소는 다음과 같습니다.

 https://내아이디.github.io/프로젝트이름/

예) 아이디 hong, 저장소 my-site → https://hong.github.io/my-site/

## Vercel·Netlify로 배포하기

GitHub Pages·Vercel·Netlify 비교

항목GitHub Pages[바로가기 ↗](https://pages.github.com/)Vercel[바로가기 ↗](https://vercel.com)Netlify[바로가기 ↗](https://www.netlify.com)

설명GitHub 저장소의 파일을 웹사이트로 공개하는 기능Next.js(React 기반 개발 도구)를 만든 회사가 운영하는 배포 플랫폼정적 사이트(Jamstack) 배포를 대중화한 원조 서비스

출시 시점2008년 12월2016년 4월 (Now로 첫 공개)

2020년 4월 Vercel로 이름 변경2015년 4월

만든이톰 프레스턴 워너·크리스 완스트라스·PJ 하이엇기예르모 라우치매트 빌만·크리스천 바흐

이름의 뜻·어원GitHub에 웹페이지를 공개하는 기능으로, Pages는 ‘페이지들’이라는 뜻입니다.라틴어 vertere(베르테레, 돌다·전환하다)에서 따온 신조어로, "전환·움직임"의 어감을 담았습니다.Net(네트워크·인터넷) + -ify(~하게 만들다)의 조합입니다. "웹 배포를 누구나 쉽게"라는 의미를 담았습니다. 'Jamstack'이라는 용어를 만든 회사로도 알려져 있습니다.

추천 용도소개 페이지·강의 자료·문서·포트폴리오를 별도 배포 서비스 가입 없이 공개할 때[Next.js·React](https://bizroasting.com#ref-react)로 만든 앱을 배포하거나 서버에서 실행할 함수를 함께 운영하는 프로젝트사이트에 입력 폼·인증·함수를 연결하고 빌드 플러그인을 활용하려는 프로젝트

자동 배포·미리보기설정한 브랜치나 Actions로 자동 배포. PR별 미리보기는 별도 구성이 필요합니다.GitHub 푸시 시 자동 빌드 + 브랜치·PR별 Preview URL 제공동일하게 푸시 시 자동 빌드 + Deploy Preview 제공

무료 플랜·기본 주소GitHub Free의 공개 저장소에서 무료 · 계정.github.io/저장소/Hobby 플랜(개인·비상업) · 프로젝트.vercel.appFree 플랜(개인·소규모) · 프로젝트.netlify.app

서버에서 코드 실행지원하지 않습니다. 브라우저에서 실행되는 JavaScript는 사용할 수 있습니다.Vercel Functions로 실행합니다.Netlify Functions로 실행합니다.

이 단계의 목표

GitHub와 Vercel(또는 Netlify)을 연동해 푸시하면 자동으로 사이트가 갱신되도록 만듭니다

1

### vercel.com 접속 → GitHub로 로그인

[vercel.com](https://vercel.com)에 접속해서 Sign Up 또는 Continue with GitHub을 클릭합니다. GitHub 계정과 자동으로 연동되므로 새로 회원가입을 하지 않아도 됩니다.

권한 요청 화면이 뜨면 Authorize Vercel을 눌러 저장소 접근을 허용합니다. 처음에는 무료 Hobby 플랜으로 시작해도 충분합니다.

2

### 새 프로젝트 만들기 (Import)

대시보드 우측 상단 Add New ▾ → Project를 누르고, GitHub 저장소 목록에서 앞에서 만든 저장소를 찾아 Import 버튼을 클릭합니다.

 # Import 화면 설정 Project Name: my-project ← 자동 입력됨 Framework Preset: Other ← 정적 HTML이면 그대로 Root Directory: ./ ← 보통 그대로 둠 [Deploy] 클릭

※ Next.js · React · Vite 같은 프레임워크는 Vercel이 자동으로 감지합니다.

3

### 1~2분 대기 → 배포된 URL 확인

Deploy를 누르면 1~2분 안에 빌드가 끝납니다. 이어서 Vercel이 무료 도메인을 자동으로 만들어 줍니다. 만들어진 URL은 다음과 같은 형식입니다.

 https://프로젝트이름.vercel.app/

예) 저장소 my-site → https://my-site.vercel.app/

내 도메인이 있다면 Settings → Domains에서 직접 연결할 수 있습니다.

4

### 이후엔 푸시만 하면 자동 재배포

한 번 연동해두면, 다음부터는 AI에게 푸시해달라고 말하는 것만으로 사이트가 자동으로 갱신됩니다.

 # AI에게 이렇게 말하세요 > 변경사항 커밋하고 GitHub에 푸시해줘

※ 푸시 직후 Vercel 대시보드에서 빌드 진행 상황을 실시간으로 볼 수 있습니다.

Netlify도 똑같습니다

Netlify를 골랐어도 순서는 위 Vercel과 거의 같습니다. 버튼과 메뉴 이름만 다릅니다.

단계VercelNetlify

1. 로그인vercel.com → Continue with GitHub[netlify.com](https://www.netlify.com) → Sign up / Log in with GitHub

2. 불러오기Add New ▾ → Project → ImportAdd new site → Import an existing project → GitHub 저장소 선택

3. 배포Framework·Root 확인 → Deploy빌드 설정(정적이면 비워둠) → Deploy site

4. 주소프로젝트.vercel.app프로젝트.netlify.app

Netlify도 한 번 연동하면 이후엔 GitHub에 푸시만 해도 자동으로 재배포됩니다. 내 도메인은 Site settings → Domain management에서 연결합니다.

## 더 알고 싶다면

꼭 알아야 할 용어

용어쉬운 설명

repository / repo (저장소)프로젝트 파일과 변경 기록을 보관하는 공간입니다. repository를 줄여 repo라고 부릅니다.

push (푸시)내 컴퓨터에 저장한 커밋을 GitHub에 올리는 작업입니다.

pull (풀)GitHub의 변경 내용을 받아 내 작업에 반영하는 작업입니다.

clone (클론)저장소의 파일과 변경 기록을 내 컴퓨터로 복사하는 작업입니다.

fork (포크)GitHub의 저장소를 내 계정에 복사해 별도로 작업하는 기능입니다.

commit (커밋)변경 내용을 Git 기록에 저장하는 작업입니다.

branch (브랜치)기존 코드에서 분리해 수정할 수 있는 별도의 작업 버전입니다.

PR (풀 리퀘스트)수정한 코드를 반영해 달라고 요청하고 검토받는 기능입니다.

conflict (충돌)서로 다른 변경 내용을 Git이 자동으로 합치지 못해 직접 정리해야 하는 상태입니다.

.gitignoreGit이 새로 추적하지 않을 파일과 폴더의 규칙을 적는 파일입니다.

React와 Next.js는 무엇인가요?

 용어 쉬운 설명 대표 사용 사례

 React

(리액트) 2013년 페이스북(Meta)이 공개한 자바스크립트 라이브러리입니다. 화면을 작은 부품(컴포넌트)으로 만들어 조립하고, 여러 페이지에서 재사용합니다. 인스타그램, 넷플릭스, 에어비앤비, 페이스북

 Next.js

(넥스트JS) 2016년 Vercel이 공개한 React 기반 프레임워크입니다. React에 서버 처리, 페이지 주소 관리, 이미지 최적화, 검색 엔진 최적화(SEO) 기능을 추가한 개발 도구입니다. 틱톡, 노션, 트위치, 훌루

워크트리(worktree) · 한 저장소를 여러 폴더에서 동시에 다루기

워크트리는 같은 저장소를 여러 폴더에서 동시에 작업할 수 있게 하는 기능입니다.

언제 쓰면 좋을까요?

 자주 쓰이는 상황

- 개발 도중 긴급 수정 요청이 왔을 때, 작업을 멈추지 않고 옆 폴더에서 바로 처리

- 동료 코드를 검토할 때, 내 폴더는 그대로 둔 채 별도 폴더에서 확인

- AI에게 작업을 맡길 때, 내 폴더와 분리해 충돌 예방

핵심 명령어 3가지

 # 새 워크트리 만들기 (fix-login 브랜치를 ../my-project-fix 폴더로 펼침) git worktree add ../my-project-fix fix-login # 현재 만들어진 워크트리 목록 보기 git worktree list # 다 쓴 워크트리 정리하기 git worktree remove ../my-project-fix

※ add 뒤에는 새로 만들 폴더 경로와 그 폴더에서 사용할 브랜치 이름을 차례대로 적습니다.

 주의 · 같은 브랜치를 두 폴더에서 동시에 열 수는 없습니다.

### 이제 내 프로젝트로 직접 띄워볼 차례입니다

 [← 실전 과제로 돌아가기](https://bizroasting.com/vibe-coding-tasks.html) [CLI로 더 깊이 →](https://bizroasting.com/checklist.html)

또는 바로 시작하기 · [GitHub](https://github.com) · [Vercel](https://vercel.com) · [Netlify](https://www.netlify.com)

 [ ←목록으로 ](https://bizroasting.com/index.html#section-2)

1 / 7
