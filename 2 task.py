class Road:

    def __init__(self, length, width, high, weight_of_1cm=25):
        self.length = length
        self.width = width
        self.high = high
        self.weight_of_1cm = weight_of_1cm

    def asphalt_weight(self):
        return self.length * self.width * self.high * self.weight_of_1cm // 1000


length = int(input('Введите длину дороги: '))
width = int(input('Введите ширину дороги: '))
high = int(input('Введите высоту дороги: '))

a = Road(length, width, high)
print(a.asphalt_weight())
