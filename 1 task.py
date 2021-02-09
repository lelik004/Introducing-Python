class Matrix:
    def __init__(self, list_for_m):
        self.list_for_m = list_for_m

    def __add__(self, other):
        self.matrix_sum = []
        for sublist in zip(self.list_for_m, other.list_for_m):
            self.aux_list = []
            for numbers in zip(sublist[0], sublist[1]):
                self.aux_list.append(sum(numbers))
            self.matrix_sum.append(self.aux_list)

        print('Сумма матриц:')
        print('\n'.join(['\t'.join(['%d' % i for i in row]) for row in self.matrix_sum]))

    def __str__(self):
        return '\n'.join(['\t'.join(['%d' % i for i in row]) for row in self.list_for_m])


list_for_m1 = [[6, 2, 1], [4, 5, 6], [3, 5, 10]]
list_for_m2 = [[2, 8, 9], [2, 51, 32], [5, 8, 1]]

m1 = Matrix(list_for_m1)
m2 = Matrix(list_for_m2)

print(f'Матрица №1:\n{m1}')
print(f'Матрица №2:\n{m2}')
m3 = m1 + m2
