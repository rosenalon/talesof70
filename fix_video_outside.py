import re

# ===== HOMEPAGE =====
hp = open('index.html', 'rb').read()

# Strategy: Hide the ENTIRE vlog-featured section (broken video area)
# Then inject a clean hero section right after it, using unique IDs that 
# no theme CSS can match

# Add CSS to hide original hero and style new one
fix_css = b"""<style id="vfix2">
.vlog-featured{display:none!important}
#clean-hero{background:#1a1a2e;padding:40px 0;color:#fff;display:block!important}
#clean-hero .ch-inner{max-width:1100px;margin:0 auto;display:flex;gap:40px;align-items:center;padding:0 30px;direction:rtl}
#clean-hero .ch-vid{flex:1.2;min-width:0}
#clean-hero .ch-wrap{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:6px}
#clean-hero .ch-wrap iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
#clean-hero .ch-txt{flex:1;text-align:right}
#clean-hero .ch-txt h1{font-size:28px;color:#29aae3;margin-bottom:18px}
#clean-hero .ch-txt p{font-size:15px;line-height:1.9;margin-bottom:12px;color:rgba(255,255,255,0.9)}
#clean-hero .ch-txt a{color:#29aae3}
@media(max-width:900px){#clean-hero .ch-inner{flex-direction:column}}
</style>"""

hp = hp.replace(b'</head>', fix_css + b'\n</head>')

# Find end of vlog-featured section and inject clean hero after it
end_featured = hp.find(b'</div>\n</div>', hp.find(b'vlog-featured-1', hp.find(b'<body')))
# Walk forward to find the actual close of the featured section
# Look for the vlog-section that comes after
next_section = hp.find(b'<div class="vlog-section', hp.find(b'vlog-format-inplay', hp.find(b'<body')))
if next_section < 0:
    next_section = hp.find(b'vlog-no-sid', hp.find(b'<body'))
    if next_section > 0:
        next_section = hp.rfind(b'<div', next_section - 50, next_section)

