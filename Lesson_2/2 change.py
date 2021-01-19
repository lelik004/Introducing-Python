my_str = input('Введите элементы списка через пробел: ')
my_list = my_str.split(' ')
a = 0

while a <= len(my_list) - 2:
    my_list[a], my_list[a+1] = my_list[a+1], my_list[a]
    a += 2

print(my_list)
