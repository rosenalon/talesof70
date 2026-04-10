import re

ab = open('מעשה-ב-70-למה/index.html', 'rb').read()
body_start = ab.find(b'<body')

# Search for ANY video/youtube/iframe content
for term in [b'youtube', b'iframe', b'FiuItIwjx28', b'fluid-width', b'video-wrapper', b'entry-content', b'fitvid']:
    idx = ab.find(term, body_start)
    if idx > 0:
        chunk = ab[idx-50:idx+200]
        chunk = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', chunk)
        chunk = re.sub(rb'srcdoc="[^"]{50,}"', b'srcdoc="[...]"', chunk)
        print(f"'{term.decode()}' at {idx}:")
        print(f"  {chunk.decode('utf-8','replace')[:250]}")
    else:
        print(f"'{term.decode()}': NOT FOUND in body")
    print()
