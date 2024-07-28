code = int(input('Введите в первое поле любое число от 3 до 20 ')) # переменная первого поля

str_password = '' # строка переменной пароля

for a in range(1, code):  # цикл перебора первого числа пары
    for i in range(1, code):  # цикл подбора второго числа пары
        if a >= i:  # отсечение равных чисел и повторов
            continue
        elif code % (a + i) == 0:
            str_password = str_password + str(a)  # добавление первого числа пары
            str_password = str_password + str(i)  # добавление второго числа пары

print('Пароль для второго поля: ', str_password)