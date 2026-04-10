import re

hp = open('index.html', 'rb').read()
body_start = hp.find(b'<body')
body = hp[body_start:]
first_article = body.find(b'<article')
pre_article = body[:first_article]

# Search for ANY youtube/player/embed related content
for term in [b'youtube', b'ytm-', b'yt-player', b'ytp-', b'player', b'video-stream', 
             b'html5-video', b'srcdoc', b'sandbox', b'fitvid', b'movie_player',
             b'iframe', b'embed', b'data:text/html', b'<video']:
    count = pre_article.count(term)
    if count > 0:
        positions = [m.start() for m in re.finditer(re.escape(term), pre_article)]
        print(f"'{term.decode()}': {count} occurrences")
        for pos in positions[:3]:
            context = pre_article[max(0,pos-20):pos+80]
            context = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', context)
            print(f"  @{pos}: ...{context.decode('utf-8','replace')}...")
