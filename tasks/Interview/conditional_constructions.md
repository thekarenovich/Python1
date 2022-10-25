### В чем разница между двумя нижеследующими конструкциями?

```python
# Первая конструкция:
if x % 5 == 0:
    print('Х делится на 5')
if x % 2 == 0:
    print('Х – четное число')

# Вторая конструкция:
if x % 2 == 0:
    print('Х – четное число')
elif x % 5 == 0:
    print('Х делится на 5')
```
    
> Разница между конструкциями связана с порядком работы интерпретатора Python:
>
> 1. В первом случае всегда будут вычислены оба условных оператора (т.е. будем иметь двойное время работы программы независимо от исходного числа).
> 2. В следующем случае при срабатывании первого условия второе не будет вычисляться никогда (мы тем самым сокращаем количество выполняемых скриптом операций).

### Что такое тернарный оператор и есть ли он в языке Python?
> Тернарная операция, как следует из названия, работает с тремя операндами. 
> Первый задает условие, а второй и третий возвращаются в качестве значений в зависимости от истинности или ложности первого.

```python
# Условное выражение
def category_to_show(gender):
    category = 'site.com'
    if gender == 'М':
        category = 'site.com/male'
    elif gender == 'Ж':
        category = 'site.com/female'
    return category


print(category_to_show('М'))  # site.com/male
print(category_to_show('Ж'))  # site.com/female

# Тернарный оператор
def category_to_show(gender):
    category = 'site.com/male' if gender == 'М' else 'site.com/female'
    return category
    
print(category_to_show('М'))  # site.com/male
print(category_to_show('Ж'))  # site.com/female
```
