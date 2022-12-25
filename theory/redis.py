from pprint import pprint
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

# r.set(name='test_key', value='erik')
# print(r.get('test_key'), '\n\n')

# Строка
r.set('index', '1')
print(f"index: {r.get('index')}")
r.incr('index')  # Увеличить строку на 1
print(f"index: {r.get('index')}")
r.decr('index')  # Уменьшить строку на 1
print(f"index: {r.get('index')}")
r.incrby('index', 3)  # Увеличить строку на 3
print(f"index: {r.get('index')}")
print('\n\n')
# Вывод:
# index: 1
# index: 2
# index: 1
# index: 4


# Список
r.lpush('my_list', 'A')
print(f"my_list: {r.lrange('my_list', 0, -1)}")
r.rpush('my_list', 'B')  # Добавить вторую строку в список справа
print(f"my_list: {r.lrange('my_list', 0, -1)}")
r.rpush('my_list', 'C')  # Вставить третью строку в список справа
print(f"my_list: {r.lrange('my_list', 0, -1)}")
r.lrem('my_list', 1, 'C')  # Удалить из списка 1 экземпляр, значение которого "C"
print(f"my_list: {r.lrange('my_list', 0, -1)}")
r.lpush('my_list', 'C')  # Вставить строку в наш список слева
print(f"my_list: {r.lrange('my_list', 0, -1)}")
r.rpush('my_list', r.lpop('my_list'))  # Вытащить первый элемент нашего списка и переместить его в конец
print(f"my_list: {r.lrange('my_list', 0, -1)}")

r.lrem('my_list', 6, 'A')
r.lrem('my_list', 5, 'B')
r.lrem('my_list', 3, 'C')
print('\n\n')
# Вывод:
# my_list: ['A']
# my_list: ['A', 'B']
# my_list: ['A', 'B', 'C']
# my_list: ['A', 'B']
# my_list: ['C', 'A', 'B']
# my_list: ['A', 'B', 'C']


# Множества
r.sadd('my_set_1', 'Y')  # Добавить элемент в set 1
print(f"my_set_1: {r.smembers('my_set_1')}")
r.sadd('my_set_1', 'X')  # Добавить элемент в set 1
print(f"my_set_1: {r.smembers('my_set_1')}")
r.sadd('my_set_2', 'X')  # Добавить элемент в set 2
print(f"my_set_2: {r.smembers('my_set_2')}")
r.sadd('my_set_2', 'Z')  # Добавить элемент в set 2
print(f"my_set2: {r.smembers('my_set_2')}")
print(f"sunion: {r.sunion('my_set_1', 'my_set_2')}")  # Объединение set 1 и set 2
print(f"sinter: {r.sinter('my_set_1', 'my_set_2')}")  # Пересечение set 1 и set 2
print('\n\n')
# Вывод:
# my_set_1: {'Y'}
# my_set_1: {'X', 'Y'}
# my_set_2: {'X'}
# my_set2: {'X', 'Z'}
# sunion: {'X', 'Y', 'Z'}
# sinter: {'X'}


# Хэш
record = {
    "name": "PythonRu",
    "description": "Redis tutorials",
    "website": "https://pythonru.com/"
}
r.hset('business', 'record', 'erik')
pprint(f"business: {r.hgetall('business')}")


print('\n\n\nall KEYS: ', r.keys('*'))

r.close()
