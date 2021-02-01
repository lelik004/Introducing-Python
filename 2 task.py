final_dict = {}
words_in_line = 0
cnt_lines = 0

with open('file_for_2_task.txt') as file:
    for line in file:
        cnt_lines += 1
        if line.split(' ') == ['\n']:
            words_in_line = 0
            new_dict = {cnt_lines: words_in_line}
        else:
            words_in_line = len(line.split(' '))
            new_dict = {cnt_lines: words_in_line}
        final_dict.update(new_dict)

print('Количество строк: ', cnt_lines)
cnt_lines = 1

for el in final_dict.items():
    print(f'В строке {cnt_lines} содержится {final_dict.get(cnt_lines)} слов')
    cnt_lines += 1
