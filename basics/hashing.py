def countElem(n,array):
    hasmapp=[0]*(max(array)+1)  #here we are creating an array of length which is just greater than 1 compared to the maximum value in a input or given array
    for num in array:
        hasmapp[num]+=1   #then for every numbers in an array we put the count value inside a hasmapp.
    print(hasmapp[n])
countElem(5,[0,1,2,5,5,5,3])


def countCharacter(s,array):     
    hassmap=[0] * 26  #as the total number of characters are 26 so we are creating the hassmap having 26 values
    for letter in array:
        hassmap[ord(letter)-ord('a')]+=1    #here we are subtracting the ascii value of eachletter with the ascii value of 'a'
    print(hassmap[ord(s)-ord('a')])      #then this gets the actual count of the letter   

countCharacter('v',['v','a','v','v','b','c','b','e','v'])