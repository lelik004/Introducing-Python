new_str = input('Введите строку: ')
new_list = list(new_str.split(' '))
count = 1
for el in new_list:
    print(count, '%.10s' % el)
    count += 1
