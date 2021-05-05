"""
3.	Реализовать базовый класс Worker (работник):
●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия»,
    например, {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
    (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
    значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Имя сотрудника {self.name} {self.surname}')
        return self.name + ' ' + self.surname

    def get_total_income(self):
        print(f'Доход {self.name} {self.surname} с учетом премии {self._income["wage"]+self._income["bonus"]}')
        return self._income["wage"]+self._income["bonus"]


position = Position('Ivan', 'Ivanov', 'director', 1000, 300)
print(position.get_full_name())
print(position.get_total_income())
