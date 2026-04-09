import re, os

NEW = 'https://rosenalon.github.io/talesof70'

# Same header as the new homepage
new_header = f'''<header style="background:#fff;padding:12px 30px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 1px 8px rgba(0,0,0,0.08);position:sticky;top:0;z-index:100;direction:rtl">
  <div style="display:flex;align-items:center;gap:12px">
    <a href="{NEW}/" style="font-size:22px;font-weight:700;color:#29aae3;text-decoration:none;font-family:Assistant,Arial,sans-serif">מעשה ב - 70</a>
    <span style="font-size:12px;color:#999">בשיתוף עם דיבור אחר</span>
  </div>
  <div style="display:flex;align-items:center;gap:25px;font-size:15px;font-family:Assistant,Arial,sans-serif">
    <a href="{NEW}/%d7%9e%d7%a2%d7%a9%d7%94-%d7%91-70-%d7%9c%d7%9e%d7%94/" style="color:#2e2e3b;text-decoration:none;font-weight:600">מעשה ב-70, למה?</a>
    <a href="{NEW}/%d7%99%d7%95%d7%a6%d7%a8%d7%99%d7%9d-%d7%95%d7%a9%d7%95%d7%aa%d7%a4%d7%99%d7%9d/" style="color:#2e2e3b;text-decoration:none;font-weight:600">יוצרים ושותפים</a>
  </div>
</header>'''

new_footer = f'<footer style="background:#1a1a2e;color:rgba(255,255,255,0.6);padding:25px;text-align:center;margin-top:40px;font-size:13px">כל הזכויות שמורות למרכז הבינתחומי הרצליה | 2018</footer>'

for page in ['מעשה-ב-70-למה', 'יוצרים-ושותפים']:
    fpath = os.path.join(page, 'index.html')
    if not os.path.exists(fpath):
        print(f"SKIP: {fpath}")
        continue
    
    html = open(fpath, 'r', encoding='utf-8').read()
    
    # Remove old header (the inline div version)
    html = re.sub(
        r'<div style="background:#fff;padding:15px 30px;display:flex.*?</div>\s*</div>',
        '',
        html,
        count=1,
        flags=re.DOTALL
    )
    
    # Remove old footer
    html = re.sub(r'<div style="background:#2c3e50[^"]*"[^>]*>.*?</div>', '', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<footer[^>]*>.*?</footer>', '', html, count=1, flags=re.DOTALL)
    
    # Insert new header after <body...>
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + new_header, html)
    
    # Insert new footer before </body>
    html = html.replace('</body>', new_footer + '\n</body>')
    
    open(fpath, 'w', encoding='utf-8').write(html)
    print(f"Fixed: {page} ({len(html)} bytes)")

print("Done")
