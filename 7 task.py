def fact(n):
    fact = 1
    for el in range(1, n + 1):
        fact *= el
        yield fact


for el in fact(int(input('Введите число n: '))):
    print(el)
