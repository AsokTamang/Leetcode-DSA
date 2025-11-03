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
       
    if count!=0 and amount==0:  #here amount = 0 means we have the required quantity of coins in a given list of coins inorder to make the given quantity of amount
     return count
    return -1
print(minimumcoins( [2, 5],  3))    
#time complexity : O(NlogN)
#space complexity : O(1)    


