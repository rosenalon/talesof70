import os

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

# Remove old fix if present
html = html.replace('<style>\n.students-thumbnail img, .student-photo img, article img[class*="thumbnail"] {\n  max-width: 80px !important;\n  height: auto !important;\n}\nimg[src*="students-thumbnail"] {\n  max-width: 80px !important;\n  height: auto !important;\n}\n.entry-content img {\n  max-width: 120px !important;\n  height: auto !important;\n}\n.entry-content .wp-post-image, .entry-content img.size-full, .entry-content img.size-large {\n  max-width: 120px !important;\n  height: auto !important;\n  display: inline-block !important;\n}\n</style>', '')

css = """<style>
.entry-content img, .vlog-single-content img {
  max-width: 60px !important;
  height: auto !important;
  display: inline-block !important;
  border-radius: 50%;
}
.entry-content img.vlog-logo, img.vlog-logo {
  max-width: 200px !important;
  border-radius: 0 !important;
}
</style>"""

if 'max-width: 60px' not in html:
    html = html.replace('</head>', css + '\n</head>')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed")
