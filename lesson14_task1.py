my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
count = 0


def rec_print():
    global count
    if count >= len(my_list):
        print('Конец списка')
        return
    print(my_list[count], end=' ')
    count += 1
    rec_print()


rec_print()
