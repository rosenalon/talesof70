import re

# Check about page - what's around the video area
ab = open('מעשה-ב-70-למה/index.html', 'rb').read()
body_start = ab.find(b'<body')

# Find our injected clean video
clean = ab.find(b'clean-about-vid', body_start)
print(f"Clean video div at: {clean}")

# Find the hidden original
fwvw = ab.find(b'fluid-width-video-wrapper', body_start)
print(f"Original video wrapper at: {fwvw}")

# Check what's around clean video
if clean > 0:
    chunk = ab[clean-300:clean+500]
    chunk = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', chunk)
    chunk = re.sub(rb'srcdoc="[^"]{50,}"', b'srcdoc="[...]"', chunk)
    print(f"\nAround clean video:")
    print(chunk.decode('utf-8','replace'))

# Check all style rules that mention display:none
styles = re.findall(rb'display:\s*none', ab[body_start:body_start+50000])
print(f"\ndisplay:none occurrences in first 50K of body: {len(styles)}")

# Check if our vfix2 style is there
vfix = ab.find(b'vfix2')
print(f"vfix2 style present: {vfix > 0}")
