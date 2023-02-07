import requests
import time


all_urls = (f"http://127.0.0.1:8000/static/{x}" for x in range(1, 16))
start_time = time.time()
for _ in range(100):
    for url in all_urls:
        resp = requests.get(url, headers={'Cache-Control': 'no-cache'})
        assert resp.status_code == 200
end_time = time.time()
print("Done!")
print(end_time - start_time)
