# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# import math
#
# distance_per_day = int(input("Введите число n, сколько за день проезжает автомобиль "))
# distance = int(input("Введите число m, расстояние, которое нужно проехать "))
# print("Для преодоления расстояния m необходимо ", int((distance / distance_per_day)))
# print(math.ceil(distance / distance_per_day))
# print((distance + distance_per_day + 1) // distance_per_day)

# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

# class_1 = int(input("Введите количество учеников 1ого класса "))
# class_2 = int(input("Введите количество учеников 2ого класса "))
# class_3 = int(input("Введите количество учеников 3его класса "))
# print(
#     class_1 // 2 + class_1 % 2 + class_2 // 2 + class_2 % 2 + class_3 // 2 + class_3 % 2
# )


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6


# n = int(input("Введите число: "))
#
# pre = 0 #fib 0
# cur = 1 #fib 1
# i = 2
# while n > cur:
#     temp = cur
#     cur = pre + cur
#     pre= temp
#     i += 1
# if cur == n:
#     print(i)
# else:
#     print(-1)

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# n = int(input())
# sp = []
# i = 0
# for _ in range(n):
#     sp.append(int(input("Введите температуру от -50 до 50: ")))
# max_days = 0
# temp_days = 0
# for i in sp:
#     if i > 0:
#         temp_days = temp_days + 1
#         if max_days < temp_days:
#             max_days = temp_days
#     else:
#         temp_days = 0
#
# print(max_days)

# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input("Введите количество арбузов: "))
# sp = []
# i = 0
# for _ in range(n):
#     sp.append(int(input("Введите массы арбузов: ")))
# min = sp[0]
# max = sp[0]
#
# for i in sp:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(min, max)

# from random import choice
#
# x = choice([True, False])
#
# print(x)