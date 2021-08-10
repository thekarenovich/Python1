import random

password = ''
everything = [] # this list will contain every type of symbols, which you have chosen 

lowercase_letters = []
for i in range(65, 91):
    lowercase_letters.append(chr(i+32))
    everything.append(lowercase_letters)

print('HI!\nLet\'s create your own password.\nYour password have lowercase letters, but you can add uppercase letters, special symbols, digits.')

number_of_symbols = int(input("Well, how many symbols do you want to have in your pass? "))
while(number_of_symbols < 6 or number_of_symbols > 40):
    if(number_of_symbols < 6 and number_of_symbols >= 0 ):
        number_of_symbols = int(input("Your password have to contain at least 6 symbols. Try again: "))
    elif(number_of_symbols < 0):
        number_of_symbols = int(input("Number of symbols have to be natural number, I mean more that zero. Try again: "))
    elif(number_of_symbols > 40):
        number_of_symbols = int(input("Number of symbols have to contain not more than 40 symbols. Try again: "))
        

uppercase_letters = input('Do you want to have uppercase letters in your pass? ')
uppercase_letters = uppercase_letters.lower()
if(uppercase_letters == 'yes'):
    uppercase_letters=[]
    for i in range(65, 91):
        uppercase_letters.append(chr(i))
        everything.append(uppercase_letters)


special_symbols = input('Do you want to have special symbols in your pass? ')
special_symbols = special_symbols.lower()
if(special_symbols == 'yes'):
    special_symbols = ['+','-','_','/','*','#','!','?','$','&','=','<','>','@']
    everything.append(special_symbols)

digits = input('Do you want to have digits in your pass? ')
digits = digits.lower()
if(digits == 'yes'):
    digits = [i for i in range(11)]
    everything.append(digits)
    
    
    
    
number_of_symbols_2 = number_of_symbols 

while(number_of_symbols > 0):
    step1 = random.choice(everything)
    step2 = random.choice(step1)
    password+=str(step2)
    number_of_symbols-=1


listt = [] #list for checking presence of type of symbol in the password
l = False
u = False
d = False
s = False

#if variable is list, not string('yes' or 'no') and if there is defined symbol in ther password it's True
#if there isn't symbol in pass - False
for i in lowercase_letters:
    if(i in password):
        l = True
listt.append(l)    
if(isinstance(uppercase_letters, list)==True):
    for i in uppercase_letters:
        if(i in password):
            u = True
    listt.append(u)
if(isinstance(digits, list)==True):
    for i in digits:
        if(str(i) in password):
            d = True
    listt.append(d)
if(isinstance(special_symbols, list)==True):
    for i in special_symbols:
        if(i in password):
            s = True
    listt.append(s)

#if at least a variable is False and it's list      
if(all(i==True for i in listt) == False):
    listttt = []
    listttt = [i for i in range(number_of_symbols_2-3)]
    place = random.choice(listttt)
    password = password.replace(password[place], random.choice(lowercase_letters))
    if(uppercase_letters != 'yes'):
        password = password.replace(password[place+1], random.choice(uppercase_letters))
    if(special_symbols != 'yes'):
        password = password.replace(password[place+2], random.choice(special_symbols))
    if(digits != 'yes'):
        password = password.replace(password[place+3], str(random.choice(digits)))

print(password)
