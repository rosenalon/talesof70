import re, os

NEW = 'https://rosenalon.github.io/talesof70'

# Matching header from homepage
HEADER = f'''<header style="background:#fff;padding:12px 30px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 1px 8px rgba(0,0,0,0.08);position:sticky;top:0;z-index:100;direction:rtl;font-family:Assistant,Arial,sans-serif">
  <div style="display:flex;align-items:center;gap:12px">
    <a href="{NEW}/" style="font-size:22px;font-weight:700;color:#29aae3;text-decoration:none">מעשה ב - 70</a>
    <span style="font-size:12px;color:#999">בשיתוף עם דיבור אחר</span>
  </div>
  <div style="display:flex;align-items:center;gap:25px;font-size:15px">
    <a href="{NEW}/%d7%9e%d7%a2%d7%a9%d7%94-%d7%91-70-%d7%9c%d7%9e%d7%94/" style="color:#2e2e3b;text-decoration:none;font-weight:600">מעשה ב-70, למה?</a>
    <a href="{NEW}/%d7%99%d7%95%d7%a6%d7%a8%d7%99%d7%9d-%d7%95%d7%a9%d7%95%d7%aa%d7%a4%d7%99%d7%9d/" style="color:#2e2e3b;text-decoration:none;font-weight:600">יוצרים ושותפים</a>
  </div>
</header>'''

FOOTER = '<footer style="background:#1a1a2e;color:rgba(255,255,255,0.6);padding:25px;text-align:center;margin-top:40px;font-size:13px;font-family:Assistant,Arial,sans-serif">כל הזכויות שמורות למרכז הבינתחומי הרצליה | 2018</footer>'

CSS = """@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Assistant',Arial,sans-serif;background:#f5f5f5;color:#2e2e3b;direction:rtl}"""

# ===== REBUILD CREATORS PAGE =====
print("=== Rebuilding creators page ===")
cr_path = os.path.join('יוצרים-ושותפים', 'index.html')
old = open(cr_path, 'r', encoding='utf-8').read()

# Extract ALL student cards: photo + name + school + year
students = []
# Pattern: img with base64 src, then student-name div
for m in re.finditer(r'<img src="(data:image[^"]+)"[^>]*>\s*(?:<div class="student-info">)?\s*<div class="student-name">([^<]+)</div>\s*<div class="student-school">([^<]*)</div>\s*<div class="student-year">([^<]*)</div>', old):
    students.append({
        'img': m.group(1),
        'name': m.group(2).strip(),
        'school': m.group(3).strip(),
        'year': m.group(4).strip()
    })

# Also try cards without photos
for m in re.finditer(r'<div class="student-name">([^<]+)</div>\s*<div class="student-school">([^<]*)</div>\s*<div class="student-year">([^<]*)</div>', old):
    name = m.group(1).strip()
    if not any(s['name'] == name for s in students):
        students.append({
            'img': '',
            'name': name,
            'school': m.group(2).strip(),
            'year': m.group(3).strip()
        })

print(f"  Extracted {len(students)} students ({sum(1 for s in students if s['img'])} with photos)")

# Build student cards
student_html = ''
for s in students:
    photo = f'<img src="{s["img"]}" style="width:70px;height:70px;border-radius:50%;object-fit:cover;flex-shrink:0">' if s['img'] else ''
    student_html += f'''<div style="border:1px solid #e0e0e0;background:#fff;border-radius:4px;padding:10px;display:flex;align-items:center;gap:10px;direction:rtl">
  {photo}
  <div>
    <div style="font-size:14px;font-weight:bold">{s['name']}</div>
    <div style="font-size:12px;color:#666">{s['school']}</div>
    <div style="font-size:12px;color:#999">{s['year']}</div>
  </div>
</div>
'''

creators_html = f'''<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>יוצרים ושותפים – מעשה ב – 70</title>
<style>
{CSS}
.sg{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:20px 0}}
@media(max-width:768px){{.sg{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:480px){{.sg{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
{HEADER}
<div style="max-width:900px;margin:30px auto;padding:0 30px">
  <h1 style="font-size:24px;text-align:center;margin-bottom:25px">יוצרים ושותפים</h1>
  <div style="text-align:center;margin-bottom:30px;font-size:15px;line-height:2">
    <p><strong>יזום והפקה:</strong> עדי קול ואלון רוזן</p>
    <p><strong>ליווי מקצועי:</strong> דניאל נחנסון</p>
    <p><strong>עורך:</strong> הארי טולדו</p>
    <p><strong>עוזרת עריכה:</strong> טלי גולדרינג</p>
    <p><strong>רכזת פרויקט:</strong> נעם בר לב</p>
    <p><strong>צוות דיבור אחר:</strong> ברי רוזנברג</p>
    <p><strong>לייקה:</strong> יפעת מור</p>
  </div>
  <h2 style="font-size:18px;text-align:center;margin:25px 0 15px">הסטודנטים</h2>
  <div class="sg">
{student_html}
  </div>
  <div style="text-align:center;margin:30px 0;font-size:14px;line-height:1.8">
    <p><strong>שותפים:</strong> פרויקט "מעשה ב 70" פועל בשיתוף עם מיזם <a href="https://www.facebook.com/diburacher/" target="_blank" style="color:#29aae3">דיבור אחר</a>.</p>
  </div>
  <h2 style="font-size:18px;text-align:center;margin:25px 0 15px">תורמים</h2>
  <div style="display:flex;justify-content:center;gap:60px;margin:20px 0;text-align:center;flex-wrap:wrap;font-size:14px">
    <div><strong>קרן לאוטמן</strong></div>
    <div><strong>בעידוד ותמיכת קרן מתנאל</strong></div>
    <div><strong>קרן דרהי</strong></div>
  </div>
  <h2 style="font-size:18px;text-align:center;margin:25px 0 15px">תומכים</h2>
  <div style="display:flex;justify-content:center;gap:60px;margin:20px 0;text-align:center;flex-wrap:wrap;font-size:14px">
    <div><strong>איירון סורס</strong></div>
  </div>
</div>
{FOOTER}
</body>
</html>'''

