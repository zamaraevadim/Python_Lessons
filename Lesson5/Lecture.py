# # Функции
# def sum_numbers(n):
#     summa = 0
#     for i in range(1,n + 1):
#         summa += i
#     return summa
# print(sum_numbers(5))

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q','e','l'))

# import modul1

# print(modul1.max1(5,9))

# import modul1 as m1

# print(m1.max1(5,9))

# # Рекурсия

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
#     print(list_1)
# # Алгоритмы
# # Быстрая сортировка
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.
a = 3
b = 5


def f(a,b):
    m = 1
    for i in range(b):
       m = m * a
    return m
print(f(a, b))