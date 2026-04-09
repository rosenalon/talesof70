import re, os

NEW = 'https://rosenalon.github.io/talesof70'

# Simple header that matches the site without theme CSS conflicts
header = f'''<div style="background:#fff;padding:15px 30px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 2px 10px rgba(0,0,0,0.08);direction:rtl">
  <a href="{NEW}/" style="text-decoration:none"><img src="https://img.youtube.com/vi/FiuItIwjx28/default.jpg" alt="מעשה ב-70" style="height:45px;border-radius:4px"></a>
  <div style="display:flex;gap:25px;font-size:15px;font-family:Assistant,Arial,sans-serif">
    <a href="{NEW}/%d7%9e%d7%a2%d7%a9%d7%94-%d7%91-70-%d7%9c%d7%9e%d7%94/" style="color:#2e2e3b;text-decoration:none">מעשה ב-70, למה?</a>
    <a href="{NEW}/%d7%99%d7%95%d7%a6%d7%a8%d7%99%d7%9d-%d7%95%d7%a9%d7%95%d7%aa%d7%a4%d7%99%d7%9d/" style="color:#2e2e3b;text-decoration:none">יוצרים ושותפים</a>
  </div>
</div>'''

footer = '<div style="background:#2c3e50;color:rgba(255,255,255,0.7);padding:20px;text-align:center;margin-top:40px;font-size:12px">כל הזכויות שמורות למרכז הבינתחומי הרצליה | 2018</div>'

base_css = """@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Assistant',Arial,sans-serif;background:#fff;color:#2e2e3b;direction:rtl}"""

# ===== REBUILD ABOUT PAGE =====
about_path = os.path.join('מעשה-ב-70-למה', 'index.html')
old_about = open(about_path, 'r', encoding='utf-8').read()

# Extract bottom image
imgs = re.findall(r'(data:image/png;base64,[A-Za-z0-9+/=]{1000,})', old_about)
img_data = max(imgs, key=len) if imgs else ''
img_html = f'<div style="text-align:center;margin:20px 0"><img src="{img_data}" style="max-width:700px;width:100%;height:auto;border-radius:4px" alt="מעשה ב-70"></div>' if img_data else ''
print(f"About: bottom image {len(img_data)//1024} KB")

about_html = f'''<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>מעשה ב-70, למה?</title>
<style>{base_css}</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
{header}
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
{footer}
</body>
</html>'''

open(about_path, 'w', encoding='utf-8').write(about_html)
print(f"About page rebuilt: {len(about_html)} bytes")

# ===== REBUILD CREATORS PAGE =====
creators_path = os.path.join('יוצרים-ושותפים', 'index.html')
old_creators = open(creators_path, 'r', encoding='utf-8').read()

# Extract student cards with photos
students_html = ''
for m in re.finditer(r'<div class="student-card">(.*?)</div>\s*</div>', old_creators, re.DOTALL):
    students_html += f'<div class="sc">{m.group(1)}</div></div>\n'

# If no cards found, extract content block
if not students_html:
    # Get everything between הסטודנטים and שותפים
    stu_start = old_creators.find('הסטודנטים')
    stu_end = old_creators.find('שותפים', stu_start + 20) if stu_start > 0 else -1
    if stu_start > 0 and stu_end > 0:
        students_html = old_creators[stu_start+30:stu_end-50]
        print(f"Extracted student block: {len(students_html)} chars")

student_photo_count = students_html.count('border-radius:50%')
print(f"Student photos found: {student_photo_count}")

creators_html = f'''<!DOCTYPE html>
<html dir="rtl" lang="he">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>יוצרים ושותפים – מעשה ב – 70</title>
<style>
{base_css}
.sg{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:20px 0}}
.sc{{border:1px solid #e0e0e0;background:#fafafa;border-radius:4px;padding:12px;display:flex;align-items:center;gap:8px;direction:rtl}}
.sc img{{width:70px;height:70px;border-radius:50%;object-fit:cover;flex-shrink:0}}
.student-name{{font-size:14px;font-weight:bold;margin-bottom:3px}}
.student-school{{font-size:12px;color:#666}}
.student-year{{font-size:12px;color:#999}}
@media(max-width:768px){{.sg{{grid-template-columns:repeat(2,1fr)}}}}
@media(max-width:480px){{.sg{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
{header}
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
    {students_html}
  </div>
  <div style="text-align:center;margin:30px 0;font-size:14px;line-height:1.8">
    <p><strong>שותפים:</strong> פרויקט "מעשה ב 70" פועל בשיתוף עם מיזם <a href="https://www.facebook.com/diburacher/" target="_blank" style="color:#29aae3">דיבור אחר</a>.</p>
  </div>
  <h2 style="font-size:18px;text-align:center;margin:25px 0 15px">תורמים</h2>
  <div style="display:flex;justify-content:center;gap:60px;margin:20px 0;text-align:center;flex-wrap:wrap">
    <div><strong>קרן לאוטמן</strong></div>
    <div><strong>בעידוד ותמיכת קרן מתנאל</strong></div>
    <div><strong>קרן דרהי</strong></div>
  </div>
</div>
{footer}
</body>
</html>'''

open(creators_path, 'w', encoding='utf-8').write(creators_html)
print(f"Creators page rebuilt: {len(creators_html)} bytes")
print("Done")
