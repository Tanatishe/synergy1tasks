x = int(input('X = '))
count = 0
for i in range (1,x+1):
    if not x%i:
        count +=1
print(count)
