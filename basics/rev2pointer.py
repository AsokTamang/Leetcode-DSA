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
