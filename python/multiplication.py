import random

questions = [
    "whats the output of 5X5?",
    "whats the output of 3X9?",
    "whats the output of 8X8?",
    "whats the output of 4X9?",
    "whats the output of 7X8?",
]
answers = [25, 27, 64, 36, 56]
package = dict(
    zip(questions, answers)
)  # here we are pairing the question with it's respective answer then we are using dict to pair them in dictionary

question = random.choice(
    questions
)  # here we are picking the random question from the list of questions
for i in range(3):

    answer = input(
        question
    )  # then we are storing the input entered by user in answer variable
    if package[question] == int(answer):
        print("You guessed the  answer correctly!")
        break
    elif i == 2:
        print("You failed sorry!")
    elif int(answer) > int(package[question]):
        print("The number you guessed is too high")
    elif int(answer) < int(package[question]):
        print("The number you guessed is too low")

    else:
        print("You guessed it wrong,please try again")
