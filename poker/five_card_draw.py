from poker.utils.hand_rankings_helpers import *
from standard_deck.deck import Deck


class FiveCardDraw():
    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()

    def deal(self):
        return self._deck.deck[:5]

    def is_one_pair(cards):
        if count_pairs(cards) == 1 and count_trips(cards) == 0:
            return True
        return False

    def is_two_pair(cards):
        if count_pairs(cards) == 2:
            return True
        return False

    def is_three_of_a_kind(cards):
        if count_trips(cards) == 1 and count_pairs(cards) == 0:
            return True
        return False

    def is_straight(cards):
        if contains_n_card_straight(cards, 5) and not contains_n_card_flush(cards, 5)[0]:
            return True
        return False

    def is_flush(cards):
        if contains_n_card_flush(cards, 5)[0] and not contains_n_card_straight(cards, 5):
            return True
        return False

    def is_full_house(cards):
        if count_trips(cards) == 1 and count_pairs(cards) == 1:
            return True
        return False

    def is_four_of_a_kind(cards):
        if count_quads(cards) == 1:
            return True
        return False

    def is_straight_flush(cards):
        if contains_n_card_flush(cards, 5)[0] and contains_n_card_straight(cards, 5):
            if not FiveCardDraw.is_royal_flush(cards):
                return True
        return False

    def is_royal_flush(cards):
        if contains_n_card_flush(cards, 5)[0]:
            ranks = get_ranks(cards)
            if len(set(ranks) - set({'10', 'jack', 'queen', 'king', 'ace'})) == 0:
                return True
        return False

    def determine_hand(cards):
        assert len(cards) == 5

        hand = 'high hand'
        rank = 1
        if FiveCardDraw.is_royal_flush(cards):
            hand = 'royal flush'
            rank = 10
        elif FiveCardDraw.is_straight_flush(cards):
            hand = 'straight flush'
            rank = 9
        elif FiveCardDraw.is_four_of_a_kind(cards):
            hand = 'four of a kind'
            rank = 8
        elif FiveCardDraw.is_full_house(cards):
            hand = 'full house'
            rank = 7
        elif FiveCardDraw.is_flush(cards):
            hand = 'flush'
            rank = 6
        elif FiveCardDraw.is_straight(cards):
            hand = 'straight'
            rank = 5
        elif FiveCardDraw.is_three_of_a_kind(cards):
            hand = 'three of a kind'
            rank = 4
        elif FiveCardDraw.is_two_pair(cards):
            hand = 'two pair'
            rank = 3
        elif FiveCardDraw.is_one_pair(cards):
            hand = 'one pair'
            rank = 2
        return cards, hand, rank
