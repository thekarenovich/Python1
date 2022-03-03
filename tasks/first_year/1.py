'''
Преобразовать элементы списка s из строковой в числовую форму.
Подсчитать количество различных элементов в последовательности s.
Обратить последовательность s без использования функций.
Выдать список индексов, на которых найден элемент x в последовательности s.
Сложить элементы списка s с четными индексами.
Найти строку максимальной длины в списке строк s.
'''

s = ['1', '2', '3', '4', '5']

result1 = [int(i) for i in s] #[1, 2, 3, 4, 5]
print(result1)

result2 = len(set(s))
print(result2)

result3 = [ s[i] for i in range(len(s)-1, -1, -1) ]
print(result3)

s.append('3')
x = '3' #s = ['1', '2', '3', '4', '5', '3']
result4 = [ i for i in range(len(s)) if s[i]==x ]
print(result4)

s = result1
result5 = sum([ s[i] for i in range(len(s)) if i%2==0])
print(result5)

s = ['aaa', 'aaaa', 'aa']
result6 = max(s, key=len)
print(result6)

