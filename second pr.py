class Person:
    def __init__(self, fio, age):
        self.fio = fio
        self.age = age

    def __str__(self):
        return f"Фио - {self.fio} Возраст - {self.age}"


class Driver(Person):
    def __init__(self, fio, age, xp):
        super().__init__(fio, age)
        self.experience = xp

    def __str__(self):
        return f"Тип - {self.__class__.__name__} ФИО - {self.fio} " \
               f"Возраст - {self.age} Опыт вождения - {self.experience}"


class Engine:
    def __init__(self, force, company):
        self.force = force
        self.company = company

    def __str__(self):
        return f"Тип - {self.__class__.__name__} Производитель - {self.company} " \
               f"Сила - {self.force}"


class Car:
    def __init__(self, brand, driver, engine):
        self.brand = brand
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Машина поехала вперед")

    def stop(self):
        print("Машина остановилась")

    def turn_right(self):
        print("Машина повернула на 90 градусов направо")

    def turn_left(self):
        print("Машина повернула на 90 градусов налево")

    def __str__(self):
        return f"Тип - {self.__class__.__name__} Бренд - {self.brand} " \
               f"Водитель - {self.driver} Двигатель - {self.engine}"


class Lorry(Car):
    def __init__(self, brand, driver, engine, carrying=False):
        super().__init__(brand, driver, engine)
        self.carrying = carrying

    def __str__(self):
        return f"Тип - {self.__class__.__name__} Бренд - {self.brand} " \
               f"Водитель - {self.driver} Двигатель - {self.engine}" \
               f"Загружен - {self.carrying}"


class SportCar(Car):
    def __init__(self, brand, driver, engine, speed=0):
        super().__init__(brand, driver, engine)
        self.speed = speed

    def start(self):
        self.speed = 100
        super().start()
        print("Разгоняюсь до 100 км/ч")

    def stop(self):
        super().stop()
        self.speed = 0

    def __str__(self):
        return f"Тип - {self.__class__.__name__} Бренд - {self.brand} " \
               f"Водитель - {self.driver} Двигатель - {self.engine}" \
               f"Скорость - {self.speed}"


engine1 = Engine(700, "Mercedes")
engine2 = Engine(1400, "Lamborgini")
obj1 = Driver("БНА", 20, "3 года")
obj2 = Driver("ОВА", 40, "10 лет")
car1 = Lorry("Мерседес", obj1, engine1)
car2 = SportCar("Лада", obj2, engine2)
print(obj1)
print(obj2)
print(car1)
print(car2)
car2.start()
car2.turn_right()
car2.turn_right()
car2.stop()
