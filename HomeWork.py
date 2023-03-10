# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите разность: '))
l = int(input('Введите колличество элементов: '))

progression = []
progression.append(a1)
for i in range(2, l+1):
    progression.append(a1 + (i-1) * d)

print(progression)


# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
my_list = [random.randint(-99, 100) for _ in range(100)]

min = int(input('Введите нижнюю границу диапазона: '))
max = int(input('Введите верхнюю границу диапазона: '))

indexes = []
for i in range(len(my_list)):
    if my_list[i] <= max and my_list[i] >= min:
        indexes.append(i)

print(indexes)
