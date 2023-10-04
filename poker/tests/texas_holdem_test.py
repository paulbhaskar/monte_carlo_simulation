import math
import pytest

from monte_carlo_simulation.monte_carlo import multiple_trials
from poker.texas_holdem import *
from poker.tests.fixtures import *

deck = Deck()


def single_trial(func):
    deck.shuffle()
    cards = deck.deck[:7]
    return func(cards)


class TestPokerHandProbabilities:

    @pytest.mark.slow
    def test_is_one_pair(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_one_pair, trials=1000000)
        assert math.isclose(mean * 100, 43.8, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_two_pair(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_two_pair, trials=1000000)
        assert math.isclose(mean * 100, 23.5, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_three_of_a_kind(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_three_of_a_kind, trials=1000000)
        assert math.isclose(mean * 100, 4.83, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_straight(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_straight, trials=1000000)
        assert math.isclose(mean * 100, 4.62, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_flush(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_flush, trials=1000000)
        assert math.isclose(mean * 100, 3.03, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_full_house(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_full_house, trials=1000000)
        assert math.isclose(mean * 100, 2.60, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_four_of_a_kind(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_four_of_a_kind, trials=1000000)
        assert math.isclose(mean * 100, .168, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_straight_flush(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_straight_flush, trials=1000000)
        assert math.isclose(mean * 100, .0279, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_royal_flush(self):
        mean = multiple_trials(single_trial)(
            TexasHoldem.is_royal_flush, trials=1000000)
        assert math.isclose(mean * 100, .0032, abs_tol=0.1)


class TestDetermineHand:

    def test_determine_hand_1(self, cards4):
        hand = TexasHoldem.determine_hand(cards4)[1]
        assert hand == 'two pair'
        assert TexasHoldem.is_one_pair(cards4) is False
        assert TexasHoldem.is_two_pair(cards4) is True

    def test_determine_hand_2(self, cards6):
        hand = TexasHoldem.determine_hand(cards6)[1]
        assert hand == 'full house'
        assert TexasHoldem.is_one_pair(cards6) is False
        assert TexasHoldem.is_two_pair(cards6) is False
        assert TexasHoldem.is_three_of_a_kind(cards6) is False
        assert TexasHoldem.is_full_house(cards6) is True

    def test_determine_hand_3(self, cards7):
        hand = TexasHoldem.determine_hand(cards7)[1]
        assert hand == 'two pair'
        assert TexasHoldem.is_one_pair(cards7) is False
        assert TexasHoldem.is_two_pair(cards7) is True
        assert TexasHoldem.is_straight(cards7) is False
        assert TexasHoldem.is_flush(cards7) is False

    def test_determine_hand_4(self, cards8):
        hand = TexasHoldem.determine_hand(cards8)[1]
        assert hand == 'one pair'
        assert TexasHoldem.is_one_pair(cards8) is True
        assert TexasHoldem.is_two_pair(cards8) is False
        assert TexasHoldem.is_straight(cards8) is False
        assert TexasHoldem.is_flush(cards8) is False

    def test_determine_hand_5(self, cards9):
        hand = TexasHoldem.determine_hand(cards9)[1]
        assert hand == 'straight flush'
        assert TexasHoldem.is_straight(cards9) is False
        assert TexasHoldem.is_flush(cards9) is False
        assert TexasHoldem.is_straight_flush(cards9) is True
        assert TexasHoldem.is_royal_flush(cards9) is False

    def test_determine_hand_6(self, cards10):
        hand = TexasHoldem.determine_hand(cards10)[1]
        assert hand == 'royal flush'
        assert TexasHoldem.is_straight(cards10) is False
        assert TexasHoldem.is_flush(cards10) is False
        assert TexasHoldem.is_straight_flush(cards10) is False
        assert TexasHoldem.is_royal_flush(cards10) is True

    def test_determine_hand_7(self, cards11):
        hand = TexasHoldem.determine_hand(cards11)[1]
        assert hand == 'straight flush'
        assert TexasHoldem.is_straight(cards11) is False
        assert TexasHoldem.is_flush(cards11) is False
        assert TexasHoldem.is_straight_flush(cards11) is True
        assert TexasHoldem.is_royal_flush(cards11) is False

    def test_determine_hand_8(self, cards12):
        hand = TexasHoldem.determine_hand(cards12)[1]
        assert hand == 'flush'
        assert TexasHoldem.is_straight(cards12) is False
        assert TexasHoldem.is_flush(cards12) is True
        assert TexasHoldem.is_straight_flush(cards12) is False
        assert TexasHoldem.is_royal_flush(cards12) is False

    def test_determine_hand_9(self, cards17):
        hand = TexasHoldem.determine_hand(cards17)[1]
        assert hand == 'royal flush'
        assert TexasHoldem.is_one_pair(cards17) is False
        assert TexasHoldem.is_two_pair(cards17) is False
        assert TexasHoldem.is_straight(cards17) is False
        assert TexasHoldem.is_flush(cards17) is False
        assert TexasHoldem.is_straight_flush(cards17) is False
        assert TexasHoldem.is_royal_flush(cards17) is True

    def test_determine_hand_10(self, cards18):
        hand = TexasHoldem.determine_hand(cards18)[1]
        assert hand == 'straight flush'
        assert TexasHoldem.is_one_pair(cards18) is False
        assert TexasHoldem.is_two_pair(cards18) is False
        assert TexasHoldem.is_straight(cards18) is False
        assert TexasHoldem.is_flush(cards18) is False
        assert TexasHoldem.is_straight_flush(cards18) is True
        assert TexasHoldem.is_royal_flush(cards18) is False

    def test_determine_hand_11(self, cards19):
        hand = TexasHoldem.determine_hand(cards19)[1]
        assert hand == 'straight'
        assert TexasHoldem.is_one_pair(cards19) is False
        assert TexasHoldem.is_two_pair(cards19) is False
        assert TexasHoldem.is_three_of_a_kind(cards19) is False
        assert TexasHoldem.is_straight(cards19) is True
        assert TexasHoldem.is_flush(cards19) is False
        assert TexasHoldem.is_full_house(cards19) is False

    def test_determine_hand_12(self, cards20):
        hand = TexasHoldem.determine_hand(cards20)[1]
        assert hand == 'four of a kind'
        assert TexasHoldem.is_one_pair(cards20) is False
        assert TexasHoldem.is_two_pair(cards20) is False
        assert TexasHoldem.is_three_of_a_kind(cards20) is False
        assert TexasHoldem.is_full_house(cards20) is False
        assert TexasHoldem.is_four_of_a_kind(cards20) is True

    def test_determine_hand_13(self, cards21):
        hand = TexasHoldem.determine_hand(cards21)[1]
        assert hand == 'full house'
        assert TexasHoldem.is_one_pair(cards21) is False
        assert TexasHoldem.is_two_pair(cards21) is False
        assert TexasHoldem.is_three_of_a_kind(cards21) is False
        assert TexasHoldem.is_full_house(cards21) is True
        assert TexasHoldem.is_four_of_a_kind(cards21) is False

    def test_determine_hand_14(self, cards22):
        hand = TexasHoldem.determine_hand(cards22)[1]
        assert hand == 'full house'
        assert TexasHoldem.is_one_pair(cards22) is False
        assert TexasHoldem.is_two_pair(cards22) is False
        assert TexasHoldem.is_three_of_a_kind(cards22) is False
        assert TexasHoldem.is_full_house(cards22) is True
        assert TexasHoldem.is_four_of_a_kind(cards22) is False

    def test_determine_hand_15(self, cards23):
        hand = TexasHoldem.determine_hand(cards23)[1]
        assert hand == 'flush'
        assert TexasHoldem.is_straight(cards23) is False
        assert TexasHoldem.is_flush(cards23) is True
        assert TexasHoldem.is_straight_flush(cards23) is False
        assert TexasHoldem.is_royal_flush(cards23) is False

    def test_determine_hand_16(self, cards24):
        hand = TexasHoldem.determine_hand(cards24)[1]
        assert hand == 'royal flush'
        assert TexasHoldem.is_one_pair(cards24) is False
        assert TexasHoldem.is_straight(cards24) is False
        assert TexasHoldem.is_flush(cards24) is False
        assert TexasHoldem.is_straight_flush(cards24) is False
        assert TexasHoldem.is_royal_flush(cards24) is True

    def test_determine_hand_17(self, cards25):
        hand = TexasHoldem.determine_hand(cards25)[1]
        assert hand == 'straight flush'
        assert TexasHoldem.is_straight(cards25) is False
        assert TexasHoldem.is_flush(cards25) is False
        assert TexasHoldem.is_straight_flush(cards25) is True
        assert TexasHoldem.is_royal_flush(cards25) is False

    def test_determine_hand_18(self, cards26):
        hand = TexasHoldem.determine_hand(cards26)[1]
        assert hand == 'three of a kind'
        assert TexasHoldem.is_one_pair(cards26) is False
        assert TexasHoldem.is_two_pair(cards26) is False
        assert TexasHoldem.is_three_of_a_kind(cards26) is True
        assert TexasHoldem.is_straight(cards26) is False
        assert TexasHoldem.is_flush(cards26) is False
        assert TexasHoldem.is_straight_flush(cards26) is False

    def test_determine_hand_19(self, cards27):
        hand = TexasHoldem.determine_hand(cards27)[1]
        assert hand == 'four of a kind'
        assert TexasHoldem.is_one_pair(cards27) is False
        assert TexasHoldem.is_two_pair(cards27) is False
        assert TexasHoldem.is_three_of_a_kind(cards27) is False
        assert TexasHoldem.is_straight(cards27) is False
        assert TexasHoldem.is_full_house(cards27) is False
        assert TexasHoldem.is_four_of_a_kind(cards27) is True
        assert TexasHoldem.is_straight_flush(cards27) is False

    def test_determine_hand_20(self, cards28):
        hand = TexasHoldem.determine_hand(cards28)[1]
        assert hand == 'straight flush'
        assert TexasHoldem.is_one_pair(cards28) is False
        assert TexasHoldem.is_straight(cards28) is False
        assert TexasHoldem.is_flush(cards28) is False
        assert TexasHoldem.is_straight_flush(cards28) is True
        assert TexasHoldem.is_royal_flush(cards28) is False


class TestCheckIfBothHoleCardsUsed:
    def test_check_if_both_hole_cards_used_1(self, cards29):
        card = Card('diamonds', '7')
        card2 = Card('diamonds', '8')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards29, hole_cards) is False

    def test_check_if_both_hole_cards_used_2(self, cards30):
        card = Card('diamonds', '8')
        card2 = Card('diamonds', '2')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards30, hole_cards) is True

    def test_check_if_both_hole_cards_used_3(self, cards31):
        card = Card('diamonds', '8')
        card2 = Card('diamonds', '2')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards31, hole_cards) is False

    def test_check_if_both_hole_cards_used_4(self, cards32):
        card = Card('hearts', '2')
        card2 = Card('diamonds', '2')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards32, hole_cards) is True

    def test_check_if_both_hole_cards_used_5(self, cards33):
        card = Card('spades', '4')
        card2 = Card('spades', '5')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards33, hole_cards) is False

    def test_check_if_both_hole_cards_used_6(self, cards33):
        card = Card('spades', 'jack')
        card2 = Card('spades', 'queen')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards33, hole_cards) is True

    def test_check_if_both_hole_cards_used_7(self, cards33):
        card = Card('spades', 'jack')
        card2 = Card('spades', '5')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards33, hole_cards) is False

    def test_check_if_both_hole_cards_used_8(self, cards33):
        card = Card('spades', 'jack')
        card2 = Card('spades', 'ace')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards33, hole_cards) is False

    def test_check_if_both_hole_cards_used_9(self, cards33):
        card = Card('spades', 'ace')
        card2 = Card('diamonds', 'ace')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards33, hole_cards) is False

    def test_check_if_both_hole_cards_used_10(self, cards34):
        card = Card('spades', 'ace')
        card2 = Card('spades', '3')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards34, hole_cards) is True

    def test_check_if_both_hole_cards_used_11(self, cards34):
        card = Card('spades', '6')
        card2 = Card('spades', '7')
        hole_cards = [card, card2]
        assert TexasHoldem.check_if_both_hole_cards_used(
            cards34, hole_cards) is True


