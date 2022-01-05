import random

print(f"Играем в крестики -нолики \nВы играете крестиками \nПросто выбирайте номер клетки и это будет Ваш ход")

print(f"                                   | 0 | 1 | 2 |")
print(f"                                   | 3 | 4 | 5 |")
print(f"                                   | 6 | 7 | 8 |")


l = [0,1,2,3,4,5,6,7,8] # вывод доски с Х и O
ll = ['0','1','2','3','4','5','6','7','8'] # вывод оставшихся чисел (для метода join)
lll = [0,1,2,3,4,5,6,7,8] 
k = 9 # количество ходов

while(k>0):

    x = int(input("Ваш ход: "))

    if(x in l):
        index = l.index(x)
        l.remove(x)
        l.insert(index,'X')
        ll.remove(str(x))
        lll.remove(x)
        k-=1
    else:
        while(x not in l):
            x = int(input(f"Доступные номера клеток: {', '.join(ll)}: "))
        index = l.index(x)
        l.remove(x)
        l.insert(index,'x')
        ll.remove(str(x))
        lll.remove(x)
        k-=1

    if(l[0]==l[4]==l[8] or l[2]==l[4]==l[6] or l[0]==l[1]==l[2] or l[3]==l[4]==l[5] or l[6]==l[7]==l[8] or l[0]==l[3]==l[6] or l[1]==l[4]==l[7] or l[2]==l[5]==l[8]):
        print("Вы выиграли!")
        print(f"                              | {l[0]} | {l[1]} | {l[2]} |")
        print(f"                              | {l[3]} | {l[4]} | {l[5]} |")
        print(f"                              | {l[6]} | {l[7]} | {l[8]} |")
        break

    if(lll!=[]):
        o = random.choice(lll)
        print(f"Ход компьютера: {o}")
        index = l.index(o)
        l.remove(o)
        l.insert(index,'O')
        ll.remove(str(o))
        lll.remove(o)
        k-=1
        print(f"                                   | {l[0]} | {l[1]} | {l[2]} |")
        print(f"                                   | {l[3]} | {l[4]} | {l[5]} |")
        print(f"                                   | {l[6]} | {l[7]} | {l[8]} |")

    if(l[0]==l[4]==l[8] or l[2]==l[4]==l[6] or l[0]==l[1]==l[2] or l[3]==l[4]==l[5] or l[6]==l[7]==l[8] or l[0]==l[3]==l[6] or l[1]==l[4]==l[7] or l[2]==l[5]==l[8]):
        print("Вы проиграли...")
        print(f"                               | {l[0]} | {l[1]} | {l[2]} |")
        print(f"                               | {l[3]} | {l[4]} | {l[5]} |")
        print(f"                               | {l[6]} | {l[7]} | {l[8]} |")
        break

    if(ll==[] or k==0):
        print(f"/nНичья :))")
        break

  


    

    

    
        
    
    
