#Longest Substring With At Most K Distinct Characters
def brutelongestsubstring(s,k):
    n=len(s)
    maxlength=float('-inf')
    for i in range(n):
        m=set()
        for j in range(i,n):
            m.add(s[j])
            if len(m)>k:
                break
            maxlength=max(maxlength,j-i+1)
    return maxlength
print(brutelongestsubstring("abcddefg" ,3))  
#time complexity : O(N**2)
#space complexity : O(1)

#optimal solution
def optimalongestsubstring(s,k):
    n=len(s)
    l=r=0
    m={}
    maxlength = float('-inf')
    while r<n:
        m[s[r]]=m.get(s[r],0)+1
        if len(m) > k:
            m[s[l]]-=1
            if m[s[l]]==0:
                del m[s[l]]
            l+=1
        if len(m)<=k:        
         maxlength=max(maxlength,r-l+1)
         r+=1
    return maxlength
print(optimalongestsubstring("aababbcaacc" , k = 2))  
#time complexity : O(N)
#space complexity : O(M)  number of unique characters from the given string s

#Subarrays with K Different Integers
def brutesubarray(nums,k):
    count = 0
    n=len(nums)
    for i in range(n):
        m=set()
        for j in range(i,n):    
            m.add(nums[j])
            if len(m)==k:
                count+=1
            elif len(m)>k:
                break
    return count
print(brutesubarray([1, 2, 1, 3, 4], k = 3))       

#optimal solution
#inorder to find the number of subarrays having exactly k distinct integers , we can find find the number of subarrays having less than equal to k-1 distinct integers and k , and then we can subtract between k and k-1,
def optimalkdiff(nums,k):
    def solvelesseqlk(nums,value):
        if value<0:
            return 0
        l=r=0
        n=len(nums)
        m={}
        count=0
        while r<n:
            m[nums[r]]=m.get(nums[r],0)+1
            if len(m)>value:
                m[nums[l]]-=1
                if m[nums[l]]==0:
                    del m[nums[l]]
                l+=1
            if len(m)<=value:
                count+=r-l+1  #we have to the number of all the subarrays ending at index r consisting the number less than or equal to k distinct numbers or elements
                r+=1     
        return count           



    return solvelesseqlk(nums,k) - solvelesseqlk(nums,k-1)
     
print(optimalkdiff([1, 2, 1, 2, 3], 2  ))
#time complexity : O(N)
#space complexity : O(M)  number of distinct elements in nums 

#minimum window substring
#Given two strings s and t. Find the smallest window substring of s that includes all characters in t (including duplicates) , in the window. Return the empty string "" if no such substring exists.
from collections import Counter
def bruteminimumwindow(s,t):
    n=len(s)
    k=Counter(t)
    minlength = 10 ** 9
    ans = ''
    for i in range(n):
        m={}
        for j in range(i,n):
            valid=True
            m[s[j]]=m.get(s[j],0) + 1
            for char in t:
              if m.get(char,0) < k[char]:      #if the char from t is still not stored in m yet , then its default value will be 0
                  valid = False 
            if valid and j-i+1<minlength:
                minlength=j-i+1
                ans=s[i:j+1]
    return ans
print(bruteminimumwindow("aAbBDdcC" , "Bc"))       
#time complexity : O(N**2)
#space complexity : O(M)  number of unique characters


#optimal solution
def optminimumwindow(s,t):
    n=len(s)
    l=r=0
    k=Counter(t)  #this stores the counting of character of t as key-value pair
    formed = 0
    minlength = 10**9
    ans = ''
    while r<n:
        if s[r] in t:
            k[s[r]]-=1
            if k[s[r]]==0:  #if the the freq of current r inddexed char becomes 0 then it means we have the required freq of this char thats in t, in this valid window
                formed+=1  
        
        while l<=r and formed==len(k):  #if we have found all the characters of t in the current window then
            if r-l+1 < minlength:
                minlength=r-l+1
                ans = s[l:r+1]
           
            if s[l] in t:
                 
             if k[s[l]]==0:  #if the l indexed char's freq is 0 then it means we have the req char of req freq which is of l index , and when we remove this , the formed value will also decrease so
                    formed-=1
             k[s[l]]+=1    #making the freq of l index as previous
            l+=1
        r+=1
    return ans
print(optminimumwindow( "aAbBDdcC" ,  "Bc"))
                     

#Minimum Window Subsequence
#﻿Given strings s1 and s2, return the minimum contiguous substring part of s1, so that s2 is a subsequence of the part.
#If there is no such window in s1 that covers all characters in s2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.
def bruteminsubseq(s1,s2):
    ans=''
    n=len(s1)
    minlength = 10**9
    for i in range(n):
        k=0
        for j in range(i,n):
            if s1[j] == s2[k]:
                k+=1
            if k ==len(s2):
                if j-i+1<minlength:
                    minlength=j-i+1
                    ans = s1[i:j+1]
                    break
    return ans
print(bruteminsubseq("abcdebdde", "bde"))            
#time complexity : O(N**2)
#space complexity : O(1)

#optimal solution
def optimalminsubseq(s1,s2):
    n=len(s1)
    start=i=j = 0
    minlength = float('inf')
    while i < n:
        if s1[i] == s2[j]:
            j+=1
        if j == len(s2):
             end = i+1
             j-=1   #putting the j pointer back to the last index of s2 
             while j>=0:
                 if s1[i] == s2[j]:
                     j-=1
                 i-=1
             i+=1  #putting the i pointer at the start position for the valid window
             if end - i <minlength:
                 minlength=end - i 
                 start = i
        i+=1 

    if minlength==float('inf'):
        return ''
    else:
     return s1[start:start+minlength]
print(optimalminsubseq("abcdebdde","bde"))   
#time complexity : O(N)
#space complexity : O(1) 


#longest Substring Without Repeating Characters
def brutelongestrep(s):
    n=len(s)
    maxlength = float('-inf')
    for i in range(n):
        m=[]
        for j in range(i,n):
            if s[j] in m:
                break
            m.append(s[j])
            maxlength=max(maxlength,j-i+1)
    return maxlength
print(brutelongestrep("aaabbbccc"))   
#time complexity : O(N**2)
#space complexity : O(M)  number of unique characters in a given string s

#optimal solution
def optimallongestrep(s):
    n=len(s)
    l=r=0
    m={}
    maxlength = float('-inf')
    while r<n:
        if s[r] in m and l<=m[s[r]]:  #if the current r indexed value is in m already , then we move the left pointer to the next position of initial value of this r indexed character
            l=m[s[r]]+1
            m[s[r]]=r
        m[s[r]]=r  #storing the char with its index as key-value pair in m
        
        maxlength=max(maxlength,r-l+1)
        r+=1
    return maxlength
print(optimallongestrep("abcddabac"))   
#time complexity : O(N)
#space complexity : O(M) 















            

        

