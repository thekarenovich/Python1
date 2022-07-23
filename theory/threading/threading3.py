import threading


locker = threading.RLock()


def inc_value():
    print(1)
    locker.acquire()
    print(2)

# При Lock
# t1 = threading.Thread(target=inc_value()).start()  # напечатается 1 и 2
# t2 = threading.Thread(target=inc_value()).start()  # напечатается лишь 1, ибо уже заблокировано

# При RLock
t1 = threading.Thread(target=inc_value()).start()  # напечатается 1 и 2
t2 = threading.Thread(target=inc_value()).start()  # напечатается 1 и 2
