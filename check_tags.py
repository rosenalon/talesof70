import re

hp = open('index.html', 'rb').read()

# Extract the html tag
html_tag = re.search(rb'<html[^>]*>', hp).group(0)
print(f"HTML tag ({len(html_tag)} bytes):")
# Truncate style attribute for display
display = re.sub(rb'style="[^"]{100,}"', b'style="[HUGE]"', html_tag)
display = re.sub(rb"style='[^']{100,}'", b"style='[HUGE]'", display)
if b'style>' in html_tag or b'style ' in html_tag:
    # style with no quotes
    print(display.decode('utf-8','replace')[:500])
else:
    print(display.decode('utf-8','replace')[:500])

# Check if style attr on html has content
style_match = re.search(rb'style="([^"]*)"', html_tag)
if style_match:
    print(f"\nHTML style attribute: {len(style_match.group(1))} bytes")
    print(f"  Preview: {style_match.group(1)[:200].decode('utf-8','replace')}")
else:
    # Could be style= without quotes or empty
    if b' style>' in html_tag or b' style ' in html_tag:
        print("\nHTML has empty style attribute")
    style_match2 = re.search(rb"style='([^']*)'", html_tag)
    if style_match2:
        print(f"\nHTML style (single quotes): {len(style_match2.group(1))} bytes")

# Check body tag
body_tag = re.search(rb'<body[^>]*>', hp).group(0)
print(f"\nBody tag ({len(body_tag)} bytes):")
print(body_tag.decode('utf-8','replace')[:500])

# Check what's between <html> and <head>
html_end = hp.find(b'>', hp.find(b'<html')) + 1
head_start = hp.find(b'<head')
between = hp[html_end:head_start]
between_display = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', between)
print(f"\nBetween html and head ({len(between)} bytes):")
print(between_display.decode('utf-8','replace')[:500])
