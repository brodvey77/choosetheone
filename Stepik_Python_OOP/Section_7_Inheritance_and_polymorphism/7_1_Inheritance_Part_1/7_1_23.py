class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class WaterVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass

class Motorcycle(LandVehicle):
    pass

class Bicycle(LandVehicle):
    pass

class Propeller(AirVehicle):
    pass

class Jet(AirVehicle):
    pass

print(issubclass(LandVehicle, Vehicle))
print(issubclass(WaterVehicle, Vehicle))
print(issubclass(AirVehicle, Vehicle))