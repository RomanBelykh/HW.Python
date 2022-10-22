
#Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(number):
    if number ==1 or number ==2:
       return 1
    else:
       return Fibonacci(number-1) + Fibonacci(number-2)
N = int(input('Введите чило - '))
ans = list ()
for i in range(1, N+1):
    ans.append(Fibonacci(i)*((-1)**(i+1)))
ans.reverse()
ans.append(0)
for i in range(1, N+1):
        ans.append(Fibonacci(i))
print(*ans)
 #Эту задачу я подсмотрел