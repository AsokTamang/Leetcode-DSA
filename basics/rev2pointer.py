#longest substring without repeating characters
def longestsubstring(s):
    n=len(s)
    maxlength = 0
    for i in range(n):
        seen = set()
        for j in range(i,n):
            if s[j] in seen:
                break
            seen.add(s[j])
            maxlength=max(maxlength,j-i+1)
    return maxlength
print(longestsubstring("aaabbbccc"))   
#time complexity : O(N**2)
#space complexity : O(1)     

#optimal approach
def optimallongestsubstring(s):
    l=r=0
    n=len(s)
    m={}  #here we are storing the character and its corresponding index as key-value pair
    maxlength = 0
    while r<n:
        if s[r] in m and m[s[r]]>=l:
            l=m[s[r]] + 1
        m[s[r]] = r
        maxlength=max(maxlength,r-l+1)
        r+=1
    return maxlength
print(optimallongestsubstring("abcddabac"))    
#time complexity : O(N)
#space complexity : O(M) number of unique characters in the given string  




 