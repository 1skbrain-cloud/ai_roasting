import subprocess, hashlib, json, os, sys
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse, urldefrag

HOST = "bizroasting.com"
OUT = sys.argv[1]
MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 300
os.makedirs(OUT, exist_ok=True)

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.assets = []; self.title = ""; self._t = False
    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "a" and a.get("href"): self.links.append(("a", a["href"]))
        if tag == "link" and a.get("href"): self.assets.append(("link:" + (a.get("rel") or ""), a["href"]))
        if tag in ("script", "img", "iframe") and a.get("src"): self.assets.append((tag, a["src"]))
        if tag == "title": self._t = True
    def handle_endtag(self, tag):
        if tag == "title": self._t = False
    def handle_data(self, d):
        if self._t: self.title += d

def fetch(url):
    r = subprocess.run(["curl", "-sS", "-L", "-m", "30", "-o", "-", "-w", "\n__STATUS__%{http_code} %{content_type}", url],
                       capture_output=True)
    body, _, meta = r.stdout.rpartition(b"\n__STATUS__")
    if not meta: return 0, "", b""
    code, ctype = meta.decode(errors="replace").split(" ", 1)
    return int(code), ctype, body

def norm(base, href):
    u, _ = urldefrag(urljoin(base, href.strip()))
    p = urlparse(u)
    if p.scheme not in ("http", "https"): return None
    return u

queue = ["https://bizroasting.com/"]
seen = set(); pages = {}; external_assets = {}; broken = []
while queue and len(seen) < MAX:
    url = queue.pop(0)
    if url in seen: continue
    seen.add(url)
    code, ctype, body = fetch(url)
    if code != 200:
        broken.append((url, code)); continue
    if "html" not in ctype:
        continue
    p = P(); p.feed(body.decode("utf-8", errors="replace"))
    pages[url] = {"title": p.title.strip()[:80], "size": len(body), "links": []}
    for kind, href in p.links:
        u = norm(url, href)
        if not u: continue
        host = urlparse(u).netloc.lower()
        if host == HOST or host == "www." + HOST:
            pages[url]["links"].append(u)
            if u not in seen and u not in queue: queue.append(u)
        else:
            pages[url]["links"].append(u)
    for kind, src in p.assets:
        u = norm(url, src)
        if u and urlparse(u).netloc.lower() not in (HOST, "www." + HOST):
            external_assets[u] = kind

json.dump({"pages": pages, "broken": broken, "external_assets": external_assets, "remaining_queue": queue[:50], "seen": len(seen)},
          open(os.path.join(OUT, "graph.json"), "w"), ensure_ascii=False, indent=1)
print("seen", len(seen), "html pages", len(pages), "broken", len(broken), "queue left", len(queue))
