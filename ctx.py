#!/usr/bin/env python3
"""Contexte des VRAIES impasses : entête de section + onglet parent + lignes."""
import os
import re

DOCS = "/root/tchounis-pharmacy/content/docs"
PAT = [
    re.compile(r"non\s+v[ée]rifi", re.I),
    re.compile(r"^\s*(?:<Tab value=\"[^\"]+\">)?\s*Non\s+pr[ée]cis[ée]\s+dans\s+les\s+sources\s+consult[ée]es"),
    re.compile(r"^\s*\|[^|]*Non\s+pr[ée]cis[ée][^|]*\|\s*—\s*\|\s*—\s*\|\s*$"),
    re.compile(r"non\s+pr[ée]cis[ée]\s+dans\s+les\s+sources\s+consult[ée]es", re.I),
]

for root, _d, names in os.walk(DOCS):
    for n in sorted(names):
        if not n.endswith(".mdx") or n == "index.mdx":
            continue
        p = os.path.join(root, n)
        rel = os.path.relpath(p, DOCS)
        if rel.endswith("/index.mdx"):
            continue
        lines = open(p, encoding="utf-8").read().split("\n")
        hits = []
        for i, l in enumerate(lines):
            if any(pat.search(l) for pat in PAT):
                hits.append(i)
        if not hits:
            continue
        print(f"\n########## {rel}")
        last_head = ""
        shown = set()
        for i in hits:
            head = ""
            for j in range(i, -1, -1):
                if re.match(r"^#{2,4} ", lines[j]):
                    head = lines[j].strip()
                    break
            tab = ""
            for j in range(i, -1, -1):
                m = re.match(r"^\s*<Tab value=\"([^\"]+)\">", lines[j])
                if m and j != i:
                    tab = m.group(1)
                    break
                m2 = re.match(r"^\s*<Tab value=\"([^\"]+)\">\s*$", lines[j])
                if m2:
                    tab = m2.group(1)
                    break
            key = (head, tab)
            if key not in shown:
                shown.add(key)
                print(f"  --- SECTION: {head}   || ONGLET: {tab or '(aucun)'}")
            print(f"  {i+1:4} | {lines[i].strip()[:190]}")
