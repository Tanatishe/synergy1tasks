A = int(input())
B = int(input())
l = []
for i in range(A,B+1):
    if i%2 == 0:
        l.append(i)
print(*l)
