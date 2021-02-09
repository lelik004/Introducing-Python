class Wear:
    def __init__(self, size_value):
        self.size_value = size_value


class Suit(Wear):

    @property
    def cons_tiss(self):
        cons = self.size_value / 6.5 + 0.5
        return cons


class Coat(Wear):

    @property
    def cons_tiss(self):
        cons = 2 * self.size_value + 0.3
        return cons


size, height = 2, 1.7
s = Suit(height)
c = Coat(size)

print(f'Суммарный расход ткани:  {s.cons_tiss + c.cons_tiss}')
