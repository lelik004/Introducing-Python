basic_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
final_list = [el for el in basic_list if basic_list.count(el) == 1]

print(final_list)