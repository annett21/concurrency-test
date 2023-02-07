import httpx
import asyncio
import time
from utils import get_static_url


static_url = get_static_url()


async def get_file(url):
    async with httpx.AsyncClient() as client:
        print(f"Uploading {url}: starting")
        resp = await client.get(url)
        assert resp.status_code == 200
        print(f"Uploading {url}: finishing")


async def main():
    urls = (static_url + str(name) for name in range(1, 16))
    tasks = [asyncio.create_task(get_file(url)) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time - start_time)