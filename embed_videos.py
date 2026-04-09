import xml.etree.ElementTree as ET
import re, os
from urllib.parse import unquote

OLD = 'https://talesof70.runi.ac.il'
NEW = 'https://rosenalon.github.io/talesof70'

tree = ET.parse('wp_export.xml')
root = tree.getroot()
ns = {'content': 'http://purl.org/rss/1.0/modules/content/', 'wp': 'http://wordpress.org/export/1.2/'}

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
        video_map[path] = yt[0]

print(f"Found {len(video_map)} video mappings\n")

count = 0
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root_dir, fname)
        if '2018' not in fpath:
            continue
        rel = fpath.replace('.\\', '').replace('\\', '/').replace('/index.html', '')
        html = open(fpath, 'r', encoding='utf-8').read()

        vid_id = None
        for path, yt_id in video_map.items():
            if path in rel or rel in path:
                vid_id = yt_id
                break

        if not vid_id:
            continue

        embed_html = f'<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;margin-bottom:20px"><iframe src="https://www.youtube.com/embed/{vid_id}" style="position:absolute;top:0;left:0;width:100%;height:100%" frameborder="0" allowfullscreen></iframe></div>'

        # Replace the cover link (thumbnail + play button) with embedded player
        # The pattern: <a class="vlog-cover" ... href="javascript:void(0);">...(img + play button)...</a>
        html = re.sub(
            r'<a\s+class="vlog-cover"[^>]*href="[^"]*"[^>]*>.*?</a>',
            embed_html,
            html,
            flags=re.DOTALL,
            count=1
        )

        # Also add CSS to fix any remaining image sizing
        if 'embed-fix-applied' not in html:
            fix = '<!--embed-fix-applied--><style>.vlog-cover img,.meta-media img,.entry-image img{max-width:100%!important;height:auto!important}</style>'
            html = html.replace('</head>', fix + '\n</head>')

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        count += 1
        print(f"  [{count}] {fpath}")

print(f"\nFixed {count} files")
