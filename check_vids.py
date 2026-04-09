import os, re

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d != '.git']
    for fname in files:
        if fname != 'index.html':
            continue
        fpath = os.path.join(root, fname)
        if fpath == '.\\index.html':
            continue
        if '2018' not in fpath:
            continue
        html = open(fpath, 'r', encoding='utf-8').read()
        # Find youtube/vimeo URLs
        vids = re.findall(r'(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/|vimeo\.com/)([A-Za-z0-9_-]+)', html)
        has_void = 'javascript:' in html
        if vids or has_void:
            print(f"{fpath}")
            print(f"  Videos: {vids[:3]}")
            print(f"  Has javascript:void: {has_void}")
            break  # just check first post
