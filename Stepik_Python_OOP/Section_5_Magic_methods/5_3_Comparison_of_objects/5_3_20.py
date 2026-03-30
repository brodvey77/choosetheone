from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        parts = version.split('.')
        numbers = [int(part) for part in parts]
        while len(numbers) < 3:
            numbers.append(0)
        self._version = tuple(numbers)

    def __repr__(self):
        return f"Version('{self._version[0]}.{self._version[1]}.{self._version[2]}')"

    def __str__(self):
        return f"{self._version[0]}.{self._version[1]}.{self._version[2]}"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self._version == other._version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self._version < other._version
        return NotImplemented


versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))
print('/' * 40)
print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))