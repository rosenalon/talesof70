import re
html = open(r'2018\03\09\ריקה-סוסקין\index.html', 'r', encoding='utf-8').read()

# Search broadly for any URL-like strings with video platforms
for pat in ['youtu', 'vimeo', 'wistia', 'dailymotion', 'video', 'iframe', 'embed', 'player', 'oembed']:
    count = html.lower().count(pat)
    if count > 0:
        print(f"'{pat}' appears {count} times")

# Find ALL URLs in the file
urls = re.findall(r'https?://[^\s"\'<>]{10,200}', html)
video_urls = [u for u in urls if any(v in u.lower() for v in ['youtu', 'vimeo', 'video', 'player', 'embed'])]
print(f"\nVideo-related URLs: {len(video_urls)}")
for u in set(video_urls):
    print(f"  {u[:150]}")

# Also check for data attributes with video info
data_attrs = re.findall(r'data-[a-z-]+="([^"]*(?:youtu|vimeo|video)[^"]*)"', html, re.IGNORECASE)
print(f"\nData attributes with video: {data_attrs}")
