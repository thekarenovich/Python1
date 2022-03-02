def divide(x, y):
    assert y != 0 , 'Нельзя делить на 0' 
    # при невыполнении условия, выбрасывается ошибка
    return round(x/y, 2)

z = divide(21,3)
print(z)

a = divide(21,0)
print(a)
