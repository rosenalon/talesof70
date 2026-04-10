import re

OLD = b'https://talesof70.runi.ac.il'
NEW = b'https://rosenalon.github.io/talesof70'

# ===== REPROCESS HOMEPAGE FROM ORIGINAL CAPTURE =====
hp = open('singlefile_homepage.html', 'rb').read()
hp = hp.replace(OLD, NEW)

# Remove CSP if any
hp = re.sub(rb'<meta[^>]*[Cc]ontent-[Ss]ecurity-[Pp]olicy[^>]*>', b'', hp)

# DON'T touch the video area structure at all.
# Instead: hide the broken video and add a NEW clean one ABOVE it.
# Find the hero section and inject our embed BEFORE it, then hide original video
inject_css = b"""<style id="vfix">
/* Hide the broken original video player */
.vlog-featured .vlog-popup-wrapper{display:none!important}
.vlog-featured .vlog-cover{display:none!important}
/* Show our clean replacement */
.clean-hero-video{position:relative;padding-bottom:56.25%;height:0;overflow:hidden}
.clean-hero-video iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
/* Fix sticky header */
#vlog-sticky-header{transform:translate3d(0,-100px,0)!important;transition:transform .3s ease!important}
#vlog-sticky-header.visible{transform:translate3d(0,0,0)!important}
#vlog-responsive-header{display:none!important}
/* Visibility fixes */
.row.vlog-posts.row-eq-height{display:flex!important;flex-wrap:wrap!important;visibility:visible!important;opacity:1!important}
.row.vlog-posts.row-eq-height>*{display:block!important;visibility:visible!important;opacity:1!important}
article{display:block!important;visibility:visible!important;opacity:1!important}
.vlog-module,.vlog-content,.vlog-section{overflow:visible!important;max-height:none!important;height:auto!important}
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

hp = hp.replace(b'</head>', inject_css + b'\n</head>')

# Insert clean video div inside the col-lg-8 that held the video
# Find: <div class="vlog-format-content video">
marker = b'<div class="vlog-format-content video">'
idx = hp.find(marker, hp.find(b'<body'))
if idx > 0:
    hp = hp[:idx] + b'<div class="clean-hero-video"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>\n' + hp[idx:]
    print("Homepage: injected clean video BEFORE original wrapper")

open('index.html', 'wb').write(hp)
print(f"Homepage saved: {len(hp)} bytes")

# ===== REPROCESS ABOUT FROM ORIGINAL CAPTURE =====
ab = open('singlefile_about.html', 'rb').read()
ab = ab.replace(OLD, NEW)
ab = re.sub(rb'<meta[^>]*[Cc]ontent-[Ss]ecurity-[Pp]olicy[^>]*>', b'', ab)

# Same approach: hide original video, inject clean one
about_css = b"""<style id="vfix">
.entry-content-single .fluid-width-video-wrapper{display:none!important}
.clean-about-video{max-width:640px;margin:0 auto 20px}
.clean-about-video .vw{position:relative;padding-bottom:56.25%;height:0;overflow:hidden}
.clean-about-video .vw iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:0}
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

ab = ab.replace(b'</head>', about_css + b'\n</head>')

# Inject clean video before the fluid-width wrapper
marker = b'<div class=fluid-width-video-wrapper'
idx = ab.find(marker, ab.find(b'<body'))
if idx > 0:
    ab = ab[:idx] + b'<div class="clean-about-video"><div class="vw"><iframe src="https://www.youtube.com/embed/FiuItIwjx28" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></div>\n' + ab[idx:]
    print("About: injected clean video BEFORE original wrapper")

open('מעשה-ב-70-למה/index.html', 'wb').write(ab)
print(f"About saved: {len(ab)} bytes")

# ===== REPROCESS CREATORS FROM ORIGINAL CAPTURE =====
cr = open('singlefile_creators.html', 'rb').read()
cr = cr.replace(OLD, NEW)
cr = re.sub(rb'<meta[^>]*[Cc]ontent-[Ss]ecurity-[Pp]olicy[^>]*>', b'', cr)

cr_css = b"""<style id="vfix">
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

cr = cr.replace(b'</head>', cr_css + b'\n</head>')
open('יוצרים-ושותפים/index.html', 'wb').write(cr)
print(f"Creators saved: {len(cr)} bytes")
