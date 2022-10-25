# a, b - local variables
# c, d - global variables

def sum_1():  
    a = 10
    b = 20  
    sum = a + b  
    print("Sum:", sum)   

def sum_2():  
    sum = c + d
    print("Sum:", sum)  

  
def sub():  
    sub = c - d
    print("Subtraction:", sub)


c = 30  
d = 40 
  
sum_1()
sum_2()
sub()
