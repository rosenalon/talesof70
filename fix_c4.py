import os, re

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

# Remove any old CSS fixes
html = re.sub(r'<style>[^<]*(?:entry-content img|120px|60px|80px|students-thumbnail|student-item)[^<]*</style>', '', html)

css = """<style>
.students-row {
  display: flex !important;
  flex-wrap: wrap !important;
  direction: rtl !important;
  gap: 15px !important;
}
.student-item {
  width: 31% !important;
  box-sizing: border-box !important;
  border: 1px solid #eee !important;
  padding: 15px !important;
  display: flex !important;
  align-items: center !important;
  direction: rtl !important;
  gap: 10px !important;
}
.student-img img {
  width: 100px !important;
  height: 100px !important;
  border-radius: 50% !important;
  object-fit: cover !important;
}
.student-details {
  text-align: right !important;
}
.student-name {
  font-size: 16px !important;
  margin: 0 0 5px 0 !important;
}
.student-school, .student-year {
  font-size: 13px !important;
  color: #666 !important;
  display: block !important;
}
.student-school p {
  margin: 0 !important;
}
@media (max-width: 768px) {
  .student-item {
    width: 48% !important;
  }
}
@media (max-width: 480px) {
  .student-item {
    width: 100% !important;
  }
}
</style>"""

html = html.replace('</head>', css + '\n</head>')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
