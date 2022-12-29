# from 10 to any 
def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result
    
print(convert_to(123, 2))
print(convert_to(123, 8))
print(convert_to(123, 16))
print(convert_to(123, 32, upper=True))
print(convert_to(123, 64))

# from any to 10
number = '11001'
result = int(number, 2)
print(result)

number = '12367'
result = int(number, 8)
print(result)

number = '123f'
result = int(number, 16)
print(result)

number = '123z'
result = int(number, 36)
print(result)
