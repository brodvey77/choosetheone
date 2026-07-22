class HtmlTag:
    level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        indent = '  ' * HtmlTag.level
        print(indent + f'<{self.tag}>', end='' if self.inline else '\n')
        HtmlTag.level += 1
        return self

    def print(self, content):
        indent = '  ' * HtmlTag.level
        if self.inline:
            print(content, end='')
        else:
            print(indent + content)

    def __exit__(self, exc_type, exc_val, exc_tb):
        HtmlTag.level -= 1
        if self.inline:
            print(f'</{self.tag}>', end='\n')
        else:
            indent = '  ' * HtmlTag.level
            print(indent + f'</{self.tag}>')





class HtmlTag:
    _level = 0

    def __init__(self, tag, inline=False):
        self.tag = tag
        self.inline = inline
        self._end = '' if self.inline else '\n'

    def __enter__(self):
        print(self._current_indent + f'<{self.tag}>', end=self._end)
        type(self)._level += 1
        return self

    def __exit__(self, *exc_info):
        type(self)._level -= 1
        print(self._indent + f'</{self.tag}>')

    def print(self, message):
        print(self._indent + message, end=self._end)

    @property
    def _indent(self):
        return '' if self.inline else self._current_indent

    @property
    def _current_indent(self):
        return '  ' * type(self)._level
