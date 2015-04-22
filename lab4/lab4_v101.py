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
        
        number_of_players = raw_input("How many players? Min 2 max 5 > ")
        print ""    
        
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
            if 1 < number_of_players < 6:
                print "%s players will attend the game\n" % number_of_players
                
                new_deck = Deck(deck_of_cards)
                
                for i in range(number_of_players):
                    i = i + 1
                    hand = new_deck.make_hand()
                    
                    new_player = Player(i, hand)
                    players.append(new_player)
                    
                Winner = Player(0, ())
                
                for p in players:
                    print p.hand                    
                    p.hand_value = Player.evaluate(p);
                    
                    if p.hand_value > Winner.hand_value:
                        Winner = p
                    
                    print ""
                    
                if Winner in players:
                    players.remove(Winner)
                         
                i = 4    
                for p in players:
                    print ""
                    if Winner.hand_value == p.hand_value:
                        if Winner.get_high_card(i) < p.get_high_card(i):
                            i = i - 1
                            Winner = p
                            #break
                        elif Winner.hand == p.hand:
                            print "The game is tied between player%s and player%s" % (Winner.number, p.number)
                            exit(1)
                       
                   
                Winner.is_winner()
                         
            else:
                print "You entered a number less than 2 or greater than 5"
                exit(1)
        else:
            print "Must enter a valid number higher than 2 and lower than 5"
            exit(1)
        
class Deck(object):   

    def __init__(self, deck):
        self.deck = deck
        shuffle(deck)
        print "The Deck is shuffled\n"

    def make_hand(self):
        hand = ()
        
        for c in range(5):
            r = randint(0, len(self.deck) - 1)
            hand = hand + (self.deck[r],)
            deck_of_cards.remove(self.deck[r])
        return hand
        
class Player(object):
    hand_value = 0
    
    def __init__(self, number, hand):
        self.hand = hand
        self.number = number
        
        print "Player %s has entered the game" % number
        print "______________________________"
        print ""
    
    def is_winner(self):
        print "The winner is player %s" % self.number
    
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
        
    def evaluate(self):
        
        ranks = []
        suits = []
        
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
            #ranks = [2, 2, 2, 2, 6]
        #print suits
        #print ranks[0] + 1
        #print self.hand
            
        if all(x == suits[0] for x in suits):
            print "it's a flush"
             
            i = 0
            for c in ranks[:-1]:
                if ranks[i + 1] == ranks[i] + 1:
                    i += 1
            if i == 4:
                #pass
                print "It's a straight flush"
            else:
                return 5
                
            if ranks[4] == 14:
                print "It's a royal flush!!!!"
                return 9
            else:
                return 8
        
        elif all(x == y for x, y in enumerate(ranks, ranks[0])):
            print "It's a straight"
            return 4
        
        elif ranks == [2, 3, 4, 5, 14]:
            print "It's a straight"
            return 14
        
        elif set(x for x in ranks if ranks.count(x) >= 3):
            if set(y for y in ranks if ranks.count(y) == 2):
                print "House"
                return 6
            elif len(set(ranks)) == 3:
                print "Three of a kind"
                return 3
            else:
                print "Four of a kind"
                return 7
        
        elif len(set(ranks)) == 3:
            print "Two pairs"
            return 2
        
        elif len(set(ranks)) == 4:
            print "One pair"
            return 1   
    
        else:
            HC = max(ranks)
            #print ranks
            print "High Card: %s" % HC
            return 0
            #print self.hand_value

new_game = Engine()
Engine.play(new_game)
