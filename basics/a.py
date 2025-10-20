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

        
