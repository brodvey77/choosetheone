# def get_digits(number: int|float) -> list[int]:
#     return [int(i) for i in str(number) if i.isdigit()]
#
#
# print(get_digits(16733))
# print(get_digits(13.909934))


# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     d = {}
#     l = ('name', 'top_grade')
#     maxi_grade = (grades['name'],max(grades['grades']))
#     d = dict(zip(l,maxi_grade))
#     return d
#
# def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
#     return {'name': grades['name'], 'top_grade': max(grades['grades'])}
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# info = {'name': 'Timur', 'grades': [30, 57, 99]}
#
# print(top_grade(info))
#
# # TEST_2:
# print(top_grade({'name': 'Ruslan', 'grades': [19, 48, 86, 45, 32]}))
#
# # TEST_3:
# annotations = top_grade.__annotations__
#
# print(annotations['grades'])
#
# # TEST_4:
# info = {'name': 'Artur', 'grades': [100, 28, 3, 97, 5]}
# result = top_grade(info)
#
# print(result)
#
# # TEST_5:
# info = {'name': 'Dima', 'grades': [99, 99, 99, 99, 99]}
#
# print(top_grade(info))
#
# # TEST_6:
# info = {'name': 'Vlad', 'grades': [22, 22, 66, 66, 5]}
#
# print(top_grade(info))
#
# # TEST_7:
# info = {'name': 'Egor', 'grades': [33, 33, 33, 64, 5]}
#
# print(top_grade(info))
#
# # TEST_8:
# print(*top_grade.__annotations__.values())
#
# # dict[str, str | list[int]] dict[str, str | int]
#
# # TEST_9:
# info = {'name': 'Roman', 'grades': [40]}
#
# print(top_grade(info))
#
# from collections import deque
# def cyclic_shift(numbers: list[int|float], step: int) -> None:
#     temp = deque(numbers)
#     temp.rotate(step)
#     numbers[:] = [i for i in temp]
#
#
#
#
# numbers = [1, 2, 3, 4, 5]
# cyclic_shift(numbers, 1)
#
# print(numbers)
# Sample Output 1:
#
# [5, 1, 2, 3, 4]


# def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int|float]]:
#     d = {}
#     l = len(matrix)
#     for i in range(1, l + 1):
#         d[i] = matrix[i - 1]
#     return d


# def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
#     return dict(enumerate(matrix, 1))

# # TEST_1:
# matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]
#
# print(matrix_to_dict(matrix))
#
# # TEST_2:
# matrix = [[5.1, 6, 7.94]]
#
# print(matrix_to_dict(matrix))
#
# # TEST_3:
# annotations = matrix_to_dict.__annotations__
#
# print(annotations['return'])
#
# # TEST_4:
# matrix = [[3, 66, 71], [8.0, 3.1, 2.88], [13, 22, 76], [19, 21, 22]]
#
# print(matrix_to_dict(matrix))
#
# # TEST_5:
# print(*matrix_to_dict.__annotations__.values())
#
# # TEST_6:
# matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
#
# print(matrix_to_dict(matrix))
#
# # TEST_7:
# matrix = [[1, 2, 3, 4, 5, 6, 7, 8]]
#
# print(matrix_to_dict(matrix))