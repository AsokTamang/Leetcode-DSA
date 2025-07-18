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
