from random import randint
n = int(input("Введите число кустов: "))

kust = [randint(0, 10) for _ in range(n)]
res = []
for i in range(len(kust)):
    if kust[i-1] <= kust[i] and kust[i] >= kust[(i+1) % len(kust)]:
        res.append(kust[i-1]+kust[i]+kust[(i+1) % len(kust)])

print(kust)
print(f"Урожай: {max(res)}")
