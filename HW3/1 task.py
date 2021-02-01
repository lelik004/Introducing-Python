def my_func(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        return
    return a / b


a = float(input('Введите a: '))
b = float(input('Ввведите b: '))

if my_func(a, b) is not None:
    print(f'a/b={my_func(a, b)}')
