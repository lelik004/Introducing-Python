count = 1
name = []
price = []
quantity = []
unit = []
goods_list = [(count, {
    'Название': input('Введите название товара: '),
    'Цена': input('Введите цену товара: '),
    'Количество': input('Введите количество товара: '),
    'ед.': input('Введите единицу измерения: ')
    })]
while input('Если хотите добавить еще товар - нажмите Enter,\nесли нет - наберите 0\n') != '0':
    count += 1
    goods_list.append((count, {
        'Название': input('Введите название товара: '),
        'Цена': input('Введите цену товара: '),
        'Количество': input('Введите количество товара: '),
        'ед.': input('Введите единицу измерения: ')
        }))

for el in goods_list:
    name.append(el[1].get('Название'))
    price.append(el[1].get('Цена'))
    quantity.append(el[1].get('Количество'))
    unit.append(el[1].get('ед.'))
goods_dict = {'Название': name,'Цена': price, 'Количество': quantity, 'ед.': unit}

for key in goods_dict:
    print('{}: {}'.format(key, goods_dict[key]))
