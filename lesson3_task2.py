stages = []
counter = 1
for _ in ['Homo habilis','Homo erectus','Homo neanderthalensis','Homo sapiens','Homo sapiens sapiens']:
    stages.append(input(f'Введите название стадии {counter}: '))
    counter+=1
print(*stages,sep='=>')