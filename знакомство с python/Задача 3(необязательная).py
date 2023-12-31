import time


# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения
# (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

def all_divisors(n):
    i = 1
    res = []
    while i <= n:
        if n % i == 0:
            res.append(i)
        i += 1
    print(res)

all_divisors(190187200) # на выполнение ушло 29.4959 сек
