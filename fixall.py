import os
import re

OLD = 'https://talesof70.runi.ac.il'
NEW = 'https://rosenalon.github.io/talesof70'

fixes = """<style>
#vlog-sticky-header { transform: translate3d(0, -100px, 0) !important; transition: transform 0.3s ease !important; }
#vlog-sticky-header.visible { transform: translate3d(0, 0, 0) !important; }
#vlog-responsive-header { display: none !important; }
.vlog-site-content { padding-top: 36px !important; margin-top: 0 !important; }
</style>
<script>
window.addEventListener('scroll', function() {
  var header = document.getElementById('vlog-sticky-header');
  var mainHeader = document.querySelector('.vlog-header-middle');
  if (header && mainHeader) {
    var threshold = mainHeader.offsetTop + mainHeader.offsetHeight;
    if (window.scrollY > threshold) { header.classList.add('visible'); }
    else { header.classList.remove('visible'); }
  }
});
</script>"""

count = 0
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root, fname)
        html = open(fpath, 'r', encoding='utf-8').read()
        changed = False
        if OLD in html:
            html = html.replace(OLD, NEW)
            changed = True
        if 'vlog-sticky-header.visible' not in html and '</head>' in html:
            html = html.replace('</head>', fixes + '\n</head>')
            changed = True
        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
            print(f"  [{count}] {fpath}")

print(f"\nFixed {count} files")
