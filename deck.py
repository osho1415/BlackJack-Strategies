import random 

class Deck: 

    TITLE_MAP = {
        '2': "Two",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine",
        '10': "Ten",
        'Q': "Queen",
        'K': "King",
        'A': "Ace",
    }

    POINT_MAP = {
        "2" : 2 ,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Q': 10,
        'K': 10,
        'A': [1,11]
    }

    def __init__ (self): 

        # initialize a shuffled 48-deck, excluding jacks
        self.deck = []
        for title in self.TITLE_MAP: 
            self.deck += [title]*4
        random.shuffle(self.deck)
        self.initial_cards()


    def print_deck(self): 
        print(self.deck)

    def initial_cards(self):
        return[self.deck.pop(0),self.deck.pop(0)]
    
    def get_cards(self): 
        return self.dealer_card, self.player_card
    
    def get_points(self,card):
        return self.POINT_MAP[card]
    
    def hit(self):
        return self.deck.pop(0) 
    
    def shuffle(self): 
        random.shuffle(self.deck)