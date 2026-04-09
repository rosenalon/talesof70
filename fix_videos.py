import xml.etree.ElementTree as ET
import re, os
from urllib.parse import unquote

OLD = 'https://talesof70.runi.ac.il'
NEW = 'https://rosenalon.github.io/talesof70'

tree = ET.parse('wp_export.xml')
root = tree.getroot()
ns = {'content': 'http://purl.org/rss/1.0/modules/content/', 'wp': 'http://wordpress.org/export/1.2/'}

# Build map: post path -> video URL
video_map = {}
for item in root.iter('item'):
    post_type = item.find('wp:post_type', ns)
    if post_type is None or post_type.text != 'post':
        continue
    link = item.find('link').text or ''
    content = item.find('content:encoded', ns)
    if content is None or not content.text:
        continue
    yt = re.findall(r'https?://(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([A-Za-z0-9_-]+)', content.text)
    if yt:
        path = unquote(link.replace(OLD, '').replace(NEW, '').strip('/'))
        video_map[path] = f'https://www.youtube.com/watch?v={yt[0]}'

print(f"Found {len(video_map)} video mappings\n")

# Fix all post pages
count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root_dir, fname)
        rel = fpath.replace('.\\', '').replace('\\', '/').replace('/index.html', '')
        html = open(fpath, 'r', encoding='utf-8').read()
        changed = False

        # Find matching video URL
        for path, vid_url in video_map.items():
            if path in rel or rel in path:
                # Replace javascript:void(0) with video link
                if 'javascript:' in html:
                    html = re.sub(
                        r'<a([^>]*?)href="javascript:\s*void\(0\);"',
                        f'<a\\1href="{vid_url}" target="_blank"',
                        html
                    )
                    changed = True
                break

        # Fix oversized images on post pages
        if '2018/' in fpath and 'vlog-cover' in html:
            if 'max-width:100%' not in html:
                fix_css = '<style>.vlog-cover img,.meta-media img,.entry-image img{max-width:100%!important;height:auto!important;width:100%!important}.vlog-cover{max-height:500px!important;overflow:hidden!important}</style>'
                html = html.replace('</head>', fix_css + '\n</head>')
                changed = True

        if changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
            print(f"  [{count}] {fpath}")

print(f"\nFixed {count} files")
