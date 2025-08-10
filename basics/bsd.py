#Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).
#brute approach
def brutesqr(num):
    ans = 0
    for i in range(1,num+1):
        if (i * i) <=num:
            ans = i
        else:
            break    #if the product becomes greater than the integer itself then there is no point in calculating the product , we are just breaknig or getting out of the loop.
    return ans
print(brutesqr(28))    
#time complexity : O(N)
# space complexity : O(1)  

def optimalsqr(num):
    ans = 0
    left = 1 
    right = num
    while left<=right:
        mid = (left + right) // 2
        if mid * mid <=num:   #if the product of the mid is lesser than or equal to num then the mid might be an answer so 
            ans=mid
            left=mid+1   #as the product of mid * mid is lesser we move the left pointer in the right half
        else:  #if the product is way too greater then we just move the right pointer in the left half
            right=mid - 1
    return(ans)
print(optimalsqr(28))            
#time complexity : O(logN)
#space complexity : O(1)


#Find Nth root of a number
#Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.
#brute approach
def nthroot(N,M):
    ans=0
    for i in range(1,M+1):
        if i ** N <=M:
            ans=i
        else:
            break
    if isinstance(i ** N,int):    
     return ans
    else:
        return -1
print(nthroot(3,27)) 
#time complexity :O(N)
# space complexity : O(1)

#better approach
def betternth(N, M):
    ans = -1
    left, right = 1, M
    while left <= right:
        mid = (left + right) // 2
        if (mid**N)==M:
            ans=mid
            return ans
        elif (mid ** N) < M:
            left = mid + 1
        else:
            right = mid - 1
    return ans

print(betternth(4, 69))
#time complexity : O(logM)
#space complexity : O(1)
      

           




