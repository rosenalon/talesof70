import re

# Fix both pages with CSS overrides

override_css = b"""<style id="video-fix">
.vlog-featured .fluid-width-video-wrapper{position:relative!important;padding-top:56.25%!important;height:0!important;overflow:visible!important;z-index:10!important}
.vlog-featured .fluid-width-video-wrapper iframe{position:absolute!important;top:0!important;left:0!important;width:100%!important;height:100%!important;z-index:10!important;border:0!important}
.vlog-featured .vlog-popup-wrapper{max-width:100%!important;width:100%!important;margin:0!important}
.vlog-featured .vlog-format-content{display:block!important;visibility:visible!important;opacity:1!important}
.vlog-featured .vlog-format-content iframe{height:100%!important}
.vlog-featured .vlog-cover-bg{height:auto!important;min-height:400px!important;overflow:visible!important}
.vlog-featured .vlog-cover{display:none!important}
.vlog-format-inplay{display:none!important}
.entry-content-single .fluid-width-video-wrapper{position:relative!important;padding-top:56.25%!important;height:0!important;overflow:visible!important}
.entry-content-single .fluid-width-video-wrapper iframe{position:absolute!important;top:0!important;left:0!important;width:100%!important;height:100%!important;border:0!important}
</style>"""

# Homepage
hp = open('index.html', 'rb').read()
if b'video-fix' not in hp:
    hp = hp.replace(b'</head>', override_css + b'\n</head>')
open('index.html', 'wb').write(hp)
print(f"Homepage: added video CSS overrides ({len(hp)} bytes)")

# About page
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()
if b'video-fix' not in ab:
    ab = ab.replace(b'</head>', override_css + b'\n</head>')
open('מעשה-ב-70-למה/index.html', 'wb').write(ab)
print(f"About: added video CSS overrides ({len(ab)} bytes)")

# Verify iframes exist
for name, path in [('Homepage', 'index.html'), ('About', 'מעשה-ב-70-למה/index.html')]:
    h = open(path, 'rb').read()
    body = h[h.find(b'<body'):]
    iframes = re.findall(rb'<iframe[^>]*>', body)
    print(f"{name}: {len(iframes)} iframes")
    for f in iframes:
        f = re.sub(rb'srcdoc="[^"]{50,}"', b'srcdoc="[...]"', f)
        print(f"  {f[:200].decode('utf-8','replace')}")
