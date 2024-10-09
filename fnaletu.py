import random

first = 'Мама мыла раму'
second = 'Рамена было мало'

a = list(map(lambda x, y: x == y, first, second))  # попозиционное сравнение строк


class MysticBall:  # определение класса
    def __init__(self, *words):
        self.words = words

    def __call__(self, x):  # задание метода вызова с дополнительным параметром
        return random.choice(self.words) + x


def get_advanced_writer(file_name):  # определение основной функции
    def write_everything(*data_set):  # определение внутренней функции
        a = open(file_name, 'w', encoding='utf-8')  # открыли файл для перезаписи
        for i in data_set:  # перебор входных данных
            if isinstance(i, str):  # проверка типа входных данных
                wr = i + '\n'
            else:
                wr = str(i) + '\n'
            a.write(wr)  # запись в открытый файл
        a.close()  # закрыли файл

    return write_everything  # возврат внутренней функции


# ТЕСТ ---------------------------------------------------------------------------------------------------------------

print(a)

b = get_advanced_writer('example.txt')  # вызов основной функции
b('Строка', ['Нечто', 1, 'эдакое'])  # вызов внутренней функции
with open('example.txt', 'r', encoding='utf-8') as rd:  # заглянем в получившийся файл
    print(rd.read())

first_ball = MysticBall('a1', 'b2', 'c3', 'd4')  # создание объекта класса
print(first_ball('v'))  # обращение к объекту класса с автоматическим вызовом метода call
print(first_ball('k'))
print(first_ball('s'))
