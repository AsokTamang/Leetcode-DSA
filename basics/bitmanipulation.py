def convertintobinary(num):
    res= ''
    if num == 0:
        return '0'
    while num>0:
        if num % 2 == 0:
            res+='0'
        else:
            res+='1'


        
        num=num // 2
    return  res[::-1] #here we are adding the '1' at the beginning cause our while loop condition is while num!=1
print(convertintobinary(13))    
#time complexity : O(log2N)
#space complexity : O(log2N)


def convertintodecimal(s):
    ans=0
    p= 0 
    for i in range(len(s)-1,-1,-1):
        ans+=int(s[i]) * (2**p)  #** denotes the power
        p+=1
    return ans
print(convertintodecimal('1101'))
#time complexity : O(N) 
#space complexity : O(N) 

#1s compliment
#while doing the 1s compliment, we just switch 0 with 1 and 1 with 0

#2s compliement
#while doing the 2s compliment , we just add 1 to the value of 1s compliment



#XOR
#while doing the xor which is like this ^ , if the number of ones is odd then the result of xor operation will be 1.
#but if the number of ones is even while doing the xor operation then the result of xor operation will be 0.

#right shift >>
#while doing the right shift we just shift the elements of the given digit to right side


#so while storing the negative number , computer stores the 2s compliment of this negative number 
#as the - sign is denoted by 1 and the positive sign is denoted by 0

#the right shift of a number means the value of a number will be smaller compared to the original value or original number so it's formula is num // 2 ** k where k denotes the power or position of a number from the very last index.
# the left  shift of a number means the value of a number will be greater compared to the original value , so its formula is num * (2**k)

#for the not operation of a positive number
#and for the not operation example(~5) what we do is we first flip the digits 0 and 1 then we check if its negative or positive based on the sign at the very beginning , if its a negative which is denoted by 1 then we make the 2s compliment of it, if its a positive then we stop , as the flipped output will be our answer. 

#for the not operation of a negative number
#first of we should make a 2s compliment of this negative number then we again repeat the same process which is first flipping then checking if it's a negative number or not,
#if yes then we should make a 2s compliment of this output again otherwise we must stop.

#problem1
#Check if the i-th bit is Set or Not
#Given two integers n and i, return true if the ith bit in the binary representation of n (counting from the least significant bit, 0-indexed) is set (i.e., equal to 1). Otherwise, return false.
#brute approach
def checkibit(n,indexx):
    if n ==0:
        return False
    res=''
    while n>0:
        res+='0' if n % 2 ==0 else '1'
        n=(n // 2) 

   
    if int(res[indexx]) == 1:
        return True    
    return False        
print(checkibit(10,1))
#time complexity : O(log2N)
#space complexity : O(log2N)

#for the optimal approach we do the and operation between the given number and the left shift of 1 from the given comparing index , and check whether the output is true or false
def optimalcheckibit(n,indexx):
    return (n & (1 << indexx))!=0  #here we are doing the and operation which is . or multiplication between n and the left shift of 1 by the given comparing index.
print(optimalcheckibit(10,1))
#time complexity : O(1)
#space complexity : O(1)
