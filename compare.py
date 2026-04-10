import re

files = {
    'homepage': 'index.html',
    'about': 'מעשה-ב-70-למה/index.html',
    'post_working': '2018/03/10/יעל-מזרחי/index.html',
}

for name, path in files.items():
    html = open(path, 'rb').read()
    
    html_tag = re.search(rb'<html[^>]*>', html)
    body_tag = re.search(rb'<body[^>]*>', html)
    head_start = html.find(b'<head')
    head_end = html.find(b'</head>')
    
    html_end = html_tag.end() if html_tag else 0
    between_html_head = html[html_end:head_start]
    
    print(f"\n{'='*60}")
    print(f"{name} ({len(html)} bytes)")
    print(f"{'='*60}")
    print(f"HTML tag: {html_tag.group(0)[:150].decode('utf-8','replace') if html_tag else 'NONE'}")
    print(f"Body tag: {body_tag.group(0)[:150].decode('utf-8','replace') if body_tag else 'NONE'}")
    print(f"Between <html> and <head>: {len(between_html_head)} bytes")
    
    # Check first 500 bytes of that gap
    gap_preview = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', between_html_head[:500])
    print(f"Gap preview: {gap_preview.decode('utf-8','replace')}")
    
    # Check for style elements in the gap
    gap_styles = re.findall(rb'<style[^>]*>', between_html_head)
    print(f"Style tags in gap: {len(gap_styles)}")
    
    # Check for SingleFile CSS variables
    sf_vars = between_html_head.count(b'--sf-')
    print(f"SingleFile CSS variables (--sf-): {sf_vars}")
    
    # Check meta tags in gap
    gap_metas = re.findall(rb'<meta[^>]*>', between_html_head)
    print(f"Meta tags in gap: {len(gap_metas)}")
    for m in gap_metas:
        print(f"  {m.decode('utf-8','replace')[:200]}")
