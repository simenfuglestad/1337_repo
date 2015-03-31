import random
from sys import exit

suits = ['spades', 'hearts', "diamonds", "clubs"]
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'jack', 'queen', 'king']

#Use suits and ranks to create multidimensional array?
combination_table = [[0 for x in range(5)] for x in range(2)]
print combination_table


deck_of_cards = [ (a, b) for a in ranks for b in suits ]

class Deck(object):

    def __init__(self, deck):
        self.deck = deck
        random.shuffle(deck)
        print "The deck is shuffled \n"
    
    def start(self):
        user_input = raw_input("How many players will be playing? > ")
        print ""
        
        
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input > 1:
                print "%s players will be playing\n" % user_input
                print "Will now deal 5 cards to each player\n"
            else:
                print "You must enter a number of at least 2 players\n"
                exit(0)
 
        for i in range(user_input):
            # Really necessary to make player objects?
            # Edit loop so that hands are dealt, then shown!
            #new_player = Player()
            new_player = "player " + "%s" % (i + 1)  
            print "\nDealing hand to %s " % new_player
            new_hand = Hand.get_hand(Hand())
        
        #Player().show_hand(new_hand)
        
            
    
        
        
class Hand(object):
    def __init__(self):
        pass
    
    def get_hand(self):
        
        new_hand = []
        
        for c in range(5):
            r = random.randint(0, len(newDeck.deck) -1)
            new_hand.append(newDeck.deck[r])
            
        Player().show_hand(new_hand)
                
        
class Player(object):
    def __init__(self):
        pass
        
    def show_hand(self, cards):
        print "This is my hand"
        print cards


newDeck = Deck(deck_of_cards)
newDeck.start()
