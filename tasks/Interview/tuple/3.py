# Перед студентом стоит задача: на вход функции sieve() поступает список целых чисел. 
# В результате выполнения этой функции будет получен кортеж уникальных элементов списка в обратном порядке.

def sieve(lst):
    unique = []
    [unique.append(item) for item in reversed(lst) if item not in unique]
    return tuple(unique)

  
print(sieve([1, 2, 3, 3, 2]))  # (2, 3, 1)
print(sieve([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))  # (0, 2, 9, 5, 1, 3)
print(sieve((1, 2, 3, 4, 5, 6, 7)))  # (7, 6, 5, 4, 3, 2, 1)
