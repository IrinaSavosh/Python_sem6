# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

import random

n = random.randint(5, 10)
arr_one=[random.randint(0,20) for i in range(n)]

m = random.randint(5, 10)
arr_two=[random.randint(0,20) for i in range(m)]

def something (lst_one, lst_two):
   lst_three = []
   for i in lst_one:
      if i not in lst_two:
         lst_three.append(i)
   return lst_three      

print(arr_one)
print(arr_two)
print(something(arr_one, arr_two))


