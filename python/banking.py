#banking system
#print balance
#print deposit
#print withdraw
#print totalbalance
#print exit
import time
totalbalance=500
def deposit():
 while True:
    try:
      global totalbalance
      ask=float(input('enter the amount you want to deposit.'))
      if ask<=0:
       print('It cannot be less than or equal to 0.')
      elif ask.is_integer():
        print(f'you deposited${ask}')
        totalbalance+=ask
        print(f'your current balance is:${totalbalance}')
        return(ask)
        break
      else:
       print('invalid unit')
    except ValueError:
       print('Enter numeric value')





def withdraw():
    while True:
      try:
        global totalbalance
        ask = float(input('enter the amount you want to withdraw.'))
        if ask > totalbalance:
            print('out of limit.')
        elif ask.is_integer():
            print(f'you withdrew${ask}')
            totalbalance -= ask
            print(f'your current balance is:${totalbalance}')
            return (ask)
            break
        elif not ask.is_integer():
            print('invalid unit')

      except ValueError:
          print('enter numeric value')

def total_balance():
    global totalbalance
    return(f'your total balance is :${totalbalance}')


def main():
 is_running = True
 while is_running:
   try:
      print('Banking Sytem')
      print("1:print balance"
          "2:Deposit money"
          "3:Withdraw money"
          "4:exit")

      a=int(input('enter the choice:'))
      if a == 1:
       print(total_balance())
      elif a == 2:
        print(deposit())
      elif a == 3:
        print(withdraw())
      elif a == 4:
        is_running= False
        time.sleep(1)
        print('Exiting the banking system')
      else:
        print('Invalid Unit')
   except ValueError:

       print('Enter the valid choice')
main()