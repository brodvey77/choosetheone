# class Car:
#     wheels_number = 4
#
#     def __init__(self,name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
# mazda_car = Car(name='Mazda CX7', color='red', year=2013, is_crashed=True)
#
# print(mazda_car.name, mazda_car.year, mazda_car.is_crashed)
#
# bmw_car = Car(name='BMW', color='black', year=2015, is_crashed=False)
#
# print(bmw_car.name, bmw_car.is_crashed, bmw_car.wheels_number)
#
# number_of_wheels = Car.wheels_number * 3
#
# print(number_of_wheels)

# class Car:
#     wheels_number = 4
#
#     def __init__(self,name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self, city):
#         print(self.name + " is driving from" + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#
# opel_car = Car('OPEL ASTRA', 'pink', 2000, False)
# mazda_car = Car('MAZDA CX7', 'RED', 1983, True)
# mazda_car.drive(' Moscow')
# opel_car.drive(' Kolomna')
# opel_car.change_color('magenta')
# print(opel_car.color)

# print(opel_car.wheels_number, opel_car.color, opel_car.name)

# class Circule:
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#         self.circumference = 2 * Circule.pi * self.radius
#
#     def get_area(self):
#         return self.pi * (self.radius ** 2)
#
#     # def get_circumference(self):
#     #     return 2 * self.pi * self.radius
#
# circule_1 = Circule()
# print(circule_1.get_area())
# print(circule_1.circumference)
# circule_2 = Circule(12)
# print(circule_2.get_area())
# print(circule_2.circumference)

# class Gamer:
#     active_gamer = 0
#
#     @classmethod
#     def get_active_gamers(cls):
#         return Gamer.active_gamer
#
#     @classmethod
#     def gamer_from_string(cls, data_string):
#         nickname, age, level, points = data_string.split(',')
#         return cls(nickname, age, level, points)
#
#     def __init__(self, nickname, age, level, points):
#         self.nickname = nickname
#         self.age = age
#         self.level = level
#         self.points = points
#         Gamer.active_gamer += 1
#
#     def logout(self):
#         Gamer.active_gamer -= 1
#
#     def get_nickname(self):
#         return self.nickname
#
#     def get_age(self):
#         return self.age
#
#     def get_level(self):
#         return self.level
#
#     def get_points(self):
#         return self.points
#
#     def is_adult(self):
#         return self.age >= 18
#
#     def get_adult_level_permition(self):
#         if self.is_adult():
#             print("You can go to adult level")
#         else:
#             print('You can`t go to adult level')


# print(Gamer.active_gamer)
#
# gamer_1 = Gamer('Pistrushka', 37, 12, 50)
#
# print(Gamer.active_gamer)
#
# gamer_2 = Gamer('Govnodav', 17, 5, 20)
#
#
#
# print(gamer_1.get_age())
# gamer_1.get_adult_level_permition()
#
# print(gamer_2.get_age())
# gamer_2.get_adult_level_permition()
#
# print(Gamer.active_gamer)
#
# gamer_1.logout()
# print(Gamer.active_gamer)
# print(Gamer.get_active_gamers())

# opasny = Gamer.gamer_from_string('Opasny, 40, 12, 20')
# war = Gamer.gamer_from_string('War, 12, 3, 10')
#
# print(opasny.get_age())
# print(war.get_age())
# print(Gamer.active_gamer)

# my_dict = dict.fromkeys((1, 2, 3), ('apple', 'orange', 'banana'))
# print(my_dict)

# class Car:
#     wheels_number = 4
#
#     def __init__(self,name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
#
#     def drive(self, city):
#         print(self.name + " is driving from " + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#         print('color is changed to ' + new_color)
#
# class Truck(Car):
#
#     wheels_number = 6
#
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self,name, color, year, is_crashed)
#         print('Truck is created')
#
#     def drive(self, city):
#         print('Truck ' + self.name + " is driving from " + city)
#
#     def load_cargo(self, weight):
#         print('The cargo is loaded, weight is ' + str(weight))
#
#
# man_truck = Truck('MAN', 'white', 2020, False)
#
# man_truck.drive('Monako')
# print(man_truck.wheels_number)
# print(man_truck.color)
# man_truck.change_color('red')
# print(man_truck.color)
# man_truck.load_cargo(2000)

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError('Class successor '
#                                   'must implement this method')
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying woof')
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying meow')
#
# class Mouse(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying pipipi')
#
# class Fish(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = name
#
#     def speak(self):
#         print(self.name + ' is saying nothing')
#
# spyke = Dog('Spyke')
# tom = Cat('Tom')
# jerry = Mouse('Jerry')
# freddy = Fish('Freddy')
#
# pet_list = [spyke, tom, jerry, freddy]
#
# for pet in pet_list:
#     pet.speak()
#
# def pet_voice(pet):
#     pet.speak()
#
# pet_voice(spyke)
# pet_voice(tom)
# pet_voice(jerry)
#
#
# pet_voice(freddy)


# class Swimmable:
#     def __init__(self, name):
#         print('Method init() of Swimmable')
#         self.name = name
#
#     def greetings(self):
#         print(f'Hello, my name is {self.name} and I can swim')
#
#     def swim(self):
#         print('I`m swiming')
#
#
# class Wolkable:
#     def __init__(self, name):
#         print('Method init() of Wolkable')
#         self.name = name
#
#     def greetings(self):
#         print(f'Hello, my name is {self.name} and I can walk')
#
#     def walk(self):
#         print('I`m wolking')
#
#
# class Flyable:
#     def __init__(self, name):
#         print('Method init() of Flyable')
#         self.name = name
#
#     def greetings(self):
#         print(f'Hello, my name is {self.name} and I can fly')
#
#     def fly(self):
#         print('I`m flying')
#
#
# class GameCharacter(Wolkable, Flyable, Swimmable):
#     def __init__(self, name):
#         print('Method init() of GameCharacter')
#         self.name = name
#         Swimmable.__init__(self, name)
#         Flyable.__init__(self, name)
#         Wolkable.__init__(self, name)


    # def greetings(self):
    #     print(f'Hello, my name is {self.name}')




# james = GameCharacter('James')
# james.greetings()
# james.fly()
# james.walk()
# james.swim()
#
# print(isinstance(james, Wolkable))
# print(isinstance(james, Swimmable))
# print(isinstance(james, Flyable))
# print(isinstance(james, Gamecharacter))
# print(isinstance(james, dict))
# print(isinstance(5.5, object))


# class A:
#     def some_method(self):
#         print('Method of class A')
#
#
# class B(A):
#     def some_method(self):
#         print('Method of class B')
#
#
# class C(A):
#
#     def some_method(self):
#         print('Method of class C')
#
#
# class D(B, C):
#     @classmethod
#     def some_method(cls):
#         print('Method of class D')
#
# print(D.__mro__)
# print(D.mro())
#
# help(D)
#
# some_object = D()
# some_object.some_method()
# magic methods

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.age + other.age

    def __del__(self):
        print('Person object with name ' + self.first_name + ' is deleted')

jack = Person('Jack', 'Black', 23)

jane = Person('Jane', 'Smith', 18)

print(jane + jack)
print(len([1, 2, 3, 4, 5]))
print(jack)
print(len(jack))
#
# del (jack)
# # print(jack)
#
# x = 5
# y = 3
# a = '5'
# b = '5'
# print(x.__add__(y))
# print(a.__add__(b))

