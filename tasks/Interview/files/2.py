# Выберите любую папку на своем компьютере, имеющую вложенные директории. 
# Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
# Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os. 
# Для примера возьмем следующую папку: C:/Program Files/Classic Shell.

import os
 
def print_docs(directory):
	all_files = os.walk(directory)
	for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
        print('-' * 40)
 
 
print_docs('C:/Program Files/Classic Shell')

# Результат выполнения
# Папка C:/Program Files/Classic Shell содержит:
# Директории: Skins
# Файлы: ClassicExplorer32.dll, ClassicExplorer64.dll, ClassicExplorerSettings.exe, ClassicIEDLL_32.dll, …
# ----------------------------------------
# Папка C:/Program Files/Classic Shell/Skins содержит:
# Директории:
# Файлы: Classic Skin.skin, Classic Skin.skin7, …
