# bizroasting.com 링크 맵

bizroasting.com 페이지 간 내부 링크를 노드 그래프로 보여주는 단일 HTML 파일입니다.

- `index.html`: 결과 맵 (데이터가 파일 안에 들어 있어 그냥 열면 됩니다)
- `crawl.py`: 홈에서 같은 도메인 링크를 따라가며 `graph.json`을 만듭니다
- `build_map.py`, `template.html`: `graph.json`을 `index.html`로 만듭니다

재생성 방법:

```
python3 crawl.py out 300              # out/graph.json 생성
python3 build_map.py out/graph.json index.html
```

한계: `<a href>` 링크만 따라갑니다. 자바스크립트로 만든 링크나 로그인 뒤 페이지는 빠집니다.
