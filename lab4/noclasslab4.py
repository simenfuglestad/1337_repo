import random
from sys import exit

suits = ['spades', 'hearts', "diamonds", "clubs"]
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9',
            '10', 'jack', 'queen', 'king']

deck_of_cards = [ (a, b) for a in ranks for b in suits ]

players = []
