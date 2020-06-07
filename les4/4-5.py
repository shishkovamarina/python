# 5. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


# a
def my_count(start_number, stop_number):
    for i in count(start_number):
        print(i)
        if i >= stop_number:
            break


my_count(start_number=int(input("Введите начало:\n")), stop_number=int(input("Введите конец:\n")))


# б
def my_cycle(my_list, iteration):
    i = 0
    a = cycle(my_list)
    while i < iteration:
        print(next(a))
        i += 1


my_cycle(my_list=[1, 2, 3, 4], iteration=int(input("Введите интерратор:\n")))
