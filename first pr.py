class Room:
    def __init__(self, number, level):
        self.number = number
        self.level = level

    def __str__(self):
        return f"Комната №{self.number} Тип {self.__class__.__name__}"


class ActRoom(Room):
    def __init__(self, number=1, level=1):
        super().__init__(number, level)


class BossRoom(Room):
    def __init__(self, number=2, level=4):
        super().__init__(number, level)


class TeacherRoom(Room):
    def __init__(self, number=3, level=3):
        super().__init__(number, level)


class StudyRoom(Room):
    def __init__(self, number=4, level=2):
        super().__init__(number, level)


class Person:
    def __init__(self, name, surname, feature):
        self.name = name
        self.surname = surname
        self.feature = feature
        self.access = 0

    def __str__(self):
        return f"Имя - {self.name} Фамилия - {self.surname} " \
               f"Должность - {self.__class__.__name__} Особенность - {self.feature}"

    def Enter(self, room):
        result = bool(self.access >= room.level)
        print(
            f"{self.__class__.__name__} {self.name} {self.surname} пытается войти в "
            f"{room.__class__.__name__} {room.number}: успех = {result}")


class Boss(Person):
    def __init__(self, name, surname, feature):
        super().__init__(name, surname, feature)
        self.access = 4


class Teacher(Person):
    def __init__(self, name, surname, feature):
        super().__init__(name, surname, feature)
        self.access = 3


class Pupil(Person):
    def __init__(self, name, surname, feature):
        super().__init__(name, surname, feature)
        self.access = 2


class Parents(Person):
    def __init__(self, name, surname, feature):
        super().__init__(name, surname, feature)
        self.access = 1


obj1 = Boss("Иван", "Иванов", "9 наград")
obj2 = Teacher("Вася", "Пупкин", "Любимый фильм - Титаник")
obj3 = Pupil("Петя", "Петров", "Любимый фрукт - Картошка")
obj4 = Parents("Саша", "Сашков", "Играет в воллейбол")
place1 = ActRoom()
place2 = BossRoom()
place3 = StudyRoom()
place4 = TeacherRoom()
obj4.Enter(place1)
obj4.Enter(place2)
obj4.Enter(place3)
obj4.Enter(place4)
obj1.Enter(place1)
obj2.Enter(place1)
obj3.Enter(place1)
obj4.Enter(place1)
obj3.Enter(place2)
print(obj1)
print(obj2)
print(obj3)
print(obj4)
print(place1)
print(place2)
print(place3)
