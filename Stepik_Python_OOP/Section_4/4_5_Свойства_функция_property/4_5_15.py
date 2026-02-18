
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_full_name(self, fullname):
        self.name, self.surname = fullname.split()

    fullname = property(get_full_name, set_full_name)



person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)

