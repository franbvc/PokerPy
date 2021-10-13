from typing import Sequence

card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['diamonds', 'clubs', 'hearts', 'spades']


def find_highest_card(cards):
    highest_card = ''
    highest_value = -1
    for card in cards:
        value = card_numbers.index(card[0])

        if value > highest_value:
            highest_card = card[0]
            highest_value = value
    
    return highest_card


def verify_sequence(all_cards):
    numbers = [card_numbers.index(card[0]) for card in all_cards]
    numbers.sort()
    numbers = list(set(numbers))

    sequence_length = 1
    i = 0
    while i < len(numbers)-1:
        if sequence_length > 4:
            return True

        if numbers[i+1] == numbers[i] + 1:
            sequence_length += 1
        else:
            sequence_length = 1
        i += 1

    if sequence_length > 4:
        return True

    #verify if sequence is cyclic (Ex.: Q, K, A, 2, 3)
    if numbers[0] == 0 and numbers[-1] == 12:
        sequence_forward = 1
        sequence_backward = 1

        i = 0
        while i < len(numbers)-1:
            if numbers[i+1] == numbers[i] + 1:
                sequence_forward += 1
            else:
                break
            i += 1

        i = len(numbers)-1
        while i > 0:
            if numbers[i-1] == numbers[i] - 1:
                sequence_backward += 1
            else:
                break
            i -= 1

        if sequence_backward + sequence_forward > 4:
            return True

    return False


def verify_same_number(all_cards):
    numbers = [card[0] for card in all_cards]
    numbers_quantity = {i:numbers.count(i) for i in numbers}
    same_n_combinations = []

    for value in numbers_quantity.values():
        if value == 4:
            return 'four of a kind'

        elif value > 1:
            same_n_combinations.append(value)

    if len(same_n_combinations) == 1:
        if same_n_combinations[0] == 2:
            return 'pair'
        if same_n_combinations[0] == 3:
            return 'three of a kind'

    if len(same_n_combinations) > 1:
        if 3 in same_n_combinations and 2 in same_n_combinations:
            return 'full house'

        if 3 in same_n_combinations:
            return 'three of a kind'

        else:
            return 'two pairs'
    
    return None


def verify_same_suit(all_cards):
    same_suit_cards = []
    suits = [card[1] for card in all_cards]
    suits_quantity = {i:suits.count(i) for i in suits}

    for suit in suits_quantity:
        if suits_quantity[suit] >= 5:

            for card in all_cards:
                if card[1] == suit:
                    same_suit_cards.append(card)
                    
            return True, same_suit_cards

    return False, []


def verify_straight_flush(same_suit_cards):
    return verify_sequence(same_suit_cards)


def verify_royal_flush(same_suit_cards):
    royal_flush_numbers = ['10', 'J', 'Q', 'K', 'A']
    numbers = [card[0] for card in same_suit_cards]
    
    if all(n in royal_flush_numbers for n in numbers):
        return True

    return False


def verify_hand(hole_cards, community_cards):
    hands = {
        'highcard': False,
        'pair': False,
        'two pairs': False,
        'three of a kind': False,
        'straight': False,
        'flush': False,
        'full house': False,
        'four of a kind': False,
        'straight flush': False,
        'royal flush': False
    }

    all_cards = hole_cards + community_cards
    sequence = verify_sequence(all_cards)
    five_same_suit, same_suit_cards = verify_same_suit(all_cards)

    if five_same_suit:
        straight_flush = verify_straight_flush(same_suit_cards)
        if straight_flush:
            royal_flush = verify_royal_flush(same_suit_cards)
            if royal_flush:
                return 'royal flush'
            else:
                return 'straight flush'
    
    same_number_hand = verify_same_number(all_cards)
    if same_number_hand is not None:
        if same_number_hand == 'four of a kind' or same_number_hand == 'full house':
            return same_number_hand
        hands[same_number_hand] = True

    if five_same_suit:
        return 'flush'

    if sequence:
        return 'straight'

    for hand in hands:
        if hands[hand] == True:
            return hand

    return 'highcard'


hole = [('7', 'spades'), ('K', 'diamonds')]
c_cards = [('10', 'spades'), ('9', 'spades'), ('8', 'spades'), ('7', 'hearts'), ('6', 'spades')]

# print(verify_sequence(hole + c_cards))

# print(verify_same_number(hole + c_cards))

print(verify_hand(hole, c_cards))

# print(verify_same_suit(hole + c_cards))

royal_flush_test = [('10', 'spades'), ('9', 'spades'), ('8', 'spades'), ('7', 'spades'), ('6', 'spades')]
# print(verify_sequence(royal_flush_test))