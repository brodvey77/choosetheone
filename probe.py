# build_in functions
# x = print('Hello!')
# y = set()
# print(type(x))
# print(type(y))
#
# print(x)
# print(y)

# build_in method

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
#
# my_list.clear()
# print(my_list)


# def greeting():
#     '''
# print Hello text
#     :return: non return
#     '''
#     print('Hello!')
# greeting()
#
# help(greeting)

# def print_greeting_with_name(name = 'Name'):
#     '''
# :param Name
#     :return: None
#     '''
#     print('Hello ' + name + '!')
#
# x = print_greeting_with_name('Jack')
# print(x)

# def sum_of_two_num(a=0, b=0):
#     '''
#
#     :param a: first addend
#     :param b: second addend
#     :return: sum of a and b
#     '''
#     return a + b
# x = sum_of_two_num(3, 9)
# x = sum_of_two_num()
# print(x)

# def is_hello_in_text(text):
#     if 'hello' in text.lower():
#         return True
#     else:
#         return False
# print(is_hello_in_text('Say Hello everyone'))

# def is_hello_in_text(text):
#     return 'hello' in text.lower()
# print(is_hello_in_text('Say Hello everyone'))
#
#
# def is_string_in_text(string, text):
#     return string in text
# print(is_string_in_text('he', 'The apple'))


# def greeting_depend_of_gender(name, gender):
#     if gender == 'male':
#         print('Hello ' + name + '! you look great')
#         return gender
#     elif gender == 'female':
#         print('Hello ' + name + '! you are so cool!')
#         return gender
#     else:
#         print('Hello ' + name + '! you bustard')
#         return gender


# returned_value = greeting_depend_of_gender('Jack', 'male')
# returned_value = greeting_depend_of_gender('Vika', 'female')
# returned_value = greeting_depend_of_gender('koko', 'boo')

# def ten_percent_with_args(*args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product * 0.1

# print(ten_percent_with_args(10, 30, 20, 40, 6, 8))

# def ten_percent_with_args(percent, *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product /100 *percent
#
# print(ten_percent_with_args(15, 10, 20))

#
# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
# func_with_kwargs(first=1, second=2, third=3)

# def func_with_kwargs(**kwargs):
#     print(kwargs)
#
# func_with_kwargs(first=1, second=2, third=3)


# def hello_with_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello!, Nice to meet you,{}'.format(kwargs['name']))
#     else:
#         print('Hello!, what is your name?')
#
#
# hello_with_kwargs(gender='male', age=36, name='Jack')
# hello_with_kwargs(gender='male', age=36)


# def hello_with_greetings_kwargs(greeting, **kwargs):
#     if 'name' in kwargs:
#         print('{}!, Nice to meet you,{}'.format(greeting, kwargs['name']))
#     else:
#         print('{}!, what is your name?'.format(greeting))
#
#
# hello_with_greetings_kwargs('Hello', gender='male', age=36, name='Jack')
# hello_with_greetings_kwargs('Hi', gender='male', age=36)

# def funk_args_kwargs(*args, **kwargs):
#     print('I would like {} {}'.format(args[0], kwargs['drink']))
#
# funk_args_kwargs('one', 'two', 'tree', drink='milk', color='white', food='meat')

# def cat_voice():
#     return 'Meow!' * 2
#
# def dog_voice():
#     return 'Woof!' * 2
#
#
# cat = cat_voice()
# dog = dog_voice()
#
# print(cat)
# print(dog)
#
# def get_voice(text):
#     return text + '!'
#
# voice = get_voice('hahaha')
# print(voice)


# def gen_number(a, b):
#     number_list = list(range(a, b + 1))
#     odd_number_list = [number for number in number_list if number % 2 == 1]
#     return odd_number_list
#
# x = gen_number(1, 10)
# print(x)

# def gen_number_2(a, b):
#     number_list = list(range(a, b + 1))
#     odd_number_list = []
#     for number in number_list:
#         if number % 2 == 1:
#             odd_number_list.append(number)
#     return odd_number_list
#
# x = gen_number_2(1, 100)
#
# print(x)


# def is_cat_here(*args):
#     args_in_lower_case = [str(argument).lower() for argument in list(args)]
#     if 'cat' in args_in_lower_case:
#         return True
#     else:
#         return False
#
# x = is_cat_here('dog')
#
# print(x)


# def is_item_here(item, *args):
#     if item in args:
#         return True
#     else:
#         return False
#
# print(is_item_here('Hi', 'Hello', 3 , 7, 'H'))


# def your_favorite_color(my_color, **kwargs):
#     if 'color' in kwargs:
#         print('My favourite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
#     else:
#         print('My favourite color is {}, What is your favourite color?'.format(my_color))
#
# your_favorite_color('green', color='red', car='toyota')


# class Car:
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year,
#         self.is_crashed = is_crashed
#
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#
# opel_car = Car('Opel Tigra', 'red', 2018, False)
# opel_car.drive('Paris')
#
# mazda_car = Car('Mazda CX7', 'black', 2015, True)
# mazda_car.drive('London')
# mazda_car.change_color('yellow')
# print(mazda_car.color)
#
# print(opel_car.wheels_number)
# print(opel_car.name)
# print(opel_car.year)
# print(opel_car.is_crashed)
# print(opel_car.color)

# class Circle:
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#         self.circumference = 2 * Circle.pi * self.radius
#
#     def get_area(self):
#         return self.pi * (self.radius ** 2)

# def get_circumference(self):
#     return 2 * self.pi * self.radius

# circle_1 = Circle(5)
# print(circle_1.get_area())
# print(circle_1.circumference)
# print(circle_1.get_circumference())
# circle_2 = Circle(3)
# print(circle_2.get_area())
# print(circle_2.get_circumference())
# circle_3 = Circle(5)
# circle_area = circle_3.get_area()
# print(circle_3.get_circumference())
# print(circle_area)


# class Car:
#     wheels_number = 4
#
#     def __init__(self, name, color, year, is_crashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#         print('Car is created')
#
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
#
#     def change_color(self, new_color):
#         self.color = new_color
#         print('color is changed to ' + new_color)
#
#
# class Truck(Car):
#     wheels_number = 6
#
#     def __init__(self, name, color, year, is_crashed):
#         Car.__init__(self, name, color, year, is_crashed)
#         print('Track is created')
#
#     def drive(self, city):
#         print('Truck ' + self.name + ' is driving to ' + city)
#
#     def load_cargo(self, weight):
#         print('The cargo is loaded. Weight is ' + str(weight) + ' kg')
#
#
#
# man_truck = Truck('Man', 'cyan', 1996, True)
#
# man_truck.drive('New York')
# print(man_truck.wheels_number)
# print(man_truck.color)
# man_truck.change_color('black')
# print(man_truck.color)
# man_truck.load_cargo(2000)


a = 1411*414
b = 401*2012
c = 1466*886
d = 401*1492
e = 2273*675
f = 2273*675
g = 2329*469
h = 2273*830
i = 2012*401
j = 2273*675

print((a + b + c + d + e + f + g + h + i + j) / 1000 )










