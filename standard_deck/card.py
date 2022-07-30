class Card:
    SUITS = ['spades', 'clubs', 'hearts', 'diamonds']
    RANKS = [str(value) for value in range(2, 11)]
    RANKS.extend(['jack', 'queen', 'king', 'ace'])

    def __init__(self, suit, rank):
        if(self.validate_card(suit, rank)):
            self._suit = suit
            self._rank = rank

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if(self.validate_card(suit, self._rank)):
            self._suit = suit

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        if(self.validate_card(self._suit, rank)):
            self._rank = rank

    def validate_card(self, suit, rank):
        if suit not in Card.SUITS:
            raise TypeError(
                f"{suit} is not a valid suit. Valid values of suit are {Card.SUITS}")
        elif rank not in Card.RANKS:
            raise TypeError(
                f"{rank} is not a valid rank.  Valid values of rank are {Card.RANKS}")
        return True

    def __str__(self):
        return f'{self.rank} {self.suit}'

    def __repr__(self):
        return f'{self.rank} {self.suit}'
