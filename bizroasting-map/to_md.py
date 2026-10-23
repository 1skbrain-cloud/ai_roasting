import os, re, subprocess, sys
from html.parser import HTMLParser
from urllib.parse import urljoin

BASE = "https://bizroasting.com"
OUT = sys.argv[2]
SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "header", "button", "iframe", "form", "template"}
BLOCK = {"p", "div", "section", "article", "li", "tr", "br", "h1", "h2", "h3", "h4", "h5", "h6", "table", "ul", "ol", "blockquote", "figure"}

class MD(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.out = []; s.skip = 0; s.title = ""; s.in_title = False
        s.href = None; s.main_depth = 0; s.h = 0; s.in_main = False
    def emit(s, t):
        if not s.skip: s.out.append(t)
    def handle_starttag(s, tag, a):
        a = dict(a)
        if tag == "title": s.in_title = True
        if tag == "main": s.in_main = True
        if tag in SKIP: s.skip += 1; return
        if tag in ("h1", "h2", "h3", "h4"):
            s.emit("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li": s.emit("\n- ")
        elif tag in BLOCK: s.emit("\n\n")
        elif tag == "img" and a.get("alt"):
            s.emit("![%s](%s)" % (a["alt"].strip(), urljoin(BASE, a.get("src", ""))))
        elif tag == "a" and a.get("href"):
            s.href = urljoin(BASE, a["href"])
            s.emit("[")
    def handle_endtag(s, tag):
        if tag == "title": s.in_title = False
        if tag == "main": s.in_main = False
        if tag in SKIP:
            s.skip = max(0, s.skip - 1); return
        if tag == "a" and s.href:
            s.emit("](%s)" % s.href); s.href = None
        elif tag in ("h1", "h2", "h3", "h4", "li") or tag in BLOCK:
            s.emit("\n")
    def handle_data(s, d):
        if s.in_title: s.title += d
        if s.skip: return
        s.emit(re.sub(r"\s+", " ", d))

def clean(md):
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"(?m)^- *\n", "", md)
    return md.strip() + "\n"

os.makedirs(OUT, exist_ok=True)
for path in open(sys.argv[1]).read().split():
    html = subprocess.run(["curl", "-sS", "-L", "-m", "30", BASE + path], capture_output=True).stdout.decode("utf-8", "replace")
    p = MD(); p.feed(html)
    title = p.title.split("|")[0].strip() or path
    body = clean("".join(p.out))
    name = path.strip("/").replace("/", "_").replace(".html", "") or "index"
    with open(os.path.join(OUT, name + ".md"), "w", encoding="utf-8") as f:
        f.write("# %s\n\n원본: %s%s\n\n---\n\n" % (title, BASE, path) + body)
    print(len(body), name)
