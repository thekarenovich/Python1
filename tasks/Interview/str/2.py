# Требуется определить индексы первого и последнего вхождения буквы в строке. 
# Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра: letter – искомый символ, st – целевая строка. 
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None), если же она есть, то кортеж будет состоять из первого и последнего индекса этого символа.

def first_last(letter, st):
    first = st.find(letter)
    if first < 0:
        return None, None
    last = st.rfind(letter)
    return first, last

  
print(first_last('a', 'abba'))  # (0, 3)
print(first_last('a', 'abbaaaab'))  # (0, 6)
print(first_last('a', 'a'))  # (0, 0)
print(first_last('a', 'spring'))  # (None, None)
