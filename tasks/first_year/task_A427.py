# Написать функцию split_and_add(arr, n), на вход которой приходит список чисел arr и количество итераций
# выполнения n. На каждой итерации необходимо делить спсиок на два и возвращать список поэлементных сумм.
#
# Пример:
# split_and_add([1,2,3,4,5], 2)
# итерация 1                             итерация 2
# разбиение [1,2] и [3,4,5]              разбиение [3] и [5,7]
# сумма +   [1,2]                        сумма +   [3]
#         [3,4,5]                                [5,7]
#       = [3,5,7]                              = [5,10] (ответ)



import traceback


def split_and_add(arr,n) :

    h = arr.copy()

    b = len(h) // 2

    for i in range(n):

        c = []

        c = h[:b]

        d = []

        d = h[b:]

        h = d.copy()

        c.reverse()

        d.reverse()

        h.reverse()

        for g in range(min(len(c), len(d))):

            t = c[g] + d[g]

            h[g] = t

        h.reverse()

        b //=2

        if b == 0:

            b = 1
    
    return h


# Тесты
try:
    assert split_and_add([1,2,3,4,5], 2) == [5,10]
    assert split_and_add([1,2,3,4,5], 3) == [15]
    assert split_and_add([32,45,43,23,54,23,54,34], 2) == [183, 125]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
