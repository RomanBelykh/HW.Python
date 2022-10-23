# Задача 3
# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности
from random import randint

listnum = []
for i in range(randint(5,20)):
    listnum.append(randint(0,20))

print(f'Сгенерировать список: {listnum}') 

newlist = []
for j in range(len(listnum)):
    for k in range(len(listnum)):
        if j !=k and listnum[j] == listnum[k]:
            break
    else: 
        newlist.append(listnum[j])

print(f'Список с исключением повторяющихся элементов: {newlist}')
