def my_func(var1, var2, var3):
    my_func_list = [var1, var2, var3]
    my_func_list.sort(reverse=True)
    return my_func_list[0] + my_func_list[1]


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(f"Сумма двух больших чисел равна {my_func(a, b, c)}")
