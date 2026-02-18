

class HourClock:
    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if isinstance(hours, int) and 1 <= hours <= 12:
            self._hours = hours
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)



time = HourClock(1)
print(hasattr(HourClock, 'hours'))