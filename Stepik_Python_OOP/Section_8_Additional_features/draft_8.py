
# from enum import Enum
#
# class TrafficLights(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3
#
#
# print(*TrafficLights)

# from enum import Enum
#
# class TrafficLights(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3
#
#
# print(list(TrafficLights))

# from enum import Enum
#
# class TrafficLights(Enum):
#     RED = 3
#     YELLOW = 2
#     GREEN = 1
#
#
# print(*sorted(TrafficLights, key=lambda x: x.name))

# from enum import Enum
#
# class TrafficLights(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3
#
#     @classmethod
#     def no_way(cls):
#         return cls.RED
#
#
# print(TrafficLights.no_way() is TrafficLights.RED)


# from enum import Enum
#
# class TrafficLights(Enum):
#     RED = 1
#     YELLOW = 2
#     GREEN = 3
#
#     def __eq__(self, other):
#         return self.value == other
#
#
# print(TrafficLights.GREEN == 3)

# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# combined1 = Color.RED | Color.GREEN
# combined2 = Color.RED | Color.GREEN | Color.BLUE
#
# print(combined1)
# print(combined2)
#
# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# combined1 = Color.RED | Color.GREEN
# combined2 = Color.RED | Color.GREEN | Color.BLUE
#
# print(type(combined1))
# print(type(combined2))


# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# combined1 = Color.RED | Color.GREEN              # 011 в двоичной записи и 3 в десятичной
# combined2 = Color.RED | Color.BLUE               # 101 в двоичной записи и 5 в десятичной
#
# print(combined1.name)
# print(combined1.value)
# print(combined2.name)
# print(combined2.value)

# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# combined = Color.RED | Color.GREEN | Color.BLUE
#
# print(combined ^ Color.RED)                      # исключаем Color.RED
# print(combined ^ Color.GREEN)                    # исключаем Color.GREEN
# print(combined ^ Color.BLUE)                     # исключаем Color.BLUE
# print(combined ^ (Color.BLUE | Color.RED))       # исключаем Color.BLUE и Color.RED

# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# print(~Color.RED)                                # все элементы Color, кроме Color.RED
# print(~Color.GREEN)                              # все элементы Color, кроме Color.GREEN
# print(~Color.BLUE)                               # все элементы Color, кроме Color.BLUE
# print(~(Color.RED | Color.GREEN))                # все элементы Color, кроме Color.RED и Color.GREEN


# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# combined1 = Color.RED | Color.GREEN
# combined2 = Color.RED | Color.GREEN | Color.BLUE
#
# print(Color.RED in combined1)
# print(Color.BLUE in combined1)
# print(combined1 in combined2)


# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# combined = ~(Color.RED | Color.GREEN | Color.BLUE)
#
# print(str(combined))
# print(repr(combined))
#
# from enum import Flag
#
# class Color(Flag):
#     RED = 1
#     GREEN = 2
#     BLUE = 4
#
#
# combined = Color.RED | Color.GREEN | Color.BLUE
#
# print(len(Color.RED))
# print(*Color.RED)
# print(len(combined))
# print(*combined)

# from enum import Flag
#
# class Permission(Flag):
#     READ = 1
#     WRITE = 2
#     EXECUTE = 4
#
#
# print(Permission.READ | Permission.WRITE)

# from enum import Flag
#
# class Permission(Flag):
#     READ = 1
#     WRITE = 2
#     EXECUTE = 4
#
#
# READ_WRITE = Permission.READ | Permission.WRITE
#
# print(READ_WRITE.value)

# from enum import Flag
#
# class Permission(Flag):
#     READ = 1
#     WRITE = 2
#     EXECUTE = 4
#
#
# READ_WRITE = Permission.READ | Permission.WRITE
#
# print(READ_WRITE & Permission.EXECUTE)

# from enum import Flag, auto
#
# class Permission(Flag):
#     READ = auto()
#     WRITE = auto()
#     EXECUTE = auto()
#
#
# print(~Permission.EXECUTE)

# from enum import Flag, auto
#
# class Permission(Flag):
#     READ = auto()
#     WRITE = auto()
#     EXECUTE = auto()
#
#
# READ_WRITE = Permission.READ | Permission.WRITE
#
# print(~READ_WRITE)