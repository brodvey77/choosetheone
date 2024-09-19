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


