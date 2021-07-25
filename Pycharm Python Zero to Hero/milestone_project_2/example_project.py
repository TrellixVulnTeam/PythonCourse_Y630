import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
cards_drawn_at_war = 5


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


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


if __name__ == '__main__':
    # GAME SETUP
    new_deck = Deck()
    new_deck.shuffle()

    jose = Player('Jose')
    phillip = Player('Phillip')

    for x in range(26):
        jose.add_cards(new_deck.deal_one())
        phillip.add_cards(new_deck.deal_one())

    game_on = True

    # GAME
    round_num = 0
    while game_on:

        round_num += 1
        print(f"Round {round_num}")

        # Check if a player has won
        if len(jose.all_cards) == 0:
            print(f'{jose.name}, out of cards! {phillip.name} Wins!')
            game_on = False
            break
        elif len(phillip.all_cards) == 0:
            print(f'{phillip.name}, out of cards! {jose.name} Wins!')
            game_on = False
            break

        # START NEW ROUND
        player_one_cards = [jose.remove_one()]
        player_two_cards = [phillip.remove_one()]

        # WAR
        at_war = True
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                jose.add_cards(player_two_cards)
                jose.add_cards(player_one_cards)
                at_war = False
                break
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                phillip.add_cards(player_one_cards)
                phillip.add_cards(player_two_cards)
                at_war = False
                break
            else:
                print("WAR!")
                if len(jose.all_cards) < cards_drawn_at_war:
                    print(f"{jose.name} unable to declare war")
                    print(f"{phillip.name} WINS!")
                    game_on = False
                    break
                elif len(phillip.all_cards) < cards_drawn_at_war:
                    print(f"{phillip.name} unable to declare war")
                    print(f"{jose.name} WINS!")
                    game_on = False
                    break
                else:
                    for x in range(cards_drawn_at_war):
                        player_one_cards.append(jose.remove_one())
                        player_two_cards.append(phillip.remove_one())
    print(jose, phillip)
