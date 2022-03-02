'''
#1
s = 'ABCDBCA' 
table = s.maketrans({ord('A'): 'a', ord('B'): 'b'}) #задали таблицу перевода
print(s.translate(table)) #перевод строки s по таблице

#Выход: abCDbCa
'''

#если аргументов более 1, то 1й и 2Й аргументы должны быть одинаковой длины

#на заметку, строки-аргументы - лишь перечисление символов, с которыми работаем
#то есть, работаем не с самой строкой

'''
#2
s = 'ABCDBCA' 
table1 = s.maketrans('A', 'a') 
#В s A заменяется на а
print(s.translate(table1)) 
table2 = s.maketrans('ABCD', 'abcd') 
#В строке s A заменяется на а, B - на b, C - на с, D - на d
print(s.translate(table2))

#Выход: 
#aBCDBCa 
#abcdbca
'''


'''
#3
s = 'ABCDBCA' 
table = s.maketrans('AB', 'ab', 'ACD') 
#В строке s А заменяется на а, B - на b, а также убирается A,C и D
print(s.translate(table))

#Выход: bb
'''


