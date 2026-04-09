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
        path = unquote(link.replace(OLD, '').strip('/'))
        # Normalize: remove apostrophes for matching
        normalized = path.replace("'", "").replace("\u2019", "").replace("\u05F3", "")
        video_map[path] = yt[0]
        video_map[normalized] = yt[0]

print(f"Found {len(video_map)} video mappings\n")

# Collect all local post folders
local_posts = {}
for root_dir, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html' or '2018' not in root_dir:
            continue
        fpath = os.path.join(root_dir, fname)
        rel = fpath.replace('.\\', '').replace('\\', '/').replace('/index.html', '')
        local_posts[rel] = fpath

# Match and verify
print("--- Matching ---")
matched = 0
unmatched_local = []
for rel, fpath in sorted(local_posts.items()):
    norm_rel = rel.replace("'", "").replace("\u2019", "").replace("\u05F3", "")
    vid_id = None
    for path, yt_id in video_map.items():
        norm_path = path.replace("'", "").replace("\u2019", "").replace("\u05F3", "")
        if norm_path == norm_rel or norm_rel.endswith(norm_path) or norm_path.endswith(norm_rel):
            vid_id = yt_id
            break
    if vid_id:
        matched += 1
    else:
        unmatched_local.append(rel)

print(f"Matched: {matched}")
print(f"Unmatched local folders: {len(unmatched_local)}")
for u in unmatched_local:
    print(f"  {u}")

# Now apply fixes
print("\n--- Applying fixes ---")
count = 0
for rel, fpath in sorted(local_posts.items()):
    norm_rel = rel.replace("'", "").replace("\u2019", "").replace("\u05F3", "")
    vid_id = None
    for path, yt_id in video_map.items():
        norm_path = path.replace("'", "").replace("\u2019", "").replace("\u05F3", "")
        if norm_path == norm_rel or norm_rel.endswith(norm_path) or norm_path.endswith(norm_rel):
            vid_id = yt_id
            break

    if not vid_id:
        continue

    html = open(fpath, 'r', encoding='utf-8').read()

    # Remove old embed-fix-applied CSS
    html = html.replace('<!--embed-fix-applied--><style>.vlog-cover img,.meta-media img,.entry-image img{max-width:100%!important;height:auto!important}</style>', '')

    # Smaller embed: max-width 640px, centered
    embed_html = f'<div style="max-width:640px;margin:0 auto 20px"><div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/{vid_id}" style="position:absolute;top:0;left:0;width:100%;height:100%" frameborder="0" allowfullscreen></iframe></div></div>'

    # Replace existing embed or cover link
    # First try replacing previous embed
    html = re.sub(
        r'<div style="position:relative;padding-bottom:56\.25%.*?</iframe></div></div>',
        embed_html,
        html,
        flags=re.DOTALL,
        count=1
    )

    # If still has javascript:void, replace cover link
    if 'javascript:' in html:
        html = re.sub(
            r'<a\s+class="vlog-cover"[^>]*href="[^"]*"[^>]*>.*?</a>',
            embed_html,
            html,
            flags=re.DOTALL,
            count=1
        )

    # Fix thumbnail/image sizing
    size_css = """<style>
.vlog-cover img,.meta-media img,.entry-image img{max-width:100%!important;height:auto!important}
.entry-image{max-width:640px!important;margin:0 auto!important}
.vlog-single-content .entry-image{max-width:640px!important}
.col-lg-8{max-width:640px!important;margin:0 auto!important;float:none!important}
</style>"""

    if 'entry-image{max-width:640px' not in html:
        html = html.replace('</head>', size_css + '\n</head>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1
    print(f"  [{count}] {fpath}")

print(f"\nFixed {count} files")
