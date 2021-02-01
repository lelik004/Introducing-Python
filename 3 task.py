person_dict = {}
person_20 = []
all_salary = 0
average_income = 0
c = 0

for line in open('file_for_3_task.txt'):
    line_list = line.rstrip('\n').split(' ')
    add_dict = {line_list[0]: line_list[1]}
    person_dict.update(add_dict)

for el in person_dict.items():
    if int(el[1]) < 20000:
        person_20.append(el[0])
    all_salary += int(el[1])
    c += 1

average_income = all_salary / c

print(f'Сотрудники с зарплатой менее 20 т.р.: {person_20}')
print(f'Средняя заработная плата: {round(average_income)}')
