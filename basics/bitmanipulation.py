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
    s=s[::-1]  
    for i in range(len(s)):
        ans+=int(s[i]) * (2**i)  #** denotes the power
    return ans
print(convertintodecimal('1101'))
#time complexity : O(NlogN) is for reversing the given string
#space complexity : O(N) 