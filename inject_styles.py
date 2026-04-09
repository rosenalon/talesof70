"""
Injects styles from SingleFile HTML into all scraped pages.
"""
import os
import re
from bs4 import BeautifulSoup

OLD = 'https://talesof70.runi.ac.il'
NEW = 'https://rosenalon.github.io/talesof70'

print("Reading SingleFile source...")
sf = open('singlefile_source.html', 'r', encoding='utf-8').read()
sf_soup = BeautifulSoup(sf, 'html.parser')

styles = sf_soup.find_all('style')
css_html = '\n'.join(str(s) for s in styles)
print(f"  Extracted {len(styles)} style blocks")

header_el = sf_soup.find('header', class_='vlog-site-header')
header_html = str(header_el).replace(OLD, NEW) if header_el else ''

sticky_el = sf_soup.find('div', id='vlog-sticky-header')
sticky_html = str(sticky_el).replace(OLD, NEW) if sticky_el else ''

footer_el = sf_soup.find('footer', class_='vlog-site-footer')
footer_html = str(footer_el).replace(OLD, NEW) if footer_el else ''

extra_fixes = """<style>
#vlog-sticky-header { transform: translate3d(0, -100px, 0) !important; transition: transform 0.3s ease !important; }
#vlog-sticky-header.visible { transform: translate3d(0, 0, 0) !important; }
#vlog-responsive-header { display: none !important; }
.vlog-site-content { padding-top: 36px !important; margin-top: 0 !important; }
.row.vlog-posts.row-eq-height { display: flex !important; flex-wrap: wrap !important; visibility: visible !important; opacity: 1 !important; overflow: visible !important; max-height: none !important; height: auto !important; }
.row.vlog-posts.row-eq-height > * { display: block !important; visibility: visible !important; opacity: 1 !important; }
article { display: block !important; visibility: visible !important; opacity: 1 !important; }
.vlog-module, .vlog-content, .vlog-section { overflow: visible !important; max-height: none !important; height: auto !important; }
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

print("\nProcessing pages...")
count = 0

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root, fname)
        html = open(fpath, 'r', encoding='utf-8').read()
        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.find('title')
        title = str(title_tag) if title_tag else '<title>מעשה ב – 70</title>'
        content = soup.find('div', id='content')
        if not content:
            content = soup.find('body')
        if not content:
            print(f"  SKIP: {fpath}")
            continue
        content_html = str(content).replace(OLD, NEW)
        new_html = '<!DOCTYPE html>\n<html dir="rtl" lang="he">\n<head>\n'
        new_html += '<meta charset="utf-8">\n'
        new_html += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        new_html += title + '\n'
        new_html += css_html + '\n'
        new_html += extra_fixes + '\n'
        new_html += '</head>\n'
        new_html += '<body class="rtl">\n'
        new_html += header_html + '\n'
        new_html += sticky_html + '\n'
        new_html += '<div id="content" class="vlog-site-content">\n'
        new_html += content_html + '\n'
        new_html += '</div>\n'
        new_html += footer_html + '\n'
        new_html += '</body>\n</html>'
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        count += 1
        print(f"  [{count}] {fpath}")

print(f"\nDone! Styled {count} pages.")
