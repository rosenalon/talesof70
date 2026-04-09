import os

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

# Remove old CSS fixes
old_css = []
import re
for m in re.finditer(r'<style>[^<]*(?:entry-content img|120px|60px|80px|students-thumbnail)[^<]*</style>', html):
    old_css.append(m.group())
for c in old_css:
    html = html.replace(c, '')

# Show structure around student items
# Find what class/tag wraps each student
idx = html.find('אדוה דרוקר')
if idx > 0:
    snippet = html[max(0,idx-500):idx+100]
    # Remove base64 images for readability
    snippet = re.sub(r'data:[^"]{50,}', '[IMG_DATA]', snippet)
    print("AROUND STUDENT:")
    print(snippet[-300:])
    print("---")

# Also check the overall container
idx2 = html.find('הסטודנטים')
if idx2 > 0:
    snippet2 = html[idx2:idx2+500]
    snippet2 = re.sub(r'data:[^"]{50,}', '[IMG_DATA]', snippet2)
    print("AFTER STUDENTS HEADER:")
    print(snippet2[:400])

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("\nDone inspecting")
