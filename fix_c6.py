import os, re

fpath = os.path.join('יוצרים-ושותפים', 'index.html')
html = open(fpath, 'r', encoding='utf-8').read()

# Remove ALL previous style fixes
html = re.sub(r'<style>[^<]*(?:student|entry-content|creators|120px|60px|80px|100px)[^<]*</style>', '', html)

css = """<style>
/* 3-column student grid */
.students-row {
  display: flex !important;
  flex-wrap: wrap !important;
  direction: rtl !important;
  gap: 10px !important;
  justify-content: center !important;
}
.student-item {
  width: 30% !important;
  box-sizing: border-box !important;
  border: 1px solid #ddd !important;
  background: #fafafa !important;
  padding: 10px !important;
  display: flex !important;
  align-items: center !important;
  direction: rtl !important;
  gap: 8px !important;
  min-height: 90px !important;
}
/* Student face photos ~80px circular */
.student-img img {
  width: 75px !important;
  height: 75px !important;
  max-width: 75px !important;
  border-radius: 50% !important;
  object-fit: cover !important;
  flex-shrink: 0 !important;
}
.student-details { text-align: right !important; }
.student-name {
  font-size: 14px !important;
  font-weight: bold !important;
  margin: 0 0 3px 0 !important;
}
.student-school, .student-year {
  font-size: 12px !important;
  color: #666 !important;
  display: block !important;
}
.student-school p { margin: 0 !important; }

/* Header text - smaller */
.entry-content h1, .vlog-single-content h1 {
  font-size: 22px !important;
  text-align: center !important;
}
.entry-content > p, .vlog-single-content > p {
  font-size: 14px !important;
  text-align: center !important;
  line-height: 1.8 !important;
}
.entry-content h2, .entry-content h3:not(.student-name),
.entry-content strong {
  font-size: 16px !important;
}
/* Content width */
.vlog-content, .vlog-single-content {
  max-width: 900px !important;
  margin: 0 auto !important;
  float: none !important;
}

/* Sponsor/partner logos - SMALL */
.entry-content img:not(.student-img img):not(.wp-post-image) {
  width: auto !important;
  height: auto !important;
  max-width: 75px !important;
  max-height: 75px !important;
  border-radius: 0 !important;
}
/* Override: student photos stay 75px circular */
.student-img img {
  width: 75px !important;
  height: 75px !important;
  max-width: 75px !important;
  border-radius: 50% !important;
}

@media (max-width: 768px) {
  .student-item { width: 48% !important; }
}
@media (max-width: 480px) {
  .student-item { width: 100% !important; }
}
</style>"""

html = html.replace('</head>', css + '\n</head>')

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
