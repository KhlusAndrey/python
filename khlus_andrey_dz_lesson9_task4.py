"""
4.	Реализуйте базовый класс Car:
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
    turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
    40 (WorkCar) должно выводиться сообщение о превышении скорости.

 Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_posible = is_polise

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        print(f'Машина {self.name} повернула')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость превышена! Ваша скорость: {self.speed}')


class SportCar(TownCar):
    pass


class WorkCar(SportCar):
    def __init__(self, speed, color, name, is_polise):
        super().__init__(speed, color, name, is_polise)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость превышена! Ваша скорость: {self.speed}')


class PoliceCar(WorkCar):
    pass

# Как правильнее передовать наследование классам, последовательно TownCar(Car)>>SportCar(TownCar)
# >>WorkCar(SportCar)>>PoliceCar(WorkCar) или ссылаться на один базовый родительский класс TownCar(Car)>>SportCar(Car)
# # >>WorkCar(Car)>>PoliceCar(Car)?


car = Car(60, 'red', 'opel', True)
town_car = TownCar(65, 'red', 'reno', False)
work_car = WorkCar(80, 'red', 'kia', True)

car.go()
print(car.is_posible)
car.show_speed()
town_car.show_speed()
town_car.turn()
print(town_car.is_posible)
work_car.show_speed()
work_car.stop()
