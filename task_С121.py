"""
Каждый класс реализовать в отдельном модуле, импортируя их в производные модули.
Создать класс Car с полями марка, мощность, год производства. Добавить конструктор класса.
Создать производный от Car класс PassengerCar. Новые поля: количество пассажиров, ремонтная книжка
    (словарь  запчасти: год замены). Определить конструктор, с вызовом родительского конструктора.
    Определить функции добавления заменённой запчасти в ремонтную книжку, получения года замены по названию,
    форматированной печати всей ремонтной книжки. 
    Переопределить метод преобразования в строку для печати
    основной информации (марка, мощность, год производства, количество пассажиров).
Создать производный от Car класс Truck. Новые поля: максимальная грузоподъемность, ФИ водителя, текущий груз
    (словарь  название товара: вес). Определить конструктор, с вызовом родительского конструктора.
    Определить функции изменения водителя, добавления и удаления груза, форматированной печати текущего груза.
    Переопределить метод преобразования в строку для печати основной информации (марка, мощность, год производства,
    максимальная грузоподъемность, ФИ водителя).
Создать класс Autopark. Поля: название автопарка, список легковых машин (список экземпляров класса PassengerCar),
    список грузовиков (список экземпляров класса Truck). Определить конструктор. Переопределить метод
    преобразования в строку для печати всей информации об автопарке (с использованием переопределения в классах
    PassengerCar и Truck). Переопределить методы получения количества грузовиков функцией len, получения грузовой
    машины по индексу, ИЗМЕНЕНИЯ ПО ИНДЕКСУ, удаления по индексу 
    (пусть номера у грузовых машин считаются с 1,
    а индекс 0 – список всех легковых машин). 
    Переопределить операции + и - для добавления или удаления грузовой
    машины(по значению). 
    Добавить функцию создания txt-файла и записи всей информации в него (в том числе ремонтных
    книжек и списка грузов).
    Предусмотреть хотя бы в 3 местах обработку возможных исключений.
В каждом модуле провести подробное тестирование всех создаваемых объектов и функций.
"""

#from D1 import log
from datetime import datetime, date, time

def log(key,info):
    f = open("text.txt","a")
    if key == "CRE":
        a = ("{} --- {} --- {} {} {}\n".format("CRE",datetime.now(),"Экземпляр класс", info,"создан"))
        f.write(a)
    if key == "INF":
        b = ("{} --- {} --- {} {}\n".format("INF",datetime.now(),"Изменено",info))
        f.write(b)
    if key == "PRI":
        c = ("{} --- {} --- {} {}\n".format("PRI",datetime.now(),"Напечатано",info))
        f.write(c)
    if key == "ERR":
        d = ("{} --- {} --- {} {}\n".format("ERR",datetime.now(),"Ошибка",info))
        f.write(d)
    if key == "DEL":
        e = ("{} --- {} --- {} {}\n".format("DEL",datetime.now(),"Удален",info))
        f.write(e)
    f.close()


class Car:
    mark='' # марка 
    power=None # мощность 
    year_production=None # год производства 
    def __init__(self, mark, power, year_production):
        self.mark = mark
        self.power = power
        self.year_production=year_production

class PassengerCar(Car):
    
    quantity_passengers=None # количество пассажиров
    book={} # рем. книжка (name_part:year_replace_part)
    
    def __init__(self, mark, power, year_production, quantity_passengers, book):
        Car.__init__(self, mark, power, year_production)
        self.quantity_passengers = quantity_passengers
        self.book = book

        log("CRE","obj_pc1")
        #log("CRE","obj_pc2")

    
    def edit_book(self, name_part, year_replace_part):
    	self.book[name_part]=year_replace_part

    	log("INF","book")
    	
    def find_year(self, name_part, book):
        if name_part in book:
            print(f"Её год:{book[name_part]}")
            log("PRI","name_part")
        else:
            return "Такой запчасти нет"
    def output_book(self):
        for name_part in self.book:
            print("Деталь {} была добавлена в {}".format(name_part, self.book[name_part]))
            
        log("PRI","book")
        
    def __str__(self):
        print(f'Марка - {self.mark}.\nМощность - {self.power}.\nГод выхода - {self.year_production}.\nМашина может вмещать в себя {self.quantity_passengers} человека.')

    

