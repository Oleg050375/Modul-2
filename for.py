num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prim = []  # пустой список для наполнения простыми числами
not_prim = []  # пустой список для наполнения не простыми числами
for n in range(len(num)):  # цикл по количеству элементов списка num
    if num[n] == 2:  # проверка на двойку, которая особенная в этой истории
        prim.append(num[n])
    b = 2  # установка счётчика
    while b != num[n]:  # механизм проверки на простоту
        if num[n] == 1:  # проверка на единицу, которую нужно пропустить
            break
        elif num[n] % b == 0:  # проверка на делибельность )))
            not_prim.append(num[n])
            break
        elif b == num[n] - 1:  # проверка на окончание счёта
            prim.append(num[n])
        b = b + 1  # инкремент счётчика
print('простые:', prim)
print('не простые:', not_prim)