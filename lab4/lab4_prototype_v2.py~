import random
from sys import exit

suits = ['spades', 'hearts', "diamonds", "clubs"]
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'jack', 'queen', 'king']

combination_table = [[0 for x in range(5)] for x in range(5)]
#print combination_matrix




deck_of_cards = [ (a, b) for a in ranks for b in suits ]

class Deck(object):

    def __init__(self, deck):
        self.deck = deck
        random.shuffle(deck)
        print "The deck is shuffled \n"
    
    def start(self):
        user_input = raw_input("How many players will be playing? > ")
        print ""
        
        #   Add: Create new player objects here based on input
        
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input > 1:
                print "%s players will be playing\n" % user_input
                print "Will now deal 5 cards to each player\n"
            else:
                print "You must enter a number of at least 2 players\n"
                exit(0)
 
        for i in range(user_input):
            print "\nDealing hand number %s\n" % (i + 1)
            new_hand = Deck.get_hand(self)
        
    #   Move this to class Hand?
    def get_hand(self):
        #Deck.get_deck(self)
        
        new_hand = []
        
        for c in range(5):
            r = random.randint(0, len(self.deck) -1)
            new_hand.append(self.deck[r])
            print new_hand
            
        return new_hand
            
        
    def get_deck(self):
        
        return None
        
        
class Player(object):
    def __init__(self):
        pass


class Hand(object):
    def __init__(self):
        pass
        



newDeck = Deck(deck_of_cards)
print newDeck.start()
