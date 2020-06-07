# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    result = [a, b, c]
    total = []
    max_1 = max(result)
    total.append(max_1)
    result.remove(max_1)
    max_2 = max(result)
    total.append(max_2)
    print(sum(total))


my_func(8, 4, 6)