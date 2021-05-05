"""
2.	Реализовать класс Road (дорога).
●	определить атрибуты: length (длина), width (ширина);
●	значения атрибутов должны передаваться при создании экземпляра класса;
●	атрибуты сделать защищёнными;
●	определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
●	использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в
    1 см*число см толщины полотна;
●	проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""


class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._widht = _width
        self.thiknes = 5
        self.weight = 0.025

    def calk_mass_asphalt(self):
        return round(self._lenght * self._widht * self.weight * self.thiknes)


road = Road(5000, 20)
mass = road.calk_mass_asphalt()
print(f'Масса асфальта составит = {road._widht}м * {road._lenght}м * {road.weight}т/м^2 * {road.thiknes}см = {mass} т.')
