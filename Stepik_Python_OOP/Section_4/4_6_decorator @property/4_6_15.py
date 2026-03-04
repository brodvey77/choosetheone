class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant < 0:
            return None
        return (-self.b - discriminant ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant < 0:
            return None
        return (-self.b + discriminant ** 0.5) / (2 * self.a)

    @property
    def view(self):
        # Формируем строку в зависимости от знаков коэффициентов
        a_part = f"{self.a}x^2"

        if self.b >= 0:
            b_part = f" + {self.b}x"
        else:
            b_part = f" - {abs(self.b)}x"

        if self.c >= 0:
            c_part = f" + {self.c}"
        else:
            c_part = f" - {abs(self.c)}"

        return a_part + b_part + c_part

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, coeffs):
        self.a, self.b, self.c = coeffs


# INPUT DATA:

# TEST_1:
print('test1')
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)

# TEST_2:
print('test2')
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.x1)
print(polynom.x2)

# TEST_3:
print('test3')
polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)

# TEST_4:
print('test4')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_5:
print('test5')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_6:
print('test6')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, 0, -9)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_7:
print('test7')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 0, 0)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

# TEST_8:
print('test8')
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

# TEST_9:
print('test9')
polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.a, polynom.b, polynom.c = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

# TEST_10:
print('test10')
polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)

