length = int(input("length: "))
width1 = int(input("width: "))

width2=width1
width3=width1-2
width4= width1-2

while(width1>0):
    print('-', end='')
    width1-=1

print()

while(length>0):
    print('|', end='')
    while(width3>0):
        print(" ", end='')
        width3-=1
    print('|')
    width3=width4
    length-=1


    
while(width2>0):
    print('-', end='')
    width2-=1
