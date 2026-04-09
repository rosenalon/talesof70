import os

fpath = os.path.join('מעשה-ב-70-למה', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

# Current container is max-width 700px, let's make image fill it
old = '.bottom-image img {\n  max-width: 100%;\n  height: auto;\n  border-radius: 4px;\n}'
new = '.bottom-image img {\n  max-width: 100%;\n  width: 100%;\n  height: auto;\n  border-radius: 4px;\n}'

html = html.replace(old, new)

# Also widen the container a bit
html = html.replace('max-width: 700px;', 'max-width: 800px;')

open(fpath, 'w', encoding='utf-8').write(html)
print("Done")
