words = ['read', 'minute', 'up', "see", "only"]
numbers = [i for i in range(1,6)]
wordss = {1:'read', 3:'minute', 2:'up', 5:"see", 4:"only"}
repeats = []
read = '__(1)__'
up = '__(2)__'
minute = '__(3)__'
only = '__(4)__'
see = '__(5)__'
k = 5 # количество слов 
text = '''I {} the letter. Stood {}. Sat down. Pondered for a {}. Then reread the letter again.
It is {} with the heart that one can {} rightly.'''.format(read, up, minute, only, see)

print('You have incomplete text: \n{}'.format(text))
print()
print('And you have list of words')
print('You must insert these words in right places')
print('Words:', ', '.join(words))
print()
print("You should write number of empty place and chosen word")

while(k>0):
    
    number=int(input('number: '))
    while(number not in numbers):
        number=int(input('There is not such number. Try again: '))

    word=input('word: ')
    while(word not in words):
        word=input('You don\'t have this word. Try again: ')

    if(word in repeats and number in repeats):
        print("Um, you used this combination")
    elif(number in repeats):
        print("Um, you used this number")
    elif(word in repeats):
        print("Um, you used this word")

    elif(wordss[number]==word):
        if(number==1):
            read=word
        elif(number==2):
            up=word
        elif(number==3):
            minute=word
        elif(number==4):
            only=word
        elif(number==5):
            see=word
        repeats.append(word)
        repeats.append(number)
        k-=1
        text = '''I {} the letter. Stood {}. Sat down. Pondered for a {}. Then reread the letter again.
It is {} with the heart that one can {} rightly.'''.format(read, up, minute, only, see)
        print(text)
    else:
        print("It's not right...")

print("!!!Victory!!!")
        
