# Реализуйте свою версию print(). Постарайтесь использовать максимум возможностей настоящей print().
# Для вывода используйте функцию sys.stdout.write().

import sys

def print(*args):
    sys.stdout.write(' '.join(map(str.upper, args)))
print('asd', 'sad')
