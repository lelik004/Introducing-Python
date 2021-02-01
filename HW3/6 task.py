def int_func(func_var):
    alphabet_list = list(range(65, 91)) + list(range(97, 123))
    func_set = set(func_var)
    func_set.discard(' ')

    for el in func_set:
        if alphabet_list.count(ord(el)) == 0:
            return print('Предложение содержит не латинские буквы')
    return func_var.title()


my_str = input('Введите предложение, состоящее из латинских букв: ')
print(int_func(my_str))
