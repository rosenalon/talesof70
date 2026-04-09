import requests
r = requests.get("https://talesof70.runi.ac.il/", timeout=10)
print(f"Status: {r.status_code}")
print(f"Size: {len(r.text)} bytes")
