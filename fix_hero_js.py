import re

html = open('index.html', 'rb').read()

# Find the current iframe and replace with a JS-injected version
old_iframe = b'<iframe src="https://www.youtube-nocookie.com/embed/FiuItIwjx28" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>'

new_embed = b'''<div id="hero-yt" style="position:absolute;top:0;left:0;width:100%;height:100%;background:#000"></div>
<script>
window.addEventListener("DOMContentLoaded",function(){
  var d=document.getElementById("hero-yt");
  if(d){
    var f=document.createElement("iframe");
    f.src="https://www.youtube-nocookie.com/embed/FiuItIwjx28";
    f.style.cssText="width:100%;height:100%;border:0";
    f.allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture";
    f.allowFullscreen=true;
    d.appendChild(f);
  }
});
</script>'''

if old_iframe in html:
    html = html.replace(old_iframe, new_embed)
    print("Replaced iframe with JS-injected version")
else:
    print("Iframe not found - checking alternatives")
    # Try to find any iframe with FiuItIwjx28
    count = html.count(b'FiuItIwjx28')
    print(f"  FiuItIwjx28 occurrences: {count}")

open('index.html', 'wb').write(html)
print(f"Done. Size: {len(html)}")
