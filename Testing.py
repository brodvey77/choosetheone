# ASSERT

# assert 2 + 2 == 4
# assert 2 + 2 == 5, '2 + 2 must equals 4'

# def devide(a, b):
#     assert b !=0, 'b must not equals 0'
#     return a / b
#
# print(devide(2, 2))
# print(devide(2, 0))


# def multiply_positive_numbers(a, b):
#     assert a > 0 and b > 0, 'a and b must be positive'
#     print(a * b)
#
# multiply_positive_numbers(3, -6)

# def get_access(pasword):
#     pasword_list = [111, 222 ,333]
#     assert int(pasword) in pasword_list, \
#         'Passwor is invalid'
#     print('You can make dangerous stuff')
#
# password_1 = input('Please input the password')
# get_access(password_1)

# UNIT TESTING

import unittest
import cool_game


class CoolGameFunctionsTest(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')

    def test_greet_enemy(self):
        self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! Hi will kill you bastard!')

    def test_eat_burgers(self):
        self.assertEqual(cool_game.eat_burgers(3), 'Mmm that was excellen'

    def test_eat_much_burgers(self):
        self.assertEqual(cool_game.eat_burgers(4), 'Ohh! I am overeate'

        if __name__ == "__main__":
            unittest.main()

