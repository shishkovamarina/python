# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
#
# a = 44
# b = 'hello'
# print(a)
# print(b)
# name = input('Введите название города\n')
# count = input('Введите численность населения\n')
# print(name)
# print(count)
#
# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.
#
# time = input('Введите время в секундах\n')
# if time.isdigit():
#     time = int(time)
#     hours = time // 3600
#     minutes = (time // 60) % 60
#     seconds = time % 60
#     print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
#
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#
# num = input('Введите число\n')
# if num.isdigit():
#     num = int(num)
#     num_2 = num * 11
#     num_3 = num * 111
#     sum = num + num_2 + num_3
#     print(sum)
#
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#
# num_int = input('Введите целое число\n')
# if num_int.isdigit():
#     num_int = int(num_int)
#     d = 0
#     while num_int > 10:
#         a = num_int % 10
#         num_int //= 10
#         if a > d:
#             d = a
#     print(d)
# else:
#     print('Данное значение не является целым числом')
#
# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток
# — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
# рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.
#
# revenue = input('Введите выручку\n')
# if revenue.isdigit():
#     revenue = int(revenue)
# costs = input('Введите издержки\n')
# if costs.isdigit():
#     costs = int(costs)
# if revenue > costs:
#     print('Прибыль: выручка больше издержек')
#     profitability = (revenue - costs) / revenue
#     print('Рентабельность выручки: ', profitability)
#     strength = input('Введите численность персонала\n')
#     if strength.isdigit():
#         strength = int(strength)
#     prof_person = (revenue - costs) / strength
#     print('Прибыль на одного сотрудника, ', prof_person)
# elif costs > revenue:
#     print('Убыток: издержки больше выручки')
#
# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
#
# start = input('Введите начальное значение: \n')
# finish = input('Введите окончание: \n')
# if start.isdigit():
#     start = float(start)
# if finish.isdigit():
#     finish = float(finish)
# day = 1
# if start > finish:
#     print(day)
# else:
#     while start < finish:
#         start = start + start/10
#         day += 1
#     print(day)
