class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(func):
        def wrapper(*args):
            value = int(func(*args))
            a = value // 5
            b = value % 5
            final_str = a * '*****\n'
            for el in range(0, b):
                final_str += '*'
            return final_str
        return wrapper

    def __str__(self):
        return f'{self.final_str}'

    @make_order
    def __add__(self, other):
        self.cell_sum = self.num + other.num
        return self.cell_sum

    @make_order
    def __sub__(self, other):
        self.cell_sub = abs(self.num - other.num)
        return self.cell_sub

    @make_order
    def __mul__(self, other):
        self.cell_mul = self.num * other.num
        return self.cell_mul

    @make_order
    def __truediv__(self, other):
        self.cell_div = round(self.num / other.num)
        return self.cell_div


c1 = Cell(5)
c2 = Cell(8)

c_add = c1 + c2
c_sub = c1 - c2
c_mul = c1 * c2
c_div = c1 / c2

print(f'Сложение:\n{c_add}\n')
print(f'Вычитание:\n{c_sub}\n')
print(f'Умножение:\n{c_mul}\n')
print(f'Умножение:\n{c_div}\n')
