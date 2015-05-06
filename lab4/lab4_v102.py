from random import randint
from random import shuffle
from sys import exit

#   Suit and ranks in separate lists then use double for loop to generate
#   list of tuples

#NOTE TO SELF: CALL ALL THE FUCNTIONS IN PLAY!
#def play(self):
#   start()
#   deal()
#   getWinner()
#   osv
#osv
suits = ['spades', 'hearts', "diamonds", "clubs"]
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'jack', 'queen', 'king']
                
deck_of_cards = [ (a, b) for a in ranks for b in suits ]

players = []


class Game(object):
    
    def __init__(self):
        pass
    
    def start(self):
        print "The game will now begin\n"
        
        number_of_players = raw_input("How many players? Min 2 max 5 > ")
        print ""    
        
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
            if 1 < number_of_players < 6:
                print "%s players will attend the game\n" % number_of_players
                return (len(number_of_players))
            else:
                print "You entered a number less than 2 or greater than 5"
                exit(1)
        else:
            print "Must enter a valid number higher than 2 and lower than 5"
            exit(1)
            
    def make_and_deal(self, number):
        number = Game.start()
        for i in range(number):
            i = i + 1
            new_player = Player(i, None)
            players.append(new_player)
        return players
    
    def deal(self, players):
        new_deck = Deck(deck_of_cards)
                
        for i in range(len(players)): 
            hand = new_deck.make_hand()
                    
            new_player = Player(i, hand)
            players.append(new_player)
        play()   
    
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
                        elif Winner.hand == p.hand:
                            print "The game is tied between player%s" \
                            "and player%s" % (Winner.number, p.number)
                            exit(1)
                       
                   
                Winner.is_winner()
                         
            else:
                print "You entered a number less than 2 or greater than 5"
                exit(1)
        else:
            print "Must enter a valid number higher than 2 and lower than 5"
            exit(1)
    def getWinner(self):
        pass
        
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
        print ""
        print "Player %s has entered the game" % number
        print "------------------------------"
        #print ""
    
    def is_winner(self):
        print "The winner is player %s" % self.number
        return self
    
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
            
        if all(x == suits[0] for x in suits):
            print "It's a flush"
             
            i = 0
            for c in ranks[:-1]:
                if ranks[i + 1] == ranks[i] + 1:
                    i += 1
            if i == 4:
                print "It's a straight flush"
            elif ranks == [2, 3, 4, 5, 14]:
                print "It'a straight flush with ace"
                return 8
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
            return 4
        
        elif set(x for x in ranks if ranks.count(x) >= 3):
            if set(y for y in ranks if ranks.count(y) == 2):
                print "It's a House"
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
            print "High Card: %s" % HC
            return 0

#new_game = Game()
#Game.play(new_game)

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
