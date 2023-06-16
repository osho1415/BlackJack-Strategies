from game import Game 
import matplotlib.pyplot as plt

"""
This betting strategy doesn't depend on an outcome, and bets the same amount each round.
"""
def flat_betting(iterations, funds, bet):  
    amount = funds 
    fund_track = {}
    for i in range(iterations): 
        fund_track[i] = amount
        game = Game(amount,bet,0)
        game.play_round() 
        amount = game.get_amount() 
    return fund_track

"""
This betting strategy doubles the bet after each loss, and reverts to initial_bet after a win
"""
def martingale_system(iterations,funds,bet): 
    initial_bet = bet
    amount = funds
    fund_track = {}
    for i in range(iterations): 
        fund_track[i] = amount 
        game = Game(amount,bet,0)
        game.play_round() 
        final_amount = game.get_amount()

        # IF YOU LOSE A GAME, DOUBLE THE BET
        if (final_amount <= amount): 
            bet = bet * 2 
        # IF YOU WIN A ROUND, GO BACK TO INITIAL BET
        elif (final_amount > amount): 
            bet = initial_bet

        amount = final_amount
    return fund_track

"""
This betting strategy doubles bet after each win and reverts to intial bet after a loss
"""
def paroli_system(iterations,funds,bet): 
    initial_bet = bet
    amount = funds
    fund_track = {}
    for i in range(iterations): 
        fund_track[i] = amount 
        game = Game(amount,bet,0)
        game.play_round() 
        final_amount = game.get_amount()

        # IF YOU WIN A GAME, DOUBLE THE BET
        if (final_amount > amount): 
            bet = bet * 2 
        # IF YOU LOSE A ROUND, GO BACK TO INITIAL BET
        elif (final_amount < amount): 
            bet = initial_bet

        amount = final_amount
    return fund_track

def system_1_3_2_6 (iterations,funds,bet):
    consec_win = 0  
    initial_bet = bet
    amount = funds
    fund_track = {}
    for i in range(iterations): 
        fund_track[i] = amount 
        game = Game(amount,bet,0)
        game.play_round() 
        final_amount = game.get_amount()

        # IF YOU WIN A GAME, DOUBLE THE BET
        if (final_amount > amount): 
            consec_win += 1
            # AFTER FIRST WIN TRIPLE THE BET
            if (consec_win == 1): 
                bet = initial_bet * 3 
            # AFTER SECOND CONSECUTIVE WIN DOUBLE THE INITIAL BET
            elif (consec_win == 2): 
                bet = initial_bet * 2 
            # AFTER THIRD OR MORE WIN, INCREASE INITIAL BET BY SIX TIMES
            elif (consec_win >= 3): 
                bet = initial_bet * 6
        # IF YOU LOSE A ROUND, GO BACK TO INITIAL BET
        elif (final_amount < amount): 
            consec_win = 0 
            bet = initial_bet
        amount = final_amount

    return fund_track

def fibonacci_system(iterations,funds,bet,fibonacci): 
    cur_pos = 0
    initial_bet = bet
    amount = funds
    fund_track = {}
    for i in range(iterations): 
        fund_track[i] = amount 
        game = Game(amount,bet,0)
        game.play_round() 
        final_amount = game.get_amount()

        # IF YOU WIN, GO BACK TWO STEP IN FIBONACCI 
        if (final_amount > amount): 
            if (cur_pos - 2 >= 0): 
                cur_pos -= 2 
            bet = initial_bet * fibonacci[cur_pos]
        # IF YOU LOSE, GO AHEAD BY ONE STEP IN FIBONACCI
        elif (final_amount < amount): 
            cur_pos += 1
            bet = initial_bet * fibonacci[cur_pos]
        amount = final_amount
    
    return fund_track


def main():
    fibonacci_seq = [1,1]
    for i in range(100): 
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])

    flat_result = flat_betting(10000,5000,100)
    martingale_result = martingale_system(10000,5000,100)
    paroli_result = paroli_system(10000,5000,100)
    result_1326 = system_1_3_2_6(10000,5000,100)
    fibonacci_result = fibonacci_system(10000,5000,100,fibonacci_seq)
    
    time = flat_result.keys()
    flat_y = flat_result.values()
    martingale_y = martingale_result.values()
    paroli_y = paroli_result.values()
    y_1326 = result_1326.values()
    fibonacci_y = fibonacci_result.values()


    plt.plot(time,flat_y, label = "Flat Betting")
    plt.plot(time,martingale_y, label = "Martingale System")
    plt.plot(time,paroli_y, label = "Paroli System")
    plt.plot(time,y_1326, label = "1-3-2-6 System")
    plt.plot(time,fibonacci_y, label = "Fibonacci System")

    plt.legend()
    plt.ylabel("Funds Available")
    plt.xlabel("Rounds Played")
    plt.show() 

if __name__ == "__main__": 
    main() 

