# Написать функцию max_mult(lst), которая возвращает список из двух элементов списка lst, 
# произведение которых будет максимальным. Список lst содержит целые числа.
#
# Пример:
# max_mult([1,2,3,4,5]) ==> [4,5] 
# max_mult([1,2,-3,4,-5]) ==> [-3,-5]


import traceback

def max_mult(lst) :
    
    maxpr=0 #макс. произведение

    b=[0]*2 

    pr=0 #произведение

    for i in range(len(lst)-1):
        
        for j in range(1,len(lst)):
            
            if(i!=j):
                
                pr=lst[i]*lst[j]
                
                if(maxpr<pr):
                    
                    maxpr=pr
                    
                    b[0]=lst[i]
                    
                    b[1]=lst[j]
    return(b)

# Тесты
try:
    assert max_mult([1,2,3,4,5]) == [4,5] 
    assert max_mult([1,2,-3,4,-5]) == [-3,-5]
    assert max_mult([4, 6, 2, -3, 0, 5, 1]) == [6, 5]
    assert max_mult([-5,-6,3,4,6,6,1]) == [6, 6]   
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED") 
