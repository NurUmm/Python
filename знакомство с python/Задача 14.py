# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
res = []
for i in range(n):
    num = 2 ** i
    res.append(num)
print(res)