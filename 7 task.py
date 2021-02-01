import json

average_profit = 0
profit_all = 0
profit_each = 0
company_profit_dict = {}
c = 0

with open('file_for_7_task.txt') as file:
    for line in file:
        line_list = line.split(' ')
        profit_each = int(line_list[2]) - int(line_list[3])
        if profit_each >= 0:
            profit_all += profit_each
            c += 1
        aux_dict = {line_list[0]: profit_each}
        company_profit_dict.update(aux_dict)

average_profit_dict = {'average_profit': profit_all/c}

final_list = [company_profit_dict, average_profit_dict]

with open("file7.json", "w") as write_json:
    json.dump(final_list, write_json)
    print('json файл создан')
