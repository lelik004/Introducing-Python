class Car:

    def __init__(self, name, speed, direction, color, is_police):
        self.speed = speed
        self.direction = direction
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print(f'Машина {self.color} цвета повернула {self.direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed}')

    def is_police_meth(self):
        if self.is_police == True:
            print('Машина полицейская')
        else:
            print('Машина не полицейская')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости. Скорость автомобиля {self.speed}')
        else:
            print(f'Скорость автомобиля {self.speed}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости. Скорость автомобиля {self.speed}')
        else:
            print(f'Скорость автомобиля {self.speed}')


class PoliceCar(Car):
    is_police = True


t_car = TownCar('TownCar', 70, 'направо', 'синего', False)
t_car.go()
t_car.stop()
t_car.turn()
t_car.show_speed()
t_car.is_police_meth()

w_car = WorkCar('WorkCar', 35, 'налево', 'красного', False)
w_car.go()
w_car.stop()
w_car.turn()
w_car.show_speed()
w_car.is_police_meth()

p_car = PoliceCar('PoliceCar', 70, 'налево', 'черно-белого', True)
p_car.go()
p_car.stop()
p_car.turn()
p_car.show_speed()
p_car.is_police_meth()
