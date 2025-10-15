#Longest Substring Without Repeating Characters
#Given a string, S. Find the length of the longest substring without repeating characters.
def brutelongestsubstring(s):
    maxlength = 0
    n=len(s)
    for i in range(n):
        m=set()
        for j in range(i,n):
            if s[j] in m:
                break
            m.add(s[j])
            maxlength=max(maxlength,j-i+1)  
    return maxlength
print(brutelongestsubstring("aaabbbccc"))        
#time complexity : O(N**2)
#space complexity : O(M)  M is the number of unique characters in the substring

def optimallongestsubstring(s):
    l=r=0
    n=len(s)
    m={}  #this dict stores the character and its index as key-value pair
    maxlength = 0
    while r<n:
        if s[r] in m and m[s[r]]>=l:
            l=m[s[r]] + 1
        maxlength=max(maxlength,r-l+1)
        m[s[r]] = r  #storing the character and its corresponding index in m
        r+=1
    return maxlength
print(optimallongestsubstring("abcddabac"))    

#max consecutive ones 
def brutemaxconsecones(nums , k):
    n=len(nums)
    maxlength = 0
    for i in range(n):
        count = 0
        for j in range(i,n):
            if nums[j]==0:  #we must increase the count first then only we check if the count exceeds k or not
                count+=1
            if count>k:
                break    
            maxlength=max(maxlength,j-i+1)
    return maxlength
print(brutemaxconsecones( [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3))        
#time complexity :  O(N**2)
#space complexity : O(1)

def betterapproachconsecones(nums , k):
    l=r=0
    n=len(nums)
    count = 0
    maxlength = 0
    while r<n:
        if nums[r] == 0:
            count+=1
        while count > k:
            if nums[l] == 0:
                count-=1
            l+=1  
        maxlength=max(maxlength,r-l+1)
        r+=1
    return maxlength
print(betterapproachconsecones([0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3))   
#time complexity : O(2N)
#space complexity : O(1)  


#optimal solution targetting for O(N) TC
def optimalconsecones(nums,k):
    l=r=0
    n=len(nums)
    count = 0
    maxlength = 0
    while r<n:
        if nums[r] == 0:
            count+=1
        if count > k:
            if nums[l]==0:
                count-=1
            l+=1  
        if count<=k:  #only when the count of zeros is within the limit of k, we calculate the maximum length of the substring with counsecutive ones
            maxlength = max(maxlength,r-l+1)
        r+=1    
    return maxlength
print(optimalconsecones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3)) 
#time complexity : O(N)
#space complexity : O(1)    

#fruit into baskets
def brutefruitbasket(fruits):
    n=len(fruits)
    maxlength = 0
    for i in range(n):
        diff=set()  #this is our basket
        for j in range(i,n):
            diff.add(fruits[j])
            if len(diff) > 2:  #as we can store only two different kinds of fruits in given 2 baskets, so if we store more than that , we need to remove the one from the leftmost tree 
             break
            maxlength=max(maxlength,j-i+1)
    return maxlength
print(brutefruitbasket( [1, 2, 3, 2, 2]))  
#time complexity : O(N**2)
#space complexity : O(M)    number of unique or different kinds of fruits
       
            



