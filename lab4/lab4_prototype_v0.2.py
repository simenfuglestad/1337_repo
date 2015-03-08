from random import randint
from random import shuffle
from sys import exit

#   Suit and ranks in separate lists then use double for loop to generate
#   list of tuples

suits = ['spades', 'hearts', "diamonds", "clubs"]
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'jack', 'queen', 'king']

combinations = {
                'High Card'         : 0,
                'Pair'              : 1,
                'Two-pair'          : 2,
                'Three of a kind'   : 3,
                'Straight'          : 4,
                'Flush'             : 5,
                'Full House'        : 6,
                'Four of a kind'    : 7,
                'Straight flush'    : 8,
                'Royal flush'       : 9 }
                

deck_of_cards = [ (a, b) for a in ranks for b in suits ]

players = []


class Engine(object):
    
    def __init__(self):
        pass
 
    def play(self):
        print "The game will now begin\n"
        
        number_of_players = raw_input("How many players? Min 2 max 5 >")
        print ""    
        
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
            if 1 < number_of_players < 6:
                print "%s players will attend the game\n" % number_of_players
                
                new_deck = Deck(deck_of_cards)
                
                for i in range(number_of_players):
                    i = i + 1
                    hand = new_deck.get_hand()
                    
                    new_player = Player(i, hand)
                    players.append(new_player)
                
                for p in players:
                    Player.evaluate(p)    
                                    
            else:
                print "You entered a number less than 2 or greater than 5"
                exit(0)
        else:
            print "Must enter a valid number higher than 2 and lower than 5"
            exit(0)
        
class Deck(object):
    

    def __init__(self, deck):
        self.deck = deck
        shuffle(deck)
        print "The Deck is shuffled\n"

    def get_hand(self):
        hand = ()
        
        for c in range(5):
            r = randint(0, len(self.deck) - 1)
            hand = hand + (self.deck[r],)
            
            deck_of_cards.remove(self.deck[r])
        return hand
        

class Player(object):
    
    def __init__(self, number, hand):
        self.hand = hand
        self.number = number
        print "Player %s has entered the game" % number
        print "______________________________"
        print ""
        
    def evaluate(self):
        
        found = False
        
        while not found:
            print self.hand
            for card in self.hand:
                print card[1]
                    
            found = True

new_game = Engine()
Engine.play(new_game)
