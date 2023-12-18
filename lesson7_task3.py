m = int(input('m '))
N = int(input('N '))
l = []
count = 0
for _ in range(N):
    l.append(int(input()))
l = sorted(l)
while len(l) > 0:
    if len(l) > 1 and l[0] + l[-1] <= m:
        del l[0]
    del l[-1]
    count +=1
print(count)
