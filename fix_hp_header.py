import re

# Read the real header we extracted
header_html = open('_header.html', 'r', encoding='utf-8').read()
theme_css = open('_theme_css.html', 'r', encoding='utf-8').read()
footer_html = open('_footer.html', 'r', encoding='utf-8').read()

hp = open('index.html', 'r', encoding='utf-8').read()

# Remove old simple header
hp = re.sub(r'<header[^>]*>.*?</header>', '', hp, count=1, flags=re.DOTALL)

# Remove old simple footer
hp = re.sub(r'<footer[^>]*>.*?</footer>', '', hp, count=1, flags=re.DOTALL)

# Remove old CSS that defined header/footer styles
hp = re.sub(r'header\{[^}]+\}', '', hp)
hp = re.sub(r'footer\{[^}]+\}', '', hp)
hp = re.sub(r'\.nav-links\{[^}]+\}', '', hp)
hp = re.sub(r'\.nav-links a\{[^}]+\}', '', hp)
hp = re.sub(r'\.nav-links a:hover\{[^}]+\}', '', hp)

# Inject theme CSS before </head>
extra = """<style id="hp-fixes">
#vlog-sticky-header{transform:translate3d(0,-100px,0)!important;transition:transform .3s ease!important}
#vlog-sticky-header.visible{transform:translate3d(0,0,0)!important}
#vlog-responsive-header{display:none!important}
.video-grid a img{transition:transform 0.3s ease,opacity 0.3s ease}
.video-grid a:hover img{transform:scale(1.05);opacity:0.85}
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

if 'hp-fixes' not in hp:
    hp = hp.replace('</head>', theme_css + '\n' + extra + '\n</head>')

# Inject real header after <body...>
hp = re.sub(r'(<body[^>]*>)', r'\1\n' + header_html, hp)

# Inject real footer before </body>
hp = hp.replace('</body>', footer_html + '\n</body>')

open('index.html', 'w', encoding='utf-8').write(hp)
print(f"Done. Size: {len(hp)} bytes")
