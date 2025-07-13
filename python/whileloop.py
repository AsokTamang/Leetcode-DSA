


i=1
while i<=5:
    print(f"{i}. {i*'*'}Loops are great{i*'*'}")
    i+=1

correctNumber=5

i=1
while i<=6:
    guess=int(input('Guess a number.'))
    if(i==6):
        print('You lost')
    elif(guess==correctNumber):
        print('You guessed correctly')
        break
    elif (guess>correctNumber**5):
        print('Your guess is too high')  
    elif (guess<(correctNumber/3)):
        print('Your guess is too low')  

    
    i+=1