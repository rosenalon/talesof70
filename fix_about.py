import re, os

# Fix 1: Smaller video embed on "מעשה ב-70 למה" page
fpath1 = os.path.join('מעשה-ב-70-למה', 'index.html')
if os.path.exists(fpath1):
    html = open(fpath1, 'r', encoding='utf-8').read()
    # Add same embed sizing as post pages
    if 'max-width:640px' not in html:
        css = '<style>.vlog-cover,.entry-image,.meta-media{max-width:640px!important;margin:0 auto!important;overflow:hidden!important}.vlog-cover img,.entry-image img,.meta-media img{max-width:100%!important;height:auto!important;width:100%!important}</style>'
        html = html.replace('</head>', css + '\n</head>')
    # Replace javascript:void play link with YouTube embed if present
    # The intro video is FiuItIwjx28
    if 'javascript:' in html:
        embed = '<div style="max-width:640px;margin:0 auto 20px"><div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%" frameborder="0" allowfullscreen></iframe></div></div>'
        html = re.sub(
            r'<a\s+class="vlog-cover"[^>]*href="[^"]*"[^>]*>.*?</a>',
            embed, html, flags=re.DOTALL, count=1
        )
    with open(fpath1, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed: {fpath1}")

# Fix 2: Logo SVG -> link to runi.ac.il (all pages)
count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root_dir, fname)
        html = open(fpath, 'r', encoding='utf-8').read()
        changed = False
        # Fix SVG logo links
        if 'width="350" height="123"' in html or "width='350' height='123'" in html or 'width=350' in html:
            html = re.sub(
                r'<a\s+([^>]*?)href=["\'][^"\']*["\']([^>]*>)\s*(<img[^>]*(?:width="350"|width=\'350\'|width=350)[^>]*>)',
                r'<a \1href="https://www.runi.ac.il"\2\3',
                html
            )
            changed = True
        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1

print(f"Fixed logo links in {count} files")
