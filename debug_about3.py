import re

ab = open('מעשה-ב-70-למה/index.html', 'rb').read()

# Get a big chunk around the iframe
idx = ab.find(b'entry-content entry-content-single', ab.find(b'<body'))
if idx > 0:
    chunk = ab[idx:idx+5000]
    # Truncate data URIs and long srcdoc
    chunk = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', chunk)
    # Show raw bytes for quotes
    print("ENTRY CONTENT (first 3000 bytes):")
    text = chunk[:3000].decode('utf-8', 'replace')
    print(text)
