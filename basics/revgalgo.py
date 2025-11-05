#assign cookies
def assigncookies(student,cookie):
    student.sort()  #here we are sorting both student and cookie so that the least greedy stident can be satisfied easily by the smallest amount of cookie
    cookie.sort()
    i=0  #for student
    j=0  #for cookie
    n=len(student)
    number = 0
    while i<n:
        if cookie[j]>=student[i]:
            number+=1  
            i+=1          
        j+=1  
        
    return number          
print(assigncookies([4, 5, 1] , [6, 4, 2]))
#time complexity : O(NlogN+MlogM)
#space complexity : O(1)


#Fractional Knapsack
def fractionalknapsack(val,wt,k):
    totalwt =0 
    array = sorted(zip(val,wt),key=lambda x:x[0]/x[1],reverse=True )  #here we are sorting reversely based on the fraction of value and weight
    maxvalue =0
    for val,wt in array:
        if totalwt+wt<=k:
            totalwt+=wt
            maxvalue+=val
        else:
            remainingwt = k-totalwt
            additionalval = (val/wt) * remainingwt
            maxvalue+=additionalval
    return f'{maxvalue:.6f}'
print(fractionalknapsack([60,100,120],  [10,20,30],  50)) 
#time complexity : O(NlogN)
#space complexity : O(N)  


#minimum coins
def minimumcoins(coins,amount):
    n=len(coins)
    coins.sort()
    count = 0
    s=0
    for i in range(n-1,-1,-1):
        while coins[i]<=amount:
            s+=coins[i]  #10
            amount-=coins[i] #1
            count+=1
       
    if amount==0:  #here amount = 0 means we have the required quantity of coins in a given list of coins inorder to make the given quantity of amount
     return count
    return -1
print(minimumcoins( [2, 5],  3))    
#time complexity : O(NlogN)
#space complexity : O(1)    

#lemonade change
#brute approach which means the bills consists of only 5,10, and 20
def lemonadechange(bills):
    n=len(bills)
    fives,tens = 0,0
    for num in bills:
        if num == 5:
            fives+=1
        elif num == 10:
            tens+=1
            if fives:
                fives-=1
            else:
                return False        
        else:  #if the number is 20
            if tens and fives:
                tens-=1
                fives-=1
            elif fives>=3:
                fives-=3
            else: #which means we have no change
                return False
    return True
print(lemonadechange([5, 5, 10, 20]))      
#time complexity : O(N)
#space complexity : O(1)       
                

#for the bills containing more than 20 
def optimallemonadechange(bills):
    m={}
    for num in bills:
        m[num]=m.get(num,0) + 1  
        if num > 5:
            changerequired = num - 5
            for bill in sorted(m.keys(),reverse=True):  #this loop is for checking the cash we have in our box, and here we are reversing the keys so that we can find the cash for change as soon as possible
                if  bill<=changerequired and m[bill]>0:
                    changerequired=changerequired-bill
                    m[bill]-=1
            if changerequired>0:  #if we still have change to given even after that for bill loop, then it means we dont have the required cash to give as a change for a customer
                return False      
    return True
print(optimallemonadechange([5, 5, 10, 5, 20]))          
#time complexity : O(N**2+logN)
#space complexity : O(N)


#valid parenthesis
def brutevalidparenthesis(s):
    n=len(s)
    def recursivevalidparenthesis(index,count):  #index indicates the index of a given string s and count indicates the measure based on which we determine whether the given string is valid or not
     if count<0:
         return False
     if index==n:   #if we already went through all the characters from a given string, we check the value of count
         return count==0
     char = s[index]
     if char=='(':
        return recursivevalidparenthesis(index+1,count+1)
     elif char == ')':
        return recursivevalidparenthesis(index+1,count-1)
     else:  #if the char is * then we can assume this * as ( or ) or empty character
         return recursivevalidparenthesis(index+1,count) or recursivevalidparenthesis(index+1,count+1) or recursivevalidparenthesis(index+1,count-1)         
        
    return recursivevalidparenthesis(0,0)
print(brutevalidparenthesis('*(()'))
#time complexity : O(3**N)
#space complexity : O(N)
 

#optimal approach
def optimalvalidparenthesis(s):
    minopen=0   #here minopen means we are assuming * as ) so the number of openings will be minimum
    maxopen=0   #here maxopen means we are assuming * as ( so the number of openings will be maximum
    for char in s:
        if char == '(':
            minopen+=1
            maxopen+=1
        elif char ==')':
            minopen=max(minopen-1,0) 
            maxopen-=1
        else:
            minopen=max(minopen-1,0)  #here we are using max between 0 and minopen-1 cause the minopen mustnot be 0 , as we use this value to return the answer and minopen-1 reduces the count as we are assuming * as )
            maxopen+=1  #here we are assuming * as (
        if maxopen<0:
            return False
    return minopen==0
print(optimalvalidparenthesis('(*))'))
#time complexity : O(N)
#space complexity : O(1)

        

#jump game - I
def jumpgamei(input):
    n=len(input)
    maxindex = 0  #this maxindex stores the position or the index which can be reached by the maximum jump that is available in the index
    for i in range(n):
        if i > maxindex:  #here i > maxindex means this i cannot be reached even with the maxindex until this index , which means we are unable to reach this index which proves that we can never reach the last index or final end
            return False  
        maxindex=max(maxindex,input[i]+i)
    return True
print(jumpgamei( [3, 2, 1, 0, 4]))    
#time complexity : O(N)
#space complexity : O(1)

 


