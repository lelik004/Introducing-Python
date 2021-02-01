with open('file_for_5_task.txt', 'w') as file:
    file.write(input('Введите числа через пробел: '))

with open('file_for_5_task.txt') as file:
    num_list = [int(el) for el in file.read().split(' ')]

print(f'Сумма введенных чисел равна: {sum(num_list)}')
