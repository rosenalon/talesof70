import os, re

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

# Remove all previous CSS fixes for this page
html = re.sub(r'<style>\s*\.entry-content img.*?</style>', '', html, flags=re.DOTALL)
html = re.sub(r'<style>\s*\.students-thumbnail.*?</style>', '', html, flags=re.DOTALL)

css = """<style>
/* Student card grid */
.students-list, .entry-content .row, .vlog-single-content .row {
  display: flex !important;
  flex-wrap: wrap !important;
  direction: rtl !important;
}
.students-list > div, .entry-content .col-lg-4, .entry-content .col-md-4, .entry-content .col-sm-4 {
  width: 33.33% !important;
  float: none !important;
  padding: 10px !important;
  box-sizing: border-box !important;
}
/* Student card styling */
.student-item, .entry-content .student-item {
  border: 1px solid #eee !important;
  padding: 15px !important;
  margin-bottom: 15px !important;
  display: flex !important;
  align-items: center !important;
  direction: rtl !important;
  min-height: 130px !important;
}
/* Face photos - circular, ~120px */
.entry-content img, .vlog-single-content img {
  max-width: 120px !important;
  width: 120px !important;
  height: 120px !important;
  object-fit: cover !important;
  display: inline-block !important;
  border-radius: 50% !important;
  flex-shrink: 0 !important;
}
/* Keep logos normal */
img.vlog-logo, .site-title img, .vlog-site-branding img {
  max-width: 200px !important;
  width: auto !important;
  height: auto !important;
  border-radius: 0 !important;
}
/* Sponsor/partner logos in footer area */
.entry-content img[src*="logo"], .entry-content img[src*="doner"],
.entry-content img[src*="dibur"], .entry-content img[src*="bind"] {
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
print("Fixed creators page")
