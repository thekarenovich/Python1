N = int(input())  # количество элементов в исходном списке
K = int(input())  # количество столбцо и списков

l = []  # исходный список

# добавление элементов в исх. список
for i in range(N):
    x = int(input())
    l.append(x)

if (N % K != 0):
    for d in range(1, K):
        N1 = N - d
        if (N1 % (K - 1) == 0):
            remainer = d  # количество чисел, которые будут в последнем столбце
            group = int(N1 / (K - 1))  # количество чисел, по сколько будем группировать
            break

else:
    group = int(N / K)
    remainer = 0

# print("\n",remainer,"\n",group)

ll = []  # матрица
for i in range(K):
    ll.append([])

# заполнение для полных столбцов
for i in range(K - 1):
    for j in range(group):
        ll[i].append(l[0])
        l.remove(l[0])

# заполнение для неполных столбцов
for i in range(len(l)):
    ll[K - 1].append(l[i])



while(len(ll[K - 1])!=group):
    ll[K - 1].append("")

z = []
k=0

for i in range(group):
    z.append(k)
    k+=1

print()

for ii in range(len(z)):
    for i in range(len(ll)):
        for j in range(group):
            if(j==ii):
                print(ll[i][j], end=" ")
    print()