class Truck(Car):
    mx=None # макс. грузоподъёмность 
    driver=None # ФИ водителя
    current_product={} # текущий груз (name_part:weight)
    def __init__(self, mark, power, year_production, mx, driver, current_product):
        Car.__init__(self, mark, power, year_production)
        self.mx = mx
        self.driver=driver
        self.current_product=current_product

        log("CRE", "obj_t1")
        #log("CRE", "obj_t2")
        
    def change_driver(self, driver):
        self.driver=driver

        log("INF", "driver")
        
    def plus_current_product(self, name_part, weight):
        self.current_product[name_part]=weight

        log("INF", "current_product")
        
    def minus_current_product(self, name_part):
        if name_part in current_product:
            del self.current_product[name_part]
            log("DEL", "name_part")
        else:
            print("Такой запчасти нет")
    def __str__(self):
        return 'Марка - {}.\nМощность - {}.\nГод выхода - {}.\nОно может держать {} кг.\nВодитель - {}.'.format(self.mark,self.power,self.year_production,self.mx,self.driver)





class Autopark:
    name_autopark=''
    list_pc=[]
    list_t=[]

    log("CRE","obj_ap1")
    
    def __init__(self, name_autopark, list_pc, list_t):
        self.name_autopark=name_autopark
        self.list_pc=list_pc
        self.list_t=list_t

    def get_quantity_trucks(self,list_t):
        self.list_t=list_t
        print(len(self.list_t))
        
        log("PRI","len(list_t)")
        
    def get(self, index):
        if index==0:
            i=int(input("0? Тогда введите индекс лег. машины:"))
            return(self.list_pc[i-1])

            log("PRI","list_pc[i-1]")
            
        else:
            return(self.list_t[index-1])
            
            log("PRI","list_t[index-1]")
            
    def delete(self, index):
        if index==0:
            i=int(input("0? Тогда введите индекс лег. машины:"))
            self.list_pc.pop(i-1)

            log("DEL","list_pc")
        else:
            self.list_t.pop(index-1)

            log("DEL","list_t")
            
    def change(self, index):
        if index==0:
            i=int(input("0? Тогда введите индекс лег. машины:"))
            mark=input("Введите марку лег.машины: ")
            power=int(input("Введите мощность лег.машины: "))
            year_production=int(input("Введите год выхода лег.машины: "))
            quantity_passengers=int(input("Введите количество пассажиров в лег.машине: "))
            book_1={}
            part=input("Введите деталь лег.машины для ремонтной книжки: ")
            year_part=int(input("Введите год добавления детали лег.машины для ремонтной книжки: "))
            book_1[part]=year_part
            list_pc[i-1]=PassengerCar(mark, power, year_production, quantity_passengers, book_1)
            
            log("INF","list_pc[i-1]")
            
        else:
            mark=input("Введите марку грузовика: ")
            power=int(input("Введите мощность грузовика: "))
            year_production=int(input("Введите год производства грузовика: "))
            mx=int(input("Введите макс. грузоподъёмность грузовика: "))
            driver=input("Введите имя и фамилию водителя грузовика: ")
            current_product={}
            part=input("Введите название текущего груза: ") 
            weight=int(input("Введите вес текущего груза: "))
            current_product[part]=weight
            list_t[index-1]=Truck(mark, power, year_production, mx, driver, current_product)

            log("INF","list_pc[i-1]")
            
    def __add__(self, var):
        self.list_t.append(var)
    def __sub__(self, var): 
        for i in range(len(self.list_t)):
            b=True
            if self.list_t[i].mark!=var.mark:
                b=False
            if self.list_t[i].power!=var.power:
                b=False
            if self.list_t[i].year_production!=var.year_production:
                b=False
            if self.list_t[i].driver!=var.driver:
                b=False
            if self.list_t[i].mx!=var.mx:
                b=False
            if self.list_t[i].current_product!=var.current_product:
                b=False
            if (b==True):
                self.list_t.pop(i)
                break
        if not b:
            print("Нет такой груз.машины")

        '''def __str__(self): 
            string="Name of autopark is "+self.name+"\n"
            for i in range(len(self.list_pc)):
                string+="Passenger car №"+str(i+1)+"\n"
                string+=str(self.list_pc[i])
                string+="\n"
            for i in range(len(self.list_t)):
                string+="Truck №"+str(i+1)+"\n"
                string+=str(self.list_t[i])
                string+="\n"
            return string'''

    def file(self):
            file=open(f"{self.name_autopark}.txt", "w")
            file.write("Название АвтоПарка "+self.name_autopark+"\n")
            for i in range(len(self.list_pc)):
                file.write("Лег.машина №"+str(i+1)+"\n")
                file.write(str(self.list_pc[i]))
                file.write("\n")
                file.write("Ремонтная книжка:")
                for key in self.list_pc[i].book:
                    file.write('Деталь {0} была добавлена в {1}.\n'.format(key, self.list_pc[i].book[key]))
            for i in range(len(self.list_t)):
                file.write("Груз.машина №"+str(i+1)+"\n")
                file.write(str(self.list_t[i]))
                file.write("\n")
                file.write("Текущий груз:\n")
                for key in self.list_t[i].current_product:
                    file.write('{0} кг - вес груза {1}.\n'.format(self.list_t[i].current_product[key],key))
            file.close()



