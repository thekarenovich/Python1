mylist = [1, 3, 6, 10]

a = (x**2 for x in mylist)

print(next(a)) # 1
print(next(a)) # 9
print(next(a)) # 36
print(next(a)) # 100