open(cr_path, 'w', encoding='utf-8').write(creators_html)
print(f"  Saved: {len(creators_html)} bytes")

# ===== FIX ABOUT PAGE HEADER =====
print("\n=== Fixing about page header ===")
about_path = os.path.join('מעשה-ב-70-למה', 'index.html')
about = open(about_path, 'r', encoding='utf-8').read()

# Extract bottom image
imgs = re.findall(r'(data:image/png;base64,[A-Za-z0-9+/=]{1000,})', about)
img_data = max(imgs, key=len) if imgs else ''
img_html = f'<div style="text-align:center;margin:20px 0"><img src="{img_data}" style="max-width:700px;width:100%;height:auto;border-radius:4px" alt=""></div>' if img_data else ''
print(f"  Bottom image: {len(img_data)//1024} KB")

about_html = f'''<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>מעשה ב-70, למה?</title>
<style>{CSS}</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
{HEADER}
<div style="max-width:800px;margin:30px auto;padding:0 30px">
  <h1 style="font-size:24px;text-align:center;margin-bottom:25px">מעשה ב-70, למה?</h1>
  <div style="max-width:600px;margin:0 auto 30px">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:4px;background:#000">
      <iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
  <ul style="list-style:none;padding:0;margin:0 0 30px">
    <li style="display:flex;align-items:flex-start;gap:12px;margin-bottom:15px;font-size:15px;line-height:1.7"><span style="flex-shrink:0;width:28px;height:28px;border-radius:50%;background:#47abe6;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px"><i class="fa fa-book"></i></span><span>פרויקט מעשה ב-70 מבקש לספר את סיפורה של החברה הישראלית דרך סיפורם של הפרטים המרכיבים אותה.</span></li>
    <li style="display:flex;align-items:flex-start;gap:12px;margin-bottom:15px;font-size:15px;line-height:1.7"><span style="flex-shrink:0;width:28px;height:28px;border-radius:50%;background:#47abe6;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px"><i class="fa fa-bullhorn"></i></span><span>הפרויקט נועד לתת במה וקול למגוון רחב של קהילות, אוכלוסיות וזהויות בחברה הישראלית, גם כאלה שבדרך כלל קולם אינו נשמע וסיפורם פחות מוכר.</span></li>
    <li style="display:flex;align-items:flex-start;gap:12px;margin-bottom:15px;font-size:15px;line-height:1.7"><span style="flex-shrink:0;width:28px;height:28px;border-radius:50%;background:#47abe6;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px"><i class="fa fa-smile-o"></i></span><span>במסגרת הפרויקט זכו הסטודנטים לצאת מאזור הנוחות שלהם ולהכיר פנים וקולות שונים בחברה הישראלית. להקשיב, להתחבר וליצור יחד.</span></li>
    <li style="display:flex;align-items:flex-start;gap:12px;margin-bottom:15px;font-size:15px;line-height:1.7"><span style="flex-shrink:0;width:28px;height:28px;border-radius:50%;background:#47abe6;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px"><i class="fa fa-video-camera"></i></span><span>דרך המפגש המצולם בין הסטודנטים למרואיינים, תוכלו גם אתם הצופים להיחשף לנקודות המבט השונות, להכיר ובעיקר להנות מהפסיפס החברתי המגוון.</span></li>
    <li style="display:flex;align-items:flex-start;gap:12px;margin-bottom:15px;font-size:15px;line-height:1.7"><span style="flex-shrink:0;width:28px;height:28px;border-radius:50%;background:#47abe6;color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px"><i class="fa fa-clock-o"></i></span><span>ארכיון הסיפורים שיצרנו מתעד את סיפורה של החברה בישראל בשנתה ה-70 ומשמש גם כקפסולת זמן עבור הדורות הבאים.</span></li>
  </ul>
  {img_html}
</div>
{FOOTER}
</body>
</html>'''

open(about_path, 'w', encoding='utf-8').write(about_html)
print(f"  Saved: {len(about_html)} bytes")

print("\n=== Done ===")
