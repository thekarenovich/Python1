hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n = n + 1
    while not checkPrime(n):
        n += 2
    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    # удаление по ключу
    index = hashFunction(key)
    hashTable[index] = 0

def sizeTable(hashTable):
    k = 0
    for i in range(len(hashTable)):
        if(hashTable[i] != [] and hashTable[i] != 0):
            k += 1
    return k

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable) # хэш - таблица

removeData(123)

print(hashTable) # после удаления

print('Size of table: ', sizeTable(hashTable))
