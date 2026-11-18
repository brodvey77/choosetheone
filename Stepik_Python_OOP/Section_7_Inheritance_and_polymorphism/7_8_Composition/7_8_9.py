
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=()):
        self.items = list(items)


    def add(self, goods):
        self.items.append(goods)


    def total(self):
        return sum(i.price for i in self.items)

    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]

    def __str__(self) -> str:
        return '\n'.join(str(item) for item in self.items)




item1 = Item('Yoga Mat', 130)
item2 = Item('Flannel Shirt', 22)

print(item1)
print(item2)