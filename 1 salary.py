from sys import argv

script_name, hours, rate, award = argv
rate, hours, award = [int(el) for el in [rate, hours, award]]
totally = rate * hours + award


print("Имя скрипта: ", script_name)
print('Выроботка сотрудника в часах : ', hours)
print('Ставка в час: ', rate)
print('Премия: ', award)
print('Зарплата сотрудника: ', totally)
