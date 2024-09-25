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


# try:
#     numbers = (1, 2, 3)
#     print(numbers + (4))
# except:
#     print('Произошла ошибка')
# finally:
#     print('Завершение программы')

#     numbers = list(filter(int, ['1', '2', '3', '4', '5']))
#
# letters = {'a': 'A', 'b': 'B', 'c': 'C'}
# result = None
#
# try:
#     result = letters['B']
# except:
#     print('Произошла ошибка')
# else:
#     print('Ошибок не произошло')
# finally:
#     print('Завершение программы')
#
# print(result)


# data = {'Dima': [0, 4, 4, 5, 2],
#         'Timur': [5, 5, 5, 5, 5],
#         'Arthur': [5, 0, 4, 4, 2]}
#
# try:
#     grades = data['Arthur']
#     try:
#         ratio = max(grades) / min(grades)
#         print(ratio)
#     except (TypeError, ValueError):
#         print('Произошла ошибка 2')
# except KeyError:
#     print('Произошла ошибка 1')

# def beegeek():
#     try:
#         return 'bee'
#     finally:
#         return 'geek'
#
# print(beegeek())

# def beegeek():
#     try:
#         value = 100
#         return value
#     finally:
#         value = 300
#
#
# print(beegeek())

# def beegeek():
#     try:
#         value = 100
#         return value
#     finally:
#         value = 300
#         return value
#
#
# print(beegeek())

# def beegeek():
#     try:
#         value = 100
#     except:
#         value = 200
#     else:
#         value = 300
#     finally:
#         return value
#
#
# print(beegeek())

# def beegeek():
#     try:
#         value = 100
#         return value
#     except:
#         value = 200
#     else:
#         value = 300
#     finally:
#         return value
#
#
# print(beegeek())

# def beegeek():
#     numbers = [1, 2, 3, 4]
#     try:
#         numbers.append(numbers[4])
#         return numbers
#     except:
#         numbers.append(numbers[3])
#         return numbers
#     finally:
#         numbers.append(numbers[2])
#
#
import calendar

# c_m = {k:v for k,v in enumerate((calendar.month_name)[1:], 1)}
#
# def get_mounth(n):
#     try:
#         n = int(n)
#         m = c_m[n]
#         return m
#     except KeyError:
#         return 'Введено число из недопустимого диапазона'
#     except:
#         return 'Введено некорректное значение'
#
#
#
#
# res = input()
# print(get_mounth(res))



# def add_to_list_in_dict(data, key, element):
#     try:
#         data.get(key, 0).append(element)
#         print(data)
#     except:
#         data[key] = [element]
#         print(data)
#
#
# data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# add_to_list_in_dict(data, 'c', 7)
#
#
# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key].append(element)
#     except KeyError:
#         data[key] = [element]

# def add_to_list_in_dict(data, key, element):
#     try:
#         data[key]
#     except KeyError:
#         data[key] = []
#     finally:
#         data[key].append(element)

