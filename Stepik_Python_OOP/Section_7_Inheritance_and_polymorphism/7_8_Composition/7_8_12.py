class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration

    def __str__(self):
        return f'{self.topic} — {self.start_time}, {self.duration}'


def to_minutes(hhmm: str) -> int:
    """'01:30' -> 90 минут"""
    hours, minutes = hhmm.split(':')
    return int(hours) * 60 + int(minutes)


def to_hhmm(total: int) -> str:
    """90 минут -> '01:30'"""
    return f'{total // 60:02d}:{total % 60:02d}'


class Conference:
    def __init__(self):
        self._lectures = []  # список объектов Lecture

    def add(self, lecture):
        new_start = to_minutes(lecture.start_time)
        new_end = new_start + to_minutes(lecture.duration)

        for other in self._lectures:
            other_start = to_minutes(other.start_time)
            other_end = other_start + to_minutes(other.duration)
            # Пересечение: [new_start, new_end) и [other_start, other_end)
            # касание концами (new_start == other_end) — НЕ пересечение
            if new_start < other_end and other_start < new_end:
                raise ValueError('Провести выступление в это время невозможно')

        self._lectures.append(lecture)

    def total(self):
        return to_hhmm(sum(to_minutes(l.duration) for l in self._lectures))

    def longest_lecture(self):
        if not self._lectures:
            return '00:00'
        return to_hhmm(max(to_minutes(l.duration) for l in self._lectures))

    def longest_break(self):
        if len(self._lectures) < 2:
            return '00:00'
        ordered = sorted(self._lectures, key=lambda l: to_minutes(l.start_time))
        best = 0
        for prev, curr in zip(ordered, ordered[1:]):
            prev_end = to_minutes(prev.start_time) + to_minutes(prev.duration)
            gap = to_minutes(curr.start_time) - prev_end
            if gap > best:
                best = gap
        return to_hhmm(best)