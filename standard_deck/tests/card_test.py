import pytest

from standard_deck.card import Card


class TestCard:

    def test_instantiation(self):

        # start of local variables
        suit = 'spades'
        rank = 'ace'
        # end of local variables

        # Card object instantiation
        card = Card(suit, rank)

    def test_exception(self):
        # start of local variables
        suit = 'hello'
        rank = 'world'
        # end of local variables

        with pytest.raises(TypeError):
            card = Card(suit, rank)

    def test_getters_setters(self):

        # start of local variables
        suit = 'spades'
        rank = 'ace'
        # end of local variables

        # Card object instantiation
        card = Card(suit, rank)

        # asserting that instance variables of Card object equals to the local variables as well as the getters
        assert card._suit == suit == card.suit
        assert card._rank == rank == card.rank

        # testing setters
        card.suit = 'diamonds'
        assert card._suit == 'diamonds'

        card.rank = '2'
        assert card._rank == '2'

        with pytest.raises(TypeError):
            card.suit = 'hello'

        with pytest.raises(TypeError):
            card.rank = 'world'
