def printNumbers(n, current=1):
    if current <= n:
        print(current)
    else:
        return
    printNumbers(n, current + 1)


printNumbers(10)


def printNames(n, i):
    if i > 0:
        print("Name is : ", n)

        printNames(n, i - 1)

    else:
        return


printNames("Asok", 5)


def printNumm(n):
    if n > 0:
        print(n)
        printNumm(n - 1)
    else:
        return


printNumm(8)


def naturalNumbers(n):
    if n == 0:
        return 0
    elif n < 0:
        print("the number cannot be less than 0")
        return 0
    elif n > 0:

        return int(n) + naturalNumbers(n - 1)


print(naturalNumbers(15))


def factorial(n):
    if n < 0:
        print("The factorial of a number less than 0 cannot be calculated.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))


def reverseArray(a):
    print(
        "The reverse of an array is: ", a[::-1]
    )  # this code will print the array in a reverse way.


reverseArray([1, 2, 3, 4, 5])


def palindromeString(a):
    if a == a[::-1]:
        print("The string is palindrome")
    else:
        print("Not palindrome")


palindromeString("asa")


def fibonacci(n):
    if n == 0:
        return 0    #the fibonacci of 0 is 0
    elif n == 1:
        return 1     #the fibonacci of 1 is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)    #as in the fibonacci sequence the fibonacci of a number is the sum of its preveious two values in the series we are addinf f(n-1) and f(n-2) 


print(fibonacci(8))

def fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i),end=',')
fibonacci_series(6)

