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
