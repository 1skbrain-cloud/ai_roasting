# 프롬프트 잘 쓰는 법

원본: https://bizroasting.com/ai-fluency.html

---

프롬프트 잘 쓰는 법 | AI ROASTING         [본문으로 건너뛰기](https://bizroasting.com#main)

 RCTO · 요청 작성

## RCTO는 요청을 설명하는 기본기입니다

역할(Role)·맥락(Context)·작업(Task)·출력 형식(Output)은 무엇을 요청하는지 설명하는 요소입니다. 한 번의 답변을 요청할 때도 사용하며, 여러 단계의 작업을 맡길 때는 GRVS로 수행 조건까지 정합니다.

R역할Role

어떤 역할로 답할지 한 문장으로 적습니다. 예: "너는 마케팅 카피라이터야."

C맥락Context

자료와 함께 요청하는 이유를 설명합니다. 예: "임원들이 30초 안에 판단할 보고서야."

T작업Task

수행할 작업과 적용 범위를 적습니다. 예: "보고서의 모든 항목을 핵심 위주로 다시 써줘."

O출력 형식Output

필요한 형식을 설명하거나 예시로 제시합니다. 예: "항목별 비교표로 정리해줘."

 GRVS · 작업 위임

## 여러 단계의 작업을 맡길 때는 GRVS를 정합니다

AI가 파일을 읽고 도구와 코드를 실행하면, 답변 형식뿐 아니라 작업 전체의 조건을 정해야 합니다. 수행 방법을 일일이 지시하기보다 무엇을 완성하고 어떤 기준으로 확인하며 어디서 멈출지 명확히 적습니다.

G목표Goal

작업이 끝났을 때 제출할 결과물과 이번 요청의 범위를 정합니다.

R평가 기준Rubric

결과물의 통과 여부를 판단할 기준을 적습니다.

V검증Verification

답변을 어떤 자료와 대조할지 지정합니다.

S중단 조건Stop

어디까지 수행하고 멈출지 정합니다. 금지할 행동도 명시해 허용한 범위 안에서 작업하도록 합니다.

경쟁사 분석 요청 예시

 목표(Goal) "경쟁사 3사를 비교한 분석 문서를 작성해줘."

 평가 기준(Rubric) "모든 수치와 주장은 공시·IR·뉴스에서 출처를 확인할 수 있게 제시해줘. 3사를 같은 항목과 기준으로 비교하고 추측은 넣지 마."

 검증(Verification) "각 수치를 이번에 확인한 자료와 대조하고 확인하지 못한 항목은 표시해줘. 제시한 근거 중 가장 약한 3가지를 따로 지적해줘."

 중단 조건(Stop) "비교 분석 문서를 작성하면 멈춰줘. 전략 제안, 실행안 작성, 외부 공유는 하지 마. 다음 단계는 승인 후에 진행해줘."

 최신 가이드

## 모델별로 프롬프트를 조정하는 방법

Claude Fable 5.1과 GPT-6 Astra는 작업 중 보고하거나 검증하는 방식이 다릅니다. GRVS로 작업 조건을 정한 뒤, 각 모델에서 나타나는 문제에 맞춰 지시를 조정합니다.

 ANTHROPIC

Claude Fable 5.1

긴 작업을 끝까지 마치고 중간에 보고하기

- Fable 5에서 사용하던 프롬프트로 시작합니다. 문제가 생기면 관련 지시만 수정합니다.

- 작업 중 설명이 부족하면 언제, 어떤 내용을 보고할지 알려줍니다.

- 다음 단계만 제안하고 멈추면 요청한 작업을 끝까지 마치라고 지시합니다.

- 요청하지 않은 수정과 과도한 테스트를 제한하고, 범위 밖 문제는 별도로 보고하도록 합니다. 문장이 길어지면 비유를 줄이고 내용을 직접 설명하도록 요청합니다.

 [원문 보기 ](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)

 OPENAI

GPT-6 Astra

작업을 끝까지 마치고 지침의 우선순위 정하기

- 확인 질문 때문에 자주 멈추면 합리적으로 판단할 수 있는 부분은 스스로 결정하고 이미 요청한 작업을 마치도록 지시합니다.

- 스킬·AGENTS.md 등 작업 지침 파일에서 충돌하는 내용을 확인합니다. 사용자 지시를 우선하도록 명시합니다.

- 결론부터 간결하게 설명하도록 요청합니다. 목록과 표는 내용을 비교하는 데 필요할 때 사용하도록 합니다.

- 필수 검사를 통과하면 작업을 마치도록 합니다. 새로 수정한 내용이나 실패한 검사가 없다면 테스트를 반복하지 않도록 합니다.

 [원문 보기 ](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)

 대조할 자료와 필수 검사는 유지합니다. 같은 확인을 반복하게 하는 지시만 줄입니다. Fable 5.1은 추론 수준이 낮을 때 검색을 생략하기도 합니다. 최신 정보가 필요한 작업에는 검색으로 확인하라는 지시를 넣습니다.

 한 장 요약

## 작업 위임과 요청 작성 요약

RCTO · 요청을 작성할 때

 R 역할Role

- 역할은 한 문장으로: "너는 노련한 ○○야"

 C 맥락Context

- 요청하는 이유도 설명하기

- 긴 자료는 앞에, 질문은 뒤에 배치하기

 T 작업Task

- 수행할 작업을 직접 요청: "바꿔줘 · 만들어줘"

- 필요한 완성도와 적용 범위 정하기

- 사고 순서는 AI에 맡기고 검토 요청하기

 O 출력 형식Output

- 필요한 형식을 직접 요청: "JSON으로 줘"

- 예시·태그로 형식 제시하기

GRVS · 작업을 맡길 때

목표·평가 기준·검증 방법·중단 조건

 G 목표Goal

- 제출할 결과물 정하기

- 이번 요청의 범위 정하기

 R 평가 기준Rubric

- 결과물의 통과 기준 정하기

- "출처를 확인할 수 있게 제시하고 추측은 넣지 마"

 V 검증Verification

- 대조할 자료 지정하기

- "확인하지 못한 항목은 표시해줘"

 S 중단 조건Stop

- 작업을 멈출 시점 정하기

- "정한 범위를 넘는 작업은 승인 후 진행해줘"

### 참고 문서

-  Prompting Claude Fable 5.1 Anthropic · 작업 완료, 중간 보고, 수정·테스트 범위, 문장 표현, 검색 [platform.claude.com · Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)

-  GPT-6 Astra 프롬프트 작성 안내 OpenAI · 작업 완료, 지침의 우선순위, 답변 문체, 테스트 범위 [developers.openai.com · Model guidance · GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)

-  Claude 프롬프트 작성 원칙 Anthropic · 역할, 맥락, 작업 지시, 출력 형식 [platform.claude.com · Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

 다음 단계: 멀티 페르소나 토론

AI에 서로 다른 역할을 맡겨 토론시키고 결론을 검토하는 방법을 알아봅니다.

 [멀티 페르소나 토론 체험하기 →](https://bizroasting.com/multi-persona.html)

 [ ←목록으로 ](https://bizroasting.com/index.html#section-1)
