import re

html = open('index.html', 'rb').read()

# Replace the thumbnail link with a div that gets an iframe injected via JS
old = rb'<a href="https://www.youtube.com/watch?v=FiuItIwjx28" target="_blank" style="display:block;position:relative;border-radius:4px;overflow:hidden">\n        <img src="https://img.youtube.com/vi/FiuItIwjx28/hqdefault.jpg" style="width:100%;display:block">\n        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:68px;height:48px;background:red;border-radius:12px;display:flex;align-items:center;justify-content:center">\n          <div style="width:0;height:0;border-style:solid;border-width:10px 0 10px 20px;border-color:transparent transparent transparent white;margin-left:4px"></div>\n        </div>\n      </a>'

new = rb'''<div id="hero-yt-container" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:4px;background:#000"></div>
      <script>
      (function(){
        var c=document.getElementById("hero-yt-container");
        if(c){
          var f=document.createElement("iframe");
          f.src="https://www.youtube-nocookie.com/embed/FiuItIwjx28";
          f.style.cssText="position:absolute;top:0;left:0;width:100%;height:100%;border:0";
          f.setAttribute("allow","accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture");
          f.setAttribute("allowfullscreen","");
          c.appendChild(f);
        }
      })();
      </script>'''

html = html.replace(old, new)

if b'hero-yt-container' in html:
    print("Replaced with JS-injected iframe")
else:
    print("Pattern not found, trying alternate")
    # Try simpler replacement
    html = re.sub(
        rb'<a href="https://www\.youtube\.com/watch\?v=FiuItIwjx28"[^>]*>.*?</a>',
        new,
        html,
        flags=re.DOTALL
    )
    if b'hero-yt-container' in html:
        print("Replaced via regex")
    else:
        print("FAILED")

open('index.html', 'wb').write(html)
print("Done")
