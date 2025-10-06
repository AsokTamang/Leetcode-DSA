#Next Greater Element
#brute approach
def nextgreaterelement(arr):
    ans = []
    for i in range(len(arr)): 
         ansnum = -1  
         for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                ansnum = (arr[j])  #as soon as we find the number which is greater as well as nearest , then we append this particular number in our ans variable and return
                break
         ans.append(ansnum)  #if we didn't find any number greater than the i indexed number then we just append -1 in our ans variable 
    return ans
print(nextgreaterelement([6, 8, 0, 1, 3])) 
#time complexity : O(N^2)
#space complexity : O(N)        