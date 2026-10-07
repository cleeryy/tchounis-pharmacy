#!/usr/bin/env python3
"""Tous les contenus d'onglet/lignes qui ne contiennent QUE la formule standardisée."""
import os
import re

DOCS = "/root/tchounis-pharmacy/content/docs"
ONLY = re.compile(r"^\s*(<Tab value=\"[^\"]+\">)?\s*Non\s+pr[ée]cis[ée]\s+dans\s+les\s+sources\s+consult[ée]es")

for root, _d, names in os.walk(DOCS):
    for n in sorted(names):
        if not n.endswith(".mdx") or n == "index.mdx":
            continue
        p = os.path.join(root, n)
        rel = os.path.relpath(p, DOCS)
        if rel.endswith("/index.mdx"):
            continue
        lines = open(p, encoding="utf-8").read().split("\n")
        hits = [(i, l) for i, l in enumerate(lines) if ONLY.match(l)]
        if not hits:
            continue
        print(f"\n===== {rel}")
        for i, l in hits:
            # ligne la plus proche au-dessus qui ouvre un Tab / un bloc
            ctx = ""
            for j in range(i - 1, max(-1, i - 12), -1):
                if re.search(r"<Tab( value=| value=|>)|^\s*\| [A-ZÉÈÀ]", lines[j]):
                    ctx = lines[j].strip()
                    break
            print(f"  {i+1:4} APRES: {ctx[:150]}")
            print(f"         TEXT : {l.strip()[:150]}")
