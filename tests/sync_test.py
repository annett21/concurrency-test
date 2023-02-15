import requests
import time
from utils import get_static_url


start_time = time.time()
static_url = get_static_url()
for url in (static_url + str(filename) for filename in range(1, 16)):
    resp = requests.get(url)
    assert resp.status_code == 200
end_time = time.time()

time_spent = end_time - start_time
print("Done!")
print(time_spent)
with open("test_statistic.txt", "a") as f:
    f.write(f"The sync_test was completed in: {time_spent}.\n")
