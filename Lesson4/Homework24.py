# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# n = 5
# list1 = [9,1,2,3,8]

n = (input("Введите N: "))

while not n.isdigit():
    print("Вы ввели не число")
    n = (input("Введите N: "))

    
n = int(n)

list1 = []

for i in range(n):
    el = input("Введите элемент множества n: ")
    list1.append(int(el)) 

max = 0
count = 0
count2 = 0
list2 = []
while True:

    if len(list2) == n:
        break
    num = list1[count]

    count += 1
    count2 += 1
    max += num
    
    if count2 == 3:
        list2.append(max)
        max = 0
        count2 = 0
    if count == len(list1):
        count = 0
list2.sort()

print(list2[len(list2) - 1])