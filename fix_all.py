import os, re
from urllib.parse import unquote, quote

# === Fix 1: Tag links - find ALL broken ones ===
existing = set()
for d in os.listdir('tag'):
    if os.path.isdir(os.path.join('tag', d)):
        existing.add(d)

html = open('index.html', 'r', encoding='utf-8').read()

# Find all tag hrefs
all_tag_refs = re.findall(r'href="([^"]*?/tag/[^"]*?)"', html)
print(f"Total tag links: {len(all_tag_refs)}")

fixed = 0
for href in set(all_tag_refs):
    # Extract tag name from URL
    m = re.search(r'/tag/([^/"]+)/?', href)
    if not m:
        continue
    raw = m.group(1)
    decoded = unquote(raw)
    
    if decoded in existing:
        continue
    
    # Try: spaces->hyphens, slash->hyphen
    attempt = decoded.replace(' ', '-').replace('/', '-')
    if attempt in existing:
        new_href = href.replace(f'/tag/{raw}/', f'/tag/{quote(attempt)}/')
        html = html.replace(href, new_href)
        fixed += 1
        print(f"  Fixed: '{decoded}' -> '{attempt}'")
    else:
        print(f"  STILL BROKEN: '{decoded}' (tried '{attempt}')")

print(f"\nFixed {fixed} tag links")

# === Fix 2: Replace JS iframe with simple working embed ===
# The SingleFile sandbox kills all iframes/JS. Use a plain link with thumbnail.
# But also add a script at the VERY END of body to create iframe after everything loads.
inject_script = '''<script>
window.addEventListener("load", function() {
  setTimeout(function() {
    var c = document.getElementById("hero-yt-container");
    if (c) {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/FiuItIwjx28";
      f.style.cssText = "position:absolute;top:0;left:0;width:100%;height:100%;border:0";
      f.setAttribute("allow", "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture");
      f.setAttribute("allowfullscreen", "");
      f.setAttribute("sandbox", "allow-scripts allow-same-origin allow-presentation allow-popups");
      c.innerHTML = "";
      c.appendChild(f);
    }
  }, 500);
});
</script>'''

# Make sure container exists and has fallback thumbnail
if 'hero-yt-container' not in html:
    # Find and replace current hero video section
    old = re.search(r'<a href="https://www\.youtube\.com/watch\?v=FiuItIwjx28"[^>]*>.*?</a>', html, re.DOTALL)
    if old:
        new_div = '<div id="hero-yt-container" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:4px;background:#000"><img src="https://img.youtube.com/vi/FiuItIwjx28/hqdefault.jpg" style="width:100%;position:absolute;top:0;left:0"></div>'
        html = html.replace(old.group(0), new_div)
        print("Added hero container with fallback thumbnail")

# Add script before </body>
if 'hero-yt-container' in html and inject_script not in html:
    html = html.replace('</body>', inject_script + '\n</body>')
    print("Added delayed iframe injection script")

open('index.html', 'w', encoding='utf-8').write(html)
print("Done")
