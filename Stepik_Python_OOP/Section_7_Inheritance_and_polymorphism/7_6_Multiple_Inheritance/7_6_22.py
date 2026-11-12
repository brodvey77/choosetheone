
def get_method_owner(cls, method: str):
    for i in cls.mro():
        if method in i.__dict__:
            return i





def get_method_owner(cls, method):
    for c in cls.mro():
        result = c.__dict__.get(method)
        if result:
            return c
    return None



def get_method_owner(cls, method: str):
    # Проверяем, что cls — именно класс (не экземпляр)
    if not isinstance(cls, type):
        raise TypeError("cls должен быть классом")

    # print('cls.__mro__:', cls.__mro__)
    # Идём по MRO: от самого класса до object
    for base in cls.__mro__:
        # print('base:', base, 'base.__dict__:', base.__dict__)
        # В __dict__ лежат атрибуты, определённые именно в этом классе
        if method in base.__dict__:
            return base

    # Если ни в одном классе из иерархии метод не найден
    return None



# class A:
#     def m(self):
#         pass
#
#
# class B(A):
#     pass
#
#
# print(get_method_owner(B, 'm'))


# print("_________________________")
#
class A:
    def m(self):
        pass


class B(A):
    def m(self):
        pass


print(get_method_owner(B, 'm'))

print("_________________________")
#
#
class A:
    pass


class B(A):
    pass


print(get_method_owner(B, 'm'))