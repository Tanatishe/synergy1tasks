string = input().lower()
vowels = 'aeiou'
vowels_c=consonants_c=0
for i in string:
    if i in vowels:
        vowels_c+=1
    else:
        consonants_c+=1
print(f'гласных: {vowels_c}',f'согласных: {consonants_c}',sep='\n')
for i in vowels:
    c = string.count(i)
    print([f'{i}  {c}',f'{i}  {not not c}'][not c])
