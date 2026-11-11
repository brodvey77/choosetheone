
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(A):
#     pass
#
# class E(B, D):
#     pass

class A: ...
class B(A): ...
class C(A): ...
class D(A): ...
class E(B, D): ...

print(issubclass(E, B))
print(issubclass(E, C))
print(issubclass(E, D))

print('++++++++++++++++++++++++++++++++++++++++++++++')

print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(D, A))