# Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.

def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst

print(list_sort([1, 5, 77]))  # [77, 5, 1]
print(list_sort([19, 8.3, -4, 11, 0, 5]))  # [19, 11, 8.3, 5, -4, 0]
print(list_sort([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))  # [55, -33, 13.12, 11.2, 7.1, -4.18, -0.05]
