import re

fpath = r'יוצרים-ושותפים\index.html'
html = open(fpath, 'r', encoding='utf-8').read()

# Fix 1: Make student thumbnail photos small
css_fix = """<style>
.students-thumbnail img, .student-photo img, article img[class*="thumbnail"] {
  max-width: 80px !important;
  height: auto !important;
}
img[src*="students-thumbnail"] {
  max-width: 80px !important;
  height: auto !important;
}
.entry-content img {
  max-width: 120px !important;
  height: auto !important;
}
.entry-content .wp-post-image, .entry-content img.size-full, .entry-content img.size-large {
  max-width: 120px !important;
  height: auto !important;
  display: inline-block !important;
}
</style>"""

if 'students-thumbnail' not in html or 'max-width: 80px' not in html:
    html = html.replace('</head>', css_fix + '\n</head>')

# Fix 2: Make the SVG placeholder logo link to runi.ac.il
html = re.sub(
    r'(<a[^>]*href=")[^"]*("[^>]*>)\s*(<img[^>]*src=["\']data:image/svg\+xml[^"\']*width="350"[^"\']*height="123"[^>]*>)',
    r'\g<1>https://www.runi.ac.il\2\3',
    html
)

# Also catch cases where the img is not inside a link - wrap it
html = re.sub(
    r'(?<!href="[^"]{0,500})(<img[^>]*src=["\x27]data:image/svg\+xml,[^"\']*width=.350.[^"\']*height=.123.[^>]*>)',
    r'<a href="https://www.runi.ac.il">\1</a>',
    html,
    count=0
)

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed")
