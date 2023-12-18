type = input('Укажите вид:')
name = input('Укажите кличку:')
age = int(input('Укажите возраст:'))


def age_format(age: int):
    if age in range(5, 21) or age % 10 in [0, 5, 6, 7, 8, 9]:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    else:
        return 'года'


print(f'Это {type} по кличке {name}.Возраст: {age} {age_format(age % 100)}.')
