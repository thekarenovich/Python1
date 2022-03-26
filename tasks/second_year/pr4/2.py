class Class:

    def __init__(self):
        self.name = "c200"
        self.make = "mercedez"
        self.model = 2008

    def start(self):
        print("START")

    def summ(self, value=2008):
        print(2 + value)

obj = Class()

# вывод атрибутов
#print('Atributes: ', vars(obj))
print('Atributes: ', obj.__dict__) 

# запуск метода
str_method = input('Method Name: ')
if(str_method == "start"):
    obj.start()
elif(str_method == "summ"):
    obj.summ(obj.model)

