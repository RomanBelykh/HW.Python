
# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input("Введите число n - "))
sum = 0
ans = list()
for i in range(1, n+1):
     sum += ((1+1/i)**i)
     ans.append(round(((1+1/i)**i), 2))
print(ans)
print(round(sum,1))