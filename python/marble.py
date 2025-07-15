import random

number_of_rounds = 5
total_bag = [
    "black",
    "green",
    "green",
    "green",
    "green",
    "red",
    "green",
    "red",
    "red",
    "red",
]
green = 6
red = 4
gold = 1000


for i in range(number_of_rounds):  # the marble game goes for 5 rounds
    if gold < gold / 2:
        print("You already lost half the amount, leave the game!")
        break
    amount = int(input("enter the amount you want to bet."))
    catch = random.choice(total_bag)
    if catch == "green":
        total_bag.remove("green")
        gold += amount  # if the marble is green then we add the same amount that we  bet to add on the gold
        print("You won the lottery as you got the green ball")
        print("Your bag is:", gold)
    elif catch == "red":
        total_bag.remove("red")
        gold -= amount
        print("You lost the lottery as you got the red ball")
        print("Your bag is:", gold)
    else:
        gold += 1000000
        print("You won the whole lottery")
        print("Your bag is:", gold)
        break
