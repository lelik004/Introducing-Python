proceeds = int(input('Введете выручку: '))
outgoings = int(input('Введите издержки: '))
if proceeds - outgoings > 0:
    profit = ((proceeds - outgoings) / proceeds) * 100
    print('Фирма работает в прибыль.')
    print('Рентабельность фирмы: ', '%.2f' % profit, '%', sep='')
    persons = int(input('Какое количество сотрудников в фирме? '))
    profit_for_person = (proceeds - outgoings) / persons
    print('Прибыль на каждого сотрудника составляет', '%.2f' % profit_for_person)
else:
    print('Фирма убыточная.')
