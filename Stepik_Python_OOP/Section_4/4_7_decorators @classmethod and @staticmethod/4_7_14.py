class Pet:
    pets = []
    def __init__(self, name):
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls):
        if len(cls.pets)> 0:
            return cls.pets[0]

    @classmethod
    def last_pet(cls):
        if len(cls.pets) > 0:
            return cls.pets[-1]

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())




