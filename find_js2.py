import re

hp = open('index.html', 'rb').read()

# Find ALL script tags anywhere in the document
scripts = list(re.finditer(rb'<script[^>]*>(.*?)</script>', hp, re.DOTALL))
print(f"Total scripts: {len(scripts)}")

for i, m in enumerate(scripts):
    content = m.group(1)
    if len(content) < 10:
        continue
    for keyword in [b'iframe', b'popup', b'fitvid', b'player', b'embed', b'video', b'vlog', b'youtube']:
        if keyword in content.lower():
            print(f"\n  Script {i} ({len(content)} bytes) contains '{keyword.decode()}':")
            for line in content.split(b'\n'):
                if keyword in line.lower():
                    print(f"    {line.strip().decode('utf-8','replace')[:250]}")
            break

# Also check: is the iframe actually in the rendered HTML?
body_start = hp.find(b'<body')
body = hp[body_start:]
idx = body.find(b'<iframe')
if idx > 0:
    print(f"\nIframe at body offset {idx}:")
    print(body[idx:idx+300].decode('utf-8','replace'))
    # Show 200 bytes of parent context
    print(f"\nParent context:")
    print(body[idx-300:idx].decode('utf-8','replace')[-200:])
else:
    print("\nNO IFRAME FOUND IN BODY")
