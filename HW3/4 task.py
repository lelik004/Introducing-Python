def my_func1(x, y):
    return x**y


def my_func(x, y):
    n = 1
    res = 1 / x
    while n != abs(y):
        res = res / x
        n += 1
    return res


x = int(input('x: '))
y = int(input('y: '))

print(f'Решение №1: {my_func1(x, y)}\nРешение №2: {my_func(x, y)}')
