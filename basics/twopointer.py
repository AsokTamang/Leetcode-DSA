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
             
            



