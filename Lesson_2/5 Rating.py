my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент: '))
count = 0

for el in my_list:
    if new_el > el:
        my_list.insert(count, new_el)
        break
    elif new_el <= el and count == len(my_list) - 1:
        my_list.insert(count + 1, new_el)
        break
    else:
        count += 1

print(my_list)
