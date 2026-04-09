import os, re

html = open('index.html', 'rb').read().decode('utf-8')

# Build mapping: display name -> folder name
tag_dir = 'tag'
existing = {}
for d in os.listdir(tag_dir):
    if os.path.isdir(os.path.join(tag_dir, d)):
        existing[d] = d

NEW = 'https://rosenalon.github.io/talesof70'

# Find all tag links and fix them
def fix_tag(m):
    tag_name = m.group(1)
    display = m.group(2)
    # Convert to folder format: spaces->hyphens, slash->hyphen
    folder = tag_name.replace(' ', '-').replace('/', '-')
    if folder in existing:
        return f'href="{NEW}/tag/{folder}/">{display}'
    else:
        return m.group(0)

html = re.sub(
    r'href="' + re.escape(NEW) + r'/tag/([^"]+)/">([^<]+)',
    fix_tag,
    html
)

# Verify
broken = re.findall(r'href="' + re.escape(NEW) + r'/tag/([^"]+)/"', html)
fixed = 0
still_broken = 0
for b in broken:
    folder = b.replace(' ', '-').replace('/', '-')
    if folder in existing:
        fixed += 1
    else:
        still_broken += 1
        print(f"Still broken: {b}")

open('index.html', 'wb').write(html.encode('utf-8'))
print(f"Fixed. Working: {fixed}, Still broken: {still_broken}")
