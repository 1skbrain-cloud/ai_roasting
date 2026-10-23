# 클로드 코드 해커톤 수상작

원본: https://bizroasting.com/hackathon.html

---

클로드 코드 해커톤 수상작 | AI ROASTING         [본문으로 건너뛰기](https://bizroasting.com#main)

 Hackathon

## 전 세계가 클로드 코드로 무엇을 만들었나

앤트로픽은 새 Opus 모델이 나올 때마다 클로드 코드 해커톤을 엽니다. 변호사, 심장내과 의사, 전자기기 수리 기술자, 목수의 아들, 음악가까지 개발이 본업이 아닌 사람들이 짧게는 하루, 길게는 한 주 만에 작동하는 제품을 만들어 냈습니다. Opus 4.6부터 4.8까지 세 번의 해커톤에서 뽑힌 우승작을 한자리에 모았습니다. 각 시리즈의 공식 발표 원문은 제목 아래 링크로 연결했습니다.

 Built with Opus 4.65

2026.2.10~16 · 13,000여 명 지원 · 277개 프로젝트 제출 · [공식 발표 보기 ↗](https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon)

 [![CrossBeam 데모 화면](https://bizroasting.com/assets/hackathon/blog/crossbeam.jpg)](https://www.youtube.com/watch?v=jHwBkFSvyk0) [GitHub↗](https://github.com/mikeOnBreeze/cc-crossbeam)

 1

CrossBeam

Mike Brown · 캘리포니아 개인상해 변호사

- 캘리포니아에서는 건축 허가 1차 제출의 90% 이상이 반려되고 평균 6개월씩 늦어져, 주택 소유주가 3만 달러를 고스란히 떠안습니다. 대부분 서명 누락이나 잘못된 법조항 인용 같은 행정적 문제 때문입니다.

- 설계도와 보정 요청서를 끌어다 놓으면, 여러 서브에이전트가 문서를 나눠 읽어 도면의 위치 정보를 정리하고, 보정 항목마다 전담 에이전트를 붙여 20분 만에 통과에 필요한 작업 계획을 만듭니다.

- 지자체는 제출된 허가를 일괄 처리하며 보정 요청서 초안을 자동 생성합니다. 제작자는 코드를 직접 쓰지 않았고, 2029년까지 허가 8,900여 건이 필요한 부에나파크市가 도입을 검토 중입니다.

 [![Elisa 데모 화면](https://bizroasting.com/assets/hackathon/blog/elisa.jpg)](https://www.youtube.com/watch?v=rsUaz_QAK6o) [GitHub↗](https://github.com/zoidbergclawd/elisa)

 2

Elisa

Jon McBee · 12살 딸을 둔 개발자 아버지

- 중학생이 마이크로컨트롤러를 직접 다뤄 볼 만한 마땅한 도구가 없습니다. 터미널 환경은 어린 학생에게 너무 어렵습니다.

- 기본 블록(목표·요구사항·에이전트·스킬·규칙·포털·배포)을 끼워 맞추면, 설계안을 잘게 나눠 Claude Code가 실제 코드를 작성합니다. 나이에 맞춰 개념을 풀어 주는 학습 기능도 들어 있습니다.

- 30시간 만에 코드 3만 9천여 줄과 테스트 1,500여 개를 만들어 냈고, 첫 사용자인 12살 딸은 코드 한 줄 직접 쓰지 않고도 과학 박람회 출품작에 들어갈 마이크로컨트롤러(소형 제어 칩)에 프로그램을 써넣어 작동시켰습니다.

 [![postvisit.ai 데모 화면](https://bizroasting.com/assets/hackathon/blog/postvisit.jpg)](https://youtu.be/V29UCOii2jE)

 3

postvisit.ai

Michal Milewski · 심장내과 의사 (벨기에 병원 과장)

- 환자가 겪는 어려움은 대개 진료가 끝난 뒤에 시작되지만, 의사는 다음 진료까지 환자 상태를 들여다볼 방법이 없습니다.

- 진단을 쉬운 말로 풀어 주고 진료 기록과 AI 받아쓰기 내용을 분석하며, 의사의 확인을 거쳐 학술 자료와 전체 건강 기록에서 관련 임상 근거를 찾아 줍니다.

- 환자는 자기 치료를 더 또렷이 이해하고, 의사는 건강 기록과 진료 데이터를 모아 다음 진료까지 환자 상태를 살핍니다.

 [![TARA 데모 화면](https://bizroasting.com/assets/hackathon/blog/tara.jpg)](https://www.youtube.com/watch?v=GFCrXehS1DE) [GitHub↗](https://github.com/Kye256/tara-transport-assessment)

 4

TARA

Kyeyune Kazibwe · 우간다 인프라 엔지니어

 Keep Thinking 상

- 우간다의 전통적 도로 타당성 조사는 100만~400만 달러가 들고 9~14개월이 걸리며, 정작 지역사회에 미치는 영향은 반영하지 못합니다.

- Opus 4.6의 영상 인식 능력으로 블랙박스 영상을 한 장면씩 분석해 노면 상태와 손상 형태, 보행자·자전거·노점을 가려내고, 도로를 상태별로 나눠 보수 비용과 NPV·현금흐름·민감도 분석까지 자동으로 계산합니다.

- 누가 혜택을 보는지 따지는 형평성 점수까지 담은 PDF 보고서를 몇 주가 아니라 5시간 만에 만듭니다.

 [![Conductr 데모 화면](https://bizroasting.com/assets/hackathon/blog/conductr.jpg)](https://www.youtube.com/watch?v=X6CqJoyj0kI) [GitHub↗](https://github.com/nanassound/conductr)

 5

Conductr

Asep Bagja Priandana · 에스토니아 거주 뮤지션

 Creative Exploration 상

- 연주 흐름을 끊지 않고 실시간으로 반응해 주는 AI 합주 도구가 음악가에게는 없었습니다.

- Claude를 가상 밴드 멤버로 세우는 브라우저 MIDI 악기입니다. 컨트롤러로 코드를 연주하면 Claude가 이를 읽어 드럼·베이스·멜로디·화성 4트랙을 실시간으로 만들고, "펑키하게 해줘", "클라이맥스로 끌어올려" 같은 말로 연주 도중 편곡을 바꿉니다.

- WebAssembly로 컴파일한 C 엔진이 15밀리초마다 음을 만들어 끊김이 느껴지지 않으며, JavaScript와 WebAssembly 약 4,800줄로 구현했습니다.

 Built with Opus 4.76

2026.4.21~27 · 20,000여 명 지원 · 500명 선발 · 약 250개 제출 · [공식 발표 보기 ↗](https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon)

 [![Medkit 데모 화면](https://bizroasting.com/assets/hackathon/medkit.jpg)](https://www.youtube.com/watch?v=6bN6hnx-A2A) [GitHub↗](https://github.com/bedriyan/medkit-app)

 1

Medkit

Bedirhan Keskin · 의사 출신 소프트웨어 엔지니어 (이스탄불)

- 레지던트는 충분한 사례 경험 없이 실제 환자로 연습하게 됩니다. "응급실에 환자 50명이 밀려 있는데, 배운 적 없는 사례를 실제 환자에게 처음 시도하게 된다"는 문제입니다.

- Claude Managed Agents로 게임처럼 꾸민 가상 진료실에서 문진·검사 지시·영상 판독·진단·처방을 연습하게 하고, 음성 엔진·콘텐츠 생성·3D 게임·핵심 앱을 Claude Code 세션 4개로 나눠 만들었습니다.

- 마지막에는 평가 에이전트가 전문의 시험관과 같은 공인 임상 지침으로 진료 전 과정을 채점하며, 이스탄불의 의대 3곳과 한 제약사가 시범 도입을 시작합니다.

 [![Wrench Board 데모 화면](https://bizroasting.com/assets/hackathon/wrenchboard.jpg)](https://www.youtube.com/watch?v=OZ2D_p82z6w) [GitHub↗](https://github.com/Junkz3/wrench-board)

 2

Wrench Board

Alexis Chapellier · 전직 전자기기 수리 기술자 (프랑스 Reignier-Ésery)

- 혼자 일하는 수리 기술자는 마땅한 분석 도구 없이 복잡한 회로 기판 고장을 짚어내야 합니다.

- 회로도와 보드뷰를 올리고 증상을 설명하면, Opus 4.7이 회로도를 읽어 전체 회로를 하나의 그림으로 잇고, 측정할 지점을 정확히 짚은 뒤 측정값에 따라 원인을 좁혀 갑니다.

- Claude Design으로 역할을 나눠 시제품을 만들고 Claude Code 멀티 에이전트 모드로 완성했으며, 보드뷰에 부품이 하나씩 켜지며 원인을 짚어 가는 과정을 그대로 보여 줍니다.

 [![Maieutic 데모 화면](https://bizroasting.com/assets/hackathon/maieutic.jpg)](https://www.youtube.com/watch?v=IJ9FyX2xwWA)

 3

Maieutic

Paula Vásquez-Henríquez · 칠레 콘셉시온 Universidad del Desarrollo 컴퓨터과학 교수

- 학생이 AI로 코드를 뽑아내지만 정작 그 코드가 무슨 일을 하는지는 모릅니다. 자동완성이 스스로 생각해 볼 기회를 너무 일찍 앗아 갑니다.

- 코드를 쓰기 전에 프로그램이 무엇을 해야 하는지 먼저 쉬운 말로 적게 하고, Claude가 꼬치꼬치 되물으며 설명이 충분히 구체적이어질 때까지 편집기를 잠가 둡니다.

- 핵심 기능인 Intent-Diff Review는 처음 적은 설명과 최종 코드를 견줘 차이를 drift·revision·bug로 나누고, 교수에게는 학생별 사고 흐름 요약을 대시보드로 보여 줍니다.

 [![Virtual Puppet Theater 데모 화면](https://bizroasting.com/assets/hackathon/puppet.jpg)](https://www.youtube.com/watch?v=qLuGU4PQNss) [GitHub↗](https://github.com/rhmoller/virtual-puppet-theater)

 4

Virtual Puppet Theater

Rene Hangstrup Møller · 풀스택 개발자

 Most Creative Use of Opus 4.7

- Opus 4.7의 공간 인식 능력이 실시간 놀이에서 어디까지 통하는지 시험한 작품입니다.

- 웹캠 영상과 목소리를 실시간 인형극으로 바꾸는 브라우저 앱입니다. MediaPipe 손 추적과 Three.js 3D 렌더링이 60fps로 사용자 동작을 그대로 따라 움직입니다.

- WebSocket으로 Opus 4.7과 연결한 또 다른 인형이 사용자와 대화하고, 음성 명령으로 배경을 바꾸며 3D 소품을 즉석에서 만들어 냅니다. 소스 코드는 MIT 라이선스로 공개했습니다.

 [![MaestrIA 데모 화면](https://bizroasting.com/assets/hackathon/maestria.jpg)](https://www.youtube.com/watch?v=rkH4AjoTL5Q)

 5

MaestrIA

Benjamin Torralbo · 목수 장인(Maestro Mayor)의 아들이자 견습 출신 (칠레 칠로에)

 Keep Thinking 상

- 일반인은 집수리 문제를 짚어내거나 적정 가격을 가늠하기 어렵고, 솜씨 좋은 기술자는 정작 자기를 알릴 통로가 없습니다.

- 문제를 사진으로 찍고 음성이나 글로 설명한 뒤 위치를 알려 주면, Claude가 추론 과정을 실시간으로 보여 주며 어디가 고장났는지, 필요한 자재, 심각도(1~5단계), 예상 비용, 걸리는 시간을 정리해 알려 줍니다.

- 아버지의 장인 지식을 진단 규칙 17개, 칠로에 목재 7종, 현장 용어 16개, 기준 가격 19개로 정리해 진단마다 반영하면서 정확도를 74%에서 81%로 끌어올렸고, 가까운 장인 지도와 WhatsApp 메시지 초안까지 만들어 줍니다.

 [![ARIA (Adaptive Runtime Intelligence) 데모 화면](https://bizroasting.com/assets/hackathon/aria.jpg)](https://www.youtube.com/watch?v=Hen24w2Jyz4) [GitHub↗](https://github.com/zestones/Aria)

 6

ARIA (Adaptive Runtime Intelligence)

Idriss Benguezzou, Adam Hnaien · 프랑스 산업 소프트웨어 엔지니어(데이터/AI 석사), 독학 공학 전공 학생

 Best Use of Claude Managed Agents

- 공장 설비 정비는 베테랑의 감에 기대 왔고, 값싸고 빠르게 들일 수 있는 예측 정비 시스템은 드뭅니다.

- 제조사 매뉴얼 PDF를 올리고 간단한 설정 질문 4개에 답하면 15분 만에 공장 상태가 파악되고, 이후 격리 실행과 작업 연결은 Claude Managed Agents가 맡습니다.

- 에이전트 5개가 실시간 신호를 지켜보다 고장을 감지하거나 예측하면, 필요한 부품·고장 유형·긴급도·조치 시점을 정리한 작업 지시서를 만듭니다. 초기 코드의 약 80%는 Claude Code가 작성했습니다.

 Opus 4.8 Build Day3

2026.6.13 · 1,500여 명 지원 · 310명 참가 · [공식 발표 보기 ↗](https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon)

 [![Tekton 데모 화면](https://bizroasting.com/assets/hackathon/blog/tekton.jpg)](https://www.youtube.com/watch?v=7UgtfcKL0Zg) [GitHub↗](https://github.com/tangxiya-star/Tekton)

 1

Tekton

Holly Tang, Austin Burgess · 디자이너 / 창업가(Pearl)

- 오래된 목조 건축물이 불에 타 사라질 때마다 수백 년 쌓인 건축 지식과 장인 기술도 함께 사라집니다.

- Claude가 도면·시공 문서·사진·다이어그램을 모아 339단계로 3D 모델을 쌓아 올리고, 검증 전용 서브에이전트가 따로 떨어진 환경에서 부재 하나하나의 위치를 채점합니다.

- 검사 20개를 모두 통과할 때까지 스스로 고치기를 반복하며, 부재마다 근거 문서까지 되짚는 '증거 사슬'로 당나라 건축과 노트르담 첨탑을 복원했습니다.

 [![Sim Francisco 데모 화면](https://bizroasting.com/assets/hackathon/blog/simfrancisco.jpg)](https://www.youtube.com/watch?v=WUSLZ_cEqnc) [GitHub↗](https://github.com/tejasprabhune/simfrancisco)

 2

Sim Francisco

Tanmayi Priya Dasari, Tejas Prabhune · UC버클리 EECS 전공생

- 선거 결과나 정책 향방을 미리 가늠하려면 값비싼 여론조사가 필요한 데다, 정확도도 들쭉날쭉합니다.

- 인구조사 데이터로 가상 시민 1만 명을 만들어 저마다 인구 특성·이력·가치관을 입히고, 진화 알고리즘으로 약 300개 대표 유형으로 묶어 도시 지도 위에서 뉴스에 실시간으로 반응하게 합니다.

- 2024년 대선 득표율을 81.3%로 예측(실제 83.8%)하고 예측 시장도 몇 퍼센트 이내로 따라가면서, 비용은 10~100배 낮췄습니다. 화면과 서버 코드 전체를 Opus 4.8이 작성했습니다.

 [![Custom Universe 데모 화면](https://bizroasting.com/assets/hackathon/blog/customuniverse.jpg)](https://www.youtube.com/watch?v=6erI1uxx2eo) [GitHub↗](https://github.com/jss8649/image-edit-realtime-hackathon)

 3

Custom Universe

Jake Stevens, Mauricio Pereira · RIT 컴퓨터비전 졸업(Luminal) / MIT 로보틱스 졸업(Coat Robotics)

- 로봇 연구실은 학습용 가상 데이터를 만드는 데 애를 먹고, 실사 같은 3D 장면을 만들려면 보통 물리 전문가가 있어야 합니다.

- 휴대폰 사진 한 장을 손볼 수 있는 실사 같은 3D 장면으로 바꾸는 실시간 엔진입니다. 의자를 찍으면 3D 객체로 만들어 장면에 놓고, 텍스트 명령으로 분위기를 바꿔 실시간으로 그려 냅니다.

- Opus 4.8이 프로젝트를 처음부터 끝까지 만들고 원격 NVIDIA H100까지 다뤘으며, 사용자가 자기 GPU에서 직접 돌려 로봇 학습용 데이터를 만드는 것이 목표입니다.

본업이 개발이 아니어도 만들 수 있습니다.

여기 모인 우승작 대부분은 코드를 업으로 삼지 않는 사람들이 만들었습니다.

클로드 코드를 처음 여는 법부터 차근차근 따라가 보세요.

 [클로드 코드 시작하기](https://bizroasting.com/vibe-coding-101.html) [스탑워치 쇼케이스 보기](https://bizroasting.com/showcase-stopwatch.html)

 [←목록으로](https://bizroasting.com/index.html#section-ax-cases)
