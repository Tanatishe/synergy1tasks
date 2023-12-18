number = int(input('Введите пятизначное число: '))
n1 = number%10
n2 = (number%100)//10
n3 = (number%1000)//100
n4 = (number%10000)//1000
n5 = (number%100000)//10000


print(((n2 ** n1) * n3) / (n5 - n4))
