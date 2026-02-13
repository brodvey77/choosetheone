import math

class Circle:
    def __init__(self, radius ) -> None:
        self._radius = radius
        self._diameter  = radius * 2
        self._area = math.pi * radius ** 2


    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


if __name__ == '__main__':
    circle = Circle(5)
    print(circle.get_radius())
    print(circle.get_diameter())
    print(circle.get_area())
