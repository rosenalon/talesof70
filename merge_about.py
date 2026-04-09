import re, os

old_path = os.path.join('מעשה-ב-70-למה', 'index.html')
old_html = open(old_path, 'r', encoding='utf-8').read()

# Find the bottom image (wp-image-1255 or the large PNG)
img_match = re.search(r'<img[^>]*class="[^"]*wp-image-1255[^"]*"[^>]*src="(data:image[^"]+)"[^>]*/?>',  old_html)
if not img_match:
    # Try finding any large base64 PNG
    imgs = re.findall(r'(data:image/png;base64,[A-Za-z0-9+/=]{1000,})', old_html)
    if imgs:
        img_data = max(imgs, key=len)
        print(f"Found largest PNG: {len(img_data)//1024} KB")
    else:
        img_data = None
        print("No bottom image found")
else:
    img_data = img_match.group(1)
    print(f"Found wp-image-1255: {len(img_data)//1024} KB")

clean = open('about_clean.html', 'r', encoding='utf-8').read()

if img_data:
    clean = clean.replace(
        '<div class="bottom-image" id="bottom-img"></div>',
        f'<div class="bottom-image"><img src="{img_data}" alt="מעשה ב-70"></div>'
    )
    print("Image inserted")

open(old_path, 'w', encoding='utf-8').write(clean)
print("Saved")
