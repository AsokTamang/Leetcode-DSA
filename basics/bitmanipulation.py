def convertintobinary(num):
    res= ''
    if num == 0:
        return '0'
    while num!=1:
        if num % 2 == 1:
            res+='1'
        else:
            res+='0'


        
        num=num // 2
    return '1' + res[::-1] #here we are adding the '1' at the beginning cause our while loop condition is while num!=1
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