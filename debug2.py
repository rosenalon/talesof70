import re

# ===== HOMEPAGE =====
hp = open('index.html', 'rb').read()

# Find the exact content around the video area
idx = hp.find(b'fluid-width-video-wrapper')
# Skip CSS occurrences - find it in the body
body_start = hp.find(b'<body')
idx = hp.find(b'fluid-width-video-wrapper', body_start)
if idx > 0:
    chunk = hp[idx-50:idx+2000]
    # Truncate base64/srcdoc
    chunk = re.sub(rb'srcdoc="[^"]{100,}"', b'srcdoc="[HUGE_SRCDOC]"', chunk)
    chunk = re.sub(rb'data:[^"]{100,}', b'[IMG_DATA]', chunk)
    print("HOMEPAGE VIDEO AREA:")
    print(chunk.decode('utf-8', errors='replace')[:1500])
else:
    print("fluid-width-video-wrapper NOT FOUND in body")
    # Search for any youtube/video content in body
    for term in [b'FiuItIwjx28', b'youtube', b'Watch video', b'Error 153', b'vlog-cover', b'vlog-popup']:
        idx = hp.find(term, body_start)
        if idx > 0:
            print(f"\nFound '{term.decode()}' at {idx}")

print("\n" + "="*60)

# ===== ABOUT PAGE =====
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()
body_start = ab.find(b'<body')
idx = ab.find(b'fluid-width-video-wrapper', body_start)
if idx > 0:
    chunk = ab[idx-50:idx+2000]
    chunk = re.sub(rb'srcdoc="[^"]{100,}"', b'srcdoc="[HUGE_SRCDOC]"', chunk)
    chunk = re.sub(rb'data:[^"]{100,}', b'[IMG_DATA]', chunk)
    print("ABOUT VIDEO AREA:")
    print(chunk.decode('utf-8', errors='replace')[:1500])

# Check for leftover srcdoc content
srcdoc_count = ab.count(b'srcdoc=')
iframe_count = ab.count(b'<iframe')
sandbox_count = ab.count(b'sandbox=')
print(f"\nAbout: srcdoc={srcdoc_count}, iframes={iframe_count}, sandbox={sandbox_count}")
