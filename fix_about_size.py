import os

fpath = os.path.join('מעשה-ב-70-למה', 'index.html')
html = open(fpath, 'rb').read().decode('utf-8')

css = """<style id="fix-about-size">
.vlog-cover, .entry-image, .meta-media, .vlog-single-content .entry-image {
  max-width: 500px !important;
  margin: 0 auto !important;
  overflow: hidden !important;
}
.vlog-cover img, .entry-image img, .meta-media img {
  max-width: 100% !important;
  height: auto !important;
  width: 100% !important;
}
div[style*="max-width:640px"] {
  max-width: 500px !important;
}
iframe {
  max-width: 500px !important;
}
.col-lg-8 {
  max-width: 600px !important;
  margin: 0 auto !important;
  float: none !important;
}
</style>"""

if 'fix-about-size' not in html:
    html = html.replace('</head>', css + '\n</head>')
    open(fpath, 'wb').write(html.encode('utf-8'))
    print("Fixed")
else:
    print("Already fixed")
