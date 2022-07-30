from standard_deck.deck import Deck


class TestDeck:

    def test_card_count(self):

        # Deck object instantiation
        deck = Deck()
        assert len(deck.deck) == 52
