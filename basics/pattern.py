def nForest(n):
   for i in range(n): # type: ignore
       print('*'*n) # type: ignore


nForest(5)    


#Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

#An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

#For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.

def pattern2(n):
    for i in range(n+1):
        print(i * '*')

pattern2(5)


def pattern3(n):
    for i in range(1,n+1):
      for j in range(1,i+1):
          print(j,end=' ')  #this code prints the pattern which runs inside the j loop in the same line to get the desired result

      print()  #this line prints the pattern which runs in i loop in the next line to get the desired result    
        

pattern3(5)


def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end='')   #here we are using i inside the print cause for the pattern to be matched the value must be go with the outer loop
        print()    

pattern4(5)

def pattern5(n):
    for i in range(n,0,-1):
        print('*' * i)

pattern5(5) 



def pattern6(n):
    for i in range(n,0,-1):
       for j in range(1,i+1):
           print(j,end=' ')#here we are using the end='' inroder to print the pattern which runs inside the j loop in the same row
       print()  #then we use this print() for printing the pattern that runs inside the i loop in the nextline 

pattern6(5)