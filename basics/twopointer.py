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


