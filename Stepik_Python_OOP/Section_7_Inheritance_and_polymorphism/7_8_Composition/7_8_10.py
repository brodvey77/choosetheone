
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f'{self.suit}{self.rank}'


class Deck:
    # Порядок старшинства — от младшего к старшему
    SUITS = ('♣', '♢', '♡', '♠')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self):
        # Внешний цикл — масти, внутренний — ранги:
        # колода упорядочена «сначала по мастям, затем по рангам»
        self._cards = [
            Card(suit, rank)
            for suit in self.SUITS
            for rank in self.RANKS
        ]

    def shuffle(self):
        if len(self._cards) != 52:
            raise ValueError('Перемешивать можно только полную колоду')
        random.shuffle(self._cards)

    def deal(self):
        if not self._cards:
            raise ValueError('Все карты разыграны')
        return self._cards.pop()   # pop() без индекса — удаляет последнюю

    def __str__(self) -> str:
        return f'Карт в колоде: {len(self._cards)}'