class TestCalculateFiveCardsUsed:
    def test_calculate_five_cards_used_1(self, cards35):
        community_cards = cards35[:5]
        hole_cards = cards35[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'straight', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('spades', 'ace')
        assert best_five_cards[0][1] == Card('spades', 'queen')
        assert best_five_cards[0][2] == Card('spades', 'jack')
        assert best_five_cards[0][3] == Card('hearts', 'king')
        assert best_five_cards[0][4] == Card('clubs', '10')

    def test_calculate_five_cards_used_2(self, cards36):
        community_cards = cards36[:5]
        hole_cards = cards36[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'one pair', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('clubs', 'king')
        assert best_five_cards[0][1] == Card('hearts', 'queen')
        assert best_five_cards[0][2] == Card('spades', 'king')
        assert best_five_cards[0][3] == Card('diamonds', '9')
        assert best_five_cards[0][4] == Card('diamonds', '6')

    def test_calculate_five_cards_used_3(self, cards37):
        community_cards = cards37[:5]
        hole_cards = cards37[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'high hand', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('diamonds', 'jack')
        assert best_five_cards[0][1] == Card('diamonds', '9')
        assert best_five_cards[0][2] == Card('hearts', '5')
        assert best_five_cards[0][3] == Card('hearts', 'queen')
        assert best_five_cards[0][4] == Card('spades', 'ace')

    def test_calculate_five_cards_used_4(self, cards38):
        community_cards = cards38[:5]
        hole_cards = cards38[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'one pair', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('hearts', 'jack')
        assert best_five_cards[0][1] == Card('clubs', 'king')
        assert best_five_cards[0][2] == Card('hearts', 'queen')
        assert best_five_cards[0][3] == Card('diamonds', '8')
        assert best_five_cards[0][4] == Card('spades', '8')

    def test_calculate_five_cards_used_5(self, cards39):
        community_cards = cards39[:5]
        hole_cards = cards39[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'two pair', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('hearts', 'ace')
        assert best_five_cards[0][1] == Card('hearts', '2')
        assert best_five_cards[0][2] == Card('clubs', '2')
        assert best_five_cards[0][3] == Card('diamonds', 'ace')
        assert best_five_cards[0][4] == Card('spades', 'jack')

    def test_calculate_five_cards_used_6(self, cards40):
        community_cards = cards40[:5]
        hole_cards = cards40[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'flush', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('diamonds', '4')
        assert best_five_cards[0][1] == Card('diamonds', 'jack')
        assert best_five_cards[0][2] == Card('diamonds', '5')
        assert best_five_cards[0][3] == Card('diamonds', '9')
        assert best_five_cards[0][4] == Card('diamonds', '7')

    def test_calculate_five_cards_used_7(self, cards41):
        community_cards = cards41[:5]
        hole_cards = cards41[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'two pair', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('clubs', '3')
        assert best_five_cards[0][1] == Card('diamonds', '3')
        assert best_five_cards[0][2] == Card('clubs', '8')
        assert best_five_cards[0][3] == Card('diamonds', '10')
        assert best_five_cards[0][4] == Card('spades', '8')

    def test_calculate_five_cards_used_8(self, cards42):
        community_cards = cards42[:5]
        hole_cards = cards42[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'straight', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('spades', '10')
        assert best_five_cards[0][1] == Card('diamonds', 'jack')
        assert best_five_cards[0][2] == Card('diamonds', '9')
        assert best_five_cards[0][3] == Card('spades', '8')
        assert best_five_cards[0][4] == Card('hearts', '7')

    def test_calculate_five_cards_used_9(self, cards43):
        community_cards = cards43[:5]
        hole_cards = cards43[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'flush', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('diamonds', '5')
        assert best_five_cards[0][1] == Card('diamonds', '10')
        assert best_five_cards[0][2] == Card('diamonds', 'ace')
        assert best_five_cards[0][3] == Card('diamonds', '9')
        assert best_five_cards[0][4] == Card('diamonds', '2')

    def test_calculate_five_cards_used_10(self, cards44):
        community_cards = cards44[:5]
        hole_cards = cards44[5:]
        best_five_cards = TexasHoldem.calculate_five_cards_used(
            'two pair', community_cards, hole_cards, 3, scores={})
        assert len(best_five_cards[0]) == 5
        assert best_five_cards[0][0] == Card('diamonds', 'ace')
        assert best_five_cards[0][1] == Card('spades', 'ace')
        assert best_five_cards[0][2] == Card('diamonds', 'king')
        assert best_five_cards[0][3] == Card('spades', 'king')
        assert best_five_cards[0][4] == Card('diamonds', 'queen')
