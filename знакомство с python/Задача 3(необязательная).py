import time
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения
# (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

n = 190187200 # На этом числе программа уже не выполняется. А если убирать один 0, то на ее выполнение ушло 5.206996 сек
i = 1
res = []
t0 = time.time()
while i <= n:
        if n%i == 0:
            res.append(i)
        i += 1
t1 = time.time() - t0
print(res)
print(t1)
