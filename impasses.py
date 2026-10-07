#!/usr/bin/env python3
"""Extrait le contexte des VRAIES impasses : onglets CI vides, lignes de tableau
vides, formules paresseuses « non vérifié ici », bullets partiels."""
import os
import re

DOCS = "/root/tchounis-pharmacy/content/docs"

LAZY = re.compile(r"non\s+v[ée]rifi", re.I)
TABEMPTY = re.compile(r'<Tab value="([^"]+)">\s*Non\s+pr[ée]cis[ée]')
ROWEMPTY = re.compile(r"^\|.*Non\s+pr[ée]cis[ée][^|]*\|\s*—\s*\|\s*—\s*\|\s*$")
BULLET = re.compile(r"non\s+pr[ée]cis[ée]\s+dans\s+les\s+sources\s+consult[ée]es", re.I)


def rows():
    for root, _d, names in os.walk(DOCS):
        for n in sorted(names):
            if not n.endswith(".mdx") or n == "index.mdx":
                continue
            p = os.path.join(root, n)
            rel = os.path.relpath(p, DOCS)
            if rel.endswith("/index.mdx"):
                continue
            yield rel, p


for rel, path in sorted(rows()):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = []
    for i, line in enumerate(lines):
        if LAZY.search(line):
            out.append((i + 1, "LAZY", line.strip()))
        elif TABEMPTY.search(line):
            out.append((i + 1, "TAB-VIDE", line.strip()))
        elif ROWEMPTY.match(line):
            out.append((i + 1, "ROW-VIDE", line.strip()[:180]))
        elif BULLET.search(line) and line.lstrip().startswith("-"):
            out.append((i + 1, "BULLET", line.strip()[:180]))
    if out:
        print(f"\n===== {rel}")
        for ln, tag, txt in out:
            print(f"  {ln:4} [{tag:9}] {txt}")
            if tag in ("TAB-VIDE", "ROW-VIDE"):
                for j in range(max(0, ln - 4), min(len(lines), ln + 1)):
                    if j + 1 != ln and lines[j].strip():
                        print(f"        ctx {j+1:4} | {lines[j].strip()[:170]}")
