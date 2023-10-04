import pytest

from standard_deck.card import Card


@pytest.fixture
def cards1():
    card1 = Card('clubs', '4')
    card2 = Card('hearts', '5')
    card3 = Card('spades', 'jack')
    card4 = Card('clubs', '10')
    card5 = Card('spades', '6')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards2():
    card1 = Card('spades', '2')
    card2 = Card('clubs', '7')
    card3 = Card('spades', 'jack')
    card4 = Card('clubs', '5')
    card5 = Card('diamonds', '7')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards3():
    card1 = Card('clubs', '6')
    card2 = Card('diamonds', '9')
    card3 = Card('hearts', '9')
    card4 = Card('hearts', 'jack')
    card5 = Card('spades', 'jack')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards4():
    card1 = Card('spades', '2')
    card2 = Card('clubs', '7')
    card3 = Card('spades', 'jack')
    card4 = Card('clubs', '2')
    card5 = Card('diamonds', '7')
    card6 = Card('clubs', 'jack')
    card7 = Card('diamonds', 'ace')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards5():
    card1 = Card('clubs', '4')
    card2 = Card('hearts', '4')
    card3 = Card('diamonds', '4')
    card4 = Card('clubs', '10')
    card5 = Card('spades', '6')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards6():
    card1 = Card('clubs', '4')
    card2 = Card('hearts', '4')
    card3 = Card('diamonds', '4')
    card4 = Card('clubs', '10')
    card5 = Card('hearts', '10')
    card6 = Card('diamonds', '10')
    card7 = Card('spades', 'ace')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards7():
    card1 = Card('clubs', '7')
    card2 = Card('diamonds', '6')
    card3 = Card('diamonds', '7')
    card4 = Card('diamonds', '5')
    card5 = Card('hearts', '8')
    card6 = Card('spades', '6')
    card7 = Card('diamonds', 'jack')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards8():
    card1 = Card('clubs', '2')
    card2 = Card('diamonds', '3')
    card3 = Card('spades', '3')
    card4 = Card('diamonds', '5')
    card5 = Card('hearts', '6')
    card6 = Card('spades', '7')
    card7 = Card('diamonds', '8')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards9():
    card1 = Card('spades', '4')
    card2 = Card('spades', '5')
    card3 = Card('spades', '6')
    card4 = Card('spades', '7')
    card5 = Card('spades', '8')
    card6 = Card('spades', '9')
    card7 = Card('spades', '10')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards10():
    card1 = Card('spades', '10')
    card2 = Card('spades', 'jack')
    card3 = Card('spades', 'queen')
    card4 = Card('spades', 'king')
    card5 = Card('spades', 'ace')
    card6 = Card('spades', '3')
    card7 = Card('spades', '4')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards11():
    card1 = Card('spades', 'ace')
    card2 = Card('spades', '2')
    card3 = Card('spades', '3')
    card4 = Card('spades', '4')
    card5 = Card('spades', '5')
    card6 = Card('spades', '10')
    card7 = Card('spades', 'queen')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards12():
    card1 = Card('spades', 'ace')
    card2 = Card('spades', '2')
    card3 = Card('clubs', '4')
    card4 = Card('hearts', '5')
    card5 = Card('spades', 'jack')
    card6 = Card('spades', '10')
    card7 = Card('spades', '6')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards13():
    card1 = Card('diamonds', '7')
    card2 = Card('spades', 'queen')
    card3 = Card('clubs', '8')
    card4 = Card('clubs', '5')
    card5 = Card('hearts', '6')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards14():
    card1 = Card('spades', 'ace')
    card2 = Card('clubs', 'king')
    card3 = Card('spades', '8')
    card4 = Card('diamonds', '3')
    card5 = Card('hearts', 'ace')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards15():
    card1 = Card('hearts', '5')
    card2 = Card('spades', 'king')
    card3 = Card('spades', '5')
    card4 = Card('spades', '2')
    card5 = Card('clubs', '9')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards16():
    card1 = Card('hearts', '2')
    card2 = Card('hearts', '8')
    card3 = Card('clubs', '2')
    card4 = Card('diamonds', '2')
    card5 = Card('spades', '8')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards17():
    card1 = Card('hearts', 'ace')
    card2 = Card('spades', 'ace')
    card3 = Card('diamonds', '10')
    card4 = Card('spades', '10')
    card5 = Card('spades', 'queen')
    card6 = Card('spades', 'jack')
    card7 = Card('spades', 'king')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards18():
    card1 = Card('diamonds', '6')
    card2 = Card('spades', '5')
    card3 = Card('spades', '6')
    card4 = Card('diamonds', '2')
    card5 = Card('spades', '2')
    card6 = Card('spades', '3')
    card7 = Card('spades', '4')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards19():
    card1 = Card('hearts', 'jack')
    card2 = Card('diamonds', '10')
    card3 = Card('clubs', 'jack')
    card4 = Card('diamonds', 'jack')
    card5 = Card('diamonds', 'king')
    card6 = Card('hearts', 'queen')
    card7 = Card('hearts', '9')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards20():
    card1 = Card('spades', '8')
    card2 = Card('clubs', '6')
    card3 = Card('diamonds', '6')
    card4 = Card('hearts', '6')
    card5 = Card('hearts', '8')
    card6 = Card('diamonds', '8')
    card7 = Card('clubs', '8')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards21():
    card1 = Card('spades', '3')
    card2 = Card('diamonds', '3')
    card3 = Card('spades', '8')
    card4 = Card('clubs', '8')
    card5 = Card('spades', 'king')
    card6 = Card('clubs', '5')
    card7 = Card('diamonds', '8')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards22():
    card1 = Card('diamonds', 'jack')
    card2 = Card('clubs', 'king')
    card3 = Card('hearts', 'jack')
    card4 = Card('diamonds', '3')
    card5 = Card('spades', '3')
    card6 = Card('hearts', 'king')
    card7 = Card('clubs', 'jack')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards23():
    card1 = Card('clubs', '5')
    card2 = Card('spades', '8')
    card3 = Card('spades', '9')
    card4 = Card('clubs', '10')
    card5 = Card('spades', 'jack')
    card6 = Card('spades', 'queen')
    card7 = Card('spades', 'ace')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards24():
    card1 = Card('hearts', 'queen')
    card2 = Card('hearts', 'ace')
    card3 = Card('hearts', '6')
    card4 = Card('hearts', '10')
    card5 = Card('hearts', 'king')
    card6 = Card('hearts', 'jack')
    card7 = Card('spades', 'ace')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards25():
    card1 = Card('spades', '9')
    card2 = Card('spades', '10')
    card3 = Card('diamonds', 'ace')
    card4 = Card('spades', 'queen')
    card5 = Card('clubs', 'king')
    card6 = Card('spades', 'jack')
    card7 = Card('spades', '8')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards26():
    card1 = Card('clubs', '8')
    card2 = Card('clubs', '5')
    card3 = Card('clubs', '9')
    card4 = Card('clubs', '10')
    card5 = Card('diamonds', 'jack')
    card6 = Card('spades', '5')
    card7 = Card('hearts', '5')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards27():
    card1 = Card('hearts', '3')
    card2 = Card('hearts', '2')
    card3 = Card('spades', '2')
    card4 = Card('spades', 'ace')
    card5 = Card('clubs', '2')
    card6 = Card('diamonds', '2')
    card7 = Card('diamonds', '3')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards28():
    card1 = Card('hearts', 'jack')
    card2 = Card('hearts', '9')
    card3 = Card('clubs', '8')
    card4 = Card('hearts', '10')
    card5 = Card('hearts', 'queen')
    card6 = Card('hearts', 'king')
    card7 = Card('spades', 'queen')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards29():
    card1 = Card('clubs', '2')
    card2 = Card('hearts', '2')
    card3 = Card('spades', '2')
    card4 = Card('diamonds', '2')
    card5 = Card('spades', '3')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards30():
    card1 = Card('clubs', '2')
    card2 = Card('hearts', '2')
    card3 = Card('spades', '2')
    card4 = Card('diamonds', '4')
    card5 = Card('spades', '3')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards31():
    card1 = Card('clubs', '2')
    card2 = Card('hearts', '2')
    card3 = Card('spades', '2')
    card4 = Card('diamonds', '4')
    card5 = Card('spades', 'ace')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards32():
    card1 = Card('clubs', '2')
    card2 = Card('spades', '2')
    card3 = Card('spades', '4')
    card4 = Card('diamonds', '5')
    card5 = Card('spades', 'ace')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards33():
    card1 = Card('spades', '6')
    card2 = Card('spades', '7')
    card3 = Card('spades', '8')
    card4 = Card('spades', '9')
    card5 = Card('spades', '10')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards34():
    card1 = Card('spades', '2')
    card2 = Card('spades', '4')
    card3 = Card('spades', '5')
    card4 = Card('diamonds', 'jack')
    card5 = Card('spades', '8')
    return [card1, card2, card3, card4, card5]


