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