# def f(x):
#     return x * x
# print(f(5))
# print(type(f))

# def calk1(a):
#     return a + a

# def calk2(a,b):
#     return a * b

# def math(op, x,y):
#     print(op(x,y))

# # calk1 = lambda a,b: a + b

# math(lambda a,b: a + b,5,45)

# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

list1 = [1,2,3,5,8,15,23,38]

# def f(x):
#     return x * x
# dictionary = {}
# for i in list1:
#     if i % 2 == 0:
#         dictionary[i] = f(i)
# print(dictionary)

def select(f,col):
    return [f(x) for x in col]
def where(f, col):
    return[x for x in col if f(x)]

res = select(int,list1)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res)
