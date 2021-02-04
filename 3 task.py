class Worker:

    def __init__(self, n, s, p, i):
        self.name = n
        self.surname = s
        self.position = p
        self._income = i


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


p_с = Position('Иван', 'Иванов', 'инженер', {'wage': 50000, 'bonus': 10000})
print(p_с.get_full_name())
print(p_с.get_total_income())
