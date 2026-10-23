"""Build the single-file link map from a crawl.py graph.json.

usage: python3 build_map.py <graph.json> <output.html>
"""
import json
import os
import sys
from collections import Counter
from urllib.parse import urlparse

HOST = "bizroasting.com"
TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "template.html")


def normalize(url):
    """Collapse '/', '/index.html' and '/x/' variants into one key per page."""
    p = urlparse(url.split("#")[0])
    path = p.path or "/"
    if path.endswith("/"):
        path += "index.html"
    return "https://" + HOST + path


def group_of(path):
    if path in ("/", "/index.html"):
        return "home"
    if "/assets/" in path:
        return "demo"
    if path.startswith("/showcase-") or path.startswith("/icon-gallery") or path.startswith("/eda-gallery") or path.startswith("/component-gallery"):
        return "showcase"
    return "content"


def label_of(title, path):
    name = title.split("|")[0].strip() or path
    name = name.split(" · ")[0].strip()
    return name[:28]


def main(graph_path, out_path):
    g = json.load(open(graph_path, encoding="utf-8"))
    pages = {}
    for url, info in g["pages"].items():
        key = normalize(url)
        path = urlparse(key).path
        if key not in pages:
            pages[key] = {"title": info["title"], "links": set()}
        for link in info["links"]:
            if urlparse(link).netloc.lower() in (HOST, "www." + HOST):
                pages[key]["links"].add(normalize(link))

    nodes = []
    index = {}
    for key in sorted(pages, key=lambda k: (k != "https://" + HOST + "/index.html", k)):
        path = urlparse(key).path
        index[key] = len(nodes)
        nodes.append({
            "id": len(nodes),
            "url": key,
            "path": path,
            "label": label_of(pages[key]["title"], path),
            "title": pages[key]["title"],
            "group": group_of(path),
        })

    edges = set()
    for key, info in pages.items():
        for target in info["links"]:
            if target in index and target != key:
                edges.add((index[key], index[target]))

    degree = Counter()
    for a, b in edges:
        degree[a] += 1
        degree[b] += 1
    for n in nodes:
        n["degree"] = degree[n["id"]]

    data = {
        "host": HOST,
        "nodes": nodes,
        "edges": [{"s": a, "t": b} for a, b in sorted(edges)],
        "broken": len(g.get("broken", [])),
    }
    template = open(TEMPLATE, encoding="utf-8").read()
    html = template.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("nodes", len(nodes), "edges", len(edges), "->", out_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
