import re, os

# === Step 1: Extract real header from a working post page ===
post_path = os.path.join('2018', '03', '09', 'ריקה-סוסקין', 'index.html')
post = open(post_path, 'r', encoding='utf-8').read()

# Get everything from <body> to id=content (the header area)
body_start = post.find('<body')
body_tag_end = post.find('>', body_start) + 1
content_start = post.find('id=content')
header_area = post[body_tag_end:content_start]
# Trim to before the last <div that opens the content
last_div = header_area.rfind('<div')
header_html = header_area[:last_div].strip()

# Get all CSS from the post
all_css = re.findall(r'<style[^>]*>.*?</style>', post, re.DOTALL)

# Get footer
footer_match = re.search(r'<footer[^>]*class[^>]*vlog[^>]*>.*?</footer>', post, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''

print(f"Header: {len(header_html)} chars")
print(f"CSS blocks: {len(all_css)}")
print(f"Footer: {len(footer_html)} chars")

# Save for reuse
open('_header.html', 'w', encoding='utf-8').write(header_html)
open('_footer.html', 'w', encoding='utf-8').write(footer_html)
open('_theme_css.html', 'w', encoding='utf-8').write('\n'.join(all_css))

print("Saved _header.html, _footer.html, _theme_css.html")
