import re

CLEAN_EMBED = b'<div style="max-width:640px;margin:0 auto 20px"><div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%" frameborder="0" allowfullscreen></iframe></div></div>'

# ===== HOMEPAGE =====
hp = open('index.html', 'rb').read()

# Replace the entire vlog-popup-wrapper (which contains the broken video)
# with a clean embed, same as post pages
start = hp.find(b'<div class=vlog-popup-wrapper>', hp.find(b'<body'))
if start > 0:
    # Find matching closing: vlog-popup-wrapper contains fluid-width-video-wrapper contains iframe, then two closing divs
    end = hp.find(b'</div></div></div>', start)
    if end > 0:
        end += len(b'</div></div></div>')
        old_chunk = hp[start:end]
        hp = hp[:start] + CLEAN_EMBED + hp[end:]
        print(f"Homepage: replaced {len(old_chunk)} bytes of video wrapper with clean embed")

open('index.html', 'wb').write(hp)

# ===== ABOUT PAGE =====
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()

# Same approach - find the fluid-width-video-wrapper and replace the whole thing
start = ab.find(b'<div class=fluid-width-video-wrapper', ab.find(b'<body'))
if start > 0:
    end = ab.find(b'</iframe>', start)
    if end > 0:
        # Include the closing tags for fluid-width-video-wrapper
        end = ab.find(b'</div>', end) + len(b'</div>')
        old_chunk = ab[start:end]
        ab = ab[:start] + CLEAN_EMBED + ab[end:]
        print(f"About: replaced {len(old_chunk)} bytes of video wrapper with clean embed")

open('מעשה-ב-70-למה/index.html', 'wb').write(ab)

# Verify
for name, path in [('Homepage', 'index.html'), ('About', 'מעשה-ב-70-למה/index.html')]:
    h = open(path, 'rb').read()
    count = h.count(b'youtube.com/embed/FiuItIwjx28')
    wrappers = h.count(b'vlog-popup-wrapper')
    print(f"{name}: embed refs={count}, old wrappers remaining={wrappers}")
