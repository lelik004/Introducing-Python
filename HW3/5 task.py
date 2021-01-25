def sum_of_list(res, elements_str):
    for el_f in elements_str.split(' '):
        try:
            res += int(el_f)
        except ValueError:
            pass
    return res


exit_var = 1
basic_str = input('Введите числа через пробел: ')
result = sum_of_list(0, basic_str)

print(f'Сумма чисел: {result}\n')

while exit_var == 1:
    new_str = input('Продолжайте ввод чисел через пробел. Для выхода из программы введите q\n')
    for el in new_str.split(' '):
        if el == "q":
            exit_var = 0
        else:
            result = sum_of_list(result, el)
    print(result)
