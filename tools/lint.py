#!/usr/bin/env python3
"""Lint gate for the Open IGA Operating Framework repository.

Run from the repository root: python3 tools/lint.py
Exits non-zero on any violation. No dependencies beyond Python 3.
"""
import pathlib, re, sys, collections

root = pathlib.Path(__file__).resolve().parent.parent
problems = []
census = collections.Counter()

for md in sorted(root.rglob('*.md')):
    rel = md.relative_to(root)
    t = md.read_text()
    if t.startswith('---\n'):          # YAML front matter (issue templates): exempt from rule 1
        end = t.find('\n---\n', 3)
        if end != -1:
            t = t[end + 5:]

    # 1. Setext trap: a non-blank line directly above a dashed rule renders as a heading
    for m in re.finditer(r'([^\n]+)\n(-{3,}|={3,})\n', t):
        if m.group(1).strip():
            problems.append(f'{rel}: setext trap, text directly above a rule: "{m.group(1)[:60]}"')

    # 2. Heading length: a heading longer than 120 characters is body text wearing a hash
    for m in re.finditer(r'^(#{1,6} .{121,})$', t, re.M):
        problems.append(f'{rel}: overlong heading ({len(m.group(1))} chars): "{m.group(1)[:60]}"')

    # 3. Table integrity: every row in a block carries the same pipe count
    for block in re.finditer(r'((?:^\|.*\n)+)', t, re.M):
        counts = {r.count('|') for r in block.group(1).strip().split('\n')}
        if len(counts) > 1:
            problems.append(f'{rel}: table pipe mismatch near "{block.group(1)[:50]}"')

    # 4. Forbidden characters in prose
    if re.search(r'[\u2013\u2014\u2018\u2019\u201c\u201d]', t):
        problems.append(f'{rel}: em/en dash or curly quote present')

    # 5. Relative image links resolve
    for link in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', t):
        if not link.startswith('http') and not (md.parent / link).resolve().exists():
            problems.append(f'{rel}: broken image link {link}')

    # 6. Statement census
    for prefix, num in re.findall(r'\*\*(M|O|S|P|PS|C|MS|AP|F)(\d+)\.', t):
        census[prefix] = max(census[prefix], int(num))

print('statement census (highest identifier per prefix):',
      dict(sorted(census.items())))
if problems:
    print(f'\n{len(problems)} problem(s):')
    for p in problems:
        print(' -', p)
    sys.exit(1)
print('lint clean')
