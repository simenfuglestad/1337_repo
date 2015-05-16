# NOTE: Read 'OO' as Object oriented

from random import randint
from random import shuffle
from sys import exit

# First step is to set up a deck. To do this we first make two lists, one for 
# suits and one for ranks. 

suits = ['spades', 'hearts', "diamonds", "clubs"]
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'jack', 'queen', 'king']
                
# To complete the deck we use list comprehension to create a new list of
# tuples. The tuples in the list is comprised of each element in a and b
# added in unique combinations.
deck_of_cards = [ (a, b) for a in ranks for b in suits ]

# The empty list 'players' is used later in the program for a variety of
# purposes. While it does not comply with the OO structure of the rest of
# the program it does not break any functionality and make the program 
# easier to read.

players = []

# The 'Game' class is the main class of the program. Game contains the method
# for starting a game of poker and the algorithm for determining which player
# wins the game.

class Game(object):
    
    # The __init__ of class game does not execute any methods. We chose this
    # because it is more compliant with OO structure in the way it gives us
    # control over when to call the method play(), as opposed to simply
    # executing play() every time we instanciate a game class. 
    
    def __init__(self):
        pass
    
    # play() serves as the entry point of the program as it starts and handles
    # the game itself. 
    # Play contains the algorithms for creating player objects, 
    # creating a deck object, dealing hands and determining tiebreakers. 
    # play() utilizies evaluate from the Player class to determine the hand
    # values of the different players. play() also uses isWinner from the class
    # Player() to determine the winner.
      
    def play(self):
        print "The game will now begin\n"
        
        # We added an semi-arbitrary minimum and maximum amount of players for 
        # the game to make sense to be played at all. Also a low maximum 
        # ensures that the deck Object does not run out of cards.
        
        number_of_players = raw_input("How many players? Min 2 max 5 > ")
        print ""    
        
        # We perform a check it the entered number of players is actually an
        # integer and the if it matches our criteria for min and max players
        
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
            if 1 < number_of_players < 6:
                print "%s players will attend the game\n" % number_of_players
                
                # Here we create a new deck Object using our list of tuples as 
                # a parameter. See the Deck class for more info.
                
                new_deck = Deck(deck_of_cards)
                
                # Based on the previous raw_input we create a number of new
                # player objects and add them to our empty and aforementioned
                # list 'players'. Players are given a number i and a hand as
                # parameteres. See the Player class for more info on the
                # parameteres and the Deck class for more info on make_hand()
                
                for i in range(number_of_players):
                    i = i + 1
                    hand = new_deck.make_hand()
                    
                    new_player = Player(i, hand)
                    players.append(new_player)
                
                # To begin the process of determining which Player is the 
                # winner we first create a new Player object 'Player 0'..
                    
                Winner = Player(0, ())
                
                # Here we loop thorugh the list 'players' and set each
                # player's hand_value to be equal a number returned from 
                # evaluate. The algorithm is set up so that if the loop
                # encounters a hand_value greater than what is found in
                # 'Winner', then Winner is assigned to be that Player object.
                # See the 'readme.txt' for more extensive info.
                
                for p in players:
                    print p.hand                    
                    p.hand_value = Player.evaluate(p)
                    
                    if p.hand_value > Winner.hand_value:
                        Winner = p
                    
                    print ""
                
                # After determining which Player has the highest hand value
                # we need to ensure that no other Player object has an equal
                # hand value to that of the Winner. To do this we must loop
                # over the remaning Player objects in 'players' and compare 
                # them to 'Winner'. Since we must avoide to compare 'Winner' 
                # to itself we must delete the corresponding Player object
                # before starting the loop.
                    
                if Winner in players:
                    players.remove(Winner)
                
                # For the process of checking for and then getting the
                # tiebreaker we again loop through the list of Players and
                # this time compare the hand value to 'Winner''s hand_value.
                # If there's a match we perform the method get_high_card()
                # to determine which player is the Winner. get_high_card()
                # is performed a number of times equal to the number of cards
                # in a hand, using 'i' as a control variable to determine 
                # the index of the cards that are being compared. If all the
                # get_high_card() exectuions match then the game is determined
                # a tie and the program exits.
                         
                i = 4    
                for p in players:
                    print ""
                    if Winner.hand_value == p.hand_value:
                        if Winner.get_high_card(i) < p.get_high_card(i):
                            i = i - 1
                            Winner = p
                        elif Winner.hand == p.hand:
                            print "The game is tied between player%s" \
                            "and player%s" % (Winner.number, p.number)
                            exit(1)
                
                # Finaly after ensuring we have the right Player object as a
                # 'Winner', we call is_winner() from the Player class to
                # print a simple string showing the user which player that won
                # the game.      
                   
                Winner.is_winner()
            
            # This else clause is executed if the user enters an invalid 
            # number afer starting the game.
                         
            else:
                print "You entered a number less than 2 or greater than 5"
                exit(1)
        # This else clause is executed if the user enters a non-integer value
        # after starting the game.s
        
        else:
            print "Must enter a valid number higher than 2 and lower than 5"
            exit(1)

