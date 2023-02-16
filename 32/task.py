# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
a = int(input('Введите минимальное число диапазона(не иенее 0): '))
b = int(input('Введите максимальное число диапазона (не более 100): '))
n = random.randint(10, 15)
arr=[random.randint(0,100) for i in range(n)]
print(arr)


def define_indexes(lst, min_value, max_value):
   new_lst = []
   for i in range(len(lst)):
      if lst[i] > min_value and lst[i] < max_value:
         new_lst.append(i)
   return new_lst

new_lst = define_indexes(arr, a, b)
print(new_lst)