import requests
import re
from bs4 import BeautifulSoup

url = "https://talesof70.runi.ac.il/2018/03/09/%d7%a8%d7%99%d7%a7%d7%94-%d7%a1%d7%95%d7%a1%d7%a7%d7%99%d7%9f/"
r = requests.get(url)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    html = r.text
    # Search for video URLs anywhere
    yt = re.findall(r'https?://(?:www\.)?(?:youtube\.com/(?:watch\?v=|embed/)|youtu\.be/)([A-Za-z0-9_-]+)', html)
    vim = re.findall(r'https?://(?:www\.)?(?:player\.)?vimeo\.com/(?:video/)?(\d+)', html)
    iframes = re.findall(r'<iframe[^>]*src="([^"]*)"', html)
    print(f"YouTube IDs: {yt}")
    print(f"Vimeo IDs: {vim}")
    print(f"Iframes: {iframes}")
    # Also check for oembed or data attributes
    embeds = re.findall(r'data-src="([^"]*)"', html)
    print(f"data-src: {embeds}")
    # Check for wp-embedded-content
    wp_embeds = re.findall(r'class="wp-embedded-content"[^>]*href="([^"]*)"', html)
    print(f"wp-embedded: {wp_embeds}")
    # Dump anything with video/youtube/vimeo
    for pat in ['youtube', 'vimeo', 'iframe', 'embed', 'player']:
        matches = re.findall(rf'.{{0,50}}{pat}.{{0,100}}', html, re.IGNORECASE)
        for m in matches[:2]:
            print(f"  {pat}: {m.strip()}")
