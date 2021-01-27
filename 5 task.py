from functools import reduce
new_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(lambda prev_el, el: prev_el * el, new_list))
