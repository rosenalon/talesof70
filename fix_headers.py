import re, os

# Read header/CSS from singlefile source
sf = open('singlefile_source.html', 'r', encoding='utf-8').read()

# Extract all style blocks
styles = re.findall(r'<style[^>]*>.*?</style>', sf, re.DOTALL)
css_html = '\n'.join(styles)
print(f"Extracted {len(styles)} style blocks")

# Extract header
header_match = re.search(r'<header[^>]*class="[^"]*vlog-site-header[^"]*"[^>]*>.*?</header>', sf, re.DOTALL)
header_html = header_match.group(0) if header_match else ''
print(f"Header: {len(header_html)} chars")

# Extract sticky header
sticky_match = re.search(r'<div[^>]*id=vlog-sticky-header[^>]*>.*?</div>\s*(?=<div|<section|<footer)', sf, re.DOTALL)
if not sticky_match:
    sticky_match = re.search(r'<div[^>]*id="vlog-sticky-header"[^>]*>.*?</div>\s*(?=<div|<section|<footer)', sf, re.DOTALL)
sticky_html = sticky_match.group(0) if sticky_match else ''
print(f"Sticky header: {len(sticky_html)} chars")

# Extract footer
footer_match = re.search(r'<footer[^>]*class="[^"]*vlog-site-footer[^"]*"[^>]*>.*?</footer>', sf, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''
print(f"Footer: {len(footer_html)} chars")

OLD = 'https://talesof70.runi.ac.il'
NEW = 'https://rosenalon.github.io/talesof70'
header_html = header_html.replace(OLD, NEW)
sticky_html = sticky_html.replace(OLD, NEW)
footer_html = footer_html.replace(OLD, NEW)

extra_css = """<style>
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
        print(f"SKIP: {fpath} not found")
        continue
    html = open(fpath, 'r', encoding='utf-8').read()

    # Remove old simple header
    html = re.sub(r'<header>.*?</header>', '', html, flags=re.DOTALL)

    # Remove old simple footer
    html = re.sub(r'<footer>.*?</footer>', '', html, flags=re.DOTALL)

    # Remove old simple style import
    html = html.replace("@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');", '')

    # Insert theme CSS before </head>
    html = html.replace('</head>', css_html + '\n' + extra_css + '\n</head>')

    # Insert header + sticky after <body...>
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + header_html + '\n' + sticky_html, html)

    # Insert footer before </body>
    html = html.replace('</body>', footer_html + '\n</body>')

    open(fpath, 'w', encoding='utf-8').write(html)
    print(f"Fixed: {fpath}")

print("Done")
