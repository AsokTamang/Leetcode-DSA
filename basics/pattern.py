def nForest(n):
    for i in range(n):  # type: ignore
        print("*" * n)  # type: ignore


nForest(5)


# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.


def pattern2(n):
    for i in range(n + 1):
        print(i * "*")


pattern2(5)


def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(
                j, end=" "
            )  # this code prints the pattern which runs inside the j loop in the same line to get the desired result

        print()  # this line prints the pattern which runs in i loop in the next line to get the desired result


pattern3(5)


def pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(
                i, end=""
            )  # here we are using i inside the print cause for the pattern to be matched the value must be go with the outer loop
        print()


pattern4(5)


def pattern5(n):
    for i in range(n, 0, -1):
        print("*" * i)


pattern5(5)


def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(
                j, end=" "
            )  # here we are using the end='' inroder to print the pattern which runs inside the j loop in the same row
        print()  # then we use this print() for printing the pattern that runs inside the i loop in the nextline


pattern6(5)


def pattern7(n):
    j = 0
    for i in range(1, n + 1):
        print(
            (n - i) * " " + (i + j) * "*" + (n - i) * " "
        )  # here in every iterations the value of j gets increased by 1 and the value of i + j gives us the required * pattern
        j += 1


def pattern8(n):

    for i in range(n, 0, -1):
        print((n - i) * " " + "*" * (2 * i - 1) + (n - i) * " ")


def pattern9(n):

    for i in range(
        1, n + 1
    ):  # this loop runs until the n  and in this loop the value of i starts from 1
        print(" " * (n - i) + "*" * (2 * i - 1) + " " * (n - i))

    for i in range(
        n, 0, -1
    ):  # this loop runs from n+1 till 1  and in this loop the value of i starts from the exact value of n
        print(" " * (n - i) + "*" * (2 * i - 1) + " " * (n - i))


pattern9(5)


def pattern10(n):
    for i in range(1, n + 1):
        print(i * "*")
    for i in range(n, 0, -1):
        print(i * "*")


pattern10(5)


def pattern11():
    for i in range(1, 6):
        if i % 2 != 0:  # at the odd position of outer loop the start value is 1
            start = 1
        else:
            start = 0  # but at the even position of outer loop the start value is 0
        for j in range(1, i + 1):
            print(start, end=" ")
            start = 1 - start
        print()


pattern11()


def pattern12(n):

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")

        print(" " * 2 * (n - i), end="")  # this code prints the number of spaces

        for j in range(
            i, 0, -1
        ):  # here we are making the loop to start from the i to 0
            print(j, end="")
        print()


pattern12(5)


def pattern13(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()


pattern13(5)


def pattern14():
    a = "ABCDE"
    for i in range(1, 6):

        print(a[0:i])


pattern14()


def pattern15():
    a = "ABCDE"
    for i in range(5, 0, -1):
        print(a[0:i])


pattern15()


def pattern16():
    a = "ABCDE"
    for i in range(0, 5):
        for j in range(0, i + 1):
            print(a[i], end="")
        print()


pattern16()

def pattern17():
    a= 'ABCD'
    k=3
    for i in range(1,5):
        print(' ' * k + a[0:i] + (a[i-2::-1] if i > 1 else '')  + ' ' * k)   #here we are using a[0:i] cause in the pattern every row is starting from letter A
        k-=1
#and we are also using if else condition here in this code  as for the 0 value of i the statement a[i-2:0:-1] deosnot match but for every other elements of i , the statement matches.
pattern17()


def pattern18():
    a='ABCDE'
    for i in range(5,-1,-1):
        print(a[i::])
pattern18()        


def pattern19(n):
    space1=0
    space2=8
    for i in range(n,0,-1):
        print( int(i) * '*' + space1 * ' ' + int(i) * '*')
        space1+=2
    for i in range(1,n+1):
         print( int(i) * '*' + space2 * ' ' + int(i) * '*')
         space2-=2

pattern19(5)

def pattern20():
    space1=8
    space2=0
    for i in range(1,6):
        print ( i * '*' +space1 * ' ' + i * '*' )
        space1-=2
    for i in range(5,0,-1):
         print ( i * '*' +space2 * ' ' + i * '*' )
         space2+=2
pattern20()        


def pattern21():
  
    for i in range(1,5):
        if(i==1 or i == 4):
            print('*' * 4,end=' ')
        else:
            print('*' + ' ' * 2 + '*',end=' ' )
        print()        # we are using this print() inorder to print the pattern in next line for each change in value of i
pattern21()


def pattern22(n):
    for i in range(2*n - 1):
        for j in range(2*n - 1):
            value=max(abs(n-1-i),abs(n-1-j))+1
            print(value,end='')
        print()    
pattern22(5)



