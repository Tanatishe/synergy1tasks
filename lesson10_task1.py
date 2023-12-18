type = input('Укажите вид:')
name = input('Укажите кличку:')
age = int(input('Укажите возраст:'))
owner = input('Укажите имя владельца: ')
pets = {}
pets[name] = {'Вид питомца': type,'Возраст питомца': age, 'Имя владельца': owner}

def age_format(age: int):
    if age in range(5, 21) or age % 10 in [0, 5, 6, 7, 8, 9]:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    else:
        return 'года'


print(f'Это {pets[name]['Вид питомца']} по кличке {name}.Возраст: {pets[name]['Возраст питомца']} {age_format(age % 100)}. Имя владельца: {pets[name]['Имя владельца']}.')
