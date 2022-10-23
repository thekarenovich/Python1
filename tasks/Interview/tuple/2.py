# Функция slicer() на вход принимает кортеж и случайный элемент. 
# Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.

def slicer(any_tuple, element):
    if element in any_tuple:
        if any_tuple.count(element) > 1:
            first_index = any_tuple.index(element)
            second_index = any_tuple.index(element, first_index + 1) + 1
            return any_tuple[first_index:second_index]
        else:
            return any_tuple[any_tuple.index(element):]
    else:
        return ()
      
      
print(slicer((1, 2, 3), 8))  # ()
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))  # (8, 3, 4, 8)
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))  # (8, 5, 1, 2, 9)
