# map принимает два аргумента: функцию и аргумент составного типа данных (список).

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print (new_list)  # [1, 2, 3, 4, 5, 6, 7]

# Его алгоритмическая альтернатива:
# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = []
# for item in old_list:
#     new_list.append(int(item))
# print (new_list)

# И еще пару примеров:

def miles_to_kilometers(num_miles):
    return num_miles * 1.6

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print (kilometer_distances)  # [1.6, 10.4, 27.84, 3.84, 14.4]


new_list = list(map(lambda x,y: x + y, [1,2,3], [4,5,6]))
print (new_list)  # [5, 7, 9]
