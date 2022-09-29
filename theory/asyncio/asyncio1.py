import asyncio
from time import time
# from time import sleep
 
# синхронный код: время выполнения примерно 9 сек.
# aсинхронный код: время выполнения примерно 3 сек.
# Функции, написанные с помощью async, вызываются через await
start = time()

'''
def spider(site_name):
    for page in range(1, 4):
        sleep(1)
        print(site_name, page)


spider("Blog")
spider("News")
spider("Forum")
'''


async def spider(site_name):
    for page in range(1, 4):
        await asyncio.sleep(1)  # как sleep, только для асинх.
        print(site_name, page)
    return 'Well Done. by {}'.format(site_name)


spiders = [
    asyncio.ensure_future(spider("Blog")),  # гарантирует выполнение в будущем
    asyncio.ensure_future(spider("News")),
    asyncio.ensure_future(spider("Forum"))
]

event_loop = asyncio.get_event_loop()  # получение цикла событий
result = event_loop.run_until_complete(asyncio.gather(*spiders))
# ['Well Done. by Blog', 'Well Done. by News', 'Well Done. by Forum']
# выполняется, пока не все сопрограммы(корутины) не выполнятся, т.к. указали *, т.е. все
print(result)
event_loop.close()  # завершение цикла

'''
result = event_loop.run_until_complete(asyncio.gather(spider('API')))
Если сделать так, скажем, то программа также будет работать, но в списке информация будет лишь о 'API'
К тому же, если API закончит быстрее остальных, то все закончится, остальные не успеют завершить все 
'''

end = time()
print(end - start)

'''
Мы хотим вывести все комбинации строк и цифр
Однако стоит заметить, чтобы это сделать, нужно ждать каждую строку пару секунд больше для каждой цифры
А если выводить не по очереди, а скажем, все строки будут брать по цифре, а затем ждать, а не ждать, чтобы 
Каждый мог взять все три цифры, а затем с ожиданиями брать свои три
'''
