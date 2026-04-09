import requests
import json

url = "https://talesof70.runi.ac.il/wp-json/wp/v2/posts?per_page=100"
r = requests.get(url)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    posts = r.json()
    print(f"Posts found: {len(posts)}")
    if posts:
        print(f"First post title: {posts[0].get('title',{}).get('rendered','')}")
        print(f"First post has content: {len(posts[0].get('content',{}).get('rendered',''))} chars")
        with open('wp_posts.json', 'w', encoding='utf-8') as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
        print("Saved to wp_posts.json")
else:
    print("API not accessible")
    print(r.text[:200])
