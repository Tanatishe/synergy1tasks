import collections

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },

}


def get_pet(ID):
  return pets[ID] if ID in pets.keys() else False


def pets_list():
    pass


def get_suffix(age: int):
    if age in range(5, 21) or age % 10 in [0, 5, 6, 7, 8, 9]:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    else:
        return 'года'


def create():
    last = collections.deque(pets, maxlen=1)[0]
    type = input('Укажите вид:')
    name = input('Укажите кличку:')
    age = int(input('Укажите возраст:'))
    owner = input('Укажите имя владельца: ')

    pets[last+1] = {name: {'Вид питомца': type,'Возраст питомца': age, 'Имя владельца': owner}}


def read():
    ID = int(input('Введите ID: '))
    if ID in pets:
        print(f'Это {pets[ID][list(pets[ID])[0]]['Вид питомца']} по кличке {list(pets[ID])[0]}.Возраст: {pets[ID][list(pets[ID])[0]]['Возраст питомца']} {get_suffix(pets[ID][list(pets[ID])[0]]['Возраст питомца'] % 100)}. Имя владельца: {pets[ID][list(pets[ID])[0]]['Имя владельца']}.')
    else:
        print('Wrong ID')


def update():
    pass


def delete():
    pass

while True:
    command = input('Введите команду: ')
    match command:
        case 'create':
            create()
        case 'read':
            read()
        case 'update':
            update()
        case 'delete':
            delete()
        case 'stop':
            break
        case _:
            print('Неизвестная команда')
