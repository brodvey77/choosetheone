class ElectricCar:
    def __init__(self, color):
        self.__color = color


car = ElectricCar('black')

car._ElectricCar__color = 'yellow'

print(car.__dict__)
print(car.__color)