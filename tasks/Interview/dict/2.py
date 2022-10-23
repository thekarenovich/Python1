# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». 

my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(**kwargs)


biggest_dict(k1=22, k2=31, k3=11, k4=91)
biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
print(my_dict)  
# {'first_one': 'we can do it', 'k1': 22, 'k2': 31, 'k3': 11, 'k4': 91, 'name': 'Елена', 'age': 31, 'weight': 61, 'eyes_color': 'grey'}