#   !-* * * * * (THIS IS MAIN, BODY) * * * * *-!

print("Приветствую в задании части С")
print("Интерфейс для удобства делится на несколько частей")

# CLASS PASSENGERCAR
list_pc=[]
print()
print("(1)")
print("Работаем с легковыми машинами")
print("Ниже сделаем два экземпляра")
mark=input("Введите марку лег.машины: ")

try:
    power=int(input("Введите мощность лег.машины: "))
except ValueError:
    print("Надо ввести значение типа int")
    power=int(input("Введите мощность лег.машины: "))
    
try:
    year_production=int(input("Введите год выхода лег.машины: "))
except ValueError:
    print("Надо ввести значение типа int")
    year_production=int(input("Введите год выхода лег.машины: "))
    
try:
    quantity_passengers=int(input("Введите количество пассажиров в лег.машине: "))
except ValueError:
    print("Надо ввести значение типа int")
    quantity_passengers=int(input("Введите количество пассажиров в лег.машине: "))
    
book_1={}
part=input("Введите деталь лег.машины для ремонтной книжки: ")

try:
    year_part=int(input("Введите год добавления детали лег.машины для ремонтной книжки: "))
except ValueError:
    print("Надо ввести значение типа int")
    year_part=int(input("Введите год добавления детали лег.машины для ремонтной книжки: "))
    
book_1[part]=year_part
obj_pc1=PassengerCar(mark, power, year_production, quantity_passengers, book_1)
part=input("Введите доп.деталь лег.машины для ремонтной книжки: ")

try:
    year_part=int(input("Введите год добавления доп. детали лег.машины для ремонтной книжки: "))
except ValueError:
    print("Надо ввести значение типа int")
    year_part=int(input("Введите год добавления доп. детали лег.машины для ремонтной книжки: "))
    
obj_pc1.edit_book(part, year_part)
part=input("Введите деталь, год которой хотите узнать: ")
print(obj_pc1.find_year(part, book_1))
print("Вся информация о лег.машине:")
obj_pc1.output_book()
print(obj_pc1.__str__())
list_pc.append(obj_pc1)

'''
print("И давайте сделаем ещё одну лег.машину")
mark=input("Введите марку лег.машины: ")
power=int(input("Введите мощность лег.машины: "))
year_production=int(input("Введите год выхода лег.машины: "))
quantity_passengers=int(input("Введите количество пассажиров в лег.машине: "))
book_1={}
part=input("Введите деталь лег.машины для ремонтной книжки: ")
year_part=int(input("Введите год добавления детали лег.машины для ремонтной книжки: "))
book_1[part]=year_part
obj_pc2=PassengerCar(mark, power, year_production, quantity_passengers, book_1)
part=input("Введите доп.деталь лег.машины для ремонтной книжки: ")
year_part=int(input("Введите год добавления доп. детали лег.машины для ремонтной книжки: "))
obj_pc2.edit_book(part, year_part)
part=input("Введите деталь, год которой хотите узнать: ")
obj_pc2.find_year(part, book_1)
print("Вся информация о лег.машине:")
obj_pc2.output_book()
obj_pc2.__str__()
list_pc.append(obj_pc2)
'''

#book_1 = {"part1":2002, "part2":2014}
#obj_pc1=PassengerCar("Mers", 700, 2002, 4, book_1)
#obj_pc1.edit_book("part3", 2019)
#obj_pc1.find_year("part3", book_1)
#list_pc.append(obj_pc1)


# CLASS TRUCK
list_t=[]
print()
print("(2)")
print("А теперь работаем с груз. машинами")
print("Ниже сделаем два экземпляра")
mark=input("Введите марку груз. машины: ")

try:
    power=power=int(input("Введите мощность груз. машины: "))
except ValueError:
    print("Надо ввести значение типа int")
    power=power=int(input("Введите мощность груз. машины: "))
    
    log("ERR","power")
    
try:
    year_production=int(input("Введите год выхода груз. машины: "))
except ValueError:
    print("Надо ввести значение типа int")
    year_production=int(input("Введите год выхода груз. машины: "))
    
    log("ERR","year_production")
    
try:
    mx=int(input("Введите макс. грузоподъёмность груз. машины: "))
except ValueError:
    print("Надо ввести значение типа int")
    mx=int(input("Введите макс. грузоподъёмность груз. машины: "))

    log("ERR","mx")
    
