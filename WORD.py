print("Первый пользователь вводит слово")
print("Второй пользователь угадывает слово")
word = input()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
wordd = ''

l = ['б', 'п', 'в', 'ф', 'д', 'т', 'з', 'с', 'ж', 'ш', 'ч', 'ц', 'щ', 'г', 'к', 'х', 'м', 'н', 'л', 'р', 'а', 'э', 'о', 'ы', 'и', 'у', 'я', 'е', 'ё', 'ю', 'й']

ll = [] # список букв в слове

k=5 # количество попыток

print("Время угадывать!")
print("Имеется 5 попыток")
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()


while(k>0):

    letter = input(f"\n| Введите одну строчную русскую букву: ")
    
    while(letter not in l):
         letter = input(f"\n| Введите ОДНУ СТРОЧНУЮ РУССКУЮ букву: ")

    if(letter in word):
        ll+=[letter]
        wordd=''
        for i in range(len(word)):
            if(word[i] in ll):
                print(word[i], end=' ')
                wordd+=word[i]
                
            else:
                print('_', end=' ')
                wordd+='_'

        if('_' not in wordd and k>0):
            print(f"| ДА! Это слово {word}")
            break
                
    
    else:
        print(f"\n| В слове нет такой буквы...")
        k-=1
        print(f"\n| Осталось {k} попытки")

if(k==0):
    print("GAME OVER!!!")

    
    
        
        

        
        
        
    



    


        
