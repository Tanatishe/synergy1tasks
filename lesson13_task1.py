import random as r
n = int(input('Input matrix h: '))
m = int(input('Input matrix w: '))
ran = int(input('Input range: '))

A = [[r.randint(-ran,ran) for i in range(m)] for i in range(n)]
B = [[r.randint(-ran,ran) for i in range(m)] for i in range(n)]
C = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]
for i in range(n):
    print(*A[i])
print()
for i in range(n):
    print(*B[i])
print()
for i in range(n):
    print(*C[i])