driver=input("Введите имя и фамилию владельца груз. машины: ")
part=input("Введите деталь текущего груза груз.машины: ")

try:
    weight=int(input("Введите вес детали текущего груза груз.машины: "))
except ValueError:
    print("Надо ввести значение типа int")
    weight=int(input("Введите вес детали текущего груза груз.машины: "))

    log("ERR","weight")
    
current_product={}
current_product[part]=weight
obj_t1=Truck(mark, power, year_production, mx, driver, current_product)
driver=input("Введите имя и фамилию нового владельца груз. машины: ")
obj_t1.change_driver(driver)
part=input("Введите доп.деталь текущего груза груз.машины: ")

try:
    weight=int(input("Введите вес доп.детали текущего груза груз.машины: "))
except ValueError:
    print("Надо ввести значение типа int")
    weight=int(input("Введите вес доп.детали текущего груза груз.машины: "))
    
obj_t1.plus_current_product(part,weight)
part=input("Введите деталь текущего груза груз.машины, которую хотите убрать: ")
obj_t1.minus_current_product(part)
print("Вся информация о груз. машине:")
print(obj_t1.__str__())
list_t.append(obj_t1)

'''
print("И давайте сделаем ещё одну груз.машину")
mark=input("Введите марку груз. машины: ")
power=int(input("Введите мощность груз. машины: "))
year_production=int(input("Введите год выхода груз. машины: "))
mx=int(input("Введите макс. грузоподъёмность груз. машины: "))
driver=input("Введите имя и фамилию владельца груз. машины: ")
part=input("Введите деталь текущего груза груз.машины: ")
weight=int(input("Введите вес детали текущего груза груз.машины: "))
current_product={}
current_product[part]=weight
obj_t2=Truck(mark, power, year_production, mx, driver, current_product)
driver=input("Введите имя и фамилию нового владельца груз. машины: ")
obj_t2.change_driver(driver)
part=input("Введите доп.деталь текущего груза груз.машины: ")
weight=int(input("Введите вес доп.детали текущего груза груз.машины: "))
obj_t2.plus_current_product(part,weight)
part=input("Введите деталь текущего груза груз.машины, которую хотите убрать: ")
obj_t2.minus_current_product(part)
print("Вся информация о груз. машине:")
print(obj_t2.__str__())
list_t.append(obj_t2)
'''

#current_product = {"part11":2055}
#obj_t1=Truck("Ford", 50505, 2020, 10000, "Ivan Ivanov", current_product)
#obj_t1.change_driver("Katya Ivanova")
#obj_t1.plus_current_product("part22", 1010)
#obj_t1.minus_current_product("part22")
#list_t.append(obj_t1)


# CLASS AUTOPARK
print()
print("(3)")
print("Теперь работаем с самим автопарком после создания машин")
name_park=input("Введите название автопарка:")
obj_ap1=Autopark(name_park, list_pc, list_t)
print("Количество груз.машин в автопарке:", end=' ')
obj_ap1.get_quantity_trucks(list_t)
print("Индексация у груз. машин с 1, 0 - список лег. машин")

try:
    indexx=int(input("Введите индекс машины, которой хотите получить: "))
except ValueError:
    print("Надо ввести значение типа int")
    indexx=int(input("Введите индекс машины, которой хотите получить: "))

#print(obj_ap1.get(indexx))

try:
    indexx=int(input("Введите индекс машины, которую хотите удалить: "))
except ValueError:
    print("Надо ввести значение типа int")
    indexx=int(input("Введите индекс машины, которую хотите удалить: "))
    
obj_ap1.delete(indexx)

try:
    indexx=int(input("Введите индекс машины, информацию которой хотите изменить: "))
except ValueError:
    print("Надо ввести значение типа int")
    indexx=int(input("Введите индекс машины, информацию которой хотите изменить: "))
    
obj_ap1.change(indexx)
obj_ap1+Truck("Honda", 1000, 2000, 1000, "Ivanov Ivan", current_product={"ppp":222})
obj_ap1-Truck("Honda", 1000, 2000, 1000, "Ivanov Ivan", current_product={"ppp":222})
print(obj_ap1.__str__())
obj_ap1.file()

'''obj_t2=Truck("Mersiccc", 505, 2100, 13212, "IIvanaa IIvanovaa", current_product)'''

'''
obj_1=Autopark()
plus_value=[obj_1]
plus_value=set(plus_value)
list_t=set(list_t)
C = list_t + plus_value
C=list(C)
obj_2=Autopark()
minus_value=[obj_2]
minus_value=set(minus_value)
list_t=set(list_t)
D = list_t - minus_value
D=list(D)
'''
















