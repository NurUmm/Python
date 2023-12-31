# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:

# Output:
# 2
#
# n = int(input())
# m = int(input())
# result = int(m / n + 1)
# print(round(result, 3))

# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

first = int(input("Введите количество учащихся в первом классе "))
second = int(input("Введите количество учащихся во втором классе "))
third = int(input("Введите количество учащихся в третьем классе "))

sum = first + second + third
table = sum / 2
print(sum)
print(round(table))

# Задание 5. Пришел клиент чтоб сделать заявку на кредит , зовут его Иван Николаевич, ему 48 лет,
# он получает 50 000 в месяц, но тратит на обслуживание всех кредитов 18 500 в месяц.
# Подсказка - удобно будет забить исходные данные в переменные в начале программы.
# Теперь опишем то, как выполняется процесс рассмотрения заявки в нашем условном банке.
# Проверяем два фактора. Первый -  срок окончания обслуживания кредита не должен выходить за
# 50-ый год жизни клиента. То есть, если клиенту 49 лет, и он хочет взять кредит на 15 месяцев, то отказ.
# Второй фактор - общая сумма выплачиваемых клиентом кредитов вместе с потенциальным не должна превышать
# 50 % его заработной платы. То есть если он платил 20 000 рублей при зарплате в 60 000 рублей и обслуживание
# нового кредита составит дополнительно плюсом 16000 рублей в месяц, то отказ.
# Если же оба фактора одновременно не выполняются, то одобряем заявку на кредит.
# Напишите программу, которая решает, выдать ли кредит Ивану Николаевичу или нет.
# Она запрашивает у пользователя   сумма кредита и на сколько месяцев  клиент хочет взять кредит .
# На выходе - решение банка об одобрении или отказе.
