#balance
#betamount
#condition'
# condition true = spin
# spin_condition
#if condition match money add else money subtract
#ask wanna play or no
#if no payout
#print balance
#exit
import random

balance = 100
def spin():
    symbols = ['🍎', '🥝', '🍟', '🌭']
    return(random.choice(symbols) for i in range(4))
def payout (result,bet):
    global balance
    if result[0]==result[1]==result[2]==result[3]:
        print('You hit the jackpot.')
        return bet*100
        balance+=bet

    elif result[0]==result[1] and result[0]==result[2]  or result[2]==result[1] and result[2]==result[3] or result[2]==result[1] and result[1]==result[3]:
        print('Partial win')
        return bet*50
        balance+=bet

    else:
        print('You lost')
        balance-=bet




def main():
    global balance
    global ask
    



    while balance>0:
       try:
        ask=input('Do you want to play(y/n)?').lower()
        if ask=='n':
         print(f'Your balance is:{balance}')
         break
        elif ask=='y':
          try:
            bet = int(input('enter the amount you want to bet:'))
            if bet > balance:
                print('insufficient amount')
            elif bet <= 0:
                print('amount cannot be equal to or less than 0')
            else:
                result = list(spin())
                print('Spinning........')
                print(' '.join(result))

                try:
                 ask_again=input('Do you want payout?(y/n)').lower()
                 if ask_again=='y':
                    payout(result, bet)
                    print(f'You betted {bet}')
                    new_balance=balance
                    if new_balance>balance:
                        print(f'You won {bet}')
                    elif new_balance<balance:
                        print(f'You lost {bet}')

                    print(f'Your new balance is:{balance}')
                 elif ask_again=='n':
                    pass


                except ValueError:
                    print('enter a valid input.')




          except ValueError:
           print('Invalid input')
       except ValueError:
         print('Invalid unit')




main()