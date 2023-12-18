a = int(input('Введите число: '))
nat = 'положительное'
even = ''
if a < 0:
    nat = 'отрицательное'
if a%2:
    even = 'не'
string = f'{nat} {even}четное число'
if a == 0:
    string = 'нулевое число'
print(string)
if len(even):
    print('число не является четным')
