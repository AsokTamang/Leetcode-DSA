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