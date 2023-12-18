x = int(input('Мини сумма: '))
Mike = int(input('Mike: '))
Ivan = int(int(input('Ivan:')))
if Mike >= x and Ivan >= x:
    flag = 2
elif Mike >= x:
    flag = 'Mike'
elif Ivan >= x:
    flag = 'Ivan'
elif Mike + Ivan >= x:
    flag = 1
else:
    flag = 0
print(flag)
