import math
import pytest

from monte_carlo_simulation.monte_carlo import multiple_trials
from poker.five_card_draw import *
from poker.tests.fixtures import *

deck = Deck()


def single_trial(func):
    deck.shuffle()
    cards = deck.deck[:5]
    return func(cards)


class TestPokerHandProbabilities:

    @pytest.mark.slow
    def test_is_one_pair(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_one_pair, trials=1000000)
        assert math.isclose(mean * 100, 42.2569, abs_tol=0.10)

    @pytest.mark.slow
    def test_is_two_pair(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_two_pair, trials=1000000)
        assert math.isclose(mean * 100, 4.7539, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_three_of_a_kind(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_three_of_a_kind, trials=1000000)
        assert math.isclose(mean * 100, 2.1128, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_straight(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_straight, trials=1000000)
        assert math.isclose(mean * 100, .3925, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_flush(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_flush, trials=1000000)
        assert math.isclose(mean * 100, .1965, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_full_house(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_full_house, trials=1000000)
        assert math.isclose(mean * 100, .1441, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_four_of_a_kind(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_four_of_a_kind, trials=1000000)
        assert math.isclose(mean * 100, .02401, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_straight_flush(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_straight_flush, trials=1000000)
        assert math.isclose(mean * 100, .00139, abs_tol=0.1)

    @pytest.mark.slow
    def test_is_royal_flush(self):
        mean = multiple_trials(single_trial)(
            FiveCardDraw.is_royal_flush, trials=1000000)
        assert math.isclose(mean * 100, .000154, abs_tol=0.1)


class TestDetermineHand:

    def test_determine_hand_1(self, cards1):
        hand = FiveCardDraw.determine_hand(cards1)[1]
        assert hand == 'high hand'

    def test_determine_hand_2(self, cards2):
        hand = FiveCardDraw.determine_hand(cards2)[1]
        assert hand == 'one pair'

    def test_determine_hand_3(self, cards3):
        hand = FiveCardDraw.determine_hand(cards3)[1]
        assert hand == 'two pair'

    def test_determine_hand_4(self, cards5):
        hand = FiveCardDraw.determine_hand(cards5)[1]
        assert hand == 'three of a kind'

    def test_determine_hand_5(self, cards13):
        hand = FiveCardDraw.determine_hand(cards13)[1]
        assert hand == 'high hand'

    def test_determine_hand_6(self, cards14):
        hand = FiveCardDraw.determine_hand(cards14)[1]
        assert hand == 'one pair'

    def test_determine_hand_7(self, cards15):
        hand = FiveCardDraw.determine_hand(cards15)[1]
        assert hand == 'one pair'

    def test_determine_hand_8(self, cards16):
        hand = FiveCardDraw.determine_hand(cards16)[1]
        assert hand == 'full house'

    def test_determine_hand_9(self, cards29):
        hand = FiveCardDraw.determine_hand(cards29)[1]
        assert hand == 'four of a kind'