# The deck class serves as a means of instanciating new deck objects and
# also holds a method for creating hands of cards.
      
class Deck(object):   
    
    # The __init__ of deck takes a single parameter (aside from obliagtory 
    # 'self') named 'deck'. In the play() method we pass deck as the list of 
    # tuples created in the beginning of the program. Furthermore the deck is
    # shuffled and a short message is printed to the user.
    
    def __init__(self, deck):
        self.deck = deck
        shuffle(deck)
        print "The Deck is shuffled\n"
    
    # The make_hand method selects 5 random cards (tuples) from a Deck object
    # and puts them together in a tuple of tuples. Then it removes the
    # selected card from the deck so that it can't be picked again.
    
    def make_hand(self):
        hand = ()
        
        for c in range(5):
            r = randint(0, len(self.deck) - 1)
            hand = hand + (self.deck[r],)
            deck_of_cards.remove(self.deck[r])
        return hand

# The Player class is responsible for creating Player objects that will attend
# the game and holds a number of methods related to getting the hand_value and
# determining which player is the winner. Every player object has a variable
# 'hand_value' which always defaults to zero but is utlimatly changed during
# the play() of class Game.
        
class Player(object):
    hand_value = 0
    
    # Player objects take 2 paramteres, 'number' and 'hand'. 'number' provides
    # an easy way to keep track of players while hand is the tuple of tuples
    # that is the player's hand of cards/
    
    def __init__(self, number, hand):
        self.hand = hand
        self.number = number
        print ""
        print "Player %s has entered the game" % number
        print "------------------------------"
    
    # This short method returns a string with the 'number' param attached
    # to it. Used by play() in class Game to show the user which player that
    # won the game. 
    
    def is_winner(self):
        print "The winner is player %s" % self.number
        return self
    
    # This method is used in the case that two players have equal 'hand_value'
    # and must decide by high_card. An empty list 'ranks' is instanciated
    # and then each card in the Players hand is added to it. String names
    # are replaced with integer values to match their value. Returns a number
    # in ranks speicified by the index parameter.
    
    def get_high_card(self, index):
        ranks = []
        for card in self.hand:
            if card[0] == 'jack':
                ranks.append(11)
            elif card[0] == 'queen':
                ranks.append(12)
            elif card[0] == 'king':
                ranks.append(13)
            elif card[0] == 'ace':
                ranks.append(14)
            else:
                ranks.append(int(card[0]))
        ranks.sort()
        if not ranks:
            return 0
        else:
            print ranks
            print self.number    
            return ranks[index]
    
    # evalutate() contains the main algorithms for determining a player's
    # 'hand_value'. It is setup as an eliminary sequence starting with every
    # combination that involve all suits being equal and ending with
    # high card. Returns a value between 0-9 which represents all the possible
    # combinations in poker, where 0 is high-card and 9 is royal flush. Note
    # that some combinations are inclusive of others and therefore some return
    # statements are placed AFTER checking for all possible combinations.
        
    def evaluate(self):
        
        ranks = []
        suits = []
        
        # Replace string values in hand with integers corresponding to their
        # value the append them to 'ranks' and 'suits' respectively. Ranks
        # are then sorted.
        
        for card in self.hand:
            if card[0] == 'jack':
                ranks.append(11)
            elif card[0] == 'queen':
                ranks.append(12)
            elif card[0] == 'king':
                ranks.append(13)
            elif card[0] == 'ace':
                ranks.append(14)
            else:
                ranks.append(int(card[0]))
                
            suits.append(card[1])
            ranks.sort()
        
        # First step in algorithm: Determine if flush.
            
        if all(x == suits[0] for x in suits):
            
            # Second step: Determine if straight flush.
            
            i = 0
            for c in ranks[:-1]:
                if ranks[i + 1] == ranks[i] + 1:
                    i += 1
            if i == 4:
                print "It's a straight flush"
                return 8
            elif ranks == [2, 3, 4, 5, 14]:
                print "It'a straight flush with ace"
                return 8
            
            else:
                print "It's a flush"
                return 5
            
            # Third step: Determine if royal flush    
                
            if ranks[4] == 14:
                print "It's a royal flush!!!!" 
                return 9
                
            # Here we return straght flush if royal flush fails. We do this
            # since straight flush is an inclusive combination of Royal flush.
            else:
                return 8
        
        # Fourth step: Determine if straight. 
        elif all(x == y for x, y in enumerate(ranks, ranks[0])):
            print "It's a straight"
            return 4
        
        # We want a straight with lower ace to count as well and add it
        # separatly.
        
        elif ranks == [2, 3, 4, 5, 14]:
            print "It's a straight"
            return 4
        
        # Fifth step: Determine if house. We do this by splitting up the ranks
        # in equal sets and the count the sets.
        
        elif set(x for x in ranks if ranks.count(x) >= 3):
            if set(y for y in ranks if ranks.count(y) == 2):
                print "It's a House"
                return 6
                
            # Sixth step: Determine if three of a kind 
            # We use the inforamtion already gathered from a negative testing
            # for and test the length of the sets to match three of a kind.            
                        
            elif len(set(ranks)) == 3:
                print "Three of a kind"
                return 3
            
            # Seventh setp: Determine if Four of a kind
            # Like the sixth step we use the data of the previous checks
            # and can conlude with the result being four of a kind.            
            
            else:
                print "Four of a kind"
                return 7
        
        # Eigth step: Determine if Two Pairs.
        # Same conept as with house: Makes sets out of ranks and test the
        # length of the sets to match.
        
        elif len(set(ranks)) == 3:
            print "Two pairs"
            return 2
        
        # Ninth step: Detemine if One Pair
        # Again expanding upon previous assertions and test the length of the
        # sets to match one pair.
        
        elif len(set(ranks)) == 4:
            print "One pair"
            return 1
        
        # Tenth step: Deterimine if High Card.
        # Since all other possible combinations have been tested this far
        # the only remaining outcome is high card.
        
        else:
            HC = max(ranks)
            print "High Card: %s" % HC
            return 0

