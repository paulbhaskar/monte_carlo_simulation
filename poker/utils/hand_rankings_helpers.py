def count_pairs(cards):
    hash_map = {}
    for card in cards:
        hash_map[card.rank] = hash_map.setdefault(card.rank, 0) + 1
    values = list(hash_map.values())
    return values.count(2)


def count_trips(cards):
    hash_map = {}
    for card in cards:
        hash_map[card.rank] = hash_map.setdefault(card.rank, 0) + 1
    values = list(hash_map.values())
    return values.count(3)


def count_quads(cards):
    hash_map = {}
    for card in cards:
        hash_map[card.rank] = hash_map.setdefault(card.rank, 0) + 1
    values = list(hash_map.values())
    return values.count(4)


def count_max_consecutive(arr):
    arr.sort()
    counters = []
    count = 1
    index = 0
    while index + 1 < len(arr):
        if arr[index+1] == arr[index]:
            index += 1
            continue
        elif arr[index+1] - arr[index] == 1:
            count += 1
        else:
            counters.append(count)
            count = 1
        index += 1
    counters.append(count)
    return max(counters)


def contains_n_card_straight(cards, n):
    hash_map = {'jack': 11, 'queen': 12, 'king': 13, 'ace': 14}
    card_ranks = [int(card.rank) if card.rank.isnumeric()
                  else hash_map[card.rank] for card in cards]
    if count_max_consecutive(card_ranks) >= n:
        return True

    hash_map['ace'] = 1
    card_ranks = [int(card.rank) if card.rank.isnumeric()
                  else hash_map[card.rank] for card in cards]
    if count_max_consecutive(card_ranks) >= n:
        return True
    return False


def contains_n_card_flush(cards, n):
    hash_map = {}
    for card in cards:
        hash_map[card.suit] = hash_map.setdefault(card.suit, 0) + 1

    for key, value in hash_map.items():
        if value >= n:
            return True, hash_map
    return False, hash_map


def get_ranks(cards):
    ranks = []
    for card in cards:
        ranks.append(card.rank)
    return ranks


def get_cards_by_suit(cards, suit):
    suited_cards = []
    for card in cards:
        if card.suit == suit:
            suited_cards.append(card)
    return suited_cards
