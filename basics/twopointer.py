# Longest Substring Without Repeating Characters
# Given a string, S. Find the length of the longest substring without repeating characters.


# so the question is asking us to find the substring where all the characters are completely unique
def longestsubstring(s):
    n = len(s)  # length of the given string
    maxlength = 0
    for i in range(n):
        same = set()
        length = 0
        for j in range(i, n):
            if (
                s[j] in same
            ):  # as soon as we find the same character in our current formed substring we break out of this j loop

                break
            same.add(
                s[j]
            )  # if we are finding the unique characters then we keep on adding these new characters in seen and keeps on calculating the length
            length = j - i + 1  # this
        maxlength = max(
            maxlength, length
        )  # then at the end of the loop , we calculate the maximum length
    return maxlength


print(longestsubstring("aaabbbccc"))
# time complexity : O(N**2)
# space complexity : O(M)  number of different character at each loop


# optimal solution
def optimalsubstring(s):
    n = len(s)
    l = r = 0
    maxlength = 0
    m = (
        {}
    )  # this is our dictionary which stores every characters and its corresponding indices
    while r < n:
        if (
            s[r] in m and m[s[r]] >= l
        ):  # if we find the same character in a while loop then the value of l will be s[r] + 1
            l = m[s[r]] + 1
        m[s[r]] = r  # storing the character and index
        maxlength = max(maxlength, r - l + 1)
        r += 1
    return maxlength


print(optimalsubstring("aaabbbccc"))


# Max Consecutive Ones III
# Given a binary array nums and an integer k, flip at most k 0's.
# Return the maximum number of consecutive 1's after performing the flipping operation.


def maxconsec1s(nums, k):
    n = len(nums)
    l = 0
    zeros = 0
    maxlength = 0

    for r in range(n):
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        maxlength = max(maxlength, r - l + 1)
    return maxlength


print(maxconsec1s([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=3))
# time complexity : O(2N)
# space complexity : O(1) number of unique indices consisting of 0s


# brute approach
def maxconsecones(nums, k):
    n = len(nums)
    maxlength = 0
    for i in range(n):
        count = 0
        for j in range(i, n):
            if nums[j] == 0:
                count += 1
            if count > k:
                break
            maxlength = max(maxlength, j - i + 1)
    return maxlength


print(maxconsecones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=3))
# time complexity : O(N**2)
# space complexity : O(1)


def optimizedmaxconsec1s(nums, k):
    n = len(nums)
    l = 0
    zeros = 0
    maxlength = 0

    for r in range(n):
        if nums[r] == 0:
            zeros += 1
        if zeros > k:

            if nums[l] == 0:
                zeros -= 1
            l += 1
        if zeros<=k:
            maxlength = max(maxlength, r - l + 1)  #only when the number of zeros is withinthe limit of given value k , we calculate the maximum length otherwise the substring still consists of number of 0s greater than the given value k 

    return maxlength


