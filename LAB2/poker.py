import itertools
import random

def deck():
    color = ['pik', 'kier', 'karo', 'trefl']
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jupek', 'Królowa', 'Król', 'As']
    deck = list(itertools.product(value, color))
    
    return deck

def shuffle_deck(decko):
    random.shuffle(decko)
    

def deal(deck, n):
    if(n*5 < 52):
        random.shuffle(deck)
        playersDeck = list()
        for i in range(n):
            playersCards = list()
            for j in range(5):
                playersCards.append(deck.pop(0))
            playersDeck.append(playersCards)
        return playersDeck
    else:
        return false

deck = deck()

print(deal(deck, 5))
