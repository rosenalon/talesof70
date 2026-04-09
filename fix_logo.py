import os, re

count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root_dir, fname)
        html = open(fpath, 'r', encoding='utf-8').read()
        if 'width="350" height="123"' in html or "width='350' height='123'" in html:
            # Fix links containing the SVG logo to point to runi.ac.il
            html = re.sub(
                r'<a\s+([^>]*?)href="[^"]*"([^>]*>)\s*(<img[^>]*(?:width="350"|width=\'350\')[^>]*(?:height="123"|height=\'123\')[^>]*>)',
                r'<a \1href="https://www.runi.ac.il"\2\3',
                html
            )
            # Also handle width=350 without quotes
            html = re.sub(
                r'<a\s+([^>]*?)href=["\'][^"\']*["\']([^>]*>)\s*(<img[^>]*width=350[^>]*height=123[^>]*>)',
                r'<a \1href="https://www.runi.ac.il"\2\3',
                html
            )
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1

print(f"Fixed {count} files")
