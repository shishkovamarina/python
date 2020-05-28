# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(name, surname, year_of_birth, city, email, phone):
    print(name, surname, year_of_birth, city, email, phone)


my_func(name= 'Marina', surname='Sh', year_of_birth=1987, city='Spb', email='sh@gmail.com', phone='123456789')