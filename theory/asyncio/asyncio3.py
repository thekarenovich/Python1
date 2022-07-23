# Альтернатива файлу asyncio1.py

import asyncio
import time


async def async_func(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)  # как sleep, только для асинх.
        print(site_name, page)
    return 'Well Done. by {}'.format(site_name)


async def main():
    task_a = loop.create_task(async_func('Blog'))
    task_b = loop.create_task(async_func('News'))
    task_c = loop.create_task(async_func('Forum'))
    await asyncio.wait([task_a, task_b, task_c])


if __name__ == "__main__":

    start = time.time()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    end = time.time()
    print(end - start)
