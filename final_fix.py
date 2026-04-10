import re, os

NEW = 'https://rosenalon.github.io/talesof70'

header_html = open('_header.html', 'r', encoding='utf-8').read()
footer_html = open('_footer.html', 'r', encoding='utf-8').read()
theme_css = open('_theme_css.html', 'r', encoding='utf-8').read()

extra_css = """<style id="page-fixes">
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

# === CREATORS PAGE ===
print("=== Creators page ===")
cr_path = os.path.join('יוצרים-ושותפים', 'index.html')
old = open(cr_path, 'r', encoding='utf-8').read()

# Extract student cards with photos
students = []
for m in re.finditer(r'<img src="(data:image[^"]+)"[^>]*>\s*(?:<div[^>]*>)?\s*<div[^>]*>([^<]+)</div>\s*<div[^>]*>([^<]*)</div>\s*<div[^>]*>([^<]*)</div>', old):
    students.append({'img': m.group(1), 'name': m.group(2).strip(), 'school': m.group(3).strip(), 'year': m.group(4).strip()})

# Also get students without photos
for m in re.finditer(r'<div style="font-size:14px;font-weight:bold">([^<]+)</div>\s*<div[^>]*>([^<]*)</div>\s*<div[^>]*>([^<]*)</div>', old):
    name = m.group(1).strip()
    if not any(s['name'] == name for s in students):
        students.append({'img': '', 'name': name, 'school': m.group(2).strip(), 'year': m.group(3).strip()})

print(f"  Students: {len(students)} ({sum(1 for s in students if s['img'])} with photos)")

student_cards = ''
for s in students:
    photo = f'<img src="{s["img"]}" style="width:70px;height:70px;border-radius:50%;object-fit:cover;flex-shrink:0">' if s['img'] else ''
    student_cards += f'<div class="sc">{photo}<div><div class="sn">{s["name"]}</div><div class="ss">{s["school"]}</div><div class="sy">{s["year"]}</div></div></div>\n'

creators_page = f'''<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>יוצרים ושותפים – מעשה ב – 70</title>
{theme_css}
<style id="creators-css">
.cr-wrap{{max-width:900px;margin:30px auto;padding:0 30px}}
.cr-wrap h1{{font-size:24px;text-align:center;margin-bottom:25px}}
.cr-wrap h2{{font-size:18px;text-align:center;margin:25px 0 15px}}
.credits{{text-align:center;margin-bottom:30px;font-size:15px;line-height:2}}
.credits p{{margin:0}}
.sg{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:20px 0}}
.sc{{border:1px solid #e0e0e0;background:#fff;border-radius:4px;padding:10px;display:flex;align-items:center;gap:10px;direction:rtl}}
.sn{{font-size:14px;font-weight:bold;margin-bottom:2px}}
.ss{{font-size:12px;color:#666}}
.sy{{font-size:12px;color:#999}}
.partners{{text-align:center;margin:30px 0;font-size:14px;line-height:1.8}}
.partners a{{color:#29aae3;text-decoration:none}}
.donors{{display:flex;justify-content:center;gap:60px;margin:20px 0;text-align:center;flex-wrap:wrap;font-size:14px}}
@media(max-width:768px){{.sg{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:480px){{.sg{{grid-template-columns:1fr}}}}
</style>
{extra_css}
</head>
<body class="page">
{header_html}
<div id=content>
<div class="cr-wrap">
  <h1>יוצרים ושותפים</h1>
  <div class="credits">
    <p><strong>יזום והפקה:</strong> עדי קול ואלון רוזן</p>
    <p><strong>ליווי מקצועי:</strong> דניאל נחנסון</p>
    <p><strong>עורך:</strong> הארי טולדו</p>
    <p><strong>עוזרת עריכה:</strong> טלי גולדרינג</p>
    <p><strong>רכזת פרויקט:</strong> נעם בר לב</p>
    <p><strong>צוות דיבור אחר:</strong> ברי רוזנברג</p>
    <p><strong>לייקה:</strong> יפעת מור</p>
  </div>
  <h2>הסטודנטים</h2>
  <div class="sg">
{student_cards}
  </div>
  <div class="partners">
    <p><strong>שותפים:</strong> פרויקט "מעשה ב 70" פועל בשיתוף עם מיזם <a href="https://www.facebook.com/diburacher/" target="_blank">דיבור אחר</a>.</p>
  </div>
  <h2>תורמים</h2>
  <div class="donors">
    <div><strong>קרן לאוטמן</strong></div>
    <div><strong>בעידוד ותמיכת קרן מתנאל</strong></div>
    <div><strong>קרן דרהי</strong></div>
  </div>
  <h2>תומכים</h2>
  <div class="donors"><div><strong>איירון סורס</strong></div></div>
</div>
</div>
{footer_html}
</body>
</html>'''

open(cr_path, 'w', encoding='utf-8').write(creators_page)
print(f"  Saved: {len(creators_page)} bytes")

# === ABOUT PAGE ===
print("=== About page ===")
about_path = os.path.join('מעשה-ב-70-למה', 'index.html')
about_old = open(about_path, 'r', encoding='utf-8').read()

imgs = re.findall(r'(data:image/png;base64,[A-Za-z0-9+/=]{1000,})', about_old)
img_data = max(imgs, key=len) if imgs else ''
img_html = f'<div style="text-align:center;margin:20px 0"><img src="{img_data}" style="max-width:700px;width:100%;height:auto;border-radius:4px"></div>' if img_data else ''
print(f"  Bottom image: {len(img_data)//1024} KB")

about_page = f'''<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>מעשה ב-70, למה?</title>
{theme_css}
<style id="about-css">
.about-wrap{{max-width:800px;margin:30px auto;padding:0 30px}}
.about-wrap h1{{font-size:24px;text-align:center;margin-bottom:25px}}
.about-video{{max-width:600px;margin:0 auto 30px}}
.about-video .vw{{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:4px;background:#000}}
.about-video .vw iframe{{position:absolute;top:0;left:0;width:100%;height:100%;border:0}}
.about-list{{list-style:none;padding:0;margin:0 0 30px}}
.about-list li{{display:flex;align-items:flex-start;gap:12px;margin-bottom:15px;font-size:15px;line-height:1.7}}
.about-icon{{flex-shrink:0;width:28px;height:28px;border-radius:50%;background:#47abe6;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px}}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
{extra_css}
</head>
<body class="page">
{header_html}
<div id=content>
<div class="about-wrap">
  <h1>מעשה ב-70, למה?</h1>
  <div class="about-video"><div class="vw">
    <iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>
  </div></div>
  <ul class="about-list">
    <li><span class="about-icon"><i class="fa fa-book"></i></span><span>פרויקט מעשה ב-70 מבקש לספר את סיפורה של החברה הישראלית דרך סיפורם של הפרטים המרכיבים אותה.</span></li>
    <li><span class="about-icon"><i class="fa fa-bullhorn"></i></span><span>הפרויקט נועד לתת במה וקול למגוון רחב של קהילות, אוכלוסיות וזהויות בחברה הישראלית, גם כאלה שבדרך כלל קולם אינו נשמע וסיפורם פחות מוכר.</span></li>
    <li><span class="about-icon"><i class="fa fa-smile-o"></i></span><span>במסגרת הפרויקט זכו הסטודנטים לצאת מאזור הנוחות שלהם ולהכיר פנים וקולות שונים בחברה הישראלית. להקשיב, להתחבר וליצור יחד.</span></li>
    <li><span class="about-icon"><i class="fa fa-video-camera"></i></span><span>דרך המפגש המצולם בין הסטודנטים למרואיינים, תוכלו גם אתם הצופים להיחשף לנקודות המבט השונות, להכיר ובעיקר להנות מהפסיפס החברתי המגוון.</span></li>
    <li><span class="about-icon"><i class="fa fa-clock-o"></i></span><span>ארכיון הסיפורים שיצרנו מתעד את סיפורה של החברה בישראל בשנתה ה-70 ומשמש גם כקפסולת זמן עבור הדורות הבאים.</span></li>
  </ul>
  {img_html}
</div>
</div>
{footer_html}
</body>
</html>'''

open(about_path, 'w', encoding='utf-8').write(about_page)
print(f"  Saved: {len(about_page)} bytes")

# === ADD HOVER EFFECTS TO HOMEPAGE ===
print("=== Homepage hover effects ===")
hp = open('index.html', 'r', encoding='utf-8').read()

hover_css = """<style id="hover-fx">
.video-grid a img{transition:transform 0.3s ease,opacity 0.3s ease}
.video-grid a:hover img{transform:scale(1.05);opacity:0.85}
.video-grid a:hover .play-btn{background:rgba(0,0,0,0.7)}
</style>"""

# Add class to grid and play buttons for targeting
hp = hp.replace('<div class="video-grid">', '<div class="video-grid">')
if 'hover-fx' not in hp:
    hp = hp.replace('</head>', hover_css + '\n</head>')

# Add class to play overlay divs
hp = hp.replace(
    'width:40px;height:40px;border-radius:50%;background:rgba(0,0,0,0.5)',
    'width:40px;height:40px;border-radius:50%;background:rgba(0,0,0,0.5);transition:background 0.3s ease'
)

open('index.html', 'w', encoding='utf-8').write(hp)
print(f"  Added hover effects")

print("\n=== All done ===")
