# 5. Реализуйте алгоритм перемешивания списка.

from random import randrange

num = int(input())
num_list = list(range(num))
len_list = len(num_list)

print(num_list)

for i in range(len_list):
    n1 = randrange(len_list)
    n2 = randrange(len_list)
    num_list[n1], num_list[n2] = num_list[n2], num_list[n1]

print(num_list)
