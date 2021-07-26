# Написать функцию degree_of_two, которая определяет является ли заданное число квадратом какого-либо целого числа.
#
# Примеры:
# degree_of_two(81) ==> True
# degree_of_two(6561) ==> True
# degree_of_two(333)  ==> False

import traceback


def degree_of_two(number) :

    t=False

    for i in range(1, number+1):
        if(i*i==number):
            t=True
            break
            
    return t


try:
    assert degree_of_two(1) == True
    assert degree_of_two(2) == False
    assert degree_of_two(5) == False
    assert degree_of_two(81) == True
    assert degree_of_two(6561) == True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
