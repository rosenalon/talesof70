import re

# Check homepage CSS rules related to video/iframe/popup
hp = open('index.html', 'rb').read()

# Find CSS rules that might affect iframes or video wrappers
css_blocks = re.findall(rb'<style[^>]*>(.*?)</style>', hp, re.DOTALL)
print(f"Total style blocks: {len(css_blocks)}")

suspects = []
for i, css in enumerate(css_blocks):
    for pattern in [rb'iframe', rb'vlog-popup', rb'fluid-width', rb'vlog-cover', rb'vlog-format-content', rb'vlog-format-inplay', rb'fitvid']:
        if pattern in css:
            # Extract the relevant rules
            for m in re.finditer(rb'[^{}]*' + pattern + rb'[^{]*\{[^}]*\}', css):
                rule = m.group(0).strip()
                if len(rule) < 300:
                    suspects.append((i, rule))

print(f"\nSuspect CSS rules ({len(suspects)}):")
for idx, rule in suspects[:30]:
    print(f"  Block {idx}: {rule.decode('utf-8','replace')[:200]}")

# Also check the parent elements of the iframe
body_start = hp.find(b'<body')
vid_idx = hp.find(b'fluid-width-video-wrapper', body_start)
if vid_idx > 0:
    # Go back to find parent elements and their styles
    parent_area = hp[vid_idx-500:vid_idx]
    parent_area = re.sub(rb'data:[^\s"]{50,}', b'[DATA]', parent_area)
    print(f"\nParent elements before video wrapper:")
    print(parent_area.decode('utf-8','replace')[-400:])
