import os

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

css = """<style>
.entry-content img, .vlog-single-content img {
  max-width: 60px !important;
  height: auto !important;
  display: inline-block !important;
  border-radius: 50%;
}
img.vlog-logo {
  max-width: 200px !important;
  border-radius: 0 !important;
}
</style>"""

if 'max-width: 60px' not in html:
    html = html.replace('</head>', css + '\n</head>')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed creators page")
