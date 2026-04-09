import re
html = open(r'2018\03\09\ריקה-סוסקין\index.html', 'r', encoding='utf-8').read()

# Show context around each 'youtu' occurrence
for m in re.finditer(r'youtu', html):
    start = max(0, m.start()-30)
    end = min(len(html), m.end()+50)
    ctx = html[start:end]
    # Skip if inside a style block
    style_before = html.rfind('<style', 0, m.start())
    style_end = html.rfind('</style', 0, m.start())
    if style_before > style_end:
        continue  # inside a style tag
    print(f"  youtu: ...{ctx}...")

print("\n---IFRAME---")
for m in re.finditer(r'iframe', html, re.IGNORECASE):
    start = max(0, m.start()-50)
    end = min(len(html), m.end()+100)
    ctx = html[start:end]
    style_before = html.rfind('<style', 0, m.start())
    style_end = html.rfind('</style', 0, m.start())
    if style_before > style_end:
        continue
    print(f"  iframe: ...{ctx}...")

print("\n---javascript:void---")
for m in re.finditer(r'javascript:\s*void', html):
    start = max(0, m.start()-200)
    end = min(len(html), m.end()+50)
    ctx = html[start:end]
    ctx = re.sub(r'data:image[^"]{20,}', '[IMG_DATA]', ctx)
    print(f"  void: ...{ctx}...")
    break
