import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Place your bet: "))
        except:
            print("INVALID INPUT: Bet needs to be a number")
        else:
            if chips.bet > chips.total:
                print(f"INVALID AMOUNT: Bet of {chips.bet} exceeds chips amount {chips.total}")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        choice = input("Hit or stand? ")
        if choice.lower() == "hit":
            hit(deck, hand)
            break
        elif choice.lower() == "stand":
            print("Player stands, dealer`s turn")
            playing = False
            break
        print("Please try again")


def show_except_hidden(player, dealer):
    print(f"\nPlayer total value is at {player.value}, num of aces {player.aces}")
    for card in player.cards:
        print("Player card: {}".format(card))

    print(f"\nDealer total value is at {dealer.value - dealer.cards[0].value} plus a hidden card")
    print("Dealer card: {}".format(dealer.cards[-1]))
    print("Dealer card: HIDDEN")


def show_all(player, dealer):
    print(f"\nPlayer total value is at {player.value}, num of aces {player.aces}")
    for card in player.cards:
        print("Player card: {}".format(card))
    print(f"\nDealer total value is at {dealer.value}, num of aces {player.aces}")
    for card in dealer.cards:
        print("Dealer card: {}".format(card))


def player_busts(player_chips):
    print("Player lost, cards total over 21")
    player_chips.lose_bet()
    print(f"Player lost {player_chips.bet} chips")


def dealer_busts(player_chips):
    print("Dealer lost, cards total over 21")
    player_chips.win_bet()
    print(f"Player wins {player_chips.bet} chips")


def dealer_wins(player_chips):
    print("Dealer wins with greater total")
    player_chips.lose_bet()
    print(f"Player lost {player_chips.bet} chips")


def player_wins(player_chips):
    print("Player wins with total 21")
    player_chips.win_bet()
    print(f"Player wins {player_chips.bet} chips")

def push():
    print("Dealer and player tie! PUSH")


playing = True
num_of_rounds = 0

player_chips = Chips()
while True:
    num_of_rounds += 1
    print(f"Welcome to round {num_of_rounds} of blackjack")
    print(f"Player funds: {player_chips.total}")

    new_deck = Deck()
    new_deck.shuffle()

    player = Hand()
    dealer = Hand()
    hit(new_deck, dealer)
    hit(new_deck, player)
    hit(new_deck, dealer)
    hit(new_deck, player)

    take_bet(player_chips)

    while playing:

        show_except_hidden(player, dealer)

        hit_or_stand(new_deck, player)

        if player.value > 21:
            show_except_hidden(player, dealer)
            player_busts(player_chips)
            break
        elif player.value == 21:
            player_wins(player_chips)
            break
    if player.value < 21:
        while dealer.value < player.value:
            hit(new_deck, dealer)
        show_all(player, dealer)
        if dealer.value > 21:
            dealer_busts(player_chips)
        elif dealer.value > player.value:
            dealer_wins(player_chips)
        elif dealer.value == player.value:
            push()
    if input("Play again? (yes/no)") == "yes" and player_chips.total > 0:
        playing = True
    else:
        print("Thank you for playing")
        break
