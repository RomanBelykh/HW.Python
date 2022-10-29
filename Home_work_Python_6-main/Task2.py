# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

number = int(input('Enter your number: '))
res = 1
# for i in range(1, number):
#     res *= i
#     print(res, end=' ')

numbers = [res := res * i for i in range(1, number)]
print(numbers)