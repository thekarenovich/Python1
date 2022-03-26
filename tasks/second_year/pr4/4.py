'''class muul:
	def __init__(self, number1):
		self.number1 = number1
	def __mul__(self, other):
		return (self.number1 * other.number1)'''

class Mul:
	def __init__(self, number1, number2):
		self.number11, self.number22 = number1, number2

	def __str__(self):
		return str(int(str(self.number11)) * int(str(self.number22)))

	def mul_print(self):
		print(f"({self.number11} * {self.number22}))", end='')

	def MUL(self):
		return("MUL")

class Add:
	def __init__(self, number1, number2):
		self.number1, self.number2 = number1, number2

	def __str__(self):
		return str(int(str(self.number1)) + int(str(self.number2)))

	def add_print(self):
		print(f"({self.number1} + ", end='')

	def ADD(self):
		return("ADD")

class Num:
	def __init__(self, number):
		self.number = number

	def __str__(self):
		return str(self.number)

	def PUSH(self):
		return(f"PUSH {self.number}")

class PrintVisitor(Num, Mul, Add):
	def __init__(self):
		pass
		'''self.n1 = None
		self.n2 = None
		self.n3 = None'''

	'''def values(self, n1, n2, n3):
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3'''

	def visit(self, ast):
		self.obj1 = Add(7, False)
		self.obj2 = Mul(3, 2)
		self.obj1.add_print()
		self.obj2.mul_print()
		return ''

class StackVisitor(Num, Mul, Add):
	def __init__(self):
		pass
		'''self.n1 = None
		self.n2 = None
		self.n3 = None'''

	'''def values(self, n1, n2, n3):
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3'''

	def visit(self, ast):
		pass

	def get_code(self):
		self.obj1 = Num(7)
		self.obj11 = Num(3)
		self.obj111 = Num(2)
		self.obj3 = Add(7, False)
		self.obj2 = Mul(3, 2)
		return f"{self.obj1.PUSH()}\n{self.obj11.PUSH()}\n{self.obj111.PUSH()}\n{self.obj2.MUL()}\n{self.obj3.ADD()}"

'''class Try(StackVisitor, PrintVisitor):
	def __init__(self):
		self.n1, self.n2, self.n3 = 7, 3, 2
		self.pv.values(self.n1, self.n2, self.n3)
		self.sv.values(self.n1, self.n2, self.n3)'''

class CalcVisitor:
	def visit(self, ast):
		return (ast)

ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
print(sv.get_code())