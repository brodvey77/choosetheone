class Time:
    def __init__(self, hours: int, minutes: int):
        total_minutes = hours * 60 + minutes
        self.hours = (total_minutes // 60) % 24
        self.minutes = total_minutes % 60

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return Time(self.hours + other.hours, self.minutes + other.minutes)

    def __iadd__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        self.hours += other.hours
        self.minutes += other.minutes
        total_minutes = self.hours * 60 + self.minutes
        self.hours = (total_minutes // 60) % 24
        self.minutes = total_minutes % 60
        return self




class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = Time._normalize(hours, minutes)

    @staticmethod
    def _normalize(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60

    def __str__(self):
        return f'{self.hours:>02}:{self.minutes:>02}'

    def __add__(self, other):
        if isinstance(other, Time):
            hours, minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
            return Time(hours, minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours, self.minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
            return self
        return NotImplemented


Дополнит
строку
нулями
слева
до
длины
2:

s = '1'
print(f'{s:>02}')  # 01
print(f'{s:>09}')  # 000000001

Если
поменять
знак
на
противоположный, дополнит
нулями
справа:

s = '1'
print(f'{s:<02}')  # 10
print(f'{s:<09}')  # 100000000