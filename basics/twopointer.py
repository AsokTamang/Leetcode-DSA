#Longest Substring Without Repeating Characters
#Given a string, S. Find the length of the longest substring without repeating characters.


#so the question is asking us to find the substring where all the characters are completely unique
def longestsubstring(s):
    n=len(s)  #length of the given string
    maxlength=0
    for i in range(n):
        same=set()
        length=0
        for j in range(i,n):
            if s[j] in same:    #as soon as we find the same character in our current formed substring we break out of this j loop 
                
                break
            same.add(s[j])   #if we are finding the unique characters then we keep on adding these new characters in seen and keeps on calculating the length
            length=j-i+1 #this  
        maxlength=max(maxlength,length)  #then at the end of the loop , we calculate the maximum length
    return maxlength
print(longestsubstring('aaabbbccc'))    
#time complexity : O(N**2)
#space complexity : O(M)  number of different character at each loop


#optimal solution
def optimalsubstring(s):
    n=len(s)
    l=r= 0 
    maxlength = 0
    m={ }  #this is our dictionary which stores every characters and its corresponding indices
    while r<n:
        if s[r] in m and m[s[r]] >= l:  #if we find the same character in a while loop then the value of l will be s[r] + 1
            l=m[s[r]] + 1    
        m[s[r]] = r  #storing the character and index
        maxlength=max(maxlength,r-l+1)
        r+=1
    return maxlength
print(optimalsubstring('aaabbbccc'))                 
   

