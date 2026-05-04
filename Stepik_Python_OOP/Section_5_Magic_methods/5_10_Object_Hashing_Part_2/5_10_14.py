class Row:
    """Immutable record that keeps attribute order."""

    def __init__(self, **kwargs):
        # store the order of the fields
        object.__setattr__(self, "_fields", tuple(kwargs.keys()))
        # assign the values bypassing our overridden __setattr__
        for name, value in kwargs.items():
            object.__setattr__(self, name, value)

    # -----------------------------------------------------------------
    # protection from modification
    # -----------------------------------------------------------------
    def __setattr__(self, name, value):
        # internal attribute used only during __init__
        if name == "_fields":
            object.__setattr__(self, name, value)
            return

        if name in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        else:
            raise AttributeError("Установка нового атрибута невозможна")

    def __delattr__(self, name):
        raise AttributeError("Удаление атрибута невозможно")

    # -----------------------------------------------------------------
    # representation, comparison, hash
    # -----------------------------------------------------------------
    def __repr__(self):
        parts = [f"{name}={repr(getattr(self, name))}" for name in self._fields]
        return f"Row({', '.join(parts)})"

    def __eq__(self, other):
        if not isinstance(other, Row):
            return NotImplemented
        if self._fields != other._fields:
            return False
        return all(getattr(self, n) == getattr(other, n) for n in self._fields)

    def __hash__(self):
        items = tuple((name, getattr(self, name)) for name in self._fields)
        return hash(items)



row = Row(a='A', b='B', c='C')

print(row)
print(row.a, row.b, row.c)