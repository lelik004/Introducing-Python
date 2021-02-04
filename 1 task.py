from time import sleep


class TrafficLight:

    def running(self):
        while True:
            self.__color = 'Красный'
            print(self.__color)
            sleep(7)
            self.__color = 'Желтый'
            print(self.__color)
            sleep(2)
            self.__color = 'Зелёный'
            print(self.__color)
            sleep(10)


a = TrafficLight()
print(a.running())
