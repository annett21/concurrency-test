import requests
import time
from utils import get_static_url


start_time = time.time()
static_url = get_static_url()
for url in (static_url + str(filename) for filename in [1, 6, 11]):
    resp = requests.get(url)
    assert resp.status_code == 200
end_time = time.time()

print("Done!")
print(end_time - start_time)
