# import random

# class Deck:
#     # define deck and shuffle
#     def __init__(self):
#         pass
    
#     def deck(self):
#         self.cards = []
#         suits = ['spades', 'clubs', 'hearts', 'diamonds']
#         ranks = [
#             {'rank': 'A', 'value': 11},
#             {'rank': '2', 'value': 2},
#             {'rank': '3', 'value': 3},
#             {'rank': '4', 'value': 4},
#             {'rank': '5', 'value': 5},
#             {'rank': '6', 'value': 6},
#             {'rank': '7', 'value': 7},
#             {'rank': '8', 'value': 8},
#             {'rank': '9', 'value': 9},
#             {'rank': '10', 'value': 10},
#             {'rank': 'J', 'value': 10},
#             {'rank': 'Q', 'value': 10},
#             {'rank': 'K', 'value': 10}
#         ]
    
#         for suit in suits:
#             for rank in ranks:
#                 self.cards.append((suit, rank))

#     def shuffle(self):
#         if len(self.cards) > 1:
#             random.shuffle(self.cards)

# class Human:
#     # define mechanics
#     hand = []

#     def __init__(self, cards):
#         self.cards = cards

# class Player(Human):
#     # Player
#     hand = []

#     def __init__(self, cards):
#         super().__init__(cards)

#     def deal(self, dealer):
#         if len(self.hand) == 0:
#             self.hand.append(self.cards.pop())
#             self.hand.append(self.cards.pop())
#             print(f"Player 1's hand is {self.hand}")  
#             print(f"Dealer's hand is {dealer.hand}")

#         self.total = sum([card[1]['value'] for card in self.hand])

#         while self.total < 21:
#             user_input = input('Would you like to hit or stand? ')
#             user_input = user_input.lower()
            
#             if user_input == 'hit':
#                 self.hand.append(self.cards.pop())
#                 self.total = sum([card[1]['value'] for card in self.hand])
#                 print(f"Player 1's hand is {self.hand}")
#                 print(f"Dealer's hand is {dealer.hand}")
#             elif user_input == 'stand':
#                 break
        
#         if self.total > 21:
#             print('You busted')
#         elif self.total <= 21:
#             print(self.hand)

# class Dealer(Human):
#     # Dealer/Robot
#     hand = []

#     def __init__(self, card):
#         super().__init__(card)

#     def deal(self):
#         if len(self.hand) == 0:
#             self.hand.append(self.cards.pop())
#             self.hand.append(self.cards.pop())
#             print(f"Dealer's hand is {self.hand}")

#         self.total = sum([card[1]['value'] for card in self.hand])

#         while self.total < 21:
#             if self.total < 21:
#                 self.hand.append(self.cards.pop())
#                 self.total = sum([card[1]['value'] for card in self.hand])
#                 print(f"Dealer's hand is {self.hand}")
#             elif self.total > 21:
#                 print('Dealer busted')
#                 break

# game = Deck()
# game.deck()
# game.shuffle()
# cards = game.cards
# human = Human(cards)
# hand = human.hand
# player = Player(cards)
# dealer = Dealer(cards)
# dealer.deal()
# player.deal(dealer)

# game_deck = Deck.deck
# deck = cards


import random

class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = [
            {'rank': 'A', 'value': 11},
            {'rank': '2', 'value': 2},
            {'rank': '3', 'value': 3},
            {'rank': '4', 'value': 4},
            {'rank': '5', 'value': 5},
            {'rank': '6', 'value': 6},
            {'rank': '7', 'value': 7},
            {'rank': '8', 'value': 8},
            {'rank': '9', 'value': 9},
            {'rank': '10', 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10}
        ]

        self.cards = [(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.total += card[1]['value']
        if card[1]['rank'] == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.total > 21 and self.aces > 0:
            self.total -= 10
            self.aces -= 1

class Player:
    def __init__(self):
        self.hand = Hand()

    def deal_initial_cards(self, deck):
        for _ in range(2):
            card = deck.cards.pop()
            self.hand.add_card(card)

    def hit(self, deck):
        card = deck.cards.pop()
        self.hand.add_card(card)

    def is_busted(self):
        return self.hand.total > 21

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def deal_initial_cards(self, deck):
        for _ in range(2):
            card = deck.cards.pop()
            self.hand.add_card(card)

    def hit(self, deck):
        while self.hand.total < 17:
            card = deck.cards.pop()
            self.hand.add_card(card)

    def is_busted(self):
        return self.hand.total > 21

def play_blackjack():
    deck = Deck()
    deck.create_deck()
    deck.shuffle()

    player = Player()
    dealer = Dealer()

    player.deal_initial_cards(deck)
    dealer.deal_initial_cards(deck)

    print(f"Player's hand: {player.hand.cards}")
    print(f"Dealer's hand: {dealer.hand.cards[0]}")

    while True:
        action = input("Would you like to hit or stand? ").lower()

        if action == 'hit':
            player.hit(deck)
            print(f"Player's hand: {player.hand.cards}")
            
            if player.is_busted():
                print("Player busts. Dealer wins!")
                return

        elif action == 'stand':
            dealer.hit(deck)
            print(f"Dealer's hand: {dealer.hand.cards}")

            if dealer.is_busted():
                print("Dealer busts. Player wins!")
                return

            while dealer.hand.total < 17:
                dealer.hit(deck)
                print(f"Dealer's hand: {dealer.hand.cards}")

                if dealer.is_busted():
                    print("Dealer busts. Player wins!")
                    return

                if dealer.hand.total >= 17:
                    if player.hand.total > dealer.hand.total:
                        print("Player wins!")
                    elif player.hand.total < dealer.hand.total:
                        print("Dealer wins!")
                    else:
                        print("It's a tie!")
                    return

play_blackjack()