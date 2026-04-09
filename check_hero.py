import re

html = open('index.html', 'rb').read()

# Find the hero section
m = re.search(rb'<section[^>]*1a1a2e[^>]*>(.{0,3000})</section>', html, re.DOTALL)
if m:
    snippet = re.sub(rb'data:[^"]{50,}', b'[DATA]', m.group(0))
    print(snippet.decode('utf-8', errors='replace')[:2000])
else:
    print("No hero section found")
    # Check for youtube references
    yt = re.findall(rb'.{0,30}FiuItIwjx28.{0,100}', html)
    for y in yt[:5]:
        print(y.decode('utf-8', errors='replace'))
