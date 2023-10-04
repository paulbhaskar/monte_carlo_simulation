import numpy as np
import itertools

from poker.utils.hand_rankings_helpers import *
from standard_deck.deck import Deck


class TexasHoldem():
    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._community_cards = self.deal(5)

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, deck):
        self._deck = deck

    @property
    def community_cards(self):
        return self._community_cards

    @community_cards.setter
    def community_cards(self, cards):
        self._community_cards = cards

    def deal(self, n):
        cards = self._deck.deck[:n]
        self._deck.deck = np.delete(self._deck.deck, range(0, n))
        return cards

    def is_one_pair(cards):
        if TexasHoldem.is_straight(cards) or TexasHoldem.is_flush(cards) or TexasHoldem.is_straight_flush(cards) or TexasHoldem.is_royal_flush(cards):
            return False
        if count_pairs(cards) == 1 and count_trips(cards) == 0 and count_quads(cards) == 0:
            return True
        return False

    def is_two_pair(cards):
        if TexasHoldem.is_straight(cards) or TexasHoldem.is_flush(cards) or TexasHoldem.is_straight_flush(cards) or TexasHoldem.is_royal_flush(cards):
            return False
        if count_pairs(cards) >= 2 and count_trips(cards) == 0:
            return True
        return False

    def is_three_of_a_kind(cards):
        if TexasHoldem.is_straight(cards) or TexasHoldem.is_flush(cards) or TexasHoldem.is_straight_flush(cards) or TexasHoldem.is_royal_flush(cards):
            return False
        if count_trips(cards) == 1 and count_pairs(cards) == 0 and count_quads(cards) == 0:
            return True
        return False

    def is_straight(cards):
        if contains_n_card_straight(cards, 5) and not contains_n_card_flush(cards, 5)[0]:
            return True
        return False

    def is_flush(cards):
        if contains_n_card_flush(cards, 5)[0] and not TexasHoldem.is_straight_flush(cards) and not TexasHoldem.is_royal_flush(cards):
            return True
        return False

    def is_full_house(cards):
        if (count_trips(cards) == 1 and count_pairs(cards) >= 1) or count_trips(cards) == 2:
            return True
        return False

    def is_four_of_a_kind(cards):
        if count_quads(cards) == 1:
            return True
        return False

    def is_straight_flush(cards):
        if contains_n_card_flush(cards, 5)[0]:
            suits = contains_n_card_flush(cards, 5)[1]
            flush_suit = max(suits, key=suits.get)
            suited_cards = get_cards_by_suit(cards, flush_suit)
            if contains_n_card_straight(suited_cards, 5):
                ranks = get_ranks(suited_cards)
                if not set({'10', 'jack', 'queen', 'king', 'ace'}).issubset(ranks):
                    return True
        return False

    def is_royal_flush(cards):
        if contains_n_card_flush(cards, 5)[0]:
            suits = contains_n_card_flush(cards, 5)[1]
            flush_suit = max(suits, key=suits.get)
            suited_cards = get_cards_by_suit(cards, flush_suit)
            if contains_n_card_straight(suited_cards, 5):
                ranks = get_ranks(suited_cards)
                if set({'10', 'jack', 'queen', 'king', 'ace'}).issubset(ranks):
                    return True
        return False

    def determine_hand(cards):

        hand = 'high hand'
        rank = 1
        if TexasHoldem.is_royal_flush(cards):
            hand = 'royal flush'
            rank = 10
        elif TexasHoldem.is_straight_flush(cards):
            hand = 'straight flush'
            rank = 9
        elif TexasHoldem.is_four_of_a_kind(cards):
            hand = 'four of a kind'
            rank = 8
        elif TexasHoldem.is_full_house(cards):
            hand = 'full house'
            rank = 7
        elif TexasHoldem.is_flush(cards):
            hand = 'flush'
            rank = 6
        elif TexasHoldem.is_straight(cards):
            hand = 'straight'
            rank = 5
        elif TexasHoldem.is_three_of_a_kind(cards):
            hand = 'three of a kind'
            rank = 4
        elif TexasHoldem.is_two_pair(cards):
            hand = 'two pair'
            rank = 3
        elif TexasHoldem.is_one_pair(cards):
            hand = 'one pair'
            rank = 2
        return cards, hand, rank

    def player_cards(community_cards, hole_cards):
        return np.append(community_cards, hole_cards)

    def player_hand_rankings(*hands):
        ranks = {}
        for index, hand in enumerate(hands[0]):
            ranks[index] = TexasHoldem.determine_hand(hand)[2]
        return ranks

    def check_if_both_hole_cards_used(community_cards, hole_cards):
        player_cards = TexasHoldem.player_cards(community_cards, hole_cards)
        best_hand = TexasHoldem.determine_hand(player_cards)[1]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            best_hand, community_cards, hole_cards, 3, scores={})[0]

        count = 0
        for card in best_five_cards:
            if card in hole_cards:
                count += 1
            if count == 2:
                return True
        return False

    def calculate_five_cards_used(best_hand, community_cards, hole_cards, n, scores={}):
        hash_map = {'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}

        community_card_combinations = list(
            itertools.combinations(community_cards, n))
        hole_card_combinations = list(
            itertools.combinations(hole_cards, 5-n))
        for index, hole_cards in enumerate(hole_card_combinations):
            for index, combination in enumerate(community_card_combinations):
                combination_plus_hole_cards = TexasHoldem.player_cards(
                    combination, hole_cards)
                player_hand = TexasHoldem.determine_hand(
                    combination_plus_hole_cards)
                if player_hand[1] == best_hand:
                    ranks = get_ranks(player_hand[0])
                    card_ranks = [int(rank) if rank.isnumeric()
                                  else hash_map[rank] for rank in ranks]
                    scores[sum(card_ranks)] = combination_plus_hole_cards

        if n == 5:
            best_five_card_hand = scores[max(scores)]
            return best_five_card_hand, max(scores)
        n = n + 1
        return TexasHoldem.calculate_five_cards_used(
            best_hand, community_cards, hole_cards, n, scores)
