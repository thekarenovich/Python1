# Генератор, реализующий последовательность Фибоначи до числа 144
# yield - тот же return, только значения возразает в итератор - объект

def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

for i in fibonacci():
    print(i)
    if i > 100:
        break
