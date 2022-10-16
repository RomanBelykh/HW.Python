# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input("Enter the value of N "))
n1 = int (input("Position one: "))
n2 = int (input("Position two: "))

num_list = list(range(-num, num+1))

print(num_list)
len_list = len(num_list)

if len_list >= n1>0 and len_list >=2>0:
    print(num_list[n1-1]*num_list[n2-1])
else:
    print("There are no values for these index")
