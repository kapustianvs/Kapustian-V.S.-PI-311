# -*- coding: utf-8 -*-
""".Введение в специальность. Лабораторная работа № 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jJ66zxV2P_lgvt82tcGt31AOBYvs3l6Z

Задание 1
"""

a = 5
b = int(input())
print(a * b)

"""Задание 2"""

a = int(input())
b =int(input())
print((a + b) ** 2)

"""Задание 3"""

a = 15
b = 10
c = int(input())
print((a + b) / c)

"""Задание 4"""

a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = (a + b) ** 2
print("Квадарат их суммы равен ", c)

"""Задание 5

"""

#import math
print("Введите длину каждой изтрех сторонтреугольника")
a = int(input())
b = int(input())
c = int(input())
d = a + b + c
print("Периметр равен", d)
e = d/2
#f = math.sqrt(e * (e - a) * (e - b ) * (e - c))
f = 0.5 ** (e * (e - a) * (e - b ) * (e - c))
print("Плозадь равна ", f)

"""Задание 6"""

a = int(input())
b = int(input())
c = (((a ** 3) + 14) / 5) * b
print(c)

"""Задание 7"""

first_number = int(input("Введите число "))
first_number_squared = first_number ** 2
print("Квадрат вашего числа равен", str(first_number_squared))
devider = int(input("Введите число-делитель "))
print("Квадрат, разделенный на второе чило, равен:1")
print(first_number_squared // devider)

"""Задание 8"""

x = float(input("Введите первое дробное число "))
y = float(input("Введите второе дробное число "))
z = x // y
print("Эти числа делятся на ", str(z), " целых частей")
x = int(input("Введите первое натуральное число "))
y = int(input("Введите второе наутральное число "))
z = x * y
print("Произведение этих чисел равно", str(z))
x = int(input("Введите первое натуральное число "))
y = int(input("Введите второе наутральное число "))
z = x % y
print("Остаток от деления первого числа на второе равен ", z)

"""Задания с повышенной сложностью
Задание 1
"""

seconds = int(input("Введите число секунд "))
# Тут можно попробовать целочисленное деление, но сделаю с обычным))
minutes = seconds / 60
print("Заданное количество секунд равно ", str(minutes), " минутам")
hours = minutes / 60
print("Заданное количество секунд равно ", str(hours), " часам")
days = hours / 24
print("Заданное количество секунд равно ", str(days), " дням")

"""Задание 2

"""

n = int(input("Введите челове число n "))
result = n + n * n + n * n * n
print(result)