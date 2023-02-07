import requests
import time
from dotenv import load_dotenv
import os


load_dotenv()


ngrok_url = os.getenv("NGROK_URL")

start_time = time.time()
for url in (f"{ngrok_url}/static/{x}" for x in range(1, 16)):
    resp = requests.get(url)
    assert resp.status_code == 200
end_time = time.time()

print("Done!")
print(end_time - start_time)
