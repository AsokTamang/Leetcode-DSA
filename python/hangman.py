words = ['apple','banana','orange','pineapple']
import random
hangman={0 :    ('   ',
                '   ',
                '   '),
             1:(' 0 ',
                '   ',
                '   ',),
             2:(' 0 ',
                ' | ',
                '   ',),
             3:(' 0 ',
                '/| ',
                '   ',),
             4:(' 0 ',
                '/|\ ',
                '   '),
             5:(' 0 ',
                '/|\ ',
                '/  '),
             6:(' 0 ',
                '/|\ ',
                '/ \ ',)}
answer=random.choice(words)
hint = ['_'] * len(answer)
guessed_letters=[]
g=0
def output():

   print(' '.join(hint))
def art():
  for line in hangman[g]:
      print(line)


def main():

  global g
  global guessed_letters

  is_running=True
  while is_running:
    guess = input('guess a letter:')
    if guess in guessed_letters:
     print('You already guessed this letter.')


     continue
    guessed_letters.append(guess)



    if len(guess)!=1 or not guess.isalpha():
     print('Invalid input.')
     continue





    elif guess in answer:



     for i in range(len(answer)):
         if answer[i]==guess:
            hint[i]=guess
     output()
     if '_' not in hint:
         art()
         print(f'you guessed correctly which is:{answer}.')
         is_running = False

    elif guess not in answer:
         g+=1
         art()

         if g == 6 and hint!=list(answer):
             art()
             print('you reached the limit.')
             print(f'The correct answer is:{answer}.')
             is_running = False

main()




