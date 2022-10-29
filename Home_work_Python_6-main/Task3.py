# Задайте список из k чисел последовательности (1 + 1\k)^k
# и выведите на экран их сумму.

number = int(input('Enter your number: '))
# numbers = []
# summ = 0

# for i in range(1, number):
#     num = round((1 + 1 / i)**i, 2)
#     numbers.append(num)
#     summ += num

numbers = [round((1 + 1 / i) ** i, 2) for i in range(1, number)]

print('{}, sum is: {}'.format(numbers, round(sum(numbers), 2)))
