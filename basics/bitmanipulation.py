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
#if it's negative then we should make a 2s compliment of this output again otherwise we must stop.

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
#because in the add operation , most of the time the output will be false or 0 except only when both of the inputs are true
print(optimalcheckibit(10,1))
#time complexity : O(1)
#space complexity : O(1)

#xor fact - the xor of the same number will be 0
#swap two numbers
def swaptwonums(a,b):
    a = a ^ b
    b = a ^ b   #making b equals to a 
    a= a ^ b    #making a equals to b
    return (a,b)
print(swaptwonums(5,6))   
#time complexity : O(1)
#space complexity : O(1)


#set i-th bit a 1
#brute approach
def setibnit(n,indexx):
    res= ''
    while n>0:
        res += '0' if n % 2 ==0 else '1'
        n=n//2
    res = list(res)
    if indexx>=len(res):  #if the given index is way greater than the length of the obtained binary digit, then we must add 0s in the obtained binary digit so that we can manipulate the data of the given index.
        res+=['0']*(indexx - len(res) + 1)
    res[indexx] = '1'
    ans = 0
    for i in range(len(res)):
        ans += int(res[i]) * (2 ** i)  
    return ans
print(setibnit(5,3))    
#time complexity : O(log2N)+M), M is the length of the obtained binary form
#space complexity : O(M)    

def optimalsetibit(n,indexx):
    return (n|1<<indexx)    #doing the OR operation between the given digit and value obtained by shifting 1 to the leftside to the given index, sets the i-th bit to set.
print(optimalsetibit(5,3))
#time complexity : O(1)
#space complexity : O(1)



#clear the i-th bit
#which means turning the 1 to 0 if its 1 otherwise let it be 0 at the given index
#brute approach
def bruteclearithbit(n,indexx):
    res = ''
    ans=0
    while n>0:
        res+='0' if n % 2 ==0 else '1'
        n=n//2
    res=list(res)
    if indexx>=len(res):
        res+=['0'] * (indexx - len(res) + 1)
    if res[indexx] == '1':
        res[indexx] = '0'
    for i in range(len(res)):
        ans+=int(res[i]) * (2**i)
    return ans
print(bruteclearithbit(13,3))    
#time complexity : O(log2N + M)  where M is the length of the obtained binary form of the given digit
#space complexity : O(M)

#optimal approach
def optimalclearithbit(n,indexx):
    return n & ~(1<<indexx)   #as the and operation always gives us false except both the values are true  and doing the not operation on shifting the 1 to the left side of the given index
print(optimalclearithbit(13,3))
#time complexity : O(1)
#space complexity : O(1)


#toggle the ith bit  
def toggleithbit(n,indexx):
    return n ^(1<<indexx)  #here we are using the xor cause xor changes the value only when both of the values are same which means
#it changes into 1 when there is odd number of 1, it changes into 0 when is even number of 1s.
print(toggleithbit(5,5))  
#time complexity : o(1)
#space complexity : O(1)


#remove the last setbit which is turn the last 1 into 0
#brute approach
def removelastsetbit(n):
 res=''
 while n>0:
     res+='0' if n % 2 ==0 else '1'
     n=n//2
 res=list(res)   
 for i in range(len(res)):
     if res[i] == '1':
         res[i] = '0'
         break   
     else:
         continue
 ans=0
 for i in range(len(res)):
     ans+=int(res[i]) * (2**i)
 return ans
print(removelastsetbit(13))    
#time complexity : O(log2N+M)
#space complexity : O(M+N)

#optimal solution
def optimallastsetbit(n):
    return n & (n-1)
print(optimallastsetbit(13))
#time complexity : O(1)
#space complexity : O(1)

#check if the given number is a power of 2 or not
def checkpower(n):
    return n & (n-1) == 0   #if the and operation between the given number and the number lesser than just 1 compared to the given number , gives us the value 0 then , the given number is a power of 2, otherwise its not the power of 2
print(checkpower(9))
#time complexity : O(1)


#count the number of setbits
#brute-wise approach
def countsetbits(n):
    c = 0
    while n>0:
        if n % 2 ==1:
            c+=1
        n=n//2
    return c
print(countsetbits(9))   
#time complexity : O(N)
#space complexity : O(1) 

#brute-bit-wise approach
#the bit-wise operation is much faster and effective than the normal brute approach
def bitwisecountset(n):
    c=0
    while n>0:
        c+= n & 1   #if the given number is odd then it always gives us 1 while doing the and operation with value 1 otherwise false or 0
        n = n >>1   #right shifting which means n/2**k , also means decreasing the number or value
    return c
print(bitwisecountset(8))    
#time complexity : O(N)
#space complexity : O(1)

#using the and operation between n and n-1
def countset(n):
    c=0   
    while n>0:
        n=n & (n-1)
        c+=1
    return c
print(countset(9))
#time complexity : O(number of set bits in a given digit)
#space complexity : O(1)


#check if the given number is odd or even
def checkevenodd(n):
    if n & 1 == 0:
        return 'even'
    elif n & 1 ==1:
        return 'odd'
print(checkevenodd(13))    
#time complexity : O(1)
#space complexity : O(1)

    
def setrightmostunsetbit(n):
    return n | (n+1)   #here doing the OR operation between the given digit n and n+1 helps to set the unset bit
print(setrightmostunsetbit(9))   
#time complexity : O(1)
#space complexity : O(1)    

def unsettherightmostsetbit(n):
    return n & (n-1)
print(unsettherightmostsetbit(8))
#time complexity : O(1)
#space complexity : O(1) 