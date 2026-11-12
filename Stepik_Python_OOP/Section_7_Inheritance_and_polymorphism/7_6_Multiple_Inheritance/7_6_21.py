class H:
    pass

class D(H):
    pass

class E(H):
    pass

class F(H):
    pass

class G(H):
    pass

class B(D,E):
    pass

class C(F,G):
    pass

class A(B,C):
    pass





print(issubclass(D, H))
print(issubclass(E, H))
print(issubclass(F, H))
print(issubclass(G, H))

print('+++++++++++++++++++++++++')

print(issubclass(B, D))
print(issubclass(B, E))
print(issubclass(B, F))
print(issubclass(B, G))


print('+++++++++++++++++++++++++')

print(issubclass(C, D))
print(issubclass(C, E))
print(issubclass(C, F))
print(issubclass(C, G))