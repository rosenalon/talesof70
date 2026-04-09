import os, re
from urllib.parse import unquote, quote

# Get all tag folders that actually exist
existing_tags = set()
tag_dir = 'tag'
if os.path.exists(tag_dir):
    for d in os.listdir(tag_dir):
        if os.path.isdir(os.path.join(tag_dir, d, )):
            existing_tags.add(d)

print(f"Existing tag folders: {len(existing_tags)}")
for t in sorted(existing_tags):
    print(f"  {t}")

# Get all tag links from the homepage
html = open('index.html', 'rb').read().decode('utf-8')
tag_links = re.findall(r'href="https://rosenalon\.github\.io/talesof70/tag/([^"]+)/"', html)
print(f"\nTag links in homepage: {len(tag_links)}")

# Check which are broken
broken = []
for link in tag_links:
    decoded = unquote(link)
    if decoded not in existing_tags:
        broken.append(decoded)
        print(f"  BROKEN: {decoded}")

working = len(tag_links) - len(broken)
print(f"\nWorking: {working}, Broken: {len(broken)}")
