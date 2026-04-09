import os

css_fix = """<style>
.vlog-prev-next-nav { display: flex !important; justify-content: space-between !important; direction: ltr !important; }
.vlog-prev-next-nav .vlog-prev-link { text-align: left !important; }
.vlog-prev-next-nav .vlog-next-link { text-align: right !important; }
.vlog-pn-prev { float: left !important; }
.vlog-pn-next { float: right !important; }
</style>"""

count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html' or '2018' not in root_dir:
            continue
        fpath = os.path.join(root_dir, fname)
        html = open(fpath, 'r', encoding='utf-8').read()
        if 'vlog-prev-next-nav' in html and 'vlog-pn-prev { float: left' not in html:
            html = html.replace('</head>', css_fix + '\n</head>')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1

print(f"Fixed {count} files")
