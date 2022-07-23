'''
Timer
Этот класс позволяет контролировать время запуска какого-либо действия. Timer является подклассом Thread.
threading.Timer(interval, function, args=None, kwargs=None)
Таймеры запускаются также, как и потоки, с помощью метода start().
Их можно остановить, используя метод cancel().
С помощью таймера программист может вызывать функцию,
присвоить значение переменной или, например, запустить поток в определенное время.
'''

import threading
import time


def test():
    while True:
        print('test')
        time.sleep(1)


thr = threading.Timer(5, test).start()

for _ in range(6):
    print('111')
    time.sleep(1)

print('finish')
