import re

# ===== FIX ABOUT PAGE =====
# Remove YouTube player garbage after our clean iframe div
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()

# Find our clean embed
clean_end = ab.find(b'allowfullscreen></iframe></div>')
if clean_end > 0:
    clean_end += len(b'allowfullscreen></iframe></div>')
    
    # Everything from here until the <ul> with bullet points is garbage
    next_ul = ab.find(b'<ul>', clean_end)
    # Or look for the first <li> with Hebrew content
    next_li = ab.find(b'<li><span class=li-bullet>', clean_end)
    # Or the <p> before the list
    next_p = ab.find(b'</p>', clean_end)
    
    # Find first real content marker
    targets = []
    for marker in [b'<ul>', b'<li><span class=li-bullet>', b'\n<ul>']:
        pos = ab.find(marker, clean_end)
        if pos > 0:
            targets.append(pos)
    
    if targets:
        garbage_end = min(targets)
        garbage = ab[clean_end:garbage_end]
        print(f"About: removing {len(garbage)} bytes of YouTube garbage")
        print(f"  Garbage starts with: {garbage[:100]}")
        print(f"  Garbage ends with: ...{garbage[-100:]}")
        ab = ab[:clean_end] + b'\n' + ab[garbage_end:]
    else:
        print("About: could not find end of garbage")

open('מעשה-ב-70-למה/index.html', 'wb').write(ab)
print(f"About saved: {len(ab)} bytes")

# ===== FIX HOMEPAGE =====
# Revert to original capture, then apply clean hero
hp = open('index.html', 'rb').read()

# Remove the broken clean-hero we injected (text on wrong side)
if b'id="clean-hero"' in hp:
    start = hp.find(b'<div id="clean-hero">')
    end = hp.find(b'</div>\n</div>\n</div>\n</div>', start)
    if end > 0:
        end += len(b'</div>\n</div>\n</div>\n</div>')
        hp = hp[:start] + hp[end:]
        print("Homepage: removed broken clean-hero")

# Also remove the CSS that hid vlog-featured
hp = hp.replace(b'.vlog-featured{display:none!important}', b'')

# Now use simpler approach: just replace content inside vlog-format-content
# Find the broken video wrapper and replace with clean iframe
body_start = hp.find(b'<body')
fmt_content = hp.find(b'<div class="vlog-format-content video">', body_start)
if fmt_content > 0:
    inner_start = fmt_content + len(b'<div class="vlog-format-content video">')
    # Find closing </div> for vlog-format-content by counting depth
    depth = 1
    pos = inner_start
    while depth > 0 and pos < len(hp):
        next_open = hp.find(b'<div', pos)
        next_close = hp.find(b'</div>', pos)
        if next_close < 0:
            break
        if next_open >= 0 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                inner_end = next_close
            pos = next_close + 6
    
    old_inner = hp[inner_start:inner_end]
    new_inner = b'\n <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%" frameborder="0" allowfullscreen></iframe></div>\n '
    hp = hp[:inner_start] + new_inner + hp[inner_end:]
    print(f"Homepage: replaced {len(old_inner)} bytes inside vlog-format-content")
else:
    print("Homepage: vlog-format-content not found")

open('index.html', 'wb').write(hp)
print(f"Homepage saved: {len(hp)} bytes")

# Verify
for name, path in [('Homepage', 'index.html'), ('About', 'מעשה-ב-70-למה/index.html')]:
    h = open(path, 'rb').read()
    body = h[h.find(b'<body'):]
    print(f"\n{name}:")
    print(f"  youtube.com/embed refs: {body.count(b'youtube.com/embed/FiuItIwjx28')}")
    print(f"  clean-hero divs: {body.count(b'clean-hero')}")
    print(f"  id=player garbage: {body.count(b'id=player')}")
    print(f"  ytp- garbage: {body.count(b'ytp-')}")
