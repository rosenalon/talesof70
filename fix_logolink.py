import os

count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root_dir, fname)
        html = open(fpath, 'r', encoding='utf-8').read()
        old = 'href="https://rosenalon.github.io/talesof70"'
        new = 'href="https://rosenalon.github.io/talesof70/"'
        # The logo links currently point to rosenalon.github.io/talesof70
        # Just make sure they have trailing slash
        if old in html and new not in html:
            html = html.replace(old, new)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
print(f"Fixed {count} files")
