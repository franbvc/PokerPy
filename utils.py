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


def verify_hand(hole_cards, community_cards):
    sequence = True
    five_same_suit = False

    hands = {
        'highcard': True,
        'pair': True,
        'two pairs': True,
        'three of a kind': True,
        'straight': True,
        'flush': True,
        'full house': True,
        'four of a kind': True,
        'straight flush': True,
        'royal flush': True
    }

         
        

    all_cards = hole_cards + community_cards
    numbers = [card[0] for card in all_cards]
    suits = [card[1] for card in all_cards]
    suits_quantity = {i:suits.count(i) for i in suits}
    numbers_quantity = {i:numbers.count(i) for i in numbers}

    # test for 3 or more cards of the same number
    for number in numbers_quantity:

        # four of a kind
        if numbers_quantity[number] == 4:
            hand = 
            return 'four of a kind'

        if numbers_quantity[number] >= 3:
            hands['straight'] = False
            hands['straight flush'] = False
            hands['royal flush'] = False
        
        if numbers


    # test for 5 cards of the same suit
    for suit in suits_quantity:
        if suits_quantity[suit] >= 5:
            five_same_suit = True

    # if five_same_suit == True:



    # royal_flush_numbers = ['10', 'J', 'Q', 'K', 'A']
    # if all(number in numbers for number in royal_flush_numbers):
    #     print("possible Royal Flush")
    
    print(suits_quantity)
    print(numbers_quantity)

    
    same_number = 0
    same_suit = 0

    # print(numbers, suits)

hole = [('A', 'hearts'), ('9', 'spades')]
c_cards = [('5', 'spades'), ('Q', 'hearts'), ('A', 'spades'), ('J', 'clubs'), ('K', 'spades')]

verify_hand(hole, c_cards)