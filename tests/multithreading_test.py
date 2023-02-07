import threading
import time
import requests
from utils import get_static_url


static_url = get_static_url()

def upload_file(names):
    print(f"Uploading {names}: starting")
    for url in (static_url + name for name in names):
        print(f"Uploading {url}: starting")
        resp = requests.get(url)
        assert resp.status_code == 200
        print(f"Uploading {url}: finishing")
    print(f"Uploading {names}: finishing")

if __name__ == "__main__":
    start_time = time.time()

    threads = []
    for index in range(1, 16):
        names = [str(i) for i in range(index, 16, 16)]
        thread = threading.Thread(target=upload_file, args=(names,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print("Done!")
    print(end_time - start_time)
