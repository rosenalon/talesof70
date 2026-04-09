import os

count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root_dir, fname)
        html = open(fpath, 'rb').read()
        changed = False
        if b'href="https://www.runi.ac.il"' in html:
            html = html.replace(b'href="https://www.runi.ac.il"', b'href="https://rosenalon.github.io/talesof70/"')
            changed = True
        if b"href='https://www.runi.ac.il'" in html:
            html = html.replace(b"href='https://www.runi.ac.il'", b"href='https://rosenalon.github.io/talesof70/'")
            changed = True
        if changed:
            open(fpath, 'wb').write(html)
            count += 1
            print(f"  [{count}] {fpath}")
print(f"\nFixed {count} files")
