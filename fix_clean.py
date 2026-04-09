import os, re

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'rb').read().decode('utf-8')

# Strip ALL previously added style blocks (they contain these markers)
markers = ['student', 'entry-content img', '120px', '60px', '80px', '75px',
           '100px', 'creators', 'Fix text', 'vlog-content']
for m in re.finditer(r'<style>([^<]{1,2000})</style>', html):
    block = m.group(1)
    for marker in markers:
        if marker in block:
            html = html.replace(m.group(0), '')
            break

# One clean CSS block
clean_css = """<style id="creators-fix">
/* Student grid - 3 columns */
.students-row{display:flex!important;flex-wrap:wrap!important;direction:rtl!important;gap:8px!important;justify-content:center!important}
.student-item{width:31%;box-sizing:border-box;border:1px solid #ddd;background:#fafafa;padding:8px;display:flex;align-items:center;direction:rtl;gap:8px;min-height:80px}
.student-img img{width:70px!important;height:70px!important;max-width:70px!important;border-radius:50%!important;object-fit:cover!important;flex-shrink:0!important}
.student-details{text-align:right}
.student-name{font-size:13px!important;font-weight:bold!important;margin:0 0 2px 0!important}
.student-school,.student-year{font-size:11px!important;color:#666!important;display:block!important}
.student-school p{margin:0!important}
/* Page text */
.vlog-single-content .entry-content>p,.vlog-single-content .entry-content strong{font-size:14px!important}
.vlog-single-content h1.entry-title{font-size:22px!important;text-align:center!important}
/* Sponsor logos small */
.entry-content img[class*="wp-image"]:not([class*="wp-post-image"]){max-width:120px!important;max-height:60px!important;width:auto!important;height:auto!important;border-radius:0!important}
/* Layout */
.vlog-content{max-width:900px!important;margin:0 auto!important}
@media(max-width:768px){.student-item{width:48%!important}}
@media(max-width:480px){.student-item{width:100%!important}}
</style>"""

html = html.replace('</head>', clean_css + '\n</head>')

open(fpath, 'wb').write(html.encode('utf-8'))
print("Done - clean rebuild")
