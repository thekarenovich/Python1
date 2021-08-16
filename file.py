import os

if not os.path.isdir('folder')==True:
    os.mkdir('folder')

    os.makedirs('folder/first')
    os.makedirs('folder/second')
    os.makedirs('folder/first/third')

with open('text.txt', 'w') as file:
    print('thekhachik', file=file)

os.rename("text.txt", 'rename.txt')
os.replace('rename.txt', 'folder/rename.txt')
#os.remove("folder/rename.txt")
