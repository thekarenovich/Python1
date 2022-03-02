def divide(x, y):
    assert y != 0 , 'Нельзя делить на 0' 
    # при невыполнении условия, выбрасывается ошибка
    return round(x/y, 2)

z = divide(21,3)
print(z)

a = divide(21,0)
print(a)

'''
Метод	                     Проверка на	

assertEqual(x, y)	         x == y	

assertNotEqual(x, y)	     x != y	

assertTrue(x)	             bool(x) равно True	

assertFalse(x)	             bool(x) равно False	

assertIs(x, y)	             x это y	

assertIsNot(x, y)	         x это не y	

assertIsNone(x)	             x это None	

assertIsNotNone(x)	         x это не None	

assertIn(x, y)	             x в y	

assertNotIn(x, y)	         x не в y	

assertIsInstance(x, y)	     isinstance(x, y)	

assertNotIsInstance(x,y)	 не isinstance(x, y)	
'''
