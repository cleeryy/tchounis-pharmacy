#!/usr/bin/env python3
"""Inventaire exhaustif des marqueurs d'impasse dans les 18 fiches (hors index)."""
import os
import re
import unicodedata

DOCS = "/root/tchounis-pharmacy/content/docs"

MARKERS = [
    ("LAZY-VERIF", r"non\s+v[ée]rifi"),
    ("A-COMPLETER", r"[àa]\s+compl[ée]ter"),
    ("A-VERIFIER", r"[àa]\s+v[ée]rifier"),
    ("A-CONFIRMER", r"[àa]\s+confirmer"),
    ("TODO", r"\bTODO\b|\bFIXME\b|\bXXX\b"),
    ("N-A", r"\bN/A\b|\bHors[- ]sujet\b"),
    ("NON-PRECISE", r"non\s+pr[ée]cis[ée]"),
    ("NON-DOC", r"non\s+document[ée]"),
    ("NON-RENSEIGNE", r"non\s+renseign[ée]"),
    ("ELLIPSIS", r"\.{4,}|\?\s*\?\s*\?|…"),
    ("VIGNE", r"\bà\s+titre\s+indicatif\b|\bexemple\s+à\s+compl[ée]ter\b"),
]


def strip_accents(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


files = []
for root, _dirs, names in os.walk(DOCS):
    for n in sorted(names):
        if not n.endswith(".mdx"):
            continue
        p = os.path.join(root, n)
        rel = os.path.relpath(p, DOCS)
        if rel == "index.mdx" or rel.endswith("/index.mdx"):
            continue  # hors scope : uniquement les 18 fiches
        files.append((rel, p))

print(f"FICHES ANALYSEES : {len(files)}\n")

counts = {}
total = 0
for rel, path in files:
    hits = []
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        flat = strip_accents(line).lower()
        for tag, pat in MARKERS:
            if re.search(pat, flat):
                hits.append((i, tag, line.rstrip()))
                break
    if hits:
        counts[rel] = hits
        total += len(hits)
        print(f"===== {rel}  ({len(hits)} impasse(s))")
        for i, tag, txt in hits:
            print(f"  {i:4} [{tag:14}] {txt[:200]}")
        print()

print("=== SYNTHESE ===")
for rel in sorted(counts):
    tags = {}
    for _i, t, _x in counts[rel]:
        tags[t] = tags.get(t, 0) + 1
    print(f"  {rel:44} {len(counts[rel]):3}  {tags}")
print(f"  TOTAL IMPASSES : {total}")
