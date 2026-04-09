import re, os

# Check current state of creators page
fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

# Count student photos
photos = html.count('border-radius:50%')
cards = html.count('student-card') + html.count('class="sc"')
print(f"Page size: {len(html)} bytes")
print(f"Photos: {photos}")
print(f"Cards: {cards}")

# Check if student data is there
if 'אביה סעדון' in html:
    print("Student data: YES")
else:
    print("Student data: MISSING")

# Check header type
if 'vlog-header' in html:
    print("Header: theme header")
elif '<header' in html:
    print("Header: simple header")
else:
    print("Header: NONE")

# Show first 500 chars of body
body_start = html.find('<body')
if body_start > 0:
    snippet = html[body_start:body_start+800]
    snippet = re.sub(r'data:[^"]{50,}', '[IMG]', snippet)
    print(f"\nBody start:\n{snippet}")
