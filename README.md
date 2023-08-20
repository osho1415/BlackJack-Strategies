# BlackJack-Strategies
Ran Monte-Carlo simulations to compare the final outcomes of various betting strategy in BlackJack.


This project simulates multiple games of BlackJack, with multiple rounds each game, with one player to compare the various betting strategies. The game itself is played using a intermediate strategy which is influenced by the following guidelines: 

* Hard Hands (No Aces):
  * 8 or less: Always hit.
  * 9: Double down against dealer's 3-6, otherwise hit.
  * 10 or 11: Double down unless the dealer has an Ace or a 10-value card, then hit.
  * 12-16: Stand against dealer's 2-6, otherwise hit.
  * 17 or higher: Always stand.
* Soft Hands (With an Ace):
  * Ace-2 to Ace-6: Double down if the dealer has 4-6, otherwise hit.
  * Ace-7: Stand against dealer's 2, 7, or 8, double down against 3-6, hit against 9, 10, or Ace.
  * Ace-8 or Ace-9: Always stand.
* Pairs:
  * Aces and 8s: Always split.
  * 2s or 3s: Split against dealer's 4-7, otherwise hit.
  * 4s: Split against dealer's 5-6, otherwise hit.
  * 5s: Double down against dealer's 2-9, otherwise hit.
  * 6s: Split against dealer's 2-6, otherwise hit.
  * 7s: Split against dealer's 2-7, otherwise hit.
  * 9s: Split against dealer's 2-6, 8, and 9, otherwise stand.
  * 10s: Always stand.



The following graphs the changes in funds after each round, upon the implementation of different betting strategies.
![Graph5](https://github.com/osho1415/BlackJack-Strategies/assets/71971917/7858359b-ce86-4511-aefc-707981948109)


##### RESULT 
After implementation of 50000 games with 1000 rounds each : [Download CSV File](https://github.com/osho1415/BlackJack-Strategies/blob/main/1000%20result.csv)

