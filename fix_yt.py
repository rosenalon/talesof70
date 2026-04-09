import re

html = open('index.html', 'rb').read()

# Remove ALL meta CSP tags aggressively
html = re.sub(rb'<meta[^>]*[Cc]ontent-[Ss]ecurity-[Pp]olicy[^>]*>', b'', html)
html = re.sub(rb'<meta[^>]*[Dd]isabled-CSP[^>]*>', b'', html)

# Replace the iframe embed with a thumbnail that loads YouTube on click
old_embed = re.search(rb'<div style="max-width:640px;margin:0 auto 20px">.*?</iframe>.*?</div>\s*</div>', html, re.DOTALL)
if not old_embed:
    old_embed = re.search(rb'<div style="[^"]*position:relative;padding-bottom:56\.25%[^"]*">.*?</iframe>.*?</div>', html, re.DOTALL)

# Find ANY section containing the FiuItIwjx28 embed
embed_section = re.search(rb'<section[^>]*background[^>]*1a1a2e[^>]*>.*?</section>', html, re.DOTALL)

if embed_section:
    old = embed_section.group(0)
    new_section = b'''<section style="background:#1a1a2e;padding:40px 0;color:#fff">
  <div style="max-width:1100px;margin:0 auto;display:flex;gap:40px;align-items:center;padding:0 30px;direction:rtl">
    <div style="flex:1;min-width:0">
      <div id="yt-player" style="position:relative;cursor:pointer;border-radius:4px;overflow:hidden">
        <img src="https://img.youtube.com/vi/FiuItIwjx28/hqdefault.jpg" style="width:100%;display:block">
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;background:red;border-radius:12px;display:flex;align-items:center;justify-content:center">
          <div style="width:0;height:0;border-style:solid;border-width:10px 0 10px 20px;border-color:transparent transparent transparent white;margin-left:4px"></div>
        </div>
      </div>
      <script>
      document.getElementById("yt-player").addEventListener("click", function(){
        this.innerHTML = \'<div style="position:relative;padding-bottom:56.25%;height:0"><iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28?autoplay=1" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" allowfullscreen></iframe></div>\';
      });
      </script>
    </div>
    <div style="flex:1;text-align:right">
      <h1 style="font-size:28px;color:#29aae3;margin-bottom:15px">\xd7\xa4\xd7\xa8\xd7\x95\xd7\x99\xd7\xa7\xd7\x98 "\xd7\x9e\xd7\xa2\xd7\xa9\xd7\x94 \xd7\x91 - 70"</h1>
      <p style="font-size:15px;line-height:1.8;margin-bottom:10px">\xd7\x91\xd7\x9e\xd7\xa1\xd7\x92\xd7\xa8\xd7\xaa \xd7\xa4\xd7\xa8\xd7\x95\xd7\x99\xd7\xa7\xd7\x98 \xd7\x99\xd7\x99\xd7\x97\xd7\x95\xd7\x93\xd7\x99 \xd7\x99\xd7\xa6\xd7\x90\xd7\x95 150 \xd7\xa1\xd7\x98\xd7\x95\xd7\x93\xd7\xa0\xd7\x98\xd7\x99\xd7\x9d \xd7\x9e\xd7\x94\xd7\x9e\xd7\xa8\xd7\x9b\xd7\x96 \xd7\x94\xd7\x91\xd7\x99\xd7\xa0\xd7\xaa\xd7\x97\xd7\x95\xd7\x9e\xd7\x99 \xd7\x9c\xd7\xa4\xd7\x92\xd7\x95\xd7\xa9 \xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c\xd7\x99\xd7\x95\xd7\xaa \xd7\x95\xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c\xd7\x99\xd7\x9d \xd7\x9e\xd7\x9b\xd7\x9c \xd7\xa8\xd7\x97\xd7\x91\xd7\x99 \xd7\x94\xd7\x90\xd7\xa8\xd7\xa5 \xd7\x95\xd7\x9c\xd7\xaa\xd7\xa2\xd7\x93 \xd7\x90\xd7\xaa \xd7\x94\xd7\xa1\xd7\x99\xd7\xa4\xd7\x95\xd7\xa8 \xd7\x94\xd7\x90\xd7\x99\xd7\xa9\xd7\x99 \xd7\xa9\xd7\x9c\xd7\x94\xd7\x9d \xd7\x91\xd7\x90\xd7\x9e\xd7\xa6\xd7\xa2\xd7\x95\xd7\xaa \xd7\x98\xd7\x9c\xd7\xa4\xd7\x95\xd7\xa0\xd7\x99\xd7\x9d \xd7\xa1\xd7\x9c\xd7\x95\xd7\x9c\xd7\xa8\xd7\x99\xd7\x99\xd7\x9d.</p>
      <p style="font-size:15px;line-height:1.8;margin-bottom:10px">\xd7\x93\xd7\xa8\xd7\x9a \xd7\xa9\xd7\x9c\xd7\x9c \xd7\x94\xd7\xa1\xd7\x99\xd7\xa4\xd7\x95\xd7\xa8\xd7\x99\xd7\x9d \xd7\x95\xd7\x94\xd7\x97\xd7\x95\xd7\x95\xd7\x99\xd7\x95\xd7\xaa \xd7\x94\xd7\x90\xd7\xa0\xd7\x95\xd7\xa9\xd7\x99\xd7\x95\xd7\xaa, \xd7\xa2\xd7\x95\xd7\x9c\xd7\x94 \xd7\x95\xd7\x9e\xd7\xa9\xd7\xaa\xd7\xa7\xd7\xa4\xd7\xaa \xd7\x93\xd7\x9e\xd7\x95\xd7\xaa\xd7\x94 \xd7\xa9\xd7\x9c \xd7\x94\xd7\x97\xd7\x91\xd7\xa8\xd7\x94 \xd7\x91\xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c.</p>
      <p style="font-size:15px;line-height:1.8">\xd7\x90\xd7\xaa\xd7\x9d \xd7\x9e\xd7\x95\xd7\x96\xd7\x9e\xd7\xa0\xd7\x99\xd7\x9d \xd7\x9c\xd7\x94\xd7\xa6\xd7\x98\xd7\xa8\xd7\xa3 \xd7\x90\xd7\x9c\xd7\x99\xd7\xa0\xd7\x95, \xd7\x9c\xd7\xa6\xd7\xa4\xd7\x95\xd7\xaa, \xd7\x9c\xd7\x94\xd7\xaa\xd7\xa8\xd7\x92\xd7\xa9, \xd7\x9c\xd7\xa6\xd7\x97\xd7\x95\xd7\xa7, \xd7\x9c\xd7\x91\xd7\x9b\xd7\x95\xd7\xaa \xd7\x95\xd7\x9c\xd7\x94\xd7\xaa\xd7\x97\xd7\x91\xd7\xa8 <a href="https://rosenalon.github.io/talesof70/category/%D7%9E%D7%A2%D7%A9%D7%94-%D7%91-70/" style="color:#29aae3">\xd7\x9c\xd7\xa1\xd7\x99\xd7\xa4\xd7\x95\xd7\xa8\xd7\x9d \xd7\xa9\xd7\x9c 70 \xd7\x99\xd7\xa9\xd7\xa8\xd7\x90\xd7\x9c\xd7\x99\xd7\x9d.</a></p>
    </div>
  </div>
</section>'''
    html = html.replace(old, new_section)
    print("Replaced hero section with click-to-play")
else:
    print("Hero section not found - searching for iframe directly")
    # Just replace the iframe with click-to-play
    html = re.sub(
        rb'<iframe[^>]*FiuItIwjx28[^>]*>.*?</iframe>',
        b'<div id="yt-player" onclick="this.innerHTML=\'<iframe src=https://www.youtube-nocookie.com/embed/FiuItIwjx28?autoplay=1 style=width:100%;aspect-ratio:16/9;border:0 allow=accelerometer;autoplay;clipboard-write;encrypted-media allowfullscreen></iframe>\'" style="cursor:pointer;position:relative"><img src="https://img.youtube.com/vi/FiuItIwjx28/hqdefault.jpg" style="width:100%"><div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;background:red;border-radius:12px;display:flex;align-items:center;justify-content:center"><div style="border-style:solid;border-width:10px 0 10px 20px;border-color:transparent transparent transparent white;margin-left:4px"></div></div></div>',
        html
    )
    print("Replaced iframe with click-to-play thumbnail")

open('index.html', 'wb').write(html)
print(f"Done. Size: {len(html)}")
