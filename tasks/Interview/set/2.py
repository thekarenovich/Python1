# Имеется список с произвольными данными. 
# Поставлена задача преобразовать его в множество. 
# Если какие-то элементы нельзя хешировать, то пропускаем их. 
# Функция list_to_set() выводит на печать получившееся множество.


from collections.abc import Hashable

def list_to_set(lst):
    st = {item for item in lst if isinstance(item, Hashable)}
    print(st)
    

list_to_set([1, [2]])  # {1}
list_to_set([1, [2], 55, 55, {1, 2, 3}, (2, 2), 'string', 5.11])  # {1, 5.11, 'string', 55, (2, 2)}