if next_section > 0:
    hero_html = b'''<div id="clean-hero">
<div class="ch-inner">
<div class="ch-vid"><div class="ch-wrap"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" frameborder="0" allowfullscreen></iframe></div></div>
<div class="ch-txt">
<h1>\xd7\xa4\xd7\xa8\xd7\x95\xd7\x99\xd7\xa7\xd7\x98 "\xd7\x9e\xd7\xa2\xd7\xa9\xd7\x94 \xd7\x91 \xe2\x80\x93 70"</h1>
<p>\xd7\x91\xd7\x9e\xd7\xa1\xd7\x92\xd7\xa8\xd7\xaa \xd7\xa4\xd7\xa8\xd7\x95\xd7\x99\xd7\xa7\xd7\x98 \xd7\x99\xd7\x99\xd7\x97\xd7\x95\xd7\x93\xd7\x99 \xd7\x99\xd7\xa6\xd7\x90\xd7\x95 150 \xd7\xa1\xd7\x98\xd7\x95\xd7\x93\xd7\xa0\xd7\x98\xd7\x99\xd7\x9d \xd7\x9e\xd7\x94\xd7\x9e\xd7\xa8\xd7\x9b\xd7\x96 \xd7\x94\xd7\x91\xd7\x99\xd7\xa0\xd7\xaa\xd7\x97\xd7\x95\xd7\x9e\xd7\x99 \xd7\x9c\xd7\xa4\xd7\x92\xd7\x95\xd7\xa9 \xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c\xd7\x99\xd7\x95\xd7\xaa \xd7\x95\xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c\xd7\x99\xd7\x9d \xd7\x9e\xd7\x9b\xd7\x9c \xd7\xa8\xd7\x97\xd7\x91\xd7\x99 \xd7\x94\xd7\x90\xd7\xa8\xd7\xa5 \xd7\x95\xd7\x9c\xd7\xaa\xd7\xa2\xd7\x93 \xd7\x90\xd7\xaa \xd7\x94\xd7\xa1\xd7\x99\xd7\xa4\xd7\x95\xd7\xa8 \xd7\x94\xd7\x90\xd7\x99\xd7\xa9\xd7\x99 \xd7\xa9\xd7\x9c\xd7\x94\xd7\x9d \xd7\x91\xd7\x90\xd7\x9e\xd7\xa6\xd7\xa2\xd7\x95\xd7\xaa \xd7\x98\xd7\x9c\xd7\xa4\xd7\x95\xd7\xa0\xd7\x99\xd7\x9d \xd7\xa1\xd7\x9c\xd7\x95\xd7\x9c\xd7\xa8\xd7\x99\xd7\x99\xd7\x9d.</p>
<p>\xd7\x93\xd7\xa8\xd7\x9a \xd7\xa9\xd7\x9c\xd7\x9c \xd7\x94\xd7\xa1\xd7\x99\xd7\xa4\xd7\x95\xd7\xa8\xd7\x99\xd7\x9d \xd7\x95\xd7\x94\xd7\x97\xd7\x95\xd7\x95\xd7\x99\xd7\x95\xd7\xaa \xd7\x94\xd7\x90\xd7\xa0\xd7\x95\xd7\xa9\xd7\x99\xd7\x95\xd7\xaa, \xd7\xa2\xd7\x95\xd7\x9c\xd7\x94 \xd7\x95\xd7\x9e\xd7\xa9\xd7\xaa\xd7\xa7\xd7\xa4\xd7\xaa \xd7\x93\xd7\x9e\xd7\x95\xd7\xaa\xd7\x94 \xd7\xa9\xd7\x9c \xd7\x94\xd7\x97\xd7\x91\xd7\xa8\xd7\x94 \xd7\x91\xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c.</p>
<p>\xd7\x90\xd7\xaa\xd7\x9d \xd7\x9e\xd7\x95\xd7\x96\xd7\x9e\xd7\xa0\xd7\x99\xd7\x9d \xd7\x9c\xd7\x94\xd7\xa6\xd7\x98\xd7\xa8\xd7\xa3 \xd7\x90\xd7\x9c\xd7\x99\xd7\xa0\xd7\x95, \xd7\x9c\xd7\xa6\xd7\xa4\xd7\x95\xd7\xaa, \xd7\x9c\xd7\x94\xd7\xaa\xd7\xa8\xd7\x92\xd7\xa9, \xd7\x9c\xd7\xa6\xd7\x97\xd7\x95\xd7\xa7, \xd7\x9c\xd7\x91\xd7\x9b\xd7\x95\xd7\xaa \xd7\x95\xd7\x9c\xd7\x94\xd7\xaa\xd7\x97\xd7\x91\xd7\xa8 <a href="https://rosenalon.github.io/talesof70/">\xd7\x9c\xd7\xa1\xd7\x99\xd7\xa4\xd7\x95\xd7\xa8\xd7\x9d \xd7\xa9\xd7\x9c 70 \xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c\xd7\x99\xd7\x9d.</a></p>
</div>
</div>
</div>
'''
    hp = hp[:next_section] + hero_html + hp[next_section:]
    print(f"Homepage: injected clean hero at position {next_section}")
else:
    print("ERROR: could not find injection point")

open('index.html', 'wb').write(hp)
print(f"Homepage: {len(hp)} bytes")

# ===== ABOUT PAGE =====
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()

# Same approach - hide original video wrapper, inject clean one before it
about_css = b"""<style id="vfix2">
.entry-content-single .fluid-width-video-wrapper{display:none!important}
#clean-about-vid{max-width:640px;margin:0 auto 20px;display:block!important}
#clean-about-vid .cav-wrap{position:relative;padding-bottom:56.25%;height:0;overflow:hidden}
#clean-about-vid .cav-wrap iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
</style>"""

ab = ab.replace(b'</head>', about_css + b'\n</head>')

# Find the fluid-width-video-wrapper and inject clean embed BEFORE it
fwvw = ab.find(b'<div class=fluid-width-video-wrapper', ab.find(b'<body'))
if fwvw > 0:
    clean_vid = b'<div id="clean-about-vid"><div class="cav-wrap"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" frameborder="0" allowfullscreen></iframe></div></div>\n'
    ab = ab[:fwvw] + clean_vid + ab[fwvw:]
    print(f"About: injected clean video before wrapper")

open('מעשה-ב-70-למה/index.html', 'wb').write(ab)
print(f"About: {len(ab)} bytes")

print("\nDone. Videos use unique IDs outside any theme CSS scope.")
