class RomanNumeral:
    # Словарь для преобразования римских цифр в числа
    _roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Списки для преобразования числа в римскую запись
    _int_to_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    def __init__(self, number: str):
        self._roman = number
        self._value = self._roman_to_int_converter(number)

    @classmethod
    def _roman_to_int_converter(cls, roman: str) -> int:
        """Преобразует римское число в целое"""
        total = 0
        prev_value = 0

        for char in reversed(roman):
            current_value = cls._roman_to_int[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value

        return total

    @classmethod
    def _int_to_roman_converter(cls, number: int) -> str:
        """Преобразует целое число в римское"""
        if number <= 0:
            raise ValueError("Римские числа должны быть положительными")

        result = []
        for value, symbol in cls._int_to_roman:
            while number >= value:
                result.append(symbol)
                number -= value

        return ''.join(result)

    def __str__(self) -> str:
        """Неформальное строковое представление"""
        return self._roman

    def __int__(self) -> int:
        """Приведение к типу int"""
        return self._value

    def __eq__(self, other) -> bool:
        """Оператор =="""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other) -> bool:
        """Оператор !="""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self._value != other._value

    def __gt__(self, other) -> bool:
        """Оператор >"""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self._value > other._value

    def __lt__(self, other) -> bool:
        """Оператор <"""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self._value < other._value

    def __ge__(self, other) -> bool:
        """Оператор >="""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self._value >= other._value

    def __le__(self, other) -> bool:
        """Оператор <="""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self._value <= other._value

    def __add__(self, other):
        """Оператор +"""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        result_value = self._value + other._value
        result_roman = self._int_to_roman_converter(result_value)
        return RomanNumeral(result_roman)

    def __sub__(self, other):
        """Оператор -"""
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        result_value = self._value - other._value
        result_roman = self._int_to_roman_converter(result_value)
        return RomanNumeral(result_roman)