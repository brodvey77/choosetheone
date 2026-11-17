from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length):
        self._size = length
        self._paragraph = ['']

    def add(self, words):
        words = words.split()
        for word in words:
            if len(self._paragraph[-1] + f' {word}') > self._size:
                self._paragraph.append('')
            self._paragraph[-1] = (self._paragraph[-1] + f' {word}').lstrip()

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line)
        self._paragraph = ['']


class RightParagraph(Paragraph):
    def end(self):
        for line in self._paragraph:
            print(line.rjust(self._size))
        self._paragraph = ['']








class Paragraph:
    def __init__(self, length):
        self.length = length
        self.lines = []
        self.current_line = ''

    def add(self, words):
        for word in words.split():
            if not self.current_line:
                self.current_line = word

            elif len(self.current_line) + len(word) + 1 <= self.length:
                self.current_line += ' ' + word

            else:
                self.lines.append(self.current_line)
                self.current_line = word

    def end(self):
        if self.current_line:
            self.lines.append(self.current_line)

        for line in self.lines:
            print(self.format_line(line))

        self.lines = []
        self.current_line = ''

    def format_line(self, line):
        return line


class LeftParagraph(Paragraph):
    pass


class RightParagraph(Paragraph):
    def format_line(self, line):
        return line.rjust(self.length)
