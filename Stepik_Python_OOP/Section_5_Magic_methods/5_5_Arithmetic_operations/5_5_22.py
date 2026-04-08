#
#
#
# class Queue:
#     def __init__(self, *args):
#        elements = []
#        for i in args:
#            elements.extend(str(i).split(','))
#        self._elements = elements
#
#     def __str__(self):
#         return ' -> '.join(self._elements)
#
#     def add(self, *args):
#         for i in args:
#             self._elements.append(str(i))
#         return self._elements
#
#     def pop(self):
#         if len(self._elements) == 0:
#             return None
#         else:
#             return self._elements.pop(0)
#
#     def __eq__(self, other):
#         if not isinstance(other, Queue):
#             return NotImplemented
#         return self._elements == other._elements
#
#     def __add__(self, other):
#         if not isinstance(other, Queue):
#             return NotImplemented
#         return self.__class__(*(self._elements + other._elements))
#
#     def __iadd__(self, other):
#         if isinstance(other, Queue):
#             self._elements += other._elements
#             return self
#         return NotImplemented
#
#     def __rshift__(self, n):
#         if isinstance(n, int):
#             if n >= len(self._elements):
#                 return self.__class__()
#             return self.__class__(*self._elements[n:])
#         return NotImplemented
#
#
#
#
#
#
# # INPUT DATA:
#
# # TEST_1:
# # queue = Queue(1, 2)
# # queue.add(3)
# # queue.add(4, 5)
# #
# # print(queue)
# # print(queue.pop())
# # print(queue)
#
# # TEST_2:
# # queue1 = Queue(1, 2, 3)
# # queue2 = Queue(1, 2)
# #
# # print(queue1 == queue2)
# # queue2.add(3)
# # print(queue1 == queue2)
# #
# # TEST_3:
# # queue1 = Queue(1, 2, 3)
# # queue2 = Queue(4, 5)
# #
# # print(queue1 + queue2)
# #
# # TEST_4:
# # queue1 = Queue(1, 2, 3)
# # queue2 = Queue(4, 5)
# #
# # queue1 += queue2
# #
# # print(queue1)
#
# # TEST_5:
# # queue = Queue(1, 2, 3, 4, 5)
# #
# # print(queue >> 3)
# #
# # TEST_6:
# # queue = Queue(1, 2, 3, 4, 5)
# # id1 = id(queue)
# # print(queue)
# #
# # queue += Queue(6, 7, 8, 9, 10)
# # id2 = id(queue)
# #
# # print(queue)
# # print(id1 == id2)
# #
# # queue = queue + Queue(11, 12, 13, 14, 15)
# # id3 = id(queue)
# #
# # print(queue)
# # print(id1 == id3)
#
# # TEST_7:
# queue = Queue(*'beegeek')
# for i in range(9):
#     print(f'Queue >> {i} =', queue >> i)
# #
# # # TEST_8:
# # queue = Queue(1)
# # item = queue.pop()
# # print(item)
# # print(queue.pop())
# #
# # TEST_9:
# # q1 = Queue(1, 2)
# # q2 = Queue(1, 2)
# #
# # print(q1 == q2)
# # print(q1 != q2)
#
# # # TEST_10:
# # queue = Queue(1, 2, 3)
# # print(queue.__add__([]))
# # print(queue.__iadd__('bee'))
# # print(queue.__rshift__('geek'))
#
#
# from typing import Self
#
#
# class Queue:
#     def __init__(self, *args):
#         self.queue = list(args)
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.queue))
#
#     def add(self, *args):
#         for arg in args:
#             self.queue.append(arg)
#
#     def pop(self):
#         if self.queue:
#             result = self.queue.pop(0)
#             return result
#
#     def __eq__(self, other: Self):
#         if isinstance(other, self.__class__):
#             return self.queue == other.queue
#         return NotImplemented
#
#     def __add__(self, other: Self):
#         if isinstance(other, self.__class__):
#             return self.__class__(*self.queue, *other.queue)
#         return NotImplemented
#
#     def __iadd__(self, other: Self):
#         if isinstance(other, self.__class__):
#             self.queue += other.queue
#             return self
#         return NotImplemented
#
#     def __rshift__(self, other: int):
#         if isinstance(other, int):
#             return self.__class__(*self.queue[other:])
#         return NotImplemented