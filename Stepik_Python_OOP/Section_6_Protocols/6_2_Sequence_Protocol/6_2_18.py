
class MutableString:
    def __init__(self, string=''):
        self._string = string

    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string =  self._string.upper()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._string}')"

    def __str__(self):
        return f"{self._string}"

    def __len__(self):
        return len(self._string)

    def __iter__(self):
        return iter(self._string)

    def __getitem__(self, item):
        result = self._string[item]
        return MutableString(result)

    def __setitem__(self, key, value):
        temp = list(self._string)
        temp[key] = value
        self._string = ''.join(temp)

    def __delitem__(self, key):
        temp = list(self._string)
        del temp[key]
        self._string = ''.join(temp)


    def __add__(self, other):
        if isinstance(other, (str, MutableString)):
            return MutableString(self._string + str(other))
        return NotImplemented



mutablestring = MutableString('beegeek')

s1 = mutablestring[2:]
s2 = mutablestring[:5]
s3 = mutablestring[2:5:2]

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))


class MutableString:
    """
    Класс MutableString представляет изменяемую строку.
    Внутренне хранит данные как список символов для эффективной мутации.
    """

    def __init__(self, string: str = ""):
        """
        Инициализирует изменяемую строку.

        :param string: начальное значение строки (по умолчанию пустая строка)
        """
        self._data = list(string)  # храним как список для O(1) доступа и мутации

    def lower(self) -> None:
        """
        Переводит все символы в нижний регистр (изменяет объект на месте).
        """
        self._data = [char.lower() for char in self._data]

    def upper(self) -> None:
        """
        Переводит все символы в верхний регистр (изменяет объект на месте).
        """
        self._data = [char.upper() for char in self._data]

    def __str__(self) -> str:
        """
        Возвращает неформальное строковое представление.
        """
        return ''.join(self._data)

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление.
        """
        return f"MutableString('{self}')"

    def __len__(self) -> int:
        """
        Возвращает длину строки.
        """
        return len(self._data)

    def __iter__(self):
        """
        Поддержка итерации по символам.
        """
        return iter(self._data)

    def __getitem__(self, key):
        """
        Поддержка получения элемента по индексу или срезу.
        Возвращает новый объект MutableString.
        """
        if isinstance(key, slice):
            # Срез возвращает новый MutableString
            return MutableString(''.join(self._data[key]))
        else:
            # Одиночный индекс (положительный или отрицательный)
            return MutableString(self._data[key])

    def __setitem__(self, key, value) -> None:
        """
        Поддержка изменения элемента по индексу или срезу.
        """
        if isinstance(key, slice):
            # Преобразуем значение в строку, если передан MutableString
            if isinstance(value, MutableString):
                value = str(value)
            self._data[key] = list(value)
        else:
            # Одиночный индекс — заменяем один символ
            if isinstance(value, MutableString):
                value = str(value)
            # Гарантируется, что value — строка длиной 1
            self._data[key] = value

    def __delitem__(self, key) -> None:
        """
        Поддержка удаления символа(ов) по индексу или срезу.
        """
        del self._data[key]

    def __add__(self, other):
        """
        Поддержка операции сложения: MutableString + MutableString / str.
        Возвращает новый объект MutableString.
        """
        if isinstance(other, MutableString):
            return MutableString(str(self) + str(other))
        elif isinstance(other, str):
            return MutableString(str(self) + other)
        return NotImplemented

    def __radd__(self, other):
        """
        Поддержка операции str + MutableString.
        """
        if isinstance(other, str):
            return MutableString(other + str(self))
        return NotImplemented