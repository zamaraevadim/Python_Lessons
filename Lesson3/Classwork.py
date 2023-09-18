# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6



# Примечание: Пользователь может вводить значения списка или список задан изначально.

# arr = [1, 1, 2, 0, -1, 3, 4, 4]
# set_1 = set(arr)
# print(len(set_1))

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# list1 = [1, 2, 3, 4, 5]
# k = 3

# for i in range(len(list1) - k):
#     for j in range(len(list1) - 1):
#         list1[j], list1[j - 1] = list1[j - 1], list1[j]
# print(list1)
    
# Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# Примечание: Список словарей задан изначально. Пользователь его не вводит

d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
new_set = set()
for i in d :
    for j in i.values():
        new_set.add(j)
print(new_set)