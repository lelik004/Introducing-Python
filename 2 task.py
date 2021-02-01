from random import randint

original_list = [randint(1, 1000) for el in range(20)]
final_list = []
compare_el = original_list[0]
print('Исходный список: ', original_list)

for el in original_list:
    if el > compare_el:
        final_list.append(el)
    compare_el = el

print('Финальный список: ', final_list)
