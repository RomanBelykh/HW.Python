#Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def BinaryCode (number):
    ans = list()
    rest = number% 2
    rez = number// 2
    ans.append(rest)
    while rez !=0:
       rest = rez % 2
       rez = rez// 2
       ans.append(rest)
    ans.reverse
    return ans

N = int(input('Введите число - '))
answer = BinaryCode(N)
print(N, ' в двоичном коде - ', *answer, sep ='')