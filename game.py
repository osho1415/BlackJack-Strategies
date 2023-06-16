import random 
from deck import Deck

class Game: 

    """
    amount : total money we have 
    bet : total bet placed for this round
    strategy : tells which strategy to use 
    ------for debugging or split rounds only------ 
    deckc  : the deck being used
    player : initial cards with player 
    dealer : intial cards with dealer 
    """
    def __init__ (self,amount,bet,strategy,player=None,dealer=None,deck=None): 
        self.amount = amount
        self.bet = bet 
        if (deck == None): 
            self.deck = Deck() 
        else: 
            self.deck = deck 
        self.strategy = strategy
        # STARTING A NEW ROUND
        if (player == None and dealer == None): 
            self.player_cards = self.deck.initial_cards()
            self.dealer_cards = self.deck.initial_cards()
        # CONTINUING AN OLD ROUND
        else: 
            self.player_cards = player
            self.dealer_cards = dealer 


    """ 
    This function plays a single round of blackjack, with the given parameters: 
        strategy : tells the strategy to employ: 
                0: basic strategy 
                1: Card counting 
        
        bet  : the bet placed 
        """
    def play_round(self): 
        if (self.strategy == 0): 
            self.basic_strategy()
        
        

    def basic_strategy(self): 
        if (self.amount < self.bet): 
            return None
        #PAIRS
        if (self.player_cards[0] == self.player_cards[1]):
            self.pairs(self.player_cards[0])
        # SOFT HAND
        elif (self.player_cards[0] == "A" or self.player_cards[1] == "A"):
            self.soft_hand()
        # HARD HAND
        else:
            self.hard_hand() 

    def pairs(self,card): 
        if (card == 'A' or card == '8'): 
            self.handle_pairs(card)
        elif (card == '5' or card == '10'): 
            self.hard_hand() 
        elif (card == '4' and (self.dealer_cards[0] == '5' or self.dealer_cards[0] == '6')): 
            self.handle_pairs(card) 
        elif (card == '6' and (self.dealer_cards[0] >= '2' and self.dealer_cards[0] <= '6')): 
            self.handle_pairs(card)
        elif (card == '7' and (self.dealer_cards[0] >= '5' and self.dealer_cards[0] <= '7')): 
            self.handle_pairs(card)
        elif (card == '9' and (self.dealer_cards[0] >= '2' and self.dealer_cards[0] <= '9' and self.dealer_cards[0] != '7')):
            self.handle_pairs(card)
        else : 
            self.hard_hand() 

    def handle_pairs(self, pair_card): 
        index = self.player_cards.index(pair_card)

        # CREATING A NEW 2-CARD HAND
        new_hand =[self.player_cards.pop(index)]
        new_hand.append(self.deck.hit())

        # REFURBISHING OLD HAND
        if (len(self.player_cards) == 1): 
            self.player_cards.append(self.deck.hit())
        
        sub_round1 = Game(self.amount,self.bet,self.strategy,self.player_cards,self.dealer_cards,self.deck)
        sub_round1.play_round() 
        self.amount = sub_round1.amount

        self.deck.shuffle() 
        sub_round2 = Game(self.amount,self.bet,self.strategy,new_hand,self.dealer_cards,self.deck)
        sub_round2.play_round() 
        self.amount = sub_round2.amount
        
        

    def soft_hand(self): 

        # INITIAL TOTAL CHOSEN TO <= 21
        total = self.hand_total(self.player_cards)

        while(total < 21): 
            #print(total)
            # IF HAND IS 13 OR 17 
            if (total == 13 or total == 17): 
                #print("P15")
                card_val = self.player_hit(total)
                if(card_val == 0): 
                    return None 
                total += card_val
            # IF HAND IS 18
            elif (total == 18):
                # DEALERS UP CARD B/W 2,8
                if ( (self.dealer_cards[0] not in "AKQ") and (int) (self.dealer_cards[0]) >= 2 and (int) (self.dealer_cards[0]) <= 8 ): 
                    #print("P16")
                    self.stand(total)
                    return None 
                else: 
                    #print("P17")
                    card_val = self.player_hit(total)
                    if(card_val == 0): 
                        return None 
                    total += card_val
            # IF HAND IS 19
            elif (total >= 19):
                #print("P18") 
                self.stand(total)
                return None 
            
            # RANDOMLY CHOOSE BETWEEN HIT OR STAND
            else: 
                choice = random.randint(0,1)
                if (choice): 
                    #print("P19")
                    card_val = self.player_hit(total)
                    if(card_val == 0): 
                        return None 
                    total += card_val
                else: 
                    #print("P20")
                    self.stand(total)
                    return None

        # BLACKJACK
        if (total == 21): 
            #print("P14")
            self.round_ends(1)
        # BUST 
        if (total > 21):
            #print("P21") 
            self.round_ends(-1)

        return None 

    
    def hard_hand(self): 

        total = self.hand_total(self.player_cards)

        # HIT CARDS UNTIL YOU WISH TO STAND, GET BLACKJACK OR GO BUST
        while(total < 21): 
            #print(total)
            # IF TOTAL LESS THAN 8, HIT
            if (total <= 8):
                #print("P0") 
                card_val = self.player_hit(total)
                if(card_val == 0): 
                    return None 
                total += card_val

            elif (total == 9):
                # IF DEALER CARD B/W 3,6 
                if ( self.dealer_cards[0] not in "AKQ" and (int) (self.dealer_cards[0]) >=3 and (int) (self.dealer_cards[0]) <=6): 
                    #print("P1")
                    #DOUBLE DOWN
                    self.double_down()
                card_val = self.player_hit(total)
                if(card_val == 0): 
                    return None 
                total += card_val
            
            elif(total == 10 or total == 11): 
                # IF DEALER CARD NOT A,K,Q
                if (self.dealer_cards[0] not in "AKQ"): 
                    #print("P4")
                    # IF CAN'T DOUBLE DOWN, HIT
                    self.double_down()
                card_val = self.player_hit(total)
                if(card_val == 0): 
                    return None 
                total += card_val

            elif (total >= 12 and total <= 16): 
                # IF DEALER CARD 2 TO 6
                if ( self.dealer_cards[0] not in "AKQ" and (int) (self.dealer_cards[0]) >= 2 and (int)(self.dealer_cards[0]) <= 6): 
                    #print("P7")
                    self.stand(total)
                    return None
                else: 
                    #print("P8")
                    card_val = self.player_hit(total)
                    if(card_val == 0): 
                        return None 
                    total += card_val

            # IF OVER 19, STAND 
            elif (total >=19): 
                #print("P9")
                self.stand(total)
                return None
            
            # RANDOMLY CHOOSE TO HIT OR STAND
            else: 
                choice = random.randint(0,1)
                if (choice): 
                    #print("P10")
                    card_val = self.player_hit(total)
                    if(card_val == 0): 
                        return None 
                    total += card_val
                else: 
                    #print("P11")
                    self.stand(total)
                    return None


        # BLACKJACK
        if (total == 21):
            #print("P12")
            self.round_ends(1)
        # BUST 
        elif (total > 21):
            #print("P13") 
            self.round_ends(-1)
        
        return None 

    def player_hit(self,total): 
        card = self.deck.hit()
        if (card in self.player_cards): 
            self.pairs(card)
            return 0 
        # IF ADDING 11 MAKES IT GO BUST
        elif (card == 'A'):
            self.player_cards.append(card)
            if ((total + 11) > 21): 
                return 1
            else: 
                return 11 
        else: 
            self.player_cards.append(card)
            return self.deck.get_points(card)
    
    def dealer_hit(self,total): 
        card = self.deck.hit()
        self.dealer_cards.append(card)
        # IF ADDING 11 MAKES IT GO BUST
        if (card == 'A'):
            if ((total + 11) > 21): 
                return 1
            else: 
                return 11    
        return self.deck.get_points(card)
     
    """
    If you could double down on bet, do so and return True, else False
    """
    def double_down(self) : 
        #print("double downed")
        if (self.amount - self.bet >= 0): 
            self.bet += self.bet 
            return True 
        else: 
            return False 

    """
    Upon standing dealer hits until reaches 17 or more and then cards compared
    """   
    def stand(self,total): 
        player_total = total 
        dealer_total = self.hand_total(self.dealer_cards)

        # DEALER HITS UNTIL REACHES 17 OR MORE
        while (dealer_total <= 17): 
            dealer_total += self.dealer_hit(dealer_total)
        
        # OUTCOME : 0 (tie), 1 (player victory), -1 (dealer victory)
        outcome = 0 
        # PLAYER WON
        if (dealer_total > 21): 
            outcome = 1
        elif (player_total > dealer_total): 
            outcome = 1
        # DEALER WON
        elif (dealer_total > player_total): 
            outcome = -1 
        
        #print(player_total,dealer_total)
        self.round_ends(outcome) 

    """
    This function runs at the end and adjusts the amount after each round.
    Outcome :   1 (PLAYER WINS)
                0 (TIE)
                -1 (DEALER WINS)
    """
    def round_ends(self,outcome): 
        # YOU WIN DOUBLE THE BET UPON WINNING
        if (outcome == 1): 
            self.amount += (self.bet * 1.5)
            #print("YOU WIN")
        # IF YOU TIE, YOU GET YOUR BET BACK 
        elif (outcome == 0): 
            self.amount += self.bet 
            #print("YOU TIE")
        # IF YOU LOSE, YOU LOSE YOUR BET 
        else: 
            self.amount -= self.bet
            #print("YOU LOSE")
  
    def hand_total (self,cards):
        total = 0
        A_count = 0 
        for card in cards: 
            if (card == "A"): 
                A_count += 1
            else: 
                total += self.deck.get_points(card)
        
        if (A_count >= 0): 
            for i in range(A_count): 
                if (total + 11 > 21): 
                    total  += 1
                else: 
                    total += 11
        
        return total
    
    def get_amount(self): 
        return self.amount

def main():
    total = 5000
    for i in range(100000): 
        game = Game(total,100,0)
        game.play_round()
        total = game.amount
        print(total)
if __name__ == "__main__": 
    main()

