import re, os

# Read header from a working post page
post_path = os.path.join('2018', '03', '09', 'ריקה-סוסקין', 'index.html')
post_html = open(post_path, 'r', encoding='utf-8').read()

# Extract everything between <body> and <div id=content
body_start = post_html.find('<body')
body_tag_end = post_html.find('>', body_start) + 1
content_start = post_html.find('id=content')
if content_start < 0:
    content_start = post_html.find('id="content"')

header_section = post_html[body_tag_end:content_start-5].strip()
# Find the closing tag before content
last_div = header_section.rfind('<div')
header_section = header_section[:last_div].strip()

# Extract all styles from the post page
styles = re.findall(r'<style[^>]*>.*?</style>', post_html, re.DOTALL)
css_block = '\n'.join(styles)

# Extract footer
footer_match = re.search(r'<footer[^>]*>.*?</footer>', post_html, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''

print(f"Header: {len(header_section)} chars")
print(f"CSS blocks: {len(styles)}")
print(f"Footer: {len(footer_html)} chars")

# Extra fixes
extra = """<style>
#vlog-sticky-header{transform:translate3d(0,-100px,0)!important;transition:transform .3s ease!important}
#vlog-sticky-header.visible{transform:translate3d(0,0,0)!important}
#vlog-responsive-header{display:none!important}
</style>
<script>
window.addEventListener('scroll',function(){
  var h=document.getElementById('vlog-sticky-header');
  var m=document.querySelector('.vlog-header-middle');
  if(h&&m){var t=m.offsetTop+m.offsetHeight;
    if(window.scrollY>t){h.classList.add('visible')}
    else{h.classList.remove('visible')}}
});
</script>"""

# Fix both pages
for page in ['מעשה-ב-70-למה', 'יוצרים-ושותפים']:
    fpath = os.path.join(page, 'index.html')
    if not os.path.exists(fpath):
        print(f"SKIP: {fpath}")
        continue
    html = open(fpath, 'r', encoding='utf-8').read()

    # Remove old header/footer
    html = re.sub(r'<header>.*?</header>', '', html, flags=re.DOTALL)
    html = re.sub(r'<footer>.*?</footer>', '', html, flags=re.DOTALL)

    # Remove old font import
    html = html.replace("@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');", '')

    # Remove old link to font-awesome (we get it from theme CSS)
    html = re.sub(r'<link[^>]*font-awesome[^>]*>', '', html)

    # Inject theme CSS before </head>
    html = html.replace('</head>', css_block + '\n' + extra + '\n</head>')

    # Inject header after <body...>
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + header_section, html)

    # Inject footer before </body>
    html = html.replace('</body>', footer_html + '\n</body>')

    open(fpath, 'w', encoding='utf-8').write(html)
    print(f"Fixed: {fpath} ({len(html)} bytes)")

# Also fix about page bottom image size
about_path = os.path.join('מעשה-ב-70-למה', 'index.html')
html = open(about_path, 'r', encoding='utf-8').read()
html = html.replace('max-width: 800px;', 'max-width: 900px;')
html = html.replace('.bottom-image img {', '.bottom-image img {\n  width: 100% !important;\n  max-width: 768px !important;')
open(about_path, 'w', encoding='utf-8').write(html)
print("Fixed about page image size")

print("\nDone")
