from poker.utils.hand_rankings_helpers import *
from poker.tests.fixtures import *


class TestCountPairs:
    def test_count_pairs_1(self, cards1):
        assert count_pairs(cards1) == 0

    def test_count_pairs_2(self, cards2):
        assert count_pairs(cards2) == 1

    def test_count_pairs_3(self, cards3):
        assert count_pairs(cards3) == 2

    def test_count_pairs_4(self, cards4):
        assert count_pairs(cards4) == 3

    def test_count_pairs_5(self, cards5):
        assert count_pairs(cards5) == 0

    def test_count_pairs_6(self, cards6):
        assert count_pairs(cards6) == 0

    def test_count_pairs_7(self, cards7):
        assert count_pairs(cards7) == 2

    def test_count_pairs_8(self, cards8):
        assert count_pairs(cards8) == 1


class TestCountTrips:
    def test_count_trips_1(self, cards5):
        assert count_trips(cards5) == 1

    def test_count_trips_2(self, cards6):
        assert count_trips(cards6) == 2


class TestCountMaxConsecutive:
    def test_count_max_consecutive_1(self):
        values = [4, 5, 11, 10, 6]
        assert count_max_consecutive(values) == 3

    def test_count_max_consecutive_2(self):
        values = [7, 6, 7, 5, 8, 6, 11]
        assert count_max_consecutive(values) == 4

    def test_count_max_consecutive_3(self):
        values = [2, 3, 3, 5, 6, 7, 8]
        assert count_max_consecutive(values) == 4

    def test_count_max_consecutive_4(self):
        values = [9, 10, 5, 9, 9, 9, 6, 8, 1, 3]
        assert count_max_consecutive(values) == 3

    def test_count_max_consecutive_5(self):
        values = [3, 8, 4, 9, 4, 7, 7, 6, 6, 9]
        assert count_max_consecutive(values) == 4


class TestContainsNCardStraight:
    def test_contains_n_card_straight_1(self, cards9):
        assert contains_n_card_straight(cards9, 5) == True

    def test_contains_n_card_straight_2(self, cards10):
        assert contains_n_card_straight(cards10, 5) == True

    def test_contains_n_card_straight_3(self, cards11):
        assert contains_n_card_straight(cards11, 5) == True


class TestContainsNCardFlush:
    def test_contains_n_card_flush_1(self, cards9):
        assert contains_n_card_flush(cards9, 5)[0] == True

    def test_contains_n_card_flush_2(self, cards10):
        assert contains_n_card_flush(cards10, 5)[0] == True

    def test_contains_n_card_flush_3(self, cards11):
        assert contains_n_card_flush(cards11, 5)[0] == True

    def test_contains_n_card_flush_4(self, cards12):
        assert contains_n_card_flush(cards12, 5)[0] == True
