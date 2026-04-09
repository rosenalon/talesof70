import os, re

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

css = """<style>
/* Fix text size on creators page */
.entry-content h1, .vlog-single-content h1 {
  font-size: 24px !important;
  text-align: center !important;
}
.entry-content p, .vlog-single-content p {
  font-size: 14px !important;
  text-align: center !important;
  line-height: 1.8 !important;
}
.entry-content h2, .vlog-single-content h2,
.entry-content h3:not(.student-name), .vlog-single-content h3:not(.student-name) {
  font-size: 18px !important;
  text-align: center !important;
}
/* Fix header area */
.vlog-header-middle {
  height: auto !important;
  min-height: 80px !important;
}
.vlog-slot-c, .vlog-slot-l, .vlog-slot-r {
  position: relative !important;
}
.vlog-header-wrapper {
  overflow: visible !important;
}
/* Content area width */
.vlog-content, .vlog-single-content {
  max-width: 800px !important;
  margin: 0 auto !important;
  float: none !important;
}
</style>"""

if 'Fix text size on creators' not in html:
    html = html.replace('</head>', css + '\n</head>')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
