# try:
#     num1 = int(input())
#     num2 = int(input())
#     print('Частное чисел равно', num1 / num2)
# except:
#     print('Вы ввели некорректные данные!')
#
# print('Работа программы завершена!10')
#
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print('Частное чисел равно', num1 / num2)
# except ValueError:
#     print('Нужно было ввести числа!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
#
# print('Работа программы завершена!')

# try:
#     numbers = [1, 2, 3, 4] + '5'
#     print(numbers)
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except TypeError:
#     print('TypeError')

# try:
#     a = float('10')
#     b = float('7.5')
#     print(a * b)
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# except KeyError:
#     print('KeyError')
# except IndexError:
#     print('IndexError')
# except NameError:
#     print('NameError')

# def fantastic_function(collection):
#     return collection[0] + collection[-1]
#
# try:
#     numbers = ['1', 2, '3', 4, 5]
#     print(fantastic_function(numbers))
# except:
#     print('Произошла ошибка')

# blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2},
#               {'Likes': 13, 'Comments': 2, 'Shares': 1},
#               {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
#               {'Comments': 4, 'Shares': 2},
#               {'Photos': 8, 'Comments': 1, 'Shares': 1},
#               {'Photos': 3, 'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
#
# for post in blog_posts:
#     try:
#         total_likes += post['Likes']
#     except:
#         total_likes = total_likes - 1
#
# print(total_likes)

# food = ['chocolate', 'chicken', 'corn', 'sandwich', 'soup', 'potatoes', 'beef', 'lox', 'lemonade']
# fifth = []
#
# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError:
#         fifth.append('_')
#
# print(fifth)


# numbers = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]
#
# remainders = []
#
# for number in numbers:
#     try:
#         remainders.append(36 % number)
#     except ZeroDivisionError:
#         pass
# print(remainders)

# import sys
# s, counter = 0, 0
# for line in sys.stdin:
#     try:
#         s += int(line)
#     except ValueError:
#         try:
#             s += float(line)
#         except ValueError:
#             counter += 1
# print(s)
# print(counter)

# try:
#     x = 1 / 1
# except:
#     print('Произошла ошибка')
# else:
#     print('Ошибок не произошло')

# try:
#     numbers = [1, 2, 3]
#     print(numbers * 2)
# except:
#     print('Произошла ошибка')
# finally:
#     print('Завершение программы')


try:
    numbers = (1, 2, 3)
    print(numbers + (4))
except:
    print('Произошла ошибка')
finally:
    print('Завершение программы')