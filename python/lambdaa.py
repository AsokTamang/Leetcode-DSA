import math

conversion = (
    lambda name, alias: name.strip().title() + ":" + alias.strip().title()
)  # here strip() will remove all the empty spaces in the word
print(conversion("Sri", "Krishna"))

monty_python = [
    "John Marwood Cleese",
    "Eric Idle",
    "Michael Edward Palin",
    "Terrence Vance Gilliam",
    "Terry Graham Perry Jones",
    "Graham Arthur Chapman",
]
inOrder = lambda arrays: sorted(
    arrays
)  # here we are using lambda function to sort the array in ascending order
print(inOrder(monty_python))

print(monty_python.sort(reverse=True))


def game(
    ticket, hourRate
):  # here we are defining the function with params ticket and hourrate
    return (
        lambda hours: hours * hourRate + ticket
    )  # and this function returns the lambda function


regular = game(
    5, 15
)  # here for a regular game the ticket is $5 and the hourly rate is $15
occasional = game(
    10, 20
)  # here for a occasional game the ticket is $10 and the hourly rate is $20

print("The price for a regular game to watch for 5 hours is: ", regular(5))
# or
print("The price for a regular game to watch for 5 hours is: ", game(5, 15)(5))
print("The price for a occasional game to watch for 5 hours is: ", occasional(5))
print(
    "the product of the list is :",
    (lambda *args: math.prod(args))(2, 3, 4, 5, 6, 7, 8, 9, 10),
)  # here we are passing the values for  a,b,c in the same line while using lambda function

print((lambda x: x + 5)(2))

print(
    (lambda sentence: ",".join(sentence.split(" ")))("Monty Pythons Flying Circus")
)  # here whatever we put inside the () of join method that symbol is used to join the parts or datas of the iterables.


def f(x):
    return lambda y: y + x


print(f(2)(5))

print(
    (lambda x, y: set(x + y))([1, 2, 3, 4], [3, 4, 2, 5, 6, 7, 11])
)  # here we are making the lambda function which adds two lists but removes the duplicate values


def quadractic(x):  #here we are making a quadratic eqn which returns the lambda function ax**2+bx+c
    return lambda a, b, c: a * x**2 + b * x + c


print(quadractic(5)(2,3,4))


signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups,key=lambda x:int(x[3:])))     #here in this code we are sorting the list from the 3rd position after converting it into an integer.

class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score

eric=Player('Eric',45)
sham=Player('Sham',32)
tyler=Player('Tyler',62)

playerList=[eric,sham,tyler]

a=(sorted(playerList,key=lambda x:x.score)) #here in this code we are sorting the list by the score
print([player.name for player in a])     #then we are justing printing the list of players' names but in asceding order based on the score.