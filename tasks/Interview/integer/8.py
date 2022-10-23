# Задание:
# Дана последовательность случайных цифр любой длины и «волшебное» положительное число, больше нуля. 
# Напишите функцию magic(), принимающую эти аргументы, и выясните, можно ли разделить сумму квадратов последовательности на «волшебное» число без остатка. 
# В качестве ответа возвращается «Волшебство случается» в случае успеха или «Никакого волшебства», если разделить нельзя.

# Решение:
# Так как размер последовательности не известен, в качестве «первого» параметра передаем *args, а также обязательный ключевой параметр k.
# Остается найти сумму квадратов при помощи цикла, функции map() или спискового включения и определить, делится ли она без остатка на k.

def magic(*args, k):
   sq_sum = 0
   for i in args:
       sq_sum += i ** 2
   if sq_sum % k == 0:
       return 'Волшебство случается'
   return 'Никакого волшебства'

print(magic(2, 5, 7, k=5))  # Никакого волшебства
print(magic(2, 5, 7, k=39))  # Волшебство случается
print(magic(2, 5, 7, k=2))  # Волшебство случается