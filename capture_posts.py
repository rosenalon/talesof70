import subprocess
import os
import re
from urllib.parse import unquote

OLD = 'https://talesof70.runi.ac.il'
NEW = 'https://rosenalon.github.io/talesof70'
SF = r'C:\Users\alon_\AppData\Roaming\npm\single-file.cmd'

sf = open('singlefile_source.html', 'r', encoding='utf-8').read()

urls = re.findall(r'https://(?:talesof70\.runi\.ac\.il|rosenalon\.github\.io/talesof70)/\d{4}/\d{2}/\d{2}/[^\s"<>]+', sf)
urls = sorted(set(u.rstrip('/').replace(NEW, OLD) for u in urls))
print(f"Found {len(urls)} post URLs\n")

for i, url in enumerate(urls):
    path = unquote(url.replace(OLD, '').strip('/'))
    outdir = os.path.join('.', path)
    outfile = os.path.join(outdir, 'index.html')
    
    print(f"[{i+1}/{len(urls)}] {path}")
    os.makedirs(outdir, exist_ok=True)
    
    try:
        result = subprocess.run(
            [SF, url, outfile, '--browser-wait-until', 'networkidle0', '--browser-wait-delay', '3000'],
            capture_output=True, text=True, timeout=120
        )
        if os.path.exists(outfile) and os.path.getsize(outfile) > 1000:
            html = open(outfile, 'r', encoding='utf-8').read()
            html = html.replace(OLD, NEW)
            with open(outfile, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"  OK ({os.path.getsize(outfile)//1024} KB)")
        else:
            print(f"  FAILED")
    except Exception as e:
        print(f"  ERROR: {e}")

print("\nDone! Now run:")
print('  git add -A && git commit -m "SingleFile post pages" && git push --force')
