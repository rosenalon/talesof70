import os

target = 'https://rosenalon.github.io/talesof70/'
count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root_dir, fname)
        html = open(fpath, 'rb').read()
        # Find the SVG logo pattern and fix the href before it
        old1 = b'href="https://rosenalon.github.io/talesof70"'
        new1 = b'href="https://rosenalon.github.io/talesof70/"'
        old2 = b'href=https://rosenalon.github.io/talesof70\n'
        new2 = b'href=https://rosenalon.github.io/talesof70/\n'
        old3 = b'href=https://rosenalon.github.io/talesof70>'
        new3 = b'href=https://rosenalon.github.io/talesof70/>'
        changed = False
        if old1 in html:
            html = html.replace(old1, new1)
            changed = True
        if old2 in html:
            html = html.replace(old2, new2)
            changed = True
        if old3 in html:
            html = html.replace(old3, new3)
            changed = True
        if changed:
            open(fpath, 'wb').write(html)
            count += 1
            print(f"  [{count}] {fpath}")

print(f"\nFixed {count} files")
