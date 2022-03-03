#from ast import arguments
#from os import path
import sys

arguments = sys.argv[1:]
textt = str(arguments[0])
pathFile = str(arguments[1])

lst = []
strstr = ''

with open(pathFile, "w") as file:
	file.write(textt)

with open(pathFile, "r") as file:
	for line in file:
		for item in line:
			lst.append(item)

if '\"' in lst:
	k = 0
	for item in range(len(lst)):
		if (lst[item] == '\"' and k % 2 == 0):
			lst[item] = '«'
			k += 1
		elif (lst[item] == '\"' and k % 2 != 0):
			lst[item] = '»'
			k += 1

strstr = strstr.join(lst)

with open(pathFile, "w") as file:
	file.write(strstr)

# Ввод: python3 12.py "\"TEXT\"" file.md