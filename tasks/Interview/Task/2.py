# Задан массив из чисел a1... aN, требуется найти границы его строго монотонного подотрезка максимальной длины. Если их несколько, вывести границы любого.
# Примеры:
# 1) ввод: -3, 2, 3, 4, 5, 6, 7, 7, 8
# вывод: 0, 6
# 2) ввод: -1, -1, -1, -1, -1, -1, -1, -1, -1
# вывод: 0, 0 (или другой индекс: i, i)


def function(array):
    quantity_dictionary = {}
    quantity = 1
    first_index = 0

    for index in range(1, len(array)):
        if array[index] > array[index - 1]:
            quantity += 1
            if index == (len(array) - 1):
                last_index = index - 1
                quantity_dictionary[quantity] = [first_index, last_index]
        else:
            last_index = index - 1
            quantity_dictionary[quantity] = [first_index, last_index]
            quantity = 1
            first_index = index

    if quantity_dictionary[max(quantity_dictionary)][0] == quantity_dictionary[max(quantity_dictionary)][1]:
        return 0, 0

    return quantity_dictionary[max(quantity_dictionary)][0], quantity_dictionary[max(quantity_dictionary)][1]


def test():
    assert function([-3, 2, 3, 4, 5, 6, 7, 7, 8]) == (0, 6), 'Error1'
    assert function([-1, -1, -1, -1, -1, -1, -1, -1, -1]) == (0, 0), 'Error2'

test()
