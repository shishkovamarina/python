# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_int = 8
my_float = 8.3
my_str = "Hello world"
my_list = ['n', '2d2']
my_tuple = ('c', '3')
my_dict = {'city': 'S.Petersburg', 'country': 'Russia'}

my_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in my_list:
    print(f'{i} is {type(i)}')
