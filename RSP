import random 

def game():
    
    l = ['scissors', 'paper', 'rock']
    
    print('Your possible moves are', 'scissors', 'paper', 'rock')
    user=input('Choose one of them: ')
    user=user.lower()

    while(user not in l):
        user=input("Please, choose or scissors, paper, rock: ")

    comp=random.choice(l)
    
    if(user=='scissors' and comp=='paper'):
        print("Comp\'s move is {}".format(comp))
        print("You WIN!")
    
    elif(user=='scissors' and comp=='rock'):
        print("Comp\'s move is {}".format(comp))
        print("You LOSE((((")
    
    elif(user=='paper' and comp=='scissors'):
        print("Comp\'s move is {}".format(comp))
        print("You LOSE((((")
    
    elif(user=='rock' and comp=='scissors'):
        print("Comp\'s move is {}".format(comp))
        print("You WIN!")
    
    elif(user=='paper' and comp=='rock'):
        print("Comp\'s move is {}".format(comp))
        print("You WIN!")
    
    elif(user=='rock' and comp=='paper'):
        print("Comp\'s move is {}".format(comp))
        print("You LOSE((((")
        
game()
w=True
while(w):
    answer=input("Do you want to continue? ")
    answer=answer.lower()
    if(answer=='yes'):
        print("PERFECT!")
        game()
    
    else:
        print("BYE!)))")
        break
