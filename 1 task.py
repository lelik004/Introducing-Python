line_in_file = 0
file_list = []

while line_in_file != '':
    line_in_file = input()
    file_list.append(line_in_file)

with open('file_for_1_task.txt', 'w') as file:
    for el in file_list:
        file.write(el)
        if el == '':
            break
        file.write('\n')
    print(file)
