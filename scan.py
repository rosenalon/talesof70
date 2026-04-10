import re

for name, path in [('Homepage', 'index.html'), ('About', 'מעשה-ב-70-למה/index.html')]:
    html = open(path, 'rb').read()
    body = html[html.find(b'<body'):]
    
    print(f"\n{'='*60}")
    print(f"{name}")
    print(f"{'='*60}")
    
    # Find ALL iframes in body
    iframes = list(re.finditer(rb'<iframe[^>]*>', body))
    print(f"Iframes: {len(iframes)}")
    for i, m in enumerate(iframes):
        tag = m.group(0)
        # Truncate srcdoc
        short = re.sub(rb'srcdoc="[^"]{100,}"', b'srcdoc="[HUGE]"', tag)
        print(f"  {i}: {short.decode('utf-8','replace')[:300]}")
    
    # Find sandbox
    sbox = list(re.finditer(rb'sandbox="([^"]*)"', body))
    print(f"Sandbox attrs: {len(sbox)}")
    for s in sbox:
        print(f"  {s.group(0).decode()}")
    
    # Find srcdoc
    sdoc = body.count(b'srcdoc=')
    print(f"srcdoc attrs: {sdoc}")
    
    # Find the byte position and length of the iframe with srcdoc
    iframe_start = body.find(b'<iframe', body.find(b'srcdoc') - 500 if body.find(b'srcdoc') > 0 else 0)
    if sdoc > 0:
        srcdoc_pos = body.find(b'srcdoc="')
        # Find end of srcdoc: scan for "></iframe>
        end_marker = body.find(b'"></iframe>', srcdoc_pos)
        if end_marker > 0:
            end_marker += len(b'"></iframe>')
            # Find the opening <iframe before srcdoc
            search_back = body.rfind(b'<iframe', 0, srcdoc_pos)
            if search_back > 0:
                full_iframe = body[search_back:end_marker]
                print(f"\nFull broken iframe: {len(full_iframe)} bytes")
                print(f"  Starts at body offset: {search_back}")
                print(f"  First 100: {full_iframe[:100].decode('utf-8','replace')}")
                print(f"  Last 50: {full_iframe[-50:].decode('utf-8','replace')}")
