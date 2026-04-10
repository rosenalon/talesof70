import re

# The exact pattern that WORKS in post pages:
# <div style="max-width:640px;margin:0 auto 20px">
#   <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
#     <iframe src="https://www.youtube.com/embed/VIDEO_ID" 
#       style="position:absolute;top:0;left:0;width:100%;height:100%" 
#       frameborder="0" allowfullscreen></iframe>
#   </div>
# </div>

# ===== HOMEPAGE =====
hp = open('index.html', 'rb').read()
body_start = hp.find(b'<body')

# Find the vlog-format-content div that holds the broken video
# Replace everything inside it with the clean embed
marker_start = hp.find(b'<div class="vlog-format-content video">', body_start)
if marker_start > 0:
    # Find the closing </div> for vlog-format-content
    # Inside it is: vlog-popup-wrapper > fluid-width-video-wrapper > iframe stuff
    # Count divs to find the right closing tag
    inner_start = marker_start + len(b'<div class="vlog-format-content video">')
    
    # Find content between opening and closing of vlog-format-content
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
    
    old_content = hp[inner_start:inner_end]
    new_content = b'\n <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%" frameborder="0" allowfullscreen></iframe></div>\n '
    
    hp = hp[:inner_start] + new_content + hp[inner_end:]
    print(f"Homepage: replaced {len(old_content)} bytes inside vlog-format-content")
    print(f"  Old started with: {old_content[:100]}")
else:
    print("Homepage: vlog-format-content NOT FOUND")

open('index.html', 'wb').write(hp)

# ===== ABOUT PAGE =====
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()
body_start = ab.find(b'<body')

# Find the fluid-width-video-wrapper containing the broken srcdoc iframe
fwvw_start = ab.find(b'<div class=fluid-width-video-wrapper', body_start)
if fwvw_start > 0:
    fwvw_end = ab.find(b'</div>', fwvw_start) + len(b'</div>')
    old_wrapper = ab[fwvw_start:fwvw_end]
    new_wrapper = b'<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%" frameborder="0" allowfullscreen></iframe></div>'
    ab = ab[:fwvw_start] + new_wrapper + ab[fwvw_end:]
    print(f"About: replaced {len(old_wrapper)} bytes fluid-width-video-wrapper")
else:
    print("About: fluid-width-video-wrapper NOT FOUND")

open('מעשה-ב-70-למה/index.html', 'wb').write(ab)

# ===== VERIFY =====
for name, path in [('Homepage', 'index.html'), ('About', 'מעשה-ב-70-למה/index.html')]:
    h = open(path, 'rb').read()
    body = h[h.find(b'<body'):]
    embeds = body.count(b'youtube.com/embed/FiuItIwjx28')
    srcdocs = body.count(b'srcdoc=')
    sandboxes = body.count(b'sandbox=')
    sf_hidden_iframes = len(re.findall(rb'<iframe[^>]*sf-hidden', body))
    print(f"{name}: embeds={embeds}, srcdoc={srcdocs}, sandbox={sandboxes}, sf-hidden-iframes={sf_hidden_iframes}")