#new_game = Game()
#Game.play(new_game)

# The test() function asserts wheter evaluate() returns the proper value based
# on tuples mathcing the criteria of the value.

def test():
    assert Player(0, (('4', 'diamonds'), ('5', 'diamonds'), ('king', 'hearts'),
        ('ace', 'spades'), ('jack', 'clubs'))).evaluate() == 0
        
    assert Player(1, (('4', 'diamonds'), ('4', 'spades'), ('king', 'hearts'),
        ('ace', 'spades'), ('jack', 'clubs'))).evaluate() == 1
        
    assert Player(2, (('4', 'diamonds'), ('4', 'spades'), ('king', 'hearts'),
        ('ace', 'spades'), ('king', 'clubs'))).evaluate() == 2
        
    assert Player(3, (('4', 'diamonds'), ('4', 'spades'), ('4', 'hearts'),
        ('ace', 'spades'), ('king', 'clubs'))).evaluate() == 3
    
    assert Player(4, (('4', 'diamonds'), ('5', 'spades'), ('6', 'hearts'),
        ('7', 'spades'), ('8', 'clubs'))).evaluate() == 4
    
    assert Player(4, (('ace', 'diamonds'), ('2', 'spades'), ('3', 'hearts'),
        ('4', 'spades'), ('5', 'clubs'))).evaluate() == 4
        
    assert Player(5, (('ace', 'spades'), ('2', 'spades'), ('3', 'spades'),
        ('4', 'spades'), ('jack', 'spades'))).evaluate() == 5
    
    assert Player(6, (('ace', 'spades'), ('ace', 'hearts'), ('3', 'spades'),
        ('3', 'spades'), ('3', 'spades'))).evaluate() == 6
    
    assert Player(7, (('ace', 'spades'), ('ace', 'hearts'), ('ace', 'clubs'),
        ('ace', 'clubs'), ('3', 'spades'))).evaluate() == 7
    
    assert Player(8, (('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'),
        ('5', 'hearts'), ('6', 'hearts'))).evaluate() == 8
    
    assert Player(8, (('ace', 'hearts'), ('2', 'hearts'), ('3', 'hearts'),
        ('4', 'hearts'), ('5', 'hearts'))).evaluate() == 8
    
    assert Player(9, (('10', 'clubs'), ('jack', 'clubs'), ('queen', 'clubs'),
        ('king', 'clubs'), ('ace', 'clubs'))).evaluate() == 9
    
    print "Test Complete"
test()
