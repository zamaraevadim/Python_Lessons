# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


# Input:       5

# Output:    120

n = 5
factorial = n
while n != 1:
    n = n - 1
    factorial = factorial * n
print(factorial)

