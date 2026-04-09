import re, os

# Read current creators page to get student photos
old_path = os.path.join('יוצרים-ושותפים', 'index.html')
old_html = open(old_path, 'r', encoding='utf-8').read()

# Save the content between container div
content_match = re.search(r'<div class="container">(.*?)</div>\s*<footer', old_html, re.DOTALL)
if content_match:
    page_content = content_match.group(1)
    print(f"Extracted content: {len(page_content)} chars")
else:
    print("Could not extract content")
    page_content = old_html

# Read header/footer/CSS from a post page
post_path = os.path.join('2018', '03', '09', 'ריקה-סוסקין', 'index.html')
post = open(post_path, 'r', encoding='utf-8').read()

body_end = post.find('>', post.find('<body')) + 1
content_div = post.find('id=content')
before_content = post[body_end:content_div]
last_open = before_content.rfind('<div')
header_html = before_content[:last_open].strip()

footer_match = re.search(r'<footer[^>]*class[^>]*vlog[^>]*>.*?</footer>', post, re.DOTALL)
footer_html = footer_match.group(0) if footer_match else ''

all_css = re.findall(r'<style[^>]*>.*?</style>', post, re.DOTALL)
theme_css = '\n'.join(all_css)

NEW = 'https://rosenalon.github.io/talesof70'

page = f'''<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>יוצרים ושותפים – מעשה ב – 70</title>
{theme_css}
<style>
#vlog-sticky-header{{transform:translate3d(0,-100px,0)!important;transition:transform .3s ease!important}}
#vlog-sticky-header.visible{{transform:translate3d(0,0,0)!important}}
#vlog-responsive-header{{display:none!important}}
.cr-container{{max-width:900px;margin:30px auto;padding:0 30px}}
.cr-container h1{{font-size:24px;text-align:center;margin-bottom:25px}}
.cr-container h2{{font-size:18px;text-align:center;margin:25px 0 15px}}
.credits{{text-align:center;margin-bottom:30px}}
.credits p{{font-size:15px;line-height:2;margin:0}}
.students-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:20px 0}}
.student-card{{border:1px solid #e0e0e0;background:#fafafa;border-radius:4px;padding:12px;text-align:center;display:flex;align-items:center;gap:8px;direction:rtl}}
.student-card img{{width:70px;height:70px;border-radius:50%;object-fit:cover;flex-shrink:0}}
.student-name{{font-size:14px;font-weight:bold;margin-bottom:3px}}
.student-school{{font-size:12px;color:#666}}
.student-year{{font-size:12px;color:#999}}
.partners{{text-align:center;margin:30px 0;font-size:14px;line-height:1.8}}
.partners a{{color:#29aae3;text-decoration:none}}
.donors{{display:flex;justify-content:center;gap:60px;margin:20px 0;text-align:center;flex-wrap:wrap}}
.donor{{font-size:14px}}
.donor strong{{display:block;margin-bottom:5px}}
@media(max-width:768px){{.students-grid{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:480px){{.students-grid{{grid-template-columns:1fr}}}}
</style>
<script>
window.addEventListener('scroll',function(){{
  var h=document.getElementById('vlog-sticky-header');
  var m=document.querySelector('.vlog-header-middle');
  if(h&&m){{var t=m.offsetTop+m.offsetHeight;
    if(window.scrollY>t){{h.classList.add('visible')}}
    else{{h.classList.remove('visible')}}}}
}});
</script>
</head>
<body class="page">
{header_html}

<div class="cr-container">
{page_content}
</div>

{footer_html}
</body>
</html>'''

open(old_path, 'w', encoding='utf-8').write(page)
print(f"Rebuilt creators page: {len(page)} bytes")
