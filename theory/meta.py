#coding=utf-8

#Метапрограммирование — вид программирования, связанный с созданием программ, 
#которые порождают другие программы как результат своей работы
#1
'''
def first(msg):
	print(msg)

first('Hello')

second = first
second('Hello')
'''
#Hello
#Hello


#2
#Функция может быть аргументом
'''
def inc(x):
	return x + 1

def dec(x):
	return x - 1

def operate(func, x):
	result = func(x)
	return result

print(operate(inc, 3)) #4
print(operate(dec, 3)) #2
'''


#3
#Функция модет возвращать функцию
'''
def is_called():
	def is_returned():
		print('Hello')
	return is_returned 

new = is_called()
new()
'''
#Hello


#4
#В самом простом смысле, Декоратор - вызываемый объект, который возвращает вызываемый объект
#Декоратор можно представить в виде обёртки для подарка
#Он делает его более красивым, но суть подарка не меняется
'''
def make_pretty(func):
	def inner():
		print('I got decorated')
		func()
	return inner

def ordinary():
	print('I am ordinary')

ordinary()
pretty = make_pretty(ordinary)
pretty()
'''
#I am ordinary
#I got decorated
#I am ordinary


#5
'''
def make_pretty(func):
	def inner():
		print('I got decorated')
		func()
	return inner

@make_pretty
def ordinary():
	print('I am ordinary')

ordinary()
'''
#I got decorated
#I am ordinary

#6
'''
def smart_divide(func):
	def inner(a, b):
		print('I am going to divide', a, 'and', b)
		if b == 0:
			print('Whoops! Cannot divide')
			return

		return func(a, b)
	return inner

@smart_divide
def divide(a, b):
	print(a/b)

divide(2, 5)
#('I am going to divide', 2, 'and', 5)
#0

divide(2, 0)
#('I am going to divide', 2, 'and', 0)
#Whoops! Cannot divide
'''

#7
#Если декораторов несколько, то они накладываются друг на друга
#Сверху вниз, как в примере с обёрткой с ещё одной обёрткой и подарком
#Выполняется star затем percent и наконец printer
'''
def star(func):
	def inner(*args, **kwargs):
		print('*' * 10)
		func(*args, **kwargs)
		print('*' * 10)
	return inner

def percent(func):
	def inner(*args, **kwargs):
		print('%' * 10)
		func(*args, **kwargs)
		print('%' * 10)
	return inner

@star
@percent
def printer(msg):
	print(msg)

printer('Hello')
'''
#******************************
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Hello
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#******************************