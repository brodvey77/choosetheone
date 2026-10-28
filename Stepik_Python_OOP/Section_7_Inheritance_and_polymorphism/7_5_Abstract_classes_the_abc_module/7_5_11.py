
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        pass


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        dx = abs(ord(horizontal) - ord(self.horizontal))
        dy = abs(vertical - self.vertical)

        return max(dx, dy) == 1


class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        dx = abs(ord(horizontal) - ord(self.horizontal))
        dy = abs(vertical - self.vertical)

        return (dx, dy) in ((1, 2), (2, 1))





from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        return ((ord(self.horizontal) - ord(horizontal)) ** 2
                + (self.vertical - vertical) ** 2)


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        return super().can_move(horizontal, vertical) in (1, 2)


class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        return super().can_move(horizontal, vertical) == 5

