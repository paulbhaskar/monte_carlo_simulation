import decimal

from poker.texas_holdem import *

trials = 1000000
for trial in range(trials):
    count = 0
    game = TexasHoldem()
    community_cards = game.community_cards
    player_cards = []
    hole_cards = []
    for player in range(7):
        player_hole_cards = game.deal(2)
        hole_cards.append(player_hole_cards)
        player_card = TexasHoldem.player_cards(
            community_cards, player_hole_cards)
        player_cards.append(player_card)

    trial_rankings = TexasHoldem.player_hand_rankings(player_cards)
    filtered_trial_rankings = dict(
        (key, value) for key, value in trial_rankings.items() if value >= 8)
    if len(filtered_trial_rankings) >= 2:
        bad_beat_count = 0
        keys = []
        for key, value in filtered_trial_rankings.items():
            if TexasHoldem.check_if_both_hole_cards_used(community_cards, hole_cards[key]):
                bad_beat_count += 1
                keys.append(key)
        if bad_beat_count >= 2:
            count += 1
            print(trial_rankings)
            print("community cards", community_cards)

            for key in keys:
                player_cards = TexasHoldem.player_cards(
                    community_cards, hole_cards[key])
                best_hand = TexasHoldem.determine_hand(player_cards)[1]
                best_two_hold_card_combination = TexasHoldem.calculate_five_cards_used(
                    best_hand, community_cards, hole_cards[key], 3)[0]
                print('hole cards', hole_cards[key])
                print('best five cards', best_two_hold_card_combination,
                      TexasHoldem.determine_hand(best_two_hold_card_combination)[1])

print(decimal.Decimal(count/trials) * 100)
