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


#Max Consecutive Ones III
#brute approach
def brutemaxconsecones(nums,k):
    n=len(nums)
    maximum = 0
    for i in range(n):
        count=0
        for j in range(i,n):
            if nums[j] == 0:
                count+=1    
            if count>k:
                break   
            maximum=max(maximum,j-i+1)
    return maximum
print(brutemaxconsecones( [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , 3)) 
#time complexity : O(N**2)
#space complexity : O(1)

#optimal approach
def optimalmaxconsecones(nums,k):
    n=len(nums)
    l=r=0
    count = 0
    maxlength = 0
    while r<n:
        if nums[r] == 0:
            count+=1
        if count>k:
            if nums[l] == 0:
                count-=1
            l+=1
        elif count<=k:
            maxlength=max(maxlength,r-l+1)
        r+=1
    return maxlength
print(optimalmaxconsecones([0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] ,  3))    
#time complexity : O(N)
#space complexity : O(1)                

#Fruits into basket 
#so the question is asking us to put as much as fruits in two baskets available but each basket must consists of onle one kind of fruit, and we must start from the left most tree always

#brute approach
def brutefruits(fruits):
    n=len(fruits)
    s=float('-inf')
    for i in range(n):
     m={}
     for j in range(i,n):
         m[fruits[j]]=m.get(fruits[j],0) + 1
         if len(m)>2:
             break
         
         s=max(s,sum(m.values()))
    return s         
             
    
print(brutefruits( [1, 2, 1]))     
#time complexity : O(N**2)
#space complexity : O(M)  number of unique kind of fruits in each iteration
         

#optimal solution
def optfruits(fruits):
    l=r=0
    n=len(fruits)
    m={}
    ans=float('-inf')
    while r<n:
        m[fruits[r]]=m.get(fruits[r],0) + 1 
        if len(m)>2:
            m[fruits[l]]-=1
            if m[fruits[l]] == 0:
                del m[fruits[l]]
            l+=1
        elif len(m)<=2:
            ans=max(ans,(r-l+1))  #r-l+1 also gives us the  number of fruits inside the current window , which is same as calculating sum(m.values())
            r+=1
    return ans
print(optfruits( [1, 2, 3, 2, 2]))   
#time complexity : O(N)
#space complexity : O(1)      

#Longest Repeating Character Replacement
#brute approach
def brutelongestrep(s,k):  #we cannot replace more than k characters in the window
    n=len(s)
    maxlength = 0
    for t in set(s):
        for i in range(n):
            count = 0  #count calculates the number of characters that we must replace with the current t inorder to get the longest window having repeating character
            for j in range(i,n):
                if s[j]!=t:  #only if the current j indexed character doesnot match with the current t , we need to replace this current character, thats why increase the count
                    count+=1
                if count>k:
                    break
                maxlength=max(maxlength,j-i+1) 
    return maxlength
print(brutelongestrep( "AABABBA" ,  1))  
#time complexity : O(m*N**2)  where m is the number of unique characters from given string s
#space complexity : O(1)          

#optimal solution
#so the logic behind this optimal solution is we try to find the number of character that we must replace ,with the help of the value of  maximum freq in the current window, if the freq of number to be replaced is greater than k then we just keep removing the number at l index from m , till the window is valid
def optlongestrep(s,k):
    n=len(s)
    l=r=0
    m={}
    maximfreq=0
    maxlength = 0
    while r<n:
        m[s[r]]=m.get(s[r],0) + 1
        maximfreq=max(maximfreq,m[s[r]])
        while (r-l+1) - maximfreq > k:  #(r-l+1) - maximfreq gives us the number of characters needed to be replaced at the current window
            m[s[l]]-=1
            l+=1
        maxlength=max(maxlength,r-l+1)
        r+=1
    return maxlength
print(optlongestrep( "AABABBA" , 1))    
#time complexity : O(N)
#space complexity : O(M)  number of unique characters from the given string


#Binary Subarrays With Sum
#brute approach
def brutebinarysum(nums,goal):
    n=len(nums)
    count = 0
    for i in range(n):
        s= 0
        for j in range(i,n):
            s+=nums[j]
            if s==goal:
                count+=1
            elif s>goal:
                break
    return count
print(brutebinarysum(  [0, 0, 0, 0, 1] , goal = 0))  


#optimal solution
def optimalbinarysum(nums,goal):
    def calcualtesum(nums,k):
        if k<0:
            return 0
        l=r=0
        n=len(nums)
        s=0
        count=0
        while r<n:
            s+=nums[r]
            while s>k:
                s-=nums[l]
                l+=1
            count+=r-l+1  #total number of subarrays whose sum is less than or equal to k
            r+=1    
                
        return count
    return calcualtesum(nums,goal) - calcualtesum(nums,goal-1)
print(optimalbinarysum( [0, 0, 0, 0, 1] , goal = 0))   
#time complexity : O(N)
#space complexity : O(1)         


#count number of Nice subarrays
#brute approach
def brutecount(nums,k):
    if k<0:
        return 0
    n=len(nums)
    count = 0
    for i in range(n):
        c=0
        for j in range(i,n):
            if nums[j]%2==1:  #if the number is odd , then we increase this c which denotes the number of odd numbers in the current window
                c+=1
            if c==k:
                count+=1
            elif c>k:
                break
    return count
print(brutecount( [41, 3, 5] , k = 2))   
#time complexity : O(N**2)
#space complexity : O(1)              

#optimal approach
def optcount(nums,k):
    
    def calculatecount(nums,v):
        if v<0:
         return 0
        n=len(nums)
        l=r=0
        count = 0
        odd=0
        while r<n:
            
            odd+=nums[r]  % 2   #if the number is odd then its value will be 1 , if its even then its value will be 0
            while odd>v:
                odd-=nums[l] % 2
                l+=1
            count+=r-l+1   #as we are increasing the count based on the fact that the number of odd numbers in the current window is less than or equal to the value v,
            r+=1
        return count
    return calculatecount(nums,k) - calculatecount(nums,k-1)            
print(optcount([41, 3, 5] , k = 2))
#time complexity : O(N)
#space complexity : O(1)


#Number of Substrings Containing All Three Characters
#brute approach
def brutesuball(s):
    n=len(s)
    count = 0
    for i in range(n):
        k=set()
        for j in range(i,n):
            k.add(s[j])
            if len(k) == 3:
                count+=n-j  #if at the window j , all occcurences of a,b, and c is found then ofcourse the window till the end from the starting position of this window, also consists of a,b and c
                break
    return count
print(brutesuball("ccabcc"))  
#time complexity : O(N**2)
#space complexity : O(1)       

#optimal solution
#so the logic behind this optimal solution is that ,
#we calculate the frequency of the letters a,b, and c with the help of ord('a)
#and when the frequency of all characters are greater than 0 then 
#we calculate the number of substring by n-j
#then we shrink the window with the help of l index 
def optsuball(s):
    l=r=0
    n=len(s)
    freq=[0] * 3
    count = 0
    while r<n:
        freq[ord(s[r])-ord('a')]+=1
        while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
            count+=n-r
            freq[ord(s[l])-ord('a')]-=1
            l+=1
        r+=1    
    return count
print(optsuball("abcba"))   
#time complexity : O(N)
#space complexity : O(1)         

#Maximum Points You Can Obtain from Cards
def maxmpoints(card,k):
    n=len(card)
    leftsum = 0
    r = n-1
    rightsum=0
    maxpoints=0
    for i in range(k):
        leftsum+=card[i]
    maxmpoints=leftsum  #as till now the maximum points we have found is ofcourse the leftsum as we have looped from the left side till k index
    for i in range(k-1,-1,-1):
        leftsum-=card[i]  #here we are replacing the number from the  leftindex with the right index with the help of k
        rightsum+=card[r] 
        maxpoints=max(maxpoints,leftsum+rightsum)
        r-=1   
    return maxpoints       
print(maxmpoints([5, 4, 1, 8, 7, 1, 3 ] , k = 3))
#time complexity : O(K)
#space complexity : O(1)


            




















            
















            

        

