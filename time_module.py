# import time
#
# for i in range(1, 11):
#     time.sleep(i)
#
# print('Hello World!')
import time


# import time
#
# start_time = time.time()
#
# for i in range(5):
#     print(i)
#     time.sleep(1)
#
# end_time = time.time()
#
# elapsed_time = end_time - start_time
# print(f'Время работы программы = {elapsed_time}')

# Функция monotonic()
# Для измерения времени выполнения программы идеально подходит функция monotonic(), доступная на всех ОС (начиная с Python 3.5), так как ее результат не зависит от корректировки системных часов.
#
# Функция monotonic_ns() похожа на monotonic(), но возвращает время в наносекундах. Работает не на всех операционных системах.
#
# Используемый таймер в функции monotonic() никогда не вернет при повторном вызове значение, которое будет меньше значения, полученного при предыдущем вызове. Это позволяет избежать многих ошибок, а также неожиданного поведения.
#
# В следующем примере демонстрируется применение функции monotonic() для получения текущего времени, чтобы в итоге выявить, как долго работал блок кода.
#
# Приведенный ниже код:
#
# import time
#
# start_time = time.monotonic()
#
# for i in range(5):
#     print(i)
#     time.sleep(0.5)
#
# end_time = time.monotonic()
#
# elapsed_time = end_time - start_time
# print(f'Время работы программы = {elapsed_time}')
# выводит (время работы программы может незначительно отличаться):
#
# 0
# 1
# 2
# 3
# 4
# Время работы программы = 2.547000000020489
# Принцип работы и применения функции monotonic() такой же, как и у функции time(). Однако функция monotonic() дает результат, который обладает гарантированной точностью и не зависит от внешних условий.


# import time
#
# start_time = time.perf_counter()
#
# for i in range(5):
#     print(i)
#     time.sleep(1)
#
# end_time = time.perf_counter()
#
# elapsed_time = end_time - start_time
# print(f'Время работы программы = {elapsed_time}')

# import time
#
# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c
# def calculate_it(func, *args):
#     start_time = time.time()
#     a = func(*args)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     return a, elapsed_time
#
# print(calculate_it(add, 1, 2, 3))


# import time
#
# def get_the_fastest_func(funcs: list, arg):
#     l = []
#     for c in funcs:
#         start_time = time.time()
#         result = c(arg)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         l.append(elapsed_time)
#     minimum = min(l)
#     s = l.index(minimum)
#     return funcs[s]



