import re

html = open('index.html', 'rb').read()

# Find ALL CSP-related content
csp_count = html.lower().count(b'content-security-policy')
disabled_count = html.lower().count(b'x-disabled-csp')
print(f"CSP occurrences: {csp_count}")
print(f"X-Disabled-CSP occurrences: {disabled_count}")

# Show context around each CSP
for m in re.finditer(rb'(?i).{0,50}content.security.policy.{0,200}', html):
    snippet = m.group(0)
    # Truncate base64
    snippet = re.sub(rb'data:[^"]{50,}', b'[DATA]', snippet)
    print(f"  Found: {snippet[:150]}")
