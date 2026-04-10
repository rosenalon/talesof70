import re

hp = open('index.html', 'rb').read()
body_start = hp.find(b'<body')

# Find ALL occurrences of YouTube-related strings in body
for term in [b'Watch video', b'Error 153', b'ytm-', b'yt-player', b'<ytm-', b'player-error', b'video-player']:
    idx = body_start
    while True:
        idx = hp.find(term, idx+1)
        if idx < 0:
            break
        chunk = hp[max(idx-100,0):idx+100]
        chunk = re.sub(rb'data:[^\s]{50,}', b'[DATA]', chunk)
        print(f"Found '{term.decode()}' at {idx}: ...{chunk[50:150].decode('utf-8','replace')}...")

# The srcdoc content from SingleFile contains the full YouTube mobile page
# which shows the error. Find any remaining srcdoc or huge inline HTML
srcdoc_positions = [m.start() for m in re.finditer(rb'srcdoc=', hp[body_start:])]
print(f"\nsrcdoc occurrences in body: {len(srcdoc_positions)}")

# Find any remaining <ytm or YouTube mobile player elements
ytm_count = hp.count(b'<ytm-')
print(f"<ytm- elements: {ytm_count}")

# Check for hidden iframes
hidden_iframes = re.findall(rb'<iframe[^>]*class=sf-hidden[^>]*>', hp[body_start:])
print(f"Hidden iframes: {len(hidden_iframes)}")
for h in hidden_iframes[:3]:
    print(f"  {h[:150]}")
