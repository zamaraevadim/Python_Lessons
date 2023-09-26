# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

# list1 = "a a a b c a a d c d d".split()
# dict1 = {}

# for i in list1:
#     if i in dict1:
#         dict1[i] += 1
#         print(f'{i}_{dict1[i]}',end=" ")
#     else:
#         dict1[i] = 0
#         print(i,end=" ")

# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

# text = "She sells sea shells on the sea shore The shells that \
#     she sells are sea shells I'm sure So if she sells sea shells on the sea shore \
#         I'm sure that the shells are sea shore shells".lower()

# words = text.split()
# unique_words = set(words)
# count = len(unique_words)
# print(count)

# Ваня:

# n = int(input())
# max_number = n #1
# while n != 0:
#    n = int(input())
#    if max_number <  n:#2
#        max_number = n
# print(max_number)

