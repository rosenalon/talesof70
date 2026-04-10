import re

# Check homepage
hp = open('index.html', 'rb').read()
# Find all iframe-related content
iframes = re.findall(rb'<iframe[^>]{0,500}>', hp)
print(f"Homepage iframes: {len(iframes)}")
for i, f in enumerate(iframes[:5]):
    print(f"  {i}: {f[:200]}")

# Check for sandbox attributes on parent elements
sandboxes = re.findall(rb'sandbox[^>]{0,200}', hp[:500000])
print(f"\nSandbox attrs: {len(sandboxes)}")
for s in sandboxes[:3]:
    print(f"  {s[:150]}")

# Check meta tags that might block
metas = re.findall(rb'<meta[^>]*http-equiv[^>]*>', hp[:10000])
print(f"\nMeta http-equiv tags: {len(metas)}")
for m in metas:
    print(f"  {m[:200]}")

print("\n" + "="*50)

# Check about page
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()
iframes = re.findall(rb'<iframe[^>]{0,500}>', ab)
print(f"\nAbout page iframes: {len(iframes)}")
for i, f in enumerate(iframes[:5]):
    print(f"  {i}: {f[:200]}")

sandboxes = re.findall(rb'sandbox[^>]{0,200}', ab[:500000])
print(f"\nAbout sandbox attrs: {len(sandboxes)}")
for s in sandboxes[:3]:
    print(f"  {s[:150]}")
