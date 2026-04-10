import re

hp = open('index.html', 'rb').read()
body_start = hp.find(b'<body')
body = hp[body_start:]

# Find ALL script tags in the body
scripts = list(re.finditer(rb'<script[^>]*>(.*?)</script>', body, re.DOTALL))
print(f"Scripts in body: {len(scripts)}")

for i, m in enumerate(scripts):
    content = m.group(1)
    # Check if script mentions iframe, video, popup, embed, player
    for keyword in [b'iframe', b'popup', b'fitvid', b'player', b'embed', b'video', b'vlog']:
        if keyword in content.lower():
            print(f"\n  Script {i} ({len(content)} bytes) contains '{keyword.decode()}':")
            # Show relevant lines
            for line in content.split(b'\n'):
                if keyword in line.lower():
                    print(f"    {line.strip().decode('utf-8','replace')[:200]}")
            break
