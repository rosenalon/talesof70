import re

# ===== HOMEPAGE =====
hp = open('index.html', 'rb').read()

# Remove any previous fix attempts
hp = re.sub(rb'<script>document\.write\([^<]*</script>', b'', hp)
hp = re.sub(rb'<div id="hero-yt"[^>]*></div>', b'', hp)
hp = re.sub(rb'<script>\s*window\.addEventListener\("DOMContentLoaded[^<]*</script>', b'', hp)

# Find the fluid-width-video-wrapper and put a clickable thumbnail inside
wrapper_match = re.search(rb'(class=fluid-width-video-wrapper style=padding-top:56\.25%>)', hp)
if wrapper_match:
    pos = wrapper_match.end()
    # Find next closing div
    close = hp.find(b'</div>', pos)
    # Replace everything between wrapper open and close with our thumbnail
    thumb = b'''<a href="https://www.youtube.com/watch?v=FiuItIwjx28" target="_blank" rel="noopener" style="display:block;position:absolute;top:0;left:0;width:100%;height:100%">
<img src="https://img.youtube.com/vi/FiuItIwjx28/maxresdefault.jpg" style="width:100%;height:100%;object-fit:cover">
<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;background:#cd201f;border-radius:14px;display:flex;align-items:center;justify-content:center;cursor:pointer">
<svg width="24" height="24" viewBox="0 0 24 24" fill="white"><polygon points="8,5 19,12 8,19"/></svg>
</div></a>'''
    hp = hp[:pos] + thumb + hp[close:]
    print("Homepage: inserted clickable YouTube thumbnail")
else:
    print("Homepage: wrapper not found")

iframes_left = hp.count(b'<iframe')
print(f"Homepage iframes remaining: {iframes_left}")

open('index.html', 'wb').write(hp)

# ===== ABOUT PAGE =====
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()

# The srcdoc is massive - find it by looking for the sandbox+srcdoc pattern
# Match from <iframe to </iframe> that contains srcdoc
old = re.search(rb'<iframe[^>]*srcdoc=".*?"[^>]*></iframe>', ab, re.DOTALL)
if not old:
    # srcdoc might use single quotes or be very long - try simpler
    start = ab.find(b'<iframe frameborder=0 allow="autoplay')
    if start > 0:
        end = ab.find(b'</iframe>', start) + len(b'</iframe>')
        old_bytes = ab[start:end]
        new_iframe = b'<a href="https://www.youtube.com/watch?v=FiuItIwjx28" target="_blank" rel="noopener" style="display:block;position:absolute;top:0;left:0;width:100%;height:100%"><img src="https://img.youtube.com/vi/FiuItIwjx28/maxresdefault.jpg" style="width:100%;height:100%;object-fit:cover"><div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;background:#cd201f;border-radius:14px;display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="white"><polygon points="8,5 19,12 8,19"/></svg></div></a>'
        ab = ab[:start] + new_iframe + ab[end:]
        print(f"About: replaced iframe ({len(old_bytes)} bytes) with clickable thumbnail")
    else:
        print("About: iframe not found at all")
else:
    new_iframe = b'<a href="https://www.youtube.com/watch?v=FiuItIwjx28" target="_blank" rel="noopener" style="display:block;position:absolute;top:0;left:0;width:100%;height:100%"><img src="https://img.youtube.com/vi/FiuItIwjx28/maxresdefault.jpg" style="width:100%;height:100%;object-fit:cover"><div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;background:#cd201f;border-radius:14px;display:flex;align-items:center;justify-content:center"><svg width="24" height="24" viewBox="0 0 24 24" fill="white"><polygon points="8,5 19,12 8,19"/></svg></div></a>'
    ab = ab.replace(old.group(0), new_iframe)
    print("About: replaced srcdoc iframe with clickable thumbnail")

open('מעשה-ב-70-למה/index.html', 'wb').write(ab)

print("\nBoth pages now show YouTube thumbnails with red play button.")
print("Clicking opens YouTube in new tab - this is the only reliable method for SingleFile pages.")
