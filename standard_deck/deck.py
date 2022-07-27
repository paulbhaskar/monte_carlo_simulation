import numpy as np

from standard_deck.card import Card


class Deck:
    def __init__(self):
        self._deck = np.array([])
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck = np.append(self._deck, Card(suit, rank))

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, cards):
        self._deck = cards

    def shuffle(self):
        np.random.shuffle(self.deck)

    def __str__(self):
        string_builder = []
        for card in self.deck:
            string_builder.append(f'{card.rank} {card.suit}')
        return '\n'.join(string_builder)
