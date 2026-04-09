import os, re
from urllib.parse import unquote

# Get existing tag folders
existing = set()
for d in os.listdir('tag'):
    if os.path.isdir(os.path.join('tag', d)):
        existing.add(d)

# Get all tag links from homepage
html = open('index.html', 'r', encoding='utf-8').read()
tag_links = re.findall(r'class="tag-btn" href="[^"]*?/tag/([^"]+)/"', html)
if not tag_links:
    tag_links = re.findall(r'href="[^"]*?/tag/([^"]+)/"[^>]*class="tag-btn"', html)
if not tag_links:
    tag_links = re.findall(r'href="[^"]*?/tag/([^"]+)/"', html)

print(f"Existing folders: {len(existing)}")
print(f"Tag links: {len(tag_links)}")

broken = []
for link in tag_links:
    decoded = unquote(link)
    if decoded not in existing:
        # Try common fixes
        fixed = decoded.replace(' ', '-').replace('/', '-')
        if fixed in existing:
            broken.append((decoded, fixed))
        else:
            # Try other variations
            fixed2 = decoded.replace('"', '').replace("'", "")
            if fixed2 in existing:
                broken.append((decoded, fixed2))
            else:
                broken.append((decoded, None))

for old, fix in broken:
    status = f"-> {fix}" if fix else "NO MATCH"
    print(f"  BROKEN: '{old}' {status}")

# Apply fixes
if broken:
    for old, fix in broken:
        if fix:
            html = html.replace(f'/tag/{old}/', f'/tag/{fix}/')
    
    open('index.html', 'w', encoding='utf-8').write(html)
    fixed_count = sum(1 for _, f in broken if f)
    unfixed = sum(1 for _, f in broken if not f)
    print(f"\nFixed {fixed_count}, Unfixed {unfixed}")
else:
    print("\nAll tags OK")
