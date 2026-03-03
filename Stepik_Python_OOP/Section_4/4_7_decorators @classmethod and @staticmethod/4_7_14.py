# class Pet:
#     pets = []
#     def __init__(self, name):
#         self.name = name
#         Pet.pets.append(self)
#
#     @classmethod
#     def first_pet(cls):
#         if len(cls.pets)> 0:
#             return cls.pets[0]
#
#     @classmethod
#     def last_pet(cls):
#         if len(cls.pets) > 0:
#             return cls.pets[-1]
#
#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.pets)
#
#
# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')
#
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())
#
#
# class Pet:
#     # Атрибуты класса для хранения информации о всех созданных экземплярах
#     _first = None  # самый первый созданный экземпляр
#     _last = None  # самый последний созданный экземпляр
#     _count = 0  # количество созданных экземпляров
#
#     def __init__(self, name):
#         self.name = name
#
#         # Обновляем информацию о созданных экземплярах
#         Pet._count += 1
#
#         # Если это первый созданный экземпляр
#         if Pet._first is None:
#             Pet._first = self
#
#         # Обновляем последний созданный экземпляр
#         Pet._last = self
#
#     @classmethod
#     def first_pet(cls):
#         """Возвращает самый первый созданный экземпляр класса Pet"""
#         return cls._first
#
#     @classmethod
#     def last_pet(cls):
#         """Возвращает самый последний созданный экземпляр класса Pet"""
#         return cls._last
#
#     @classmethod
#     def num_of_pets(cls):
#         """Возвращает количество созданных экземпляров класса Pet"""
#         return cls._count

class Pet:
    _first = None
    _last = None
    _counter = 0
    def __init__(self, name):
        self.name = name
        Pet._counter += 1

        if Pet._first is None:
            Pet._first = self

        Pet._last = self

    @classmethod
    def first_pet(cls):
        return cls._first

    @classmethod
    def last_pet(cls):
        return cls._last

    @classmethod
    def num_of_pets(cls):
        return cls._counter



print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())