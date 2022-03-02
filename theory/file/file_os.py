# Файлы

import os

print(os.listdir(path="projects")) # Вывод файлов, директорий данной папки в виде списка

os.truncate("file.txt", 25) # Обрезать файл до указанной длины

if not os.path.isdir("folder") == True:
    os.mkdir("folder")
# При отсутсвии папки создастся такая

os.rename("text.txt", "rename.txt") # Переименование файла
os.replace("rename.txt", "folder/rename.txt") # Перемешение файла
os.remove("folder/rename.txt") # Удаление файла

print(os.stat("1.py").st_size) # Размер файла
print(os.stat("1.py").st_atime) # Время последнего визита
print(os.stat("1.py").st_mtime) # Время последнего изменения

'''
# Запись в файл

file = open("text.txt", "w")
file.write("Hello")
file.close()

fiile = open("ttext.txt", "w")
fiile.write("Hello!")
print("LOL", file=fiile)
# В файле Hello!LOL

# Вывод строк файла
with open("text.txt","r") as file:
    for line in file:
        print(line)
        
# Вывод файла по символьно
with open("text.txt","r") as file:
    for line in file:
        for i in range(len(line)):
            print(line[i])
            
read() считывает всё
read(a) считывает 3 символа
readline() считывает одну строку
readlines() считывает всё в список

'''
