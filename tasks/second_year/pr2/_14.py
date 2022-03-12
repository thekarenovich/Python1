
# Имеем 5 кортежей, в каждом из которых 4 элемента, значит у нас будет 4 новых списка, с которыми мы будем работать
# В 0-ом кортеже будут все элементы из списков с индексом 0, 1 - 1, 2 - 2, 3 - 3
# В каждом списке находим максимальной длины строку 
# Длина полоски, состоящей из дефисов, зависит от длины максимальной строки из каждого списка
# Каждый список выводится вертикально 

from pprint import pprint

sh_ip_int_br = [
('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
('Loopback0',       '10.1.1.1', 'up', 'up'),
('Loopback100',     '100.0.0.1', 'up', 'up')
]

sh_ip_int_br1 = []
for item in range(len(sh_ip_int_br)):
   sh_ip_int_br1.append(list(sh_ip_int_br[item]))
sh_ip_int_br = sh_ip_int_br1


lists = [] # список новых списков
maxs = [] # максимумы новых списков
for item in range(len(sh_ip_int_br[0])): # проход по кортежам (индексы кортежей)
   lists.append([])
   maxs.append('')

for item in range(len(sh_ip_int_br)): # проход по кортежам (индексы кортежей)
   for item1 in range(len(sh_ip_int_br[item])): # проход по элементам кортежа (индексы элементов)
         lists[item1].append(sh_ip_int_br[item][item1])

'''
Список новых списков
lists = [
 ['FastEthernet0/0', 'FastEthernet0/1', 'FastEthernet0/2', 'Loopback0', 'Loopback100'],
 ['15.0.15.1', '10.0.12.1', '10.0.13.1', '10.1.1.1', '100.0.0.1'],
 ['up', 'up', 'up', 'up', 'up'],
 ['up', 'up', 'up', 'up', 'up']
]'''

for item in range(len(lists)):
      maxs[item] = len(max(lists[item], key=len))

for item in range(len(maxs)):
   for item1 in range(maxs[item]):
      print('-', end='')
   print(' ', end='')

print()

for item in range(len(sh_ip_int_br)):
   for item1 in range(len(sh_ip_int_br[item])):
      if(len(sh_ip_int_br[item][item1]) < maxs[item1]):
         while(len(sh_ip_int_br[item][item1]) < maxs[item1]):
            sh_ip_int_br[item][item1] += ' '
      print(sh_ip_int_br[item][item1], end=' ')

   print()

for item in range(len(maxs)):
   for item1 in range(maxs[item]):
      print('-', end='')
   print(' ', end='')

print()

'''
---------------  ---------  --  --
FastEthernet0/0  15.0.15.1  up  up
FastEthernet0/1  10.0.12.1  up  up
FastEthernet0/2  10.0.13.1  up  up
Loopback0        10.1.1.1   up  up
Loopback100      100.0.0.1  up  up
---------------  ---------  --  --
'''
