'''
c = 10  
def mul():
    c = c * 10 
    print(c) 
mul()
# it'll lead to an error, because we can change the value of a global variable only using keyword GLOBAL
'''


def mul():
    global c
    c = c * 10 
    print(c) 
    
c = 10  
mul()  
print(c)  
