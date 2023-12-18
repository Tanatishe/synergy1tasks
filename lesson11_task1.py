n = int(input())
def fact(a:int):
    if a == 1 or a == 0:
        return 1
    return a*(fact(a-1))
six = fact(n)
print(six)
l = []
for i in range(six,0,-1):
    l.append(fact(i))
print(l)
