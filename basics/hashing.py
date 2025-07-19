def countElem(n,array):
    hasmapp=[0]*(max(array)+1)  #here we are creating an array of length which is just greater than 1 compared to the maximum value in a input or given array
    for num in array:
        hasmapp[num]+=1   #then for every numbers in an array we put the count value inside a hasmapp.
    print(hasmapp[n])
countElem(5,[0,1,2,5,5,5,3])
