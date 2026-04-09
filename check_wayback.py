import requests
import re
import json

# Try Wayback Machine for the WP REST API
api_url = "https://talesof70.runi.ac.il/wp-json/wp/v2/posts?per_page=100"
wb_api = f"https://archive.org/wayback/available?url={api_url}"
r = requests.get(wb_api)
print(f"Wayback check: {r.status_code}")
if r.status_code == 200:
    print(json.dumps(r.json(), indent=2))

# Also try fetching a post page from Wayback
print("\n--- Trying cached post page ---")
post_url = "https://talesof70.runi.ac.il/2018/03/09/%d7%a8%d7%99%d7%a7%d7%94-%d7%a1%d7%95%d7%a1%d7%a7%d7%99%d7%9f/"
wb = f"https://archive.org/wayback/available?url={post_url}"
r2 = requests.get(wb)
if r2.status_code == 200:
    data = r2.json()
    snap = data.get('archived_snapshots', {}).get('closest', {})
    if snap:
        print(f"Found snapshot: {snap['url']}")
        r3 = requests.get(snap['url'])
        if r3.status_code == 200:
            yt = re.findall(r'youtube\.com/(?:watch\?v=|embed/)([A-Za-z0-9_-]+)', r3.text)
            vim = re.findall(r'vimeo\.com/(?:video/)?(\d+)', r3.text)
            iframes = re.findall(r'<iframe[^>]*src=["\x27]([^"\x27]*)["\x27]', r3.text)
            print(f"YouTube: {yt}")
            print(f"Vimeo: {vim}")
            print(f"Iframes: {iframes[:5]}")
    else:
        print("No snapshot found")
