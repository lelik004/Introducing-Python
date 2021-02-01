from itertools import count, cycle

var_1 = (int(input('Введите с какого числа выводить целые числа: ')))
var_2 = (int(input('Введите по какое число выводить целые числа: ')))
var_3 = (int(input('Сколько раз выводить элементы списка [Ц, И, К, Л]? ')))
my_list = cycle(['Ц', 'И', 'К', 'Л'])
count_var = 0
res_a = []
res_b = []

for el in count(var_1):
    if el > var_2:
        break
    res_a.append(el)

for el in my_list:
    count_var += 1
    if count_var > var_3:
        break
    res_b.append(el)

print(f'a) Спискок целых чисел от {var_1} до {var_2}: {res_a}')
print(f'b) Список повторяющихся элементов цикла: {res_b}')
