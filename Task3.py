# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
inp = list(map(float, input('Введите число - ').split()))
ans = list()
for i in inp:
    x= i - int(i)
    if x !=0:
       ans.append(round(x, 5))
if max(ans) == min(ans):
    print (max(ans))
else:
    print(max(ans) - min(ans))