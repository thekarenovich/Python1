# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.



carss =[{'number':123456,'model':'bmw', 'release': 2021},
        {'number':7891011,'model':'mers', 'release': 2022},
        {'number':200202, 'model':'tesla', 'release': 2020},
        {'number':369963, 'model':'shkoda', 'release': 2019},
        {'number':515151, 'model':'renault', 'release': 2023},
        {'number':100100, 'model':'bmw', 'release': 2001},
        {'number':200200, 'model':'mers', 'release': 2002},
        {'number':300300, 'model':'tesla', 'release': 2003},
        {'number':400400, 'model':'shkoda', 'release': 2004},
        {'number':500500, 'model':'renault', 'release': 2005}]


def A(carss) :
    for i in range(len(carss)):
        print(carss[i])
        print()



def B(carss) :
    n=int(input())
    t=False
    for i in range(len(carss)):
        if(carss[i]['number']==n):
            print()
            print(carss[i]['number'])
            print(carss[i]['model'])
            print(carss[i]['release'])
            print()
            t=True
            break
    if(t==False):
        print("Нет такой машины")



def C(carss) :
    y=int(input())
    k=0
    for i in range(len(carss)):
        if(carss[i]['release']>y):
            k+=1
    print(k)



def D(carss) :
    n=int(input())
    for i in range(len(carss)):
        if(carss[i]['number']==n):
            print("Придумайте номер машины: ")
            carss[i]['number']=int(input())
            n=carss[i]['number']
            print("Выберите марку машины: ")
            carss[i]['model']=input()
            print("Какого она года?")
            carss[i]['release']=int(input())
            break
    for i in range(len(carss)):
        if(carss[i]['number']==n):
            print("Теперь номер машины - ",carss[i]['number'])
            print("Теперь модель машины - ",carss[i]['model'])
            print("Теперь год релиза машины - ",carss[i]['release'])
            break
        


def E(carss) :
    n=int(input())
    for i in range(len(carss)):
        if(carss[i]['number']==n):
            carss.pop(i)
            break
    
    for i in range(len(carss)):
        print(carss[i])
        print()



#A(carss)

#B(carss)

#C(carss)

#D(carss)

#E(carss)
