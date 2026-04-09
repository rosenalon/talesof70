import re

html = open('index.html', 'rb').read()

# Remove ALL Content-Security-Policy meta tags completely
html = re.sub(rb'<meta\s+http-equiv=["\']?Content-Security-Policy["\']?[^>]*>', b'', html, flags=re.IGNORECASE)
html = re.sub(rb'<meta\s+http-equiv=["\']?X-Disabled-CSP["\']?[^>]*>', b'', html, flags=re.IGNORECASE)

# Also fix the embed URL - use youtube-nocookie and ensure proper attributes
html = html.replace(
    b'src="https://www.youtube.com/embed/FiuItIwjx28"',
    b'src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen'
)
html = html.replace(
    b'src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"',
    b'src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"'
)

open('index.html', 'wb').write(html)
print(f"Done. CSP tags removed. Size: {len(html)}")
