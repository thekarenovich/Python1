# Задача:
# Напишите функцию dislike_6(a), которая всегда возвращает True, если только не передается число 6 типа int или типа float (в данном случае она вернет «Только не 6!»).

# Решение:
# Вначале проверяем, является ли аргумент целым или вещественным числом. Если это так и он равен 6 или 6.0, то вернем «Только не 6!» Во всех остальных случаях результат представлен в виде True.

def dislike_6(a):
    if (type(a) is float or type(a) is int) and a == 6.0:
        return 'Только не 6!'
    return True

print(dislike_6(6.0))  # Только не 6!
print(dislike_6(6))  # Только не 6!
print(dislike_6('6'))  # True
print(dislike_6('Хорошо'))  # True
print(dislike_6([6, 6]))  # True