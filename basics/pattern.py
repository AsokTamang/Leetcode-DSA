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

    for i in range(1, n + 1):  #this loop runs until the n  and in this loop the value of i starts from 1  
        print(" " * (n - i) + "*" * (2 * i - 1) + " " * (n - i))
   
    for i in range(n, 0, -1):  #this loop runs from n+1 till 1  and in this loop the value of i starts from the exact value of n
        print(" " * (n-i) + "*" * (2 * i - 1) + " " * (n-i))
       


pattern9(5)



def pattern10(n):
    for i in range(1,n+1):
        print(i * '*')
    for i in range(n,0,-1):
        print(i*'*')

pattern10(5)


def pattern11():
    for i in range(1,6):
        if(i % 2 !=0):  #at the odd position of outer loop the start value is 1
            start=1
        else:
            start=0   #but at the even position of outer loop the start value is 0
        for j in range(1,i+1):
         print(start,end=' ')
         start=1-start
        print() 


         
pattern11()
        

