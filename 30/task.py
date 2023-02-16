# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

n = int(input('Введите начальное число: '))
m = int(input('Введите шаг прогрессии: '))
l = int(input('Введите количество элементов: '))


def arithmetic_progression(number, step, amount):
   lst = []
   for i in range(1, amount+1):
      lst.append(number + (i-1) * step)
   return lst

def show_element_from_new_line(arr):
   for i in range(len(arr)):
      print(arr[i])


lst1 = arithmetic_progression(n, m, l)
print(lst1)
show_element_from_new_line(lst1)