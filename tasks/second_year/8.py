'''
Реализуйте генератор случайных данных ФИО.
Список распространенных имен позволяется скачать из интернета.
Фамилии необходимо генерировать самостоятельно.
Впрочем, можете попробовать генерировать и имена.

Пример работы генератора:

Данил А. Фуций
Роман Д. Фецачли
Лев Ц. Шолодяк
...
'''

import random
import string 

names = [ 'Артём','Антон','Арсен','Артур','Владимир','Вадим','Виктор','Герман','Григорий','Дмитрий','Давид','Денис','Даниил','Егор','Евгений' ]
middle_names = ['А.','Б.','В.','Г.','Д.','Е.','Э.','К.','А.','Б.','В.','Г.','Д.','Е.','Э.']
last_names = ['','','','','','','','','','','','','','','']


first_letter_glas='АЕЁИОУЫЭЮЯ' #10
first_letter_sogl='БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ' #23
other_letters_glas='яюэыуоиёеа'
other_letters_sogl='ьъщшчцхфтсрпнмлкйзждгвб'


for i in range(15):
    
    #x = random.randint(10,13)
    x = 10

    k = 0 #счётчик
    # чётное - согл, нечётное - глас
    
    if x == 10:
        
        if(k%2!=0):
            z = random.randint(0,10-1)
            last_names[i]+=first_letter_glas[z]
            k+=1
        else:
            z = random.randint(0,23-1)
            last_names[i]+=first_letter_sogl[z]
            k+=1
            
        for j in range(10):
            if k%2!=0:
                y = random.randint(0,10-1)
                last_names[i]+=other_letters_glas[y]
                k+=1
            else:
                y = random.randint(0,23-1)
                last_names[i]+=other_letters_sogl[y]
                k+=1

    
A = 0
B = 14

for i in range(15):
    str1=names[random.randint(A,B)]
    str2=middle_names[random.randint(A,B)]
    str3=last_names[random.randint(A,B)]
    print(str1, ' ', str2, ' ', str3)
    B-=1
    names.remove(str1)
    middle_names.remove(str2)
    last_names.remove(str3)

