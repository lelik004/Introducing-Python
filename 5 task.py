class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'{self.title}. Отрисовка ручкой')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'{self.title}. Отрисовка карандашом')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'{self.title}. Отрисовка маркером')


stationery_var = Stationery()
stationery_var.draw()

pen_var = Pen()
pen_var.draw()

pencil_var = Pencil()
pencil_var.draw()

handle_var = Handle()
handle_var.draw()
