import re

# ===== FIX HOMEPAGE =====
hp = open('index.html', 'rb').read()

# The JS injection created a div but no iframe. Replace the whole hero-yt div with a direct iframe
# using a script tag that executes inline via document.write
old = b'<div id="hero-yt" style="position:absolute;top:0;left:0;width:100%;height:100%;background:#000"></div>'

# Use document.write in an inline script - this executes during parse, not after DOMContentLoaded
new = b'<script>document.write(\'<iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>\')</script>'

if old in hp:
    hp = hp.replace(old, new)
    print("Homepage: replaced div with document.write iframe")
else:
    print("Homepage: hero-yt div not found, searching...")
    # Remove old DOMContentLoaded script too
    hp = re.sub(rb'<script>\s*window\.addEventListener\("DOMContentLoaded"[^<]*</script>', b'', hp)
    # Find the fluid-width-video-wrapper and inject inside it
    wrapper = re.search(rb'class=fluid-width-video-wrapper[^>]*>', hp)
    if wrapper:
        insert_pos = wrapper.end()
        iframe = b'<script>document.write(\'<iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>\')</script>'
        hp = hp[:insert_pos] + iframe + hp[insert_pos:]
        print("Homepage: injected into fluid-width-video-wrapper")

# Also clean up any leftover DOMContentLoaded script
hp = re.sub(rb'<script>\s*window\.addEventListener\("DOMContentLoaded",function\(\)\{[^}]*hero-yt[^<]*</script>', b'', hp)

open('index.html', 'wb').write(hp)

# Verify
count = open('index.html', 'rb').read().count(b'FiuItIwjx28')
iframes = len(re.findall(rb'<iframe', open('index.html', 'rb').read()))
print(f"Homepage verification: FiuItIwjx28 refs={count}, iframes={iframes}")

# ===== FIX ABOUT PAGE =====
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()

# Replace the sandboxed srcdoc iframe with a proper YouTube embed
old_iframe = re.search(
    rb'<iframe\s+frameborder=0\s+allow="[^"]*"\s+allowfullscreen\s+name=fitvid0\s+sandbox="[^"]*"\s+srcdoc="[^"]*"></iframe>',
    ab,
    re.DOTALL
)

if old_iframe:
    new_iframe = b'<iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>'
    ab = ab.replace(old_iframe.group(0), new_iframe)
    print("About: replaced sandboxed srcdoc iframe with proper embed")
else:
    # Try more aggressive match
    ab = re.sub(
        rb'<iframe[^>]*srcdoc="[^"]*FiuItIwjx28[^"]*"[^>]*></iframe>',
        b'<iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>',
        ab
    )
    # Also try without the specific video ID
    ab = re.sub(
        rb'<iframe[^>]*name=fitvid0[^>]*sandbox="[^"]*"[^>]*srcdoc="[^"]*"[^>]*></iframe>',
        b'<iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>',
        ab
    )
    print("About: attempted aggressive iframe replacement")

open('מעשה-ב-70-למה/index.html', 'wb').write(ab)

# Verify about
iframes = len(re.findall(rb'<iframe', open('מעשה-ב-70-למה/index.html', 'rb').read()))
sandboxes = len(re.findall(rb'sandbox=', open('מעשה-ב-70-למה/index.html', 'rb').read()))
print(f"About verification: iframes={iframes}, sandboxes={sandboxes}")

print("\nDone")