print(optimizedmaxconsec1s([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=3))
# time complexity : O(N)
# space complexity : O(1)


#Fruit Into Baskets
def brutefruitsintobaskets(fruits):
    n =len(fruits)
    maxfruits = 0
    for i in range(n):
     m={}  #this stores the number of fruits as values and the kind of fruits as the key
     for j in range(i,n):
         m[fruits[j]] = m.get(fruits[j],0) + 1  #0 is the default value  and here we are storing the number of counts of the total fruits
         if len(m) > 2:  #as only two baskets are given , so we mustnot use third basket ,
             break
         total =j-i+1 #calculating the total length of the substring which consists of atmost 2 different kind of fruits
         maxfruits=max(maxfruits,total)
    return maxfruits     
print(brutefruitsintobaskets([1, 2, 1]))   
#time complexity : O(N**2)
#space complexity : O(1)  #cause the size of m remains same which denotes the number of fruit baskets , which is 2  

#optimal solution
def optimalfruitsinbaskets(fruits):
    m={}
    l=r=0
    n=len(fruits)
    maxlength = 0
    while r<n:
        m[fruits[r]]=m.get(fruits[r],0) + 1  #storing the count of the fruits in dictionary of m
        while len(m) > 2:
            m[fruits[l]]-=1
            if m[fruits[l]] == 0:
                del m[fruits[l]]
            l+=1    
        maxlength = max(maxlength,r-l+1)    
        r+=1    
        
    return maxlength
print(optimalfruitsinbaskets([1, 2, 3, 2, 2]))
#time complexity : O(N)
#space complexity : O(1)  the size of m is constant cause it always remains same which is 2 , cause only 2 fruits basket are given 

#optimal solution
def optimizedfruitsinbaskets(fruits):
    m={}
    l=r=0
    n=len(fruits)
    maxlength = 0
    while r<n:
        m[fruits[r]]=m.get(fruits[r],0) + 1  #storing the count of the fruits in dictionary of m
        if len(m) > 2:
            m[fruits[l]]-=1
            if m[fruits[l]] == 0:
                del m[fruits[l]]
            l+=1    
        if len(m)<=2:  #only if two different kinds of fruits are taken , we calcualte the length
         maxlength = max(maxlength,r-l+1)    
        r+=1    
        
    return maxlength
print(optimizedfruitsinbaskets([1, 2, 3, 2, 2]))
#time complexity : O(N)
#space complexity : O(1)  the size of m is constant cause it always remains same which is 2 , cause only 2 fruits basket are given 



#Longest Repeating Character Replacement
def brutelongestrepchar(s,k):
    n=len(s)
    maxlength = 0

    for target in set(s):
        for i in range(n):
            count = 0
            for j in range(i,n):
                if s[j] != target:
                    count+=1
                if count>k:
                    break
                maxlength = max(maxlength,j-i+1)  #the function will never reach this code if the total count becomes greater than k
    return maxlength
print(brutelongestrepchar("AABABBA" , k = 1))   
#time complexity : O(m*N**2)  where m is the number of unique characters from the given string
#space complexity : O(1)      

#better solution
def betterlongestrepchar(s,k):
    l=r = 0
    n=len(s)
    maxfreq = 0  #this counts the maximum freq of character for every substring obtained inside the loop
    maxlength = 0
    m={}  #this stores the freq of the character
    while r<n:
        m[s[r]]=m.get(s[r],0)+1
        maxfreq=max(maxfreq,m[s[r]])
        while (r-l+1) - maxfreq > k:    #(r-l+1) - maxfreq this value gives us the number of characters that must be replaced in the current substring , if this is greater than k then we need to minimize our window
         m[s[l]]-=1
         l+=1
        maxlength=max(maxlength,r-l+1)
        r+=1
    return maxlength
print(betterlongestrepchar("BAABAABBBAAA" ,k = 2))
#time complexity : O(N)
#space complexity : O(M)  #number of unique characters from the given string


#optimal solution
def optimallongestrepchar(s,k):
    l=r=0
    n=len(s)
    maxlength = 0
    maxfreq = 0  
    freq = [0] * 26  #as there are total 26 number of alphabets
    while r<n:
        freq[ord(s[r])-ord('A')]+=1
        maxfreq=max(maxfreq,freq[ord(s[r])-ord('A')])
        while (r-l+1) - maxfreq > k:
            freq[ord(s[l])-ord('A')]-=1  #this code ord(s[l]) - ord('A')  calculates the index for every alphabetic letters at index r , as 0 means A , 1 means B
            l+=1
        maxlength=max(maxlength,r-l+1)    
        r+=1
    return maxlength
print(optimallongestrepchar("BAABAABBBAAA" ,k = 2))    
#time complexity : O(N)
#space complexity : O(1)

#Binary Subarrays With Sum
#Given a binary array nums and an integer goal. Return the number of non-empty subarrays with a sum goal.

def brutebinarysubsum(nums,goal):
    n=len(nums)
    count = 0
    for i in range(n):
        s=0
        for j in range(i,n):   
            s+=nums[j]
            if s==goal:
                count+=1
            elif s>goal:
                break
    return count
print(brutebinarysubsum([0, 0, 0, 0, 1] , goal = 0))  
#time complexity : O(N**2)
#space complexity : O(1)       

#better approach
def optimalbinarysubarray(nums,goal):
    
    def calculatel(nums,k):
        if k<0:
            return 0
        l=r=0
        n=len(nums)
        count = 0
        s=0
        while r<n:
            s+=nums[r]
            
            while s>k: 
                s-=nums[l]
                l+=1
            count+=r-l+1  #this gives us the number of subarrays ending at index r and the sum of these subarray is lesser than or equal to the given value k    
            r+=1   
        return count
    return calculatel(nums,goal) - calculatel(nums,goal-1)  #this gives us the number of subarrays whose sum is exactly equal to the given value goal
print(optimalbinarysubarray( [0, 0, 0, 0, 1] , goal = 0))
#time complexity : O(N)
#space complexity : O(1)            

#Count number of Nice subarrays
#Given an array nums and an integer k. An array is called nice if and only if it contains k odd numbers. Find the number of nice subarrays in the given array nums.
#A subarray is continuous part of the array.

def brutecountnicesubarrays(nums,k):
    n = len(nums)
    def countnicesubarrays(array):
        count = 0
        for i in range(len(array)):
            if array[i] % 2 !=0:
                count+=1
        if count == k:
            return True  #we return true when the count of odd numbers is exactly equal to value k
        else:
            return False        

    total = 0
    for i in range(n):
        for j in range(i,n):
            if len(nums[i:j+1])>=k:  #we only pass the substring when this subsstring has the length greaer than or equal to value k
                if countnicesubarrays(nums[i:j+1]):
                    total+=1
    return total
print(brutecountnicesubarrays( [4, 8, 2] , k = 1))
#time complexity : O(N**3)
#space complexity : O(1)


#optimal solution
#in the optimal solution what we are trying to do is , we use the same logic of finding the number of subarrays having odd numbers lesser than or equal to k and
#lesser than equal to k-1
#then we substract those two values , which then provide us the actual count of subarrays having exactly k number of odd numbers 
#but first of all , what we do is , we convert all the odd numbers into 1 and all the even numbers from the given array into 1 and 0 respectively , 
#by using the formulae a %  2 
def optimalcountnice(nums,k):
    def countnice(nums,value):
        s= 0
        count = 0
        if value<0:
            return 0
        n=len(nums)
        l=r=0
        for r in range(n):
            
            s+=(nums[r] % 2) #if the number is odd adding 1 otherwise it will add 0
            while s>value:
                s-=(nums[l]  % 2)   #here if the number is odd then the remainder will be 1 otherwise 0 
                l+=1
            count+=r-l+1    #adding the number of subarrays ending at index r having the number of odd numbers lesser than or equal to the passed value
            
        return count    


    return countnice(nums,k) - countnice(nums,k-1)
print(optimalcountnice( [4, 8, 2] , k = 1))
#time complexity : O(N)
#space complexity : O(1)


#Number of Substrings Containing All Three Characters
#Given a string s , consisting only of characters 'a' , 'b' , 'c'.Find the number of substrings that contain at least one occurrence of all these characters 'a' , 'b' , 'c'.
def brutenumsubstring(s):
    n=len(s)
    count = 0
    for i in range(n):
        freq=[0] * 3
        for j in range(i,n):  
            freq[ord(s[j])-ord('a')]+=1  
            if freq[0]>0 and freq[1]>0 and freq[2]>0:
             count+=n-j   #here we are subtracting the total length n by this ending index j , cause after this index j until the last index , this substring consists of all three a,b and c characters
             break
    return count
print(brutenumsubstring("ccabcc"))                
#time complexity : O(N**2)
#space complexity : O(1)


def optimalnumsubstring(s):
    n=len(s)
    l=r=0
    count = 0
    freq= [0] * 3  #making the 3 freq for a,b,c
    while r<n:
        freq[ord(s[r])-ord('a')]+=1  #increasing the freq of the r indexed character based on the ord of a
        while freq[0]>0 and freq[1]>0 and freq[2]>0:  #if all the indices of the freq has the values greater than 0 then it means we have found a,b,c in the substring
         count+=n - r  #here r means the current index in which we have found all a,b, and c and we are substracting r from n cause it gives us the total number of subarrays which consists of all a,b, and c
         freq[ord(s[l])-ord('a')]-=1
         l+=1
        r+=1    
    return count
print(optimalnumsubstring("ccabcc"))
#time complexity : O(N)
#space complexity : O(1)  #even though we used the freq variable , its constant whose length is always 3

#Maximum Points You Can Obtain from Cards
#Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. The score is the sum of the scores of the chosen cards.
#Return the maximum score that can be obtained.
def brutemaximumcardscore(card,k):
    l=0
    n=len(card)
    r=n-1
    count=0  #this counts the number of cards taken
    s=0      #this calculates the total sum 
    while count<k:
        if card[r]>card[l]:
            s+=card[r]
            r-=1
        else:
            s+=card[l]
            l+=1
        count+=1
    return s  
print(brutemaximumcardscore( [1, 2, 3, 4, 5, 6] , k = 3))             
#time complexity : O(k)
#space complexity : O(1)


#better approach
def bettermaximumcardscore(card,k):
    total=0
    n=len(card)
    leftsum = 0
    rightsum=0
    maxsum = 0
    for i in range(k):
        leftsum+=card[i]
    maxsum=leftsum
    r=n-1
    for i in range(k-1,-1,-1):
        leftsum-=card[i]
        rightsum+=card[r]
        maxsum=max(maxsum,leftsum+rightsum)
        r-=1   


    
    return maxsum
print(bettermaximumcardscore( [1, 2, 3, 4, 5, 6] , k = 3))    
#time complexity : O(K)
#space complexity : O(1)


#HARD PROBLEMS
#Longest Substring With At Most K Distinct Characters
#Given a string s and an integer k.Find the length of the longest substring with at most k distinct characters.
def longestsubstring(s,k):
    n=len(s)
    maxlength = 0
    for i in range(n):
        m={}
        for j in range(i,n):
            m[s[j]]=m.get(s[j],0)+1
            if len(m)>k:
                break
            maxlength=max(maxlength,j-i+1)
    return maxlength
print(longestsubstring( "abcddefg" , k = 3))  
#time complexity : O(N**2)
#space complexity : O(1) 
     
            


