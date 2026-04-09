import os
from bs4 import BeautifulSoup

fixes = """<style>
/* Fix video/image sizing on subpages */
.entry-image img, .vlog-post img, article img, .wp-post-image {
  max-width: 100% !important;
  height: auto !important;
  width: 100% !important;
}
.entry-image, .meta-media {
  max-width: 100% !important;
  overflow: hidden !important;
}
iframe {
  max-width: 100% !important;
}
.vlog-content {
  width: 100% !important;
  float: none !important;
}
.container {
  max-width: 1140px !important;
  margin: 0 auto !important;
}
.col-lg-4, .col-sm-4, .col-md-4 {
  width: 33.33% !important;
  float: right !important;
}
@media (max-width: 767px) {
  .col-lg-4, .col-sm-4, .col-md-4 {
    width: 100% !important;
    float: none !important;
  }
}
</style>"""

count = 0
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root, fname)
        if fpath == '.\\index.html':
            continue  # skip homepage
        html = open(fpath, 'r', encoding='utf-8').read()
        if fixes not in html:
            html = html.replace('</head>', fixes + '\n</head>')
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1

print(f"Fixed {count} subpages")
