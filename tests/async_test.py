import httpx
import asyncio
import time
from utils import get_static_url


static_url = get_static_url()


async def get_file(url):
    async with httpx.AsyncClient() as client:
        print(url)
        resp = await client.get(url)
        assert resp.status_code == 200


async def main():
    tasks = []
    for url in (static_url + str(filename) for filename in range(1, 16)):
        tasks.append(loop.create_task(get_file(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    start_time = time.time()
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except Exception as e:
        print(str(e))
    end_time = time.time()
    print(end_time - start_time)