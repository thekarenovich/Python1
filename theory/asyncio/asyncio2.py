# Альтернатива файлу asyncio1.py

import asyncio
import time

start = time.time()


async def execute(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)  # как sleep, только для асинх.
        print(site_name, page)
    return 'Well Done. by {}'.format(site_name)


async def main():
    task1 = asyncio.create_task(
        execute('Blog'))  # создание задачи для вызова функции execute

    task2 = asyncio.create_task(
        execute('News'))

    task3 = asyncio.create_task(
        execute('Forum'))

    await task1  # вызов
    await task2
    await task3


asyncio.run(main())  # запсук

end = time.time()
print(end - start)
