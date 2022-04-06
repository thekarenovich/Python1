#1
for i in [1, 2, 3]:
  print(i, end=', ') # 1, 2, 3
  
print()

#2
lst = [1, 2, 3]
for i in range(len(lst)):
  print(f"{i} => {lst[i]}", end=', ') # 0 => 1, 1 => 2, 2 => 3
  
#3
lst = [1, 2, 3]
for i, val in enumerate(lst, start=1):
  print(f"{i} => {val}", end=', ') # 1 => 1, 2 => 2, 3 => 3
