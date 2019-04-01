import itertools
import random

def deck():
    color = ['pik', 'kier', 'karo', 'trefl']
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
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

def histogram(znaki):
    d = dict()
    for l in znaki:
        d[l] = znaki.count(l)
    return d






def hand_rank(hand):
    #hand_rank_list = [seq[0] for seq in hand[0]]  # TODO: pobierz liste rang kart gracza. Uzyj listy skladanej.
    hand_rank_list = ['2','3','2','3','5']
    hand_color_list = [seq[1] for seq in hand[0]] # TODO: pobierz liste kolorow kart gracza. Uzyj listy skladanej.

    hand_rank_histogram = histogram(hand_rank_list)

    hand_color_histogram = histogram(hand_color_list)

    def is_rank_sequence(hand):
        pomoc = []
        for i in hand_rank_list:
            if(i == 'J'):
                i = 11
                pomoc.append(i)
            elif(i == 'Q'):
                i = 12
                pomoc.append(i)
            elif(i == 'K'):
                i = 13
                pomoc.append(i)
            elif(i == 'A'):
                i = 14
                pomoc.append(i)
            else:
                pomoc.append(int(i))
        pomoc.sort()
        print(pomoc)
        for i in range(1,len(pomoc)-1):
            if( pomoc[i] - pomoc[i-1] != 1):
                return False
        return True
            
        
            
    is_hand_rank_sequence = is_rank_sequence(hand)

    hand_strength = 0

    if( (5 in hand_color_histogram.values()) and ( 'A' in hand_rank_list ) and is_hand_rank_sequence):
        hand_strength = 10
    elif( ( 5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength =  9
    elif( ( 4 in hand_rank_histogram.values())):
        hand_strength =  8
    elif( ( 3 in hand_rank_histogram.values()) and (3 in hand_rank_histogram.values())):
        hand_strength = 7
    elif( ( 5 in hand_color_histogram.values())):
        hand_strength =  6
    elif(is_hand_rank_sequence):
        hand_strength =  5
    elif( ( 3 in hand_rank_histogram.values())):
        hand_strength =  4
    elif( (1 and 2 and 2) in hand_rank_histogram.values()):
        hand_strength =  3
    elif( ( 2 in hand_rank_histogram.values())):
        hand_strength =  2
    else:
        hand_strength = 1

    return(hand_strength)

print(hand_rank(deal(deck(),1)))


