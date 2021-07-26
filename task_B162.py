# Написать функцию duplicate_encode, которая получает строку и преобразует ее: 
# если символ в строке появляется один раз, то заменить на "(", 
# иначе заменить на ")", если символ появляется больше одного раза. Регистр не должен иметь значение.
#
# Примеры:
# duplicate_encode("hello world") ==> "(()))(()()("

import traceback

def duplicate_encode(word) :
    
    a=[]
    
    b=[] 
    
    k=0
    
    t=True
    
    f=False
    
    word=word.lower()
    
    for i in range(len(word)):
        a.append(word[i])
        
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i]==a[j]):
                k+=1 
                
        if(k>1):
            for k in range(len(b)):
                if(a[i]==b[k]):
                    t=False
            if(t==True):
                b.append(a[i])
        
        k=0
        t=True

    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==b[j]):
                f=True
                
        if(f==True):
            a[i]=')'
        else:
            a[i]='('
            
        f=False

    return(''.join(a))


# Тесты:
try:
    assert duplicate_encode("hello world") == "(()))(()()("
    assert duplicate_encode("abc") == "((("
    assert duplicate_encode("(( @") == "))(("
    assert duplicate_encode("Success") == ")())())"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
