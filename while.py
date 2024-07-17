my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, 6, 5]  # исходный список
ind = 0  # переменная значения индекса с присвоением начального значения
while my_list[ind] >= 0:
    print(my_list[ind])
    ind = ind + 1  # инкремент индекса
    if ind < len(my_list):  # проверка на окончание списка
        continue
    else:
        break