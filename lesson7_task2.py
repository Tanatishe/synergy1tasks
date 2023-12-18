N = int(input())
l = list(map(int,input().split()))
l = [l[-1]] + l[:len(l)-1]
print(l)
