import multiprocessing
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

    processes = []
    for index in range(1, 3):
        names = [str(i) for i in range(index, 16, 2)]
        process = multiprocessing.Process(target=upload_file, args=(names,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    time_spent = end_time - start_time
    print("Done!")
    print(time_spent)

    with open("test_statistic.txt", "a") as f:
        f.write(f"The multiprocessing_test was completed in: {time_spent}.\n")
