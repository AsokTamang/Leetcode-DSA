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


