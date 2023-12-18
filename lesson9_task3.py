l = input().split()
l2 = []
for i in l:
    flag = "YES"
    if i not in l2:
        l2.append(i)
        flag = 'NO'
    print(i, flag)