@pytest.fixture
def cards35():
    card1 = Card('spades', 'ace')
    card2 = Card('diamonds', '6')
    card3 = Card('spades', 'queen')
    card4 = Card('spades', '3')
    card5 = Card('spades', 'jack')
    card6 = Card('hearts', 'king')
    card7 = Card('clubs', '10')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards36():
    card1 = Card('clubs', 'king')
    card2 = Card('hearts', 'queen')
    card3 = Card('hearts', '3')
    card4 = Card('hearts', '5')
    card5 = Card('spades', 'king')
    card6 = Card('diamonds', '9')
    card7 = Card('diamonds', '6')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards37():
    card1 = Card('clubs', '3')
    card2 = Card('diamonds', 'jack')
    card3 = Card('diamonds', '9')
    card4 = Card('hearts', '5')
    card5 = Card('diamonds', '2')
    card6 = Card('hearts', 'queen')
    card7 = Card('spades', 'ace')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards38():
    card1 = Card('hearts', 'jack')
    card2 = Card('clubs', 'king')
    card3 = Card('spades', '7')
    card4 = Card('diamonds', '10')
    card5 = Card('hearts', 'queen')
    card6 = Card('diamonds', '8')
    card7 = Card('spades', '8')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards39():
    card1 = Card('clubs', '9')
    card2 = Card('hearts', 'ace')
    card3 = Card('hearts', '2')
    card4 = Card('clubs', '2')
    card5 = Card('diamonds', 'ace')
    card6 = Card('spades', 'jack')
    card7 = Card('diamonds', '5')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards40():
    card1 = Card('diamonds', '4')
    card2 = Card('hearts', 'queen')
    card3 = Card('diamonds', 'jack')
    card4 = Card('diamonds', '5')
    card5 = Card('diamonds', '9')
    card6 = Card('diamonds', '7')
    card7 = Card('clubs', '3')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards41():
    card1 = Card('clubs', '3')
    card2 = Card('diamonds', '3')
    card3 = Card('clubs', '8')
    card4 = Card('diamonds', '10')
    card5 = Card('spades', '8')
    card6 = Card('hearts', '6')
    card7 = Card('diamonds', '7')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards42():
    card1 = Card('diamonds', '2')
    card2 = Card('spades', '10')
    card3 = Card('diamonds', 'jack')
    card4 = Card('diamonds', '9')
    card5 = Card('spades', '8')
    card6 = Card('spades', '7')
    card7 = Card('hearts', '7')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards43():
    card1 = Card('diamonds', '5')
    card2 = Card('diamonds', '10')
    card3 = Card('hearts', 'queen')
    card4 = Card('diamonds', 'ace')
    card5 = Card('diamonds', '9')
    card6 = Card('clubs', 'king')
    card7 = Card('diamonds', '2')
    return [card1, card2, card3, card4, card5, card6, card7]


@pytest.fixture
def cards44():
    card1 = Card('diamonds', 'ace')
    card2 = Card('spades', 'ace')
    card3 = Card('diamonds', 'king')
    card4 = Card('spades', 'king')
    card5 = Card('diamonds', 'queen')
    card6 = Card('clubs', '6')
    card7 = Card('hearts', '6')
    return [card1, card2, card3, card4, card5, card6, card7]
