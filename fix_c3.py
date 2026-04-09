import os, re

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

html = re.sub(r'<style>\s*\.entry-content img.*?</style>', '', html, flags=re.DOTALL)
html = re.sub(r'<style>\s*\.students-thumbnail.*?</style>', '', html, flags=re.DOTALL)

css = """<style>
.entry-content img, .vlog-single-content img {
  max-width: 120px !important;
  width: 120px !important;
  height: 120px !important;
  object-fit: cover !important;
  display: inline-block !important;
  border-radius: 50% !important;
}
img.vlog-logo, .site-title img, .vlog-site-branding img {
  max-width: 200px !important;
  width: auto !important;
  height: auto !important;
  border-radius: 0 !important;
}
</style>"""

if 'width: 120px' not in html:
    html = html.replace('</head>', css + '\n</head>')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
