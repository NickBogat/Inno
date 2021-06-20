class Point(object):
    def __new__(cls, *args, **kwargs):
        print("Я начал в 0 0")
        return super(Point, cls).__new__(cls)

    def __del__(self):
        print(f"Я закончил в {self.x} {self.y}")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self._z = z

    def delta(self, dx, dy):
        self.x += dx
        self.y += dy


obj = Point(1, 2, 3)
Point.color = "red"


class Warcraft:
    def __init__(self):
        self.game_type = "strategy"


class Dota(Warcraft):
    def __int__(self):
        print(f"my game type - {super(self).__init__()}")
