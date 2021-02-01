from re import findall

final_dict = {}
line_list = []

with open('file_for_6_task.txt') as file:
    for line in file:
        line_list = line.split(':')
        num_list = [int(el) for el in findall(r'\d+', line_list[1])]
        aux_dict = {line_list[0]: sum(num_list)}
        final_dict.update(aux_dict)

print(final_dict)
