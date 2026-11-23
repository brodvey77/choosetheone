
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