from random import randint

n = int(input("Количество элементов первого множества: "))
sp = [randint(0, 10) for _ in range(n)]
print(sp)
sp = set(sp)

m = int(input("Количество элементов второго множества: "))
sp2 = [randint(0, 10) for _ in range(m)]
print(sp2)
sp2 = set(sp2)

print("Результат:", sp | sp2)



