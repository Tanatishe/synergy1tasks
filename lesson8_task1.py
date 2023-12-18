s = input().lower()
print('yneos'[s[:len(s)//2] != s[:-(len(s)//2+1):-1]::2])
