class Ord:

    def __getattr__(self, symbol):
        return ord(symbol)







obj = Ord()

print(obj.a)
print(obj.b)
print(obj.в)
print(obj.г)