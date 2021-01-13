num = int(input('Введите число: '))
great_dig = num % 10
auxl_n = num // 10
while auxl_n != 0:
    if auxl_n % 10 > great_dig:
        great_dig = auxl_n % 10
    auxl_n = auxl_n // 10
print('Самая большая цифра в числе: ', great_dig)
