# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

my_list = ['Привет\n', 'Как дела?\n', 'Пока\n']
with open("test_2.txt", 'w+', encoding='UTF-8') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in one line")
    print(f"String count is {lines}")
