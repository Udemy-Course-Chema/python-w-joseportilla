# CARD 
# SUIT, RANK, VALUE

from curses.panel import new_panel
from hashlib import new
from operator import ne
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5,
    "Six":6,
    "Seven":7,
    "Eight":8,
    "Nine":9,
    "Ten":10,
    "Jack":11,
    "Queen":12,
    "King":13,
    "Ace":14
}



class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self) -> None:
        self.deck = []

        for suit in suits:
            for rank in ranks:
                # Create the card objects
                created_card = Card(suit, rank)
                self.deck.append(created_card)
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        
        return 'The deck has :' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card Objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)


    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.all_cards)} cards.'


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self, card):
        # Card passed from Deck.deal() --> Single Card
        self.cards .append(card)
        self.values += values[card.rank]
        
        # track aces
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THAN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11.
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.ace -= 1
            

class Chips:
    def __init__(self,total):
        self.total = total 
        self.bet = 0
        
    def win_bet(self):
        self.bet += self.bet
    
    def lose_bet(self):
        self.bet -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int( input("How many chips would you like to bet?") )
        except:
            print("Sorry, please provide an integer")
        else:
            if chips.bet > chip.total:
                print("Sorry, you do not have enough chips! You have {}".format( chip.total ) )
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card( single_card )
    hand.add_card()
    
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Hit or stand ? Enter H or S")
        
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player Stands Dealer\'s turn')
            playing = False
        else:
            print("Sorry, I did no understand that, Please enter H or S ")
            continue
        break

def show_some(player,dealer):
    # dealer.cards[0]
    
    # Show only ONE of the dealer's card
    print("\n Dealer's hand:")
    print("First card hidden")
    print(dealer.cards[1])
    
    # Show all cards
    for card in player.cards :
        print( card )

def show_all(player, dealer):
    # show all the dealer's cards 
    print('\n Dealer\'s hand:')
    for card in dealer.cards:
        print(card)
        
    print("\n Dealer's hand:", *dealer.cards, sep="\n")
    # calculate and display value ( J+K = 20)
    print(f"Value of dealers hand is: { dealer.value }")
    
    # show all the players cards
    print("\nPlayer's cards")
    for card in player.cards:
        print(card)
    

# GAMING SETUP
player_one = Player('One')
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True
round_num = 0

# While game on
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One Wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_one.remove_one())

    # At War
    at_war = True

    

    while at_war:
        if player_one_cards[-1].values > player_two_cards[-1].values:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].values < player_two_cards[-1].values:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        
        else:
            print('WAR')

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player two wins!!!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("Player One Wins!!!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


    



