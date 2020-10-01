# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'i', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')

# print('I', 'like', 'Python', sep='***', end='')
#

# name = input()
# print('Привет, ' + name + '!', end='')

# num_1 = int(input())
# num_2 = num_1 + 1
# num_3 = num_2 + 1
#
# print(num_1, num_2, num_3, sep='\n')

# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
# print(num_1 + num_2 + num_3)

# dlina_rebra = int(input())
# obem_kuba = dlina_rebra ** 3
# square_of_cube = 6 * dlina_rebra ** 2
#
# print('Объем =', obem_kuba)
# print('Площадь полной поверхности =', square_of_cube)

# f(a,b) = 3(a+b)3 + 275b 2 − 127a − 41

# a = int(input())
# b = int(input())
#
# c = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41
#
# print(c)

# num_1 = int(input())
# print('Следующее за числом', num_1, 'число:', num_1 + 1)
# print('Для числа', num_1, 'предыдущее число:', num_1 - 1)

# monitor = int(input())
# system_box = int(input())
# keyboard = int(input())
# mouse = int(input())
#
# print(monitor * 3 + system_box * 3 + keyboard * 3 + mouse * 3)

# number_1, number_2 = int(input()), int(input())
#
# print(number_1, '+', number_2, '=', (number_1 + number_2))
# print(number_1, '-', number_2, '=', (number_1 - number_2))
# print(number_1, '*', number_2, '=', (number_1 * number_2))

# a1, d, n = int(input()),int(input()),int(input())
# an = a1 + d * (n - 1)
# print(an)

# x = int(input())
# print(x, '---', x * 2, '---', x * 3, '---', x * 4, '---', x * 5, sep='')


#
# a = 82 // 3 ** 2 % 7
# print(a)

# b1, q, n = int(input()),int(input()),int(input())
# bn = b1 * q ** (n - 1)
# print(bn)


# cm = int(input())
# print(cm // 100)


# n = int(input())
# k = int(input())
# print(k // n)
# print(k % n)

# n = int(input())
# dead = n // 2
# life = n - dead
# print(life)

# a = int(input())  # вводимое значение
# b = (a + 3) // 4
# print (b)

# minute = int(input())
#
# print(minute, 'мин - это', minute // 60, 'час', minute % 60, 'минут')

# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
# print('Число десятков =', first_digit)
# print('Число единиц =', last_digit)


# num = int(input())
# digit3 = num % 10
# digit2 = (num // 10) % 10
# digit1 = num // 100
# print(digit1, digit2, digit3, sep=',')

# number = int(input())
#
# first_digit = number % 10
# second_digit = (number % 100) // 10
# third_digit = number // 100
#
# # Сумма цифр = 6
# # Произведение цифр = 6
#
# print('Сумма цифр =', first_digit + second_digit + third_digit )
# print('Произведение цифр', first_digit * second_digit * third_digit)

# number = int(input())
# c = number % 10
# b = (number % 100) // 10
# a = number // 100
#
# print(a, b, c, sep='')
# print(a, c, b, sep='')
# print(b, a, c, sep='')
# print(b, c, a, sep='')
# print(c, a, b, sep='')
# print(c, b, a, sep='')

# Цифра в позиции тысяч равна 3
# Цифра в позиции сотен равна 2
# Цифра в позиции десятков равна 8
# Цифра в позиции единиц равна 1

# number = int(input())
# d = number % 10
# c = (number % 100) // 10
# b = (number % 1000) // 100
# a = number // 1000
#
# print('Цифра в позиции тысяч равна', a)
# print('Цифра в позиции сотен равна', b)
# print('Цифра в позиции десятков равна', c)
# print('Цифра в позиции единиц равна', d)

# print('*' * 17)
# print('*', ' ' * 13, '*')
# print('*', ' ' * 13, '*')
# print('*' * 17)

# a = int(input())
# b = int(input())
# print('Квадрат суммы', a, 'и', b, 'равен', (a + b) ** 2)
# print('Сумма квадратов', a, 'и', b, 'равна', a**2 + b**2)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# print(a ** b + c ** d)

# a = int(input())
# aa = 10*a + a
# aaa = 100*a + aa
# print(a + aa + aaa)
# print(a)
# print(aa)
# print(aaa)