import re

# Check what the WORKING post page embed looks like
post = open('2018/03/10/יעל-מזרחי/index.html', 'rb').read()
body = post[post.find(b'<body'):]

# Find the iframe
iframe = re.search(rb'<iframe[^>]*youtube[^>]*>', body)
if iframe:
    print("WORKING POST IFRAME:")
    print(iframe.group(0).decode('utf-8','replace'))

# Find the parent div structure
embed_div = re.search(rb'<div style="max-width:640px.*?</iframe>.*?</div>\s*</div>', body, re.DOTALL)
if embed_div:
    print("\nFULL WORKING EMBED STRUCTURE:")
    print(embed_div.group(0).decode('utf-8','replace'))

# Now check what parent element contains it
idx = body.find(b'max-width:640px')
if idx > 0:
    context = body[idx-200:idx+50]
    context = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', context)
    print("\nCONTEXT BEFORE EMBED:")
    print(context.decode('utf-8','replace'))

# Check if that post page has any SingleFile restrictions
print("\n\nPOST PAGE CHECKS:")
print(f"  CSP meta tags: {body.count(b'Content-Security-Policy')}")
print(f"  sandbox attrs: {body.count(b'sandbox=')}")
print(f"  srcdoc attrs: {body.count(b'srcdoc=')}")
print(f"  sf-hidden: {body.count(b'sf-hidden')}")
