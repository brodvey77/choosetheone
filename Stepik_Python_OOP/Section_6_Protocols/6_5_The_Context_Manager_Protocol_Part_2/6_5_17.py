class TreeBuilder:
    def __init__(self):
        self.root = []
        self.stack = [self.root]

    def __enter__(self):
        current = self.stack[-1]
        new_node = []
        current.append(new_node)
        self.stack.append(new_node)
        return self

    def __exit__(self, *args):
        node = self.stack.pop()
        if not node:
            parent = self.stack[-1]
            if parent and parent[-1] is node:
                parent.pop()

    def add(self, item):
        current = self.stack[-1]
        current.append(item)

    def structure(self):
        return self.root





class TreeBuilder:
    def __init__(self):
        self.knots = [[]]

    def __enter__(self):
        self.knots.append([])

    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])
        self.knots.pop()

    def add(self, value):
        self.knots[-1].append(value)

    def structure(self):
        return self.knots[-1]