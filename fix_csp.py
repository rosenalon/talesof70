import os

fpath = 'index.html'
html = open(fpath, 'rb').read()

# Fix 1: Remove Content-Security-Policy meta tag that blocks iframes
html = html.replace(b'<meta http-equiv="Content-Security-Policy"', b'<meta http-equiv="X-Disabled-CSP"')
html = html.replace(b"<meta http-equiv='Content-Security-Policy'", b"<meta http-equiv='X-Disabled-CSP'")
html = html.replace(b'content-security-policy', b'x-disabled-csp')

# Fix 2: Use youtube-nocookie for better compatibility
html = html.replace(b'https://www.youtube.com/embed/FiuItIwjx28"', b'https://www.youtube-nocookie.com/embed/FiuItIwjx28" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"')

open(fpath, 'wb').write(html)
print("Fixed")
