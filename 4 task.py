russian_list = ['Один', 'Два', 'Три', 'Четыре']
aux_list = []
final_str = ''
c = 0

with open('file_for_4_task.txt') as file:
    content = file.readlines()

for el in content:
    aux_list.append(el.split(' '))

for el in aux_list:
    el[0] = russian_list[c]
    c += 1
    final_str += ' '.join(el)

with open('file_4.txt', 'w') as new_file:
    new_file.write(final_str)

print(final_str)
