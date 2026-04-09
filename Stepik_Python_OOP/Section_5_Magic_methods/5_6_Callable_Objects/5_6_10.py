class RaiseTo:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, x: int):
        return x ** self.degree


raise_to_three = RaiseTo(3)
raise_to_four = RaiseTo(4)

print(raise_to_three(3))
print(raise_to_four(2))