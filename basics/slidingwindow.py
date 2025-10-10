#Sliding Window Maximum
#Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#brute approach
def bruteslidingwindow(arr,k):
    if len(arr) == k:  #if the length of the given array is equal to the value of k , then we just return the maximum value from the given array
        return max(arr)
    ans = []
    i=0
    while i<=len(arr)-k:  #
        subarr=arr[i:i+k]
        ans.append(max(subarr))  #this gives us the maximum value from the obtained subarray
        i+=1
    return ans
print(bruteslidingwindow([1, 3, -1, -3, 5, 3, 6, 7], k = 3))    
#time complexity : O(N*logN)
#space complexity : O(N)

#optimal approach
#in the optimal approach what we do , is we just design the dq in monotonic manner , where the greater number will be at the 0 index of dq, 
#and in every iteration , we remove the elemnent which lies out of the new sliding window ,
#and then if we reach the first sliding window , then our work of inserting the maximum number which is the leftmost number of dq in ans start on loop
from collections import deque
def optimalslidingwindow(arr,k):
    ans = []
    n=len(arr)
    if n * k ==0:
        return []
    elif k == 1:  #if the length of the sliding window is just one then we just return the array as it is ,
        return arr  
    dq=deque()
    for i in range(n):
        #so first of all we have to code the condition of removing the element that no longer fits in the sliding window length for the current index i
        if dq and dq[0]<=i-k:
            dq.popleft()  #removing the very first index of the dq ,
        while dq and arr[dq[-1]]<=arr[i]:  #removing the smaller elements of the dq compared to the current i indexed number , as we are designing the monotonic array
            dq.pop() 
        dq.append(i)  #after removing all the smaller elements than the currrent i indexed number from dq , we can append the current i index as the left most index in dq
        #after this above while loop , the larger number will be the leftmost element of the dq
        if i >=k-1: #if the index becomes greater or equal to the k-1 value , then it means we have reached the first window and the same loop will go on
            ans.append(arr[dq[0]]) #as the maximum value will be stored as the leftmost element
    return ans
print(optimalslidingwindow([1, 3, -1, -3, 5, 3, 6, 7], k = 3))
#time complexity : O(N)
#space complexity : O(N*K)


#stock span problem
#only the values or stock price on previous consecutive days smaller than current i day is supposed to be added in the count
def brutestockspan(arr):
    n=len(arr)
    ans = []
    for i in range(n):
        count=1
        j = i -1 
        while j>=0:
            if arr[j]<=arr[i]:
                count+=1
                j-=1   
            else:
                break     
        ans.append(count)  #we are adding 1 to the count cause the current day stock price is also counted
    return ans
print(brutestockspan( [100, 80, 60, 70, 60, 75, 85]))
#time complexity : O(N^2) 
#space complexity : O(N)


#optimal solution
def optstockspan(arr):
    stack = []
    n=len(arr)
    ans=[0] * n
    for i in range(n):
        while stack and arr[stack[-1]]<=arr[i]:#removing the smaller elements from stack in comparison to the current i indexed number
            stack.pop()
        if stack:
            ans[i] = i - stack[-1]  #the i-greater boundary gives us the number of previous consecutive days and we arenot adding 1 here cause the current i indexed day will also be counted    
        else:
            ans[i] = i + 1
        stack.append(i)    
    return ans
print(optstockspan([120, 100, 60, 80, 90, 110, 115]))            
#time complexity : O(N)
#space complexity : O(N)

#Celebrity Problem
#A celebrity is a person who is known by everyone else at the party but does not know anyone in return. Given a square matrix M of size N x N where M[i][j] is 1 if person i knows person j, and 0 otherwise, determine if there is a celebrity at the party. Return the index of the celebrity or -1 if no such person exists.
#Note that M[i][i] is always 0.

#brute approach
def brutecelebprob(arr):
    r=len(arr)  #number of rows
    c=len(arr[0])#number of columns
    knowsme=[0] * r  #here we are making a knowsme list that stores the number of people who knows the  specific person denoted by the index 
    iknow=[0] * r    #here we are making a iknow list that stores the number of poeple that is known by the specific person denoted by the index
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:  #here the first index i represents the person who knows the person j 
                iknow[i]+=1   #so index i is the knower
                knowsme[j]+=1 #index j is the known 
    for i in range(r):
        if iknow[i] == 0 and knowsme[i] == r-1:   #here the number of people who knows the celeb must be r-1 which is total number of people in the crowd -1 , -1 is due to himself or herself
            return i
    return -1        
print(brutecelebprob([ [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0] ]))   
#time complexity : O(N^2)
#space complexity : O(N)              


#optimal solution 
def optimalcelebprob(arr):
    n=len(arr)
    celeb=[i for i in range(n)]  #inserting all the indices which are the persons and we are considering all of them as the celebrities right now
    while len(celeb) > 1:
        a=celeb.pop()
        b=celeb.pop()
        if arr[a][b] == 1:  #here we are checking if a knows b or not
            celeb.append(b)  #As a cannot be celebrity
        else:
            celeb.append(a)  #b cannot be celebrity as b is not known by a here, so a might be a celebrity   
    if len(celeb) == 0:
        return -1
    celebrity = celeb.pop()  #the remaining index will be the celebrity
    for i in range(n):
        if arr[celebrity][i] == 1 and arr[i][celebrity] == 0: #if the obtained celebrity knows someone and this obtained celebrity is not known by anyone , then this person is not celebrity
            return -1
    return celebrity        
print(optimalcelebprob([ [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0] ]))   
#time complexity : O(N)
#space complexity : O(N)   


 

    



    



