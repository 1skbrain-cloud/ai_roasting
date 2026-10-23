# 오픈소스 라이선스 가이드

원본: https://bizroasting.com/license-compare.html

---

오픈소스 라이선스 가이드 | AI ROASTING            [본문으로 건너뛰기](https://bizroasting.com#main)

라이선스, 슬라이드 열 장으로 먼저 보기

 스킬 배포자를 위한 기초

라이선스

내 스킬을 남이 어디까지 써도 되는지

정해 두는 한 장의 문서

종류는 많지만 제약 수위로 보면 세 단계입니다

GPL

AGPL

LGPL

MIT

Apache 2.0

5종

01 / 10 · AI ROASTING

LICENSE 파일이 없으면, 아무도 못 씁니다

 파일이 없을 때

기본 저작권법이

적용됩니다

누구도 합법적으로 사용·수정·배포할 수 없습니다.

사용 불가

 파일이 있을 때

적힌 조건만큼

허락됩니다

상업 이용, 수정, 재배포를 어디까지 열지 내가 정합니다.

넣을 때 확인할 네 가지

1LICENSE 파일을 꼭 포함

2연도와 이름을 정확히

[작성자 이름] 그대로면 효력 없음

3가져다 쓴 오픈소스의 LICENSE도 함께

4Apache는 NOTICE 파일까지

02 / 10

신호등

제약 수위로 나누면 세 단계

초록불

저작권 표시만 남기면 상업 제품에도 자유롭게 씁니다

MITApache 2.0

최대한 넓게 퍼지는 것이 목표일 때

노란불

연결해 쓰는 것은 자유, 라이브러리를 고치면 그 부분만 공개합니다

LGPL

개선된 부분을 다시 공유받고 싶을 때

빨간불

가져다 쓴 결과물도 전체 소스를 같은 조건으로 공개합니다

GPLAGPL

생태계에 환원하거나

SaaS의 무단 활용을 막을 때

03 / 10

이름

약자와 유래 ① 허용적 라이선스 둘

 MIT

Massachusetts

Institute of Technology

매사추세츠 공과대학교

유래1980년대 MIT가 X 윈도 시스템을 배포하며 처음 쓴 라이선스입니다. 학교 이름이 곧 라이선스 이름입니다.

 Apache 2.0

Apache License, Version 2.0

 A Patchy Server → Apache

유래1995년 Apache HTTP Server 프로젝트에서 만들었습니다. 초기 개발자들이 패치(patch)를 많이 적용해 생긴 말장난이 이름이 되었습니다.

학교 이름

vs

말장난

04 / 10

GNU

약자와 유래 ② GNU 라이선스 셋

GNU's Not Unix

약자 안에 자기 이름이 다시 들어가는 재귀 약자입니다. 아래 세 라이선스 이름이 모두 GNU로 시작합니다.

 GPL

GNU General

Public License

유래리처드 스톨먼이 1989년 자유 소프트웨어 운동을 위해 만들었습니다.

 LGPL

GNU Lesser General

Public License

유래Lesser는 “제약이 더 작다”는 뜻. GPL을 완화한 버전입니다.

 AGPL

GNU Affero General

Public License

유래처음 만든 회사 Affero, Inc.에서 왔습니다. 라틴어로 “전달하다”, 네트워크 전달까지 넓힌다는 뜻입니다.

05 / 10

오른쪽으로 갈수록 의무가 늘어납니다

제약 약함

매우 강함

MIT

저작권 표시만

Apache 2.0

+ 특허 보호

+ 변경 사항 명시

+ NOTICE 보존

LGPL

+ 라이브러리를 고친 부분만 소스 공개

GPL

+ 전체 소스 공개

+ 같은 GPL로 배포

AGPL

+ 서버에서 실행만 해도 공개 대상

다섯 모두 공통 · 상업적 이용 O · 수정 O · 저작권 표시 필수

06 / 10

한줄로

MIT vs Apache 2.0

 MIT

그냥 맘대로 써,

내 이름만 남겨줘

 Apache 2.0

맘대로 써. 대신 이름 남기고

특허로 뒤통수치지 마

차이는

세 가지뿐

① 특허 조항

Apache만 기여자 특허를 자동 허락하고, 소송을 걸면 라이선스가 끝납니다

② 변경 표시

Apache는 수정한 부분을 표시해야 합니다

③ NOTICE 파일

Apache는 원본 NOTICE를 함께 배포합니다. MIT는 LICENSE 하나면 끝

개인·소규모 스킬은 MIT, 기업·특허 이슈가 있으면 Apache 2.0

07 / 10

전염성

카피레프트는 가져간 쪽에도 의무를 지웁니다

 GPL

 내 코드

MIT로 만들었어도 + GPL 코드

한 조각
 ↓

전체가 GPL이 됩니다

배포하면 전체 소스를 같은 GPL로 공개

 LGPL

라이브러리를 쓰는 방식에 따라 다릅니다

그대로 연결해 쓰면

내 코드는 다른 라이선스여도 됩니다

라이브러리를 고치면

고친 부분만 LGPL로 공개합니다

MIT 프로젝트에 GPL 섞기 주의

08 / 10

AGPL

서버에서 돌리기만 해도 배포로 봅니다

 GPL

내 서버에서 실행, 사용자는 네트워크로 접속
 ↓

배포로 보지 않습니다
 ↓

소스 공개 의무 없음

SaaS 루프홀

 AGPL

내 서버에서 실행, 사용자는 네트워크로 접속
 ↓

이것만으로 배포로 간주합니다
 ↓

사용자에게 소스 접근 방법 제공

SaaS 기업이 가장 주의해야 하는 라이선스 · 예: Grafana, Nextcloud

09 / 10

고르는법

잘 모르겠으면 MIT로 시작

처음이라면
MIT

조건이 가장 단순하고 채택률이 가장 높습니다

기업 배포, 특허가 걱정되면
Apache 2.0

특허 소송 리스크를 막아 줍니다

라이브러리로 배포한다면
LGPL 3.0

자유롭게 연결하고 수정분만 공개됩니다

생태계에 환원하고 싶다면
GPL 3.0

파생 저작물도 오픈소스로 남습니다

SaaS 무임승차를 막으려면
AGPL 3.0

서버 실행도 소스 공개 대상입니다

아무것도 정하지 않으면

아무도 못 씁니다

공개할 거라면 LICENSE 파일을 꼭 넣으세요

10 / 10

  1 / 10

 스킬이나 도구를 외부에 공개할 때, 라이선스는 다른 사람이 내 결과물을 어디까지 활용할 수 있는지를 규정합니다.

 제약이 약한 라이선스는 상업적 재사용까지 폭넓게 허용하고, 제약이 강한 라이선스는 가져간 쪽에도 소스 공개 의무를 지웁니다. 종류는 많지만 제약 수위에 따라 세 단계로 정리됩니다.

신호등으로 보는 5종

## 어디까지 개방하고, 어디서부터 보호할 것인가

라이선스 선택은 결과물을 얼마나 개방하고 어디서부터 보호할지 정하는 결정입니다. 다섯 가지 라이선스는 제약 수위에 따라 세 단계로 나뉩니다.

초록불

MITApache 2.0

제약이 가장 약합니다. 누구나 상업 제품에 포함하고, 수정하고, 재배포할 수 있습니다. 저작권 표시만 유지하면 됩니다.

적합한 상황 최대한 넓은 채택이 목표일 때. 다만 경쟁사가 그대로 활용해도 제한할 수 없습니다.

노란불

LGPL

조건부로 개방합니다. 라이브러리로 연결해 쓰는 것은 자유지만, 라이브러리 자체를 수정하면 그 부분은 공개해야 합니다.

적합한 상황 라이브러리로 배포하되, 개선된 부분은 다시 공유받고자 할 때.

빨간불

GPLAGPL

가장 강하게 보호합니다. 내 코드를 사용한 결과물도 전체 소스를 같은 조건으로 공개해야 합니다. AGPL은 서버에서 실행하는 것만으로도 공개 대상이 됩니다.

적합한 상황 오픈소스 생태계에 환원하거나, 외부 SaaS의 무단 활용을 차단하고자 할 때.

라이선스 가이드표

## 5개 라이선스 한눈에 비교

왼쪽일수록 제약이 약한 초록불, 오른쪽일수록 제약이 강한 빨간불입니다

 항목 MIT Apache 2.0 GPL 3.0 LGPL 3.0 AGPL 3.0

 상업적 이용 O O O O O

 수정 허용 O O O O O

 저작권 표시 필수 필수 필수 필수 필수

 변경 사항 명시 X 필수 필수 필수 필수

 소스코드 공개 X X 필수 수정 시 필수

 동일 라이선스 적용 X X 전체 수정분만 전체

 특허 보호 X O O O O

 네트워크 서비스 공개 X X X X 필수

 제약 강도 약함 약함 강함 중간 매우 강함

   ? MIT vs Apache 2.0, 한 줄로 말하면? ▾

 MIT는 "그냥 맘대로 써, 내 이름만 남겨줘", Apache 2.0은 "맘대로 써. 대신 이름 남기고 특허로 뒤통수치지 마"입니다.

 둘 다 상업·수정·재배포·비공개 모두 허용하는 허용적 라이선스이고, 차이는 3가지뿐입니다.

- ① 특허 조항

 Apache는 기여자 특허를 자동으로 허락하고, 사용자가 특허 소송을 걸면 라이선스가 즉시 종료됩니다. MIT엔 이 장치가 없어서 나중에 누가 "내 특허다"라며 소송을 걸 수 있습니다. → 독창적 알고리즘·기업 제품은 Apache 2.0이 안전합니다.

- ② 변경 표시 의무

 Apache는 수정 부분을 표시해야 하지만, MIT는 그런 의무가 없습니다.

- ③ NOTICE 파일

 Apache는 원본 NOTICE를 함께 배포해야 하고, MIT는 LICENSE만 챙기면 끝입니다.

 요약: 개인·소규모 스킬은 MIT, 기업·특허 이슈가 있으면 Apache 2.0.

    ! 처음이라면 MIT, 특허가 걱정되면 Apache 2.0 ▾

개인 프로젝트, Claude Code 스킬, MCP 서버는 대부분 MIT면 충분합니다. 조건이 가장 단순해 채택률이 가장 높습니다.

독창적 알고리즘이 있거나 기업에서 배포한다면 Apache 2.0을 쓰세요. 특허 소송 리스크를 막아줍니다. 잘 모르겠으면 MIT로 시작해도 됩니다.

    ! MIT/Apache 라이선스 파일을 사용할 때 주의할 점 ▾

- LICENSE 파일을 반드시 포함하세요. 없으면 기본 저작권법이 적용돼 아무도 합법적으로 못 씁니다.

- 연도와 이름을 정확히 기입하세요. [작성자 이름]을 그대로 두면 법적 효력이 없습니다.

- 가져다 쓴 오픈소스의 LICENSE도 함께 포함하세요. 의존성 라이브러리의 라이선스를 삭제하면 위반입니다.

- Apache의 NOTICE 파일을 빠뜨리지 마세요. 원본에 있다면 배포 시 반드시 함께 넣어야 합니다.

- MIT와 Apache는 섞어 써도 됩니다. 단, GPL 코드를 MIT 프로젝트에 넣으면 전체가 GPL이 되니 주의하세요.

- "AS IS" 면책 조항을 이해하세요. 두 라이선스 모두 무보증 조항을 포함해, 사용 중 문제가 생겨도 법적 책임을 지지 않습니다.

허용적(Permissive) 라이선스

MIT

MIT License 초록불

가장 많이 선택되는 스킬/도구 라이선스

 이름의 유래: 매사추세츠 공과대학교(MIT)에서 1980년대 X 윈도 시스템을 배포하며 처음 사용한 라이선스입니다.

 저작권 표시만 남기면 누구나 자유롭게 수정·재배포·상업 이용이 가능합니다. npm 패키지, GitHub 공개 저장소 대부분이 이 라이선스를 씁니다.

 ✓ 상업적 이용 ✓ 수정 ✓ 배포 ✓ 사적 이용 ⚠ 저작권 표시 ⚠ 라이선스 고지

 스킬 배포자 관점

- LICENSE 파일에 MIT 전문과 이름·연도만 넣으면 끝

- 포크·수정해도 소스 공개 의무 없음

- 기업도 부담 없이 채택 → 채택률이 가장 높음

- 단점: 독점 제품에 가져다 써도 막을 수 없음

 이 라이선스를 쓰는 도구: Claude Code(@anthropic-ai/claude-code), React, Vue.js, Next.js

LICENSE 파일 표기 예시

MIT License Copyright (c) 2026 [작성자 이름] Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

APL

Apache License 2.0 초록불

특허 보호가 필요한 기업용 스킬에 적합

 이름의 유래: 1995년 Apache HTTP Server 프로젝트에서 만든 라이선스입니다. 초기 개발자들이 패치(patch)를 많이 적용해 "A Patchy Server"라는 말장난에서 이름이 나왔습니다.

 MIT만큼 자유로우면서 특허 라이선스 조항이 추가됐습니다. 독창적 알고리즘이 있거나 특허 분쟁이 걱정되면 안전합니다.

 ✓ 상업적 이용 ✓ 수정 ✓ 배포 ✓ 특허 라이선스 ⚠ 저작권 표시 ⚠ 변경 사항 명시 ⚠ NOTICE 파일 보존

 스킬 배포자 관점

- 사용자가 수정하면 변경 사항 표시 필수

- 기여자 특허는 자동으로 사용 허락

- 특허 소송을 걸면 라이선스 자동 종료(악의적 소송 방지)

- NOTICE 파일로 기여자·출처 정보를 관리

 이 라이선스를 쓰는 도구: TensorFlow, Kubernetes, Android, Swift

LICENSE 파일 표기 예시 (헤더 요약)

 Apache License Version 2.0, January 2004 http://www.apache.org/licenses/ Copyright 2026 [작성자 이름] Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

카피레프트(Copyleft) 라이선스

GPL

GPL v3.0 빨간불

GNU General Public License v3.0

 이름의 유래: 리처드 스톨먼이 1989년 자유 소프트웨어 운동을 위해 만들었습니다. GNU는 "GNU's Not Unix"의 재귀 약자입니다.

 가장 강력한 카피레프트 라이선스입니다. GPL 코드를 포함해 배포하면 전체 소스를 같은 GPL로 공개해야 합니다.

 ✓ 상업적 이용 ✓ 수정 ✓ 배포 ⚠ 소스코드 공개 ⚠ 동일 라이선스 적용 ⚠ 변경 사항 명시 ✗ 독점 소프트웨어 결합 제한

 핵심 요약

- 파생 저작물도 반드시 GPL로 배포(전염성)

- 바이너리 배포 시 소스 제공 또는 접근 방법 안내 필수

- v3는 특허 보호와 DRM 우회 금지 방지 조항 포함

- SaaS(서버 실행)는 배포로 보지 않아 공개 의무 없음

 대표 프로젝트: Linux Kernel, WordPress, GIMP, GCC

LICENSE 파일 표기 예시 (헤더 요약)

 GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 Copyright (C) 2026 [작성자 이름] This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

LGL

LGPL v3.0 노란불

GNU Lesser General Public License v3.0

 이름의 유래: GPL에서 파생된 완화 버전으로, Lesser는 "제약이 더 작다"는 뜻입니다.

 LGPL 라이브러리를 수정 없이 가져다 연결해 쓰면 내 코드에는 다른 라이선스를 써도 됩니다. 라이브러리 자체를 수정한 부분만 LGPL로 공개하면 됩니다.

 ✓ 상업적 이용 ✓ 라이브러리 링크 자유 ⚠ 라이브러리 수정 시 소스 공개 ⚠ 저작권 표시

 핵심 요약

- 라이브러리를 그대로 링크하면 내 코드 공개 불필요

- 라이브러리를 수정하면 그 부분만 LGPL로 공개

- 독점 소프트웨어에서도 LGPL 라이브러리 사용 가능

 대표 프로젝트: GNU C Library, Qt(일부), FFmpeg(일부)

LICENSE 파일 표기 예시 (헤더 요약)

 GNU LESSER GENERAL PUBLIC LICENSE Version 3, 29 June 2007 Copyright (C) 2026 [작성자 이름] This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. You should have received a copy of the GNU Lesser General Public License along with this library; if not, see <https://www.gnu.org/licenses/>.

AGL

AGPL v3.0 빨간불

GNU Affero General Public License v3.0

 이름의 유래: 처음 만든 회사 Affero, Inc.에서 왔습니다. Affero는 라틴어로 "전달하다"는 뜻으로, 네트워크 전달 상황까지 라이선스를 확장하겠다는 의도입니다.

 GPL의 강화 버전입니다. 서버에서 실행하는 것만으로 '배포'로 간주해, 네트워크 서비스도 소스 공개 대상이 됩니다.

 ✓ 상업적 이용 ⚠ 소스코드 공개 ⚠ 네트워크 서비스도 공개 대상 ⚠ 동일 라이선스 적용 ✗ SaaS 루프홀 차단

 핵심 요약

- GPL 조건 + 네트워크 사용도 배포로 간주

- 서버에서 AGPL 코드를 실행하면 사용자에게 소스 접근 방법 제공 필수

- SaaS 기업이 가장 주의해야 하는 라이선스

 대표 프로젝트: MongoDB(구버전), Grafana, Nextcloud

LICENSE 파일 표기 예시 (헤더 요약)

 GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007 Copyright (C) 2026 [작성자 이름] This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details. You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

상황별 선택 가이드

🚀

최대한 자유롭게 쓰고 싶다면?

MIT

조건이 가장 단순하고 상업 이용에 제약이 없습니다.

🏢

기업에서 특허 보호가 필요하다면?

Apache 2.0

특허 라이선스 조항이 법적 리스크를 줄여줍니다.

🤝

오픈소스 생태계에 기여하고 싶다면?

GPL 3.0

파생 저작물도 오픈소스로 유지돼 커뮤니티에 환원됩니다.

📚

라이브러리를 만들어 배포한다면?

LGPL 3.0

자유롭게 링크하되 라이브러리 수정분만 공개됩니다.

☁️

SaaS 무임승차를 막고 싶다면?

AGPL 3.0

네트워크 서비스도 배포로 간주해 소스 공개를 요구합니다.

⚠️

라이선스를 아예 명시하지 않으면?

기본 저작권 보호

누구도 사용·수정·배포할 수 없으니 반드시 명시하세요.

### 라이선스 이해 완료!

 핵심 차이를 익혔습니다. 이제 용어 사전으로 넘어가세요.
 [용어 사전 68선 →](https://bizroasting.com/glossary.html)

 [ ←목록으로 ](https://bizroasting.com/index.html#section-glossary)

1 / 10
