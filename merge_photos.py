import re, os

old_path = os.path.join('יוצרים-ושותפים', 'index.html')
old_html = open(old_path, 'r', encoding='utf-8').read()

photos = {}
for m in re.finditer(r'<div class="student-img">\s*<img[^>]*src="(data:image[^"]+)"[^>]*/>\s*</div>\s*<div class="student-details">\s*<h3 class="student-name">([^<]+)</h3>', old_html):
    photos[m.group(2).strip()] = m.group(1)

print(f"Extracted {len(photos)} photos")

clean = open('creators_clean.html', 'r', encoding='utf-8').read()

for name, img in photos.items():
    old_card = f'<div class="student-name">{name}</div>'
    new_card = f'<img src="{img}" style="width:70px;height:70px;border-radius:50%;object-fit:cover;flex-shrink:0">\n      <div class="student-name">{name}</div>'
    clean = clean.replace(old_card, new_card)

clean = clean.replace(
    'display: flex;\n  align-items: center;\n  justify-content: center;',
    'display: flex;\n  align-items: center;\n  gap: 8px;\n  direction: rtl;'
)

matched = clean.count('border-radius:50%')
print(f"Added {matched} photos")

open(old_path, 'w', encoding='utf-8').write(clean)
print("Saved")
