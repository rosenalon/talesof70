import re

hp = open('index.html', 'rb').read()

# Replace the thumbnail link with a proper iframe (same as working about page)
old = rb'<a href="https://www.youtube.com/watch?v=FiuItIwjx28" target="_blank" rel="noopener" style="display:block;position:absolute;top:0;left:0;width:100%;height:100%">\n<img src="https://img.youtube.com/vi/FiuItIwjx28/maxresdefault.jpg" style="width:100%;height:100%;object-fit:cover">\n<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;background:#cd201f;border-radius:14px;display:flex;align-items:center;justify-content:center;cursor:pointer">\n<svg width="24" height="24" viewBox="0 0 24 24" fill="white"><polygon points="8,5 19,12 8,19"/></svg>\n</div></a>'

new = rb'<iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>'

if old in hp:
    hp = hp.replace(old, new)
    print("Replaced thumbnail link with iframe")
else:
    # Try finding the link more flexibly
    hp = re.sub(
        rb'<a href="https://www\.youtube\.com/watch\?v=FiuItIwjx28"[^>]*>.*?</a>',
        new,
        hp,
        flags=re.DOTALL,
        count=1
    )
    print("Replaced via regex")

# Verify
iframes = hp.count(b'<iframe')
links_to_yt = hp.count(b'href="https://www.youtube.com/watch?v=FiuItIwjx28"')
print(f"Iframes: {iframes}, YT links remaining: {links_to_yt}")

open('index.html', 'wb').write(hp)
print("Done")
