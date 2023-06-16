# BlackJack-Strategies
Run Monte-Carlo simulations to compare the outcome of various betting strategy in BlackJack

BlackJack is a casino banking game, with the following rules: 
  Use a standard 52-card deck without jokers.
  Each round begins with the player and the dealer receiving two cards.
  The player's cards are dealt face-up, while one of the dealer's cards is dealt face-up, and the other is dealt face-down (hole card).
  The cards have the following values: number cards (2-10) are worth their face value, face cards (Jack, Queen, King) are worth 10, and the Ace can be worth either 1 or 11, depending on the player's hand.
  The player has the option to hit (receive an additional card) or stand (keep the current hand) until they decide to stand, reach a hand value of 21 (blackjack), or bust (exceed 21).
  After the player's turn, the dealer reveals their hole card and follows a fixed set of rules: they must hit until their hand value is at least 17, and then they must stand.
  The outcome is determined by comparing the final hand values. The player wins if their hand value is closer to 21 than the dealer's hand value without busting.

This project simulates multiple rounds of BlackJack with one player to compare the various betting strategies. The game itself is played using a intermediate strategy which is influenced by the following guidelines: 
  Hard Totals (hand without an Ace):
    If the player's hand value is 8 or less, always hit.
    If the hand value is 9, double down if the dealer's up-card is between 3 and 6; otherwise, hit.
    If the hand value is 10 or 11, double down unless the dealer's up-card is an Ace or a 10-value card.
    If the hand value is 12 to 16, stand if the dealer's up-card is 2 to 6; otherwise, hit.
    If the hand value is 17 or higher, always stand.
  Soft Totals (hand with an Ace):
    If the hand value is 13 to 17, always hit.
    If the hand value is 18, stand if the dealer's up-card is 2 to 8; otherwise, hit.
    If the hand value is 19 or higher, always stand.
  Pairs:
    Always split Aces and 8s.
    Never split 5s and 10s.
    Split 2s and 3s if the dealer's up-card is between 4 and 7.
    Split 4s if the dealer's up-card is 5 or 6.
    Split 6s if the dealer's up-card is between 2 and 6.
    Split 7s if the dealer's up-card is between 2 and 7.
    Split 9s if the dealer's up-card is between 2 and 9, except if the dealer has a 7.

The outcome of the simulation is graphed as a line chart, similar to the example below.
![Graph5](https://github.com/osho1415/BlackJack-Strategies/assets/71971917/7858359b-ce86-4511-aefc-707981948109)

