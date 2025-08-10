# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
def dutchnationalalgo(array):
    low = 0  # the left index or the most extreme left
    mid = 0
    high = len(array) - 1  # the last index or the most extreme right
    while mid <= high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            low += 1  # as the left most part is already sorted , we move the left towars the right direction
            mid += 1  # same with the mid's first index  its range get decreased by one as we move the mid towards the right direction
        elif array[mid] == 1:
            mid += 1  # as the mid must consists of 1 its already sorted so we are just devreasing the range of mid and moving the mid towards right direction
        elif array[mid] == 2:
            array[mid], array[high] = (
                array[high],
                array[mid],
            )  # if the mid value is 2 then we move this 2 towards the end of the array and
            high -= 1  # as the extreme right must consists of 2 , which makes it already sorted after swapping , we decrease the range of high and move the high pointer towards the left direction
    print(array)


dutchnationalalgo([1, 0, 2, 1, 0])

# timecomplexity: O(N) as the loop runs only once for every elemnents
# spacecomplexity:O(1) as the memeory used is just one


# brute approach
def bruteapp(array):
    for i in range(len(array)):
        minindex = i
        for j in range(i, len(array)):
            if array[j] < array[minindex]:
                minindex = j
        array[minindex], array[i] = array[i], array[minindex]
    print(array)


bruteapp([1, 0, 2, 1, 0])
# timecomplexity: O(N^2) as the loop runs only twice for every elemnents
# spacecomplexity:O(1) as the memeory used is just one  cause we are not using additional arrays , or dict or any storing properties

# better approach


def betterapproach(array):
    # the variables down below are used for storing the number of counts of 0,1 and 2 in an array
    count0 = 0
    count1 = 0
    count2 = 0
    # what we are doing is couting the number of 0s,1s and 2s then we start putthing them according to the indexes
    for num in array:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        elif num == 2:
            count2 += 1
    for i in range(count0):
        array[i] = 0
    for i in range(count0, count1 + count0):
        array[i] = 1
    for i in range(count1 + count0, len(array)):
        array[i] = 2
    print(array)


betterapproach([1, 0, 2, 1, 0])


# permutatiosn
# approach 1
def optimalpermutation(array, ds, m, ans):
    if len(ds) == len(array):
        ans.append(ds[:])
        return
    for i in range(len(array)):
        if i not in m:
            m[i] = True
            ds.append(array[i])
            optimalpermutation(array, ds, m, ans)
            ds.pop()
            del m[i]


ans = []
optimalpermutation([1, 2, 3], [], {}, ans)
print(ans)


# approach2
def optimalapproach(array,index,ans):
    if index == len(array)-1:
       ans.append(array[:])
       return
    for i in range(index,len(array)):
        array[index],array[i] = array[i] , array[index]
        optimalapproach(array,index+1,ans)
        array[index],array[i]=array[i],array[index]
ans=[]
optimalapproach([1,2,3],0,ans)
print(ans)              
        


#permutation 
def permutation(array,index,ans):
    if index == len(array)-1:
        ans.append(array[:])
        return
    for i in range(index,len(array)):
        array[index],array[i] = array [i], array[index]
        permutation(array,index+1,ans)
        array[index],array[i] = array [i], array[index]
ans=[]
permutation([1,2,3],0,ans)
print(ans)

        
#longest consecutive number
def linearsearch(array,num):
    for i in range(len(array)):
        if array[i] == num:
            return True
    return False    

def consec(array):
    length=1
    for i in range(len(array)):
        x = array[i]
        count = 1    #for every value of x we make the count to 1
        while linearsearch(array,x+1):   #then for every value of x we are trying to find x+1 using linear search function
            #if found we increase the count by 1
            x+=1
            count+=1
        length=max(length,count)
    print(length)
consec([5,4,3,2,1,100,200,101,201])        

# n is the number of rows and m is the number of columns
#or n is the number of elements in an outer array while m is the number of elements in an inner arrays
def matrixzero(array,n,m): 
    rows = [0] * n #here we are making the zero matrices called rows having n number of elements 
    cols = [0] * m #same with this one but with m number of elements
    #we are running the loop below to find the index on both row based as well as column based to make its corresponding elements 0
    for i in range(n):  #looping through outer loop or outer array
        for j in range(m):  #looping through inner loop 
            if array[i][j] == 0:  #here we are checking for each and every element inside the matrix that if they are equal to 0 or not
                #if yes then 
                rows[i] = 1
                cols[j] = 1   #then we find that particular index from row based index as well as column based index
    for i in range(n):
        for j in range(m):
            if rows[i] == 1 or cols[j] == 1:
                array[i][j] = 0
    print(array)
matrixzero([[0,1,1],[1,0,1],[1,1,0]],3,3)    


def optimalapproach(array,n,m):  #here n is the number of rows and m is the number of columns
    first_row_haszero=False
    first_col_haszero=False

    for j in range(m):
        if array[0][j] == 0:
            first_row_haszero=True
    for i in range(n):
        if array[i][0] == 0:
            first_col_haszero=True
    #then we make a mark in the first row and first column  based on the zero element which lies inside the matrix
    for i in range(1,n):
        for j in range(1,m):
            if array[i][j] == 0:       
                array[0][j]=0
                array[i][0]=0
    #then based on the marker on the first row or first column, we start making elements zero in the inside matrix
    for i in range(1,n):
        for j in range(1,m):
            if array[i][0] == 0 or array[0][j] == 0:
                array[i][j] = 0
    
    #then based on the first row and first column, we start making its other elements 0l
    
    if first_col_haszero:
        for i in range(n):
            array[i][0] = 0

    if first_row_haszero:
        for j in range(m):
            array[0][j] = 0
    print(array)        
optimalapproach([[1,0,1],[0,1,1],[1,1,0]],3,3) 


outer = []
n=3
for i in range(n):
    outer.append([0] * 3)
print(outer)

def rotatematrrix(array,n,m): 
    outer = []
    for i in range(n):
        outer.append([0]*m)
    
   
    for i in range(n):
        k=2
        for j in range(m):
            outer[i][j] = array[k][i]    
            k-=1
    print(outer)                          
rotatematrrix([[1,2,3],[4,5,6],[7,8,9]],3,3)
#time complexity: O(N*M)
#space complexity: O(N*M)  



def betterapproach(array,k):
   m = {0:1}   #and here we are using the first prefix sum of 0 with repition 1 cause there might be a case where the first continuous subarray gives us the result k
   count = 0
   s = 0
   for num in array:
       s+=num
       if s - k in m:
           count+=m.get(s-k,0)+1  #what we are doing is finding the number of subarrays until the current index which  has a sum of s-k because those subarray's gives the target k 
       m.get(s,0) + 1  
   print(count)        

betterapproach([1,1,1],2) 
#timecomplexity is : O(N)
#spacecomplexity is : O(N) for worst case if all the subarrays give the target k            

def practice(r,c): #r is the number of rows and c is the number of columns
    res= 1
    for i in range(1,c+1):
        print(res,end=' ')
        res =( res * (c - i)) // i
practice(5,5)        



#brute approach
def majorityeleme(array,n):
    s= []
    for i in range(len(array)):
        if array[i] in s:  #if the majority element is already in the list then we just continue or move into the another loop or another value of i
            continue    
        count = 1
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                count+=1
        if count > n/3:
            s.append(array[i]) 
    print(s)
majorityeleme( [1, 2, 1, 1, 3, 2, 2],7) 
#timecomplexity is O(N^2) as we are using the two nested loops
# space complexity is O(1) which is constant       

#better approach
def betterapproach(array,n):
    m = {}
    ans=[]
    for num in array:
        m[num] = m.get(num,0) +  1   #here the default value of the key in m is 0
    for key,value in m.items():
        if value > n/3:
            ans.append(key)
    print(ans)  
betterapproach( [1, 2, 1, 1, 3, 2, 2],7)    
#time complexity is : O(N) + O(M)
# space complexity is : O(M)   

#optimal approach 
#for the optimal approach what we do is use booyer's algorithm which is based on the last man standing
#as the question is asking to find the numbers which appear more than n/3 times where n is the length of an array. so , there must be or there is higher chance that alteast 2 elements satisy this condition
def optimalapproach(array,n):
    count1=0
    count2=0
    can1=0
    can2=0
    for num in array:
        if num == can1:
            count1+=1
        elif num == can2:
            count2+=1
        elif count1==0:
            count1=1
            can1=num
        elif count2==0:
            count2+=1
            can2=num
        else:
            count1-=1
            count2-=1
    print([can1,can2])
optimalapproach( [1, 2, 1, 1, 3, 2, 2],7)
#time complexity is : O(N)
#spacecomplexity is :O(1)  which is constant             

#Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
def var1(r,c):  #here r is the row position and c is the column postion
    res=1
    for i in range(c):
        res = (res * (r-i) )/ (c- i)
    print(int(res))
var1(5,2)    
#time complexity is : O(N)
#space complexity is : O(1)

#Given the row number n. Print the n-th row of Pascal’s triangle.
def var2(n):  #here n is the rowth number and the question is asking us to print all the elements of n
   res = 1
   for i in range(n+1):
       print(res,end=' ')
       res = (res * (n-i)) 
       res = res // (i+1)
   print()   
var2(5)   
#timecomplexity : O(N+1)  or O(N) here N is the row number
#spacecomplexity : O(1)

#var3 Given the number of rows n. Print the first n rows of Pascal’s triangle.
def var3(n):  #here instead of printing the nth row we are printing the first n rows
    
    for i in range(n):
        res = 1
        for j in range(i):  #here i acts as the rowth number and j acts as the number of columns 
            print(res,end= ' ')
            res = res * (i-j)
            res = res // (j+1)
        print(res)
var3(5)
#time complexity : O(N^2)
#space complexity : O(1)

#brute approach
def brutetriplet(array):
    a = set()
    #here we are using set so that there wont be duplicate triplets
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1,len(array)):
                if array[i] + array[j] + array[k] == 0:
                    a.add(tuple(sorted([array[i],array[j],array[k]])))
    print(list(a))
brutetriplet( [2, -2, 0, 3, -3, 5]) 
#time complexity O(N^3)
#space complexity O(1) or O(N) in worst case 

#better approach for which we use hash map or dictionary
def betterapproach(array):
   
    a = set()
    for i in range(len(array)):
        m = {}  #we must include the m inside the for loop of i as for every value of i , there must be new hasmap so it wont repeat the previously used elements
        for j in range(i+1,len(array)):
            thirdelem = -(array[i] + array[j])
            if thirdelem in m:
                a.add(tuple(sorted([array[i],array[j],thirdelem])))
            m[array[j]] = m.get(array[j],0) + 1   #here if the array j exist we increase by one otherwise the initial value will become 1
    print(list(a))
betterapproach([2, -2, 0, 3, -3, 5])                
#time complexity : O(N^2)
#space complexity :  O(k) where k is the number of unique triplets as we are using the dictionary

#optimal approach where we use two pointers
def optimaltriplet(array):
    s= set()
    array=sorted(array)
    for i in range(len(array)):
        if i > 0 and array[i] == array[i-1]:    #if the next i indexed number is equal to the previous one then we just go with the next iteration of i
            continue
        left = i + 1
        right = len(array) - 1
        
        while left < right:
            total=array[i] + array[left] + array[right]
            if total==0:
                s.add(tuple([array[i],array[left],array[right]]))
                left+=1
                right-=1
                while array[left] == array[left-1]: left+=1
                while array[right] == array[right+1] : right-=1
            elif total < 0:
                left+=1
                while array[left] == array[left-1]: left+=1

            elif total > 0:
                right-=1
                while array[right] == array[right+1] : right-=1         

    print(list(s))
optimaltriplet([2, -2, 0, 3, -3, 5]) 
#time complexity : O(N)
# space complexity :  O(1)   

def bettersubarray(array,n):
    s = 0
    m={}
    length = 0
    for i in range(n):
        s+=array[i]
        if s == 0:
            length = max(length,i+1)   #here we are coding i+1 as the i starts from 0
        elif s in m:  #if the sum is not zero but the same sum is seen previously or in the previous subarray then we calculate the subtraction of current index where we get this common sum and the index where we saw this common sum, as 
            #this subtraction gives us the length of the subarray which gives us the sum 0
            length = max(length,i-m[s])
        else:
            m[s] = i    #we are storing the index     
    print(length)
bettersubarray([15, -2, 2, -8, 1, 7, 10, 23],8)             


#Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.

def xork(array,k):
    count = 0
    ans = []
    for i in range(len(array)):
        xor = 0
        for j in range(i,len(array)):
            xor^=array[j]
            if xor == k:
                count+=1
                ans.append(array[i:j+1])
    print('The count is :',count)
    print(ans)
xork([4, 2, 2, 6, 4],6)    
#time complexity : O(N^2)
#space complexity : O(1)  


#better approach
def betterxork(array,k):
    m={0:1}  #here we are making the base case of 0 whose count is 1 cause there might be the first subarray whose xor can gives us the value k
    count = 0
    xor=0
    for i in range(len(array)):
        xor^=array[i]
        if xor^k in m :
            count += m.get(xor^k)    
        m[xor] = m.get(xor,0) + 1  
    print(count) 
betterxork([4, 2, 2, 6, 4],6)  
#time complexity : O(N)
# space complexity : O(N) in worst case3
# 3

#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

#brute approach
def merging(array):
    array=sorted(array)
    ans = []
    for i in range(len(array)):
        start,end = array[i][0] , array[i][1]
        if ans and end<=ans[-1][1]:  #if the current i index scond postion or the current end is lesser than or equal to the end of the last element of ans , then we just continue with another iteration of i. 
            continue
        for j in range(i+1,len(array)):
            if array[j][0] <= array[i][1]:
                end = max(end,array[j][1])   #in this j loop what we are doing is comparing the first index number of the second array with the last index of the first array, make the necessry changes in the end index element. 
            else:
                break  #here we are breaking the loop if the condition doesnot meet because we sorted the array in an ascending order and if the first comparison doesnot meet then ofcourse the later condition also won't meet.    
        ans.append([start,end])
    print(ans)
merging([[5,7],[1,3],[4,6],[8,10]])
#time complexity : O(N^2)  because there are two nested loops
# space complexity : O(N) for the worst case because the answer might be very close to the number of N  

#betterapproach
def optimalmerging(array):
    array=sorted(array)
    ans=[array[0]]  #we are making the first array of the original array a comparing array at first
    for i in range(1,len(array)):
        if array[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1],array[i][1])
        else:
            ans.append(array[i])
    print(ans)
optimalmerging([[5,7],[1,3],[4,6],[8,10]])  
#time complexity : O(NlogN+N)
# space complexity : O(N) for worst case.

#Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
#Merge both the arrays into a single array sorted in non-decreasing order.
#The final sorted array should be stored inside the array nums1 and it should be done in-place.
# #nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
#nums2 has a length of n.
def mergetwosortedarrays(array1,array2,m,n):   #here m is the length of the first array1 and n is the length of the second array2
    left=right= 0
    ans = []
    while left <m and right<n:
        if array1[left] <=array2[right]:
            ans.append(array1[left])
            left+=1
        else:
            ans.append(array2[right])
            right+=1
    while left<m:
        ans.append(array1[left])
        left+=1 
    while right<n:
        ans.append(array2[right])
        right+=1  
    print(ans)
mergetwosortedarrays([-5, -2, 4, 5], [-3, 1, 8],4,3)      
#time complexity : O(N + M)
# space complexity : O(N + M)

#better approach
def bettermerging(array1,array2,m,n):
    left = len(array1) - 1   #here we are taking the last index of the first array1
    right = 0      
    while left>=0 and right < n:  #this loop is for making the two arrays array1 and array2 to have a specific numbers as array1 will have the first half of numbers and array2 will have the second half of nummbers.
        if array1[left] > array2[right]:
            array1[left],array2[right] = array2[right],array1[left]
            left-=1
            right+=1
        else:
            left-=1
            right+=1
    print(sorted(array1)+sorted(array2))
bettermerging([-5, -2, 4, 5], [-3, 1, 8],4,3)    
#time complexity : O(NlogN)
#space complexity : O(1)  which is constant.

#find the missing and repeating number from an array
def bruteapp(array):
    A=B=0
    for i in range(1,len(array)+1):
        count = 0
        for j in range(len(array)):
            if i == array[j]:
                count += 1
        if count == 2:
            A=i   #A is the repeating number
        elif count == 0:
            B=i    #B is the missing number
    print([A,B])
bruteapp([3, 5, 4, 1, 1])   
#time complexity : O(N^2)
# space complexity : O(1)

#better approach 
# in this better approach we will use hashmap
def betterapp(array):
    m= {}
    A=B=0
    for num in array:   #this first loop is for calculating the number of occurences of number of an array
        m[num] = m.get(num,0) + 1
    for i in range(1,len(array)+1):   #this loop is for calculating the number of occurences of number between the range of 1 and n which is the length of an array.
        if i not in m:  #and ofcourse if the count is 0 or no i is in m,then this i is the missing number.
            B=i
        elif m[i] == 2:   #else if this particular i occurs more than 1 times then it is the repeating number
            A=i 
    print([A,B]) 
betterapp([3, 5, 4, 1, 1])  
#time complexity : O(N)
# space complexity : O(N) in the worst case            


#optimal approach
#for the optimal appr(oach of finding the repeating number and the missing number , what we will do is use the mathematical equations.
def optimalapp(array,n):
   s = (n * (n+1)) // 2
   s2 = n*(n+1)*(2*n + 1) // 6
   s1 = 0
   s2n = 0
   for num in array:
       s1 +=num
       s2n+=num * num
   val1 = s - s1
   val2 = (s2 - s2n) // val1 
   x =  (val1 + val2) // 2
   y = x - val1 
   print([y,x]) 
   #here x is the missing number and y is the repeating number  
       
optimalapp([3, 5, 4, 1, 1],5)  
#time complexity : O(N)
# space complexity : O(1)


#counting the inversion where a[i] > a[j] as i < j 

def merge(array,low,mid,high):
    left = low
    right = mid + 1 
    tempo=[]
    count = 0
    while left<=mid and right<=high:
        if array[left] <=array[right]:
            tempo.append(array[left])   #this code is sorting the array in ascending order
            left+=1
        else:
            tempo.append(array[right])
            count+=mid - left + 1 #as the array is sorted in an ascending order , if the first preceding number in the left half is greater than the number in the right half then it is sure that
            right+=1
            # the rest of the numbers in the left half is also greater than the numbers in the right half
    while left<=mid:
        tempo.append(array[left])
        left+=1
    while right<=high:
        tempo.append(array[right])
        right+=1    
    array[low:high+1] = tempo
    return count        




def mergesort(array,low,high):
    mid =( low + high ) // 2
    if low >=high :
        return 0
    cl=mergesort(array,low,mid)  #we are splitting the left half of an array
    cr=mergesort(array,mid+1,high)    #we are splitting the right half of an array
    #then if the all of the splitted arrays are splitted into single element array then we just merge them which has its own function
    cm=merge(array,low,mid,high)
    return cl+cr+cm   #we are returning the count of left half ,right half and merging
a=[2, 3, 7, 1, 3, 5]
print(mergesort(a[:],0,len(a)-1))

#time complexity : O(NlogN)
#space compelxity : O(1)


def insertpos(array,k):
    left = 0
    right = len(array) - 1
    while left<=right:
        mid = (left + right) // 2 
        if array[mid] == k:
            return mid
        elif k>array[mid]:   #if the target number is way greater then we just make our range within the right half
            left=mid + 1
        else:
            right = mid - 1
    return left    #if the target number is not found then the destination  index will be left
print(insertpos( [1, 3, 5, 6],2))            


def practicesearch(array,x):
    left = 0
    right = len(array) - 1
    while left<=right:
        mid = (left + right) // 2  
        if array[mid] == x :
            return mid
        elif array[left]<array[mid]:   #here we are checking whethter the subarray before the index mid is sorted or not
            if array[left]<=x and x<=array[mid]:  #here we are checking whether the target number exists in this preceding sorted array or not
                right=mid - 1 #if the target number lies then we just move the right half into the left half
            else:
                left=mid + 1  #if it doesnot lie then of course it will lie in the right half
        else:
            if array[mid]<=x and x<=array[right]:   #then if the target number lies in the later sorted subarray which lies after index mid then
                left=mid + 1 #then we just move the left half into right
            else:
                right = mid - 1 
    #then this whole sequence keeps on repeating till we find the target number in the mid index
    return -1
print(practicesearch([4, 5, 6, 7, 0, 1, 2],3))                



#the question is asking us to find the number of rotation of the array consisting of the distinct numbers 
#and this array is also sorted in ascending order
#now to determine the number of rotations of an array
#waht we need to do is find the smallest number in an array and determine its index which will gives us the number of rotation of an array
def rotation(array):
    left = 0
    right = len(array) - 1
    mini=float('inf')
    while left<=right:
        mid = (left + right) // 2 
        if array[left] < array[mid]:    #here we are checking if the left most number is lesser than the mid indexed nnumber then of course the most smallest number in the subarray before the mid index will be the first number in an array
          if array[left]<mini:
              index = left       #as we need the index of the smallest number , we are retrieving the index here
          left  = mid + 1 #as we have already determined the smallest number from the left subarray now we move the left pointer towards the right half.
        elif array[mid]<array[right]: #now what if the right half is sorted
            #then of course the mid indexed number will be the smallest here in this right half 
            #then we check the current smallest with the last smallest numebr that we found out
            if array[mid]<mini:
                index=mid   #then if the current smallest number is smaller than the last one then of course we change the value of index also
            right=mid - 1  #as we already found out the smallest fromn the right half there is no point in dealing with this half now , so we move the right pointer to the left half    
    return index
print('The number of rotation in an array is :', rotation( [3, 4, 5, 1, 2]))
#time complexity : O(logN)
#space complexity : O(1)






def oneelem(array):
    ans = 0
    if len(array) == 1:  #if the length of an array is just one then the answer will be that single element
        ans = array[0]
        return ans
    elif array[0]!=array[1]:
        ans=array[0]
        return ans
    elif array[len(array)-1]!=array[len(array)-2]:
        ans=array[len(array)-1]
        return ans
    
    left = 1
    right = len(array)-2 
    while left<=right:
     mid = (left + right) // 2   
     if array[mid]!=array[mid-1] and array[mid]!=array[mid+1]:
         ans=array[mid]
         return ans
     elif mid % 2 == 0 and array[mid]==array[mid+1] or array[mid]==array[mid-1]:  #if the mid index is at even index and the next element from the mid is equal to the mid index then our
                #answer lies in the right half so , we move the left pointer to right half
           left=mid+1
     elif mid % 2!=0 and array[mid]==array[mid+1] or array[mid]==array[mid-1]:    #if the mid index is at odd index and the next elemnt is equal to the midindex element then 
                #our answer lies in the left half
                right=mid-1    
print(oneelem( [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))    
#time complexity : O(logN)
#space complexity : O(1)



#peak element
def peakeleme(array):
    ans=0
    if len(array)==1:
        ans=array[0]
        return ans
    elif array[0] > array[1]:
        ans=array[0]
        return ans
    elif array[len(array)-1]>array[len(array)-2]:
        ans=array[len(array)-1]
        return ans
    left = 1
    right = len(array) - 2
    while left<=right:
        mid = (left + right) // 2
        if array[mid]>array[mid-1] and array[mid]>array[mid+1]:
            ans=mid
            return ans
        elif array[mid]<array[mid+1]:   #else if the mid index number is smaller than the later number then of course the peak number is in the right half
            left=mid+1
        elif array[mid]>array[mid+1]:   #else if the mid index number is greater than the later number then of course the peak number lies in the left half
            right=mid-1    
print(peakeleme( [1, 2, 1, 3, 5, 6, 4]))            



#Find minimum in Rotated Sorted Array
def minimumro(array):
    left = 0
    right = len(array) - 1
    small=0
    while left<=right:
        mid = (left + right) // 2
        if array[left]<array[mid]:
            small=min(small,array[left])
            left=mid+1
        elif array[mid]<array[right]:
            small=min(small,array[mid])
            right=mid-1
    return small
print(minimumro([4, 5, 6, 7, 0, 1, 2, 3]))        
#time complexity : O(logN)
#space complexity : O(1)

#Find out how many times the array is rotated
def numberrotation(array):
    small = float('inf')
    ans=0
    if len(array)==1:
        ans = 0
        return ans
    left = 0
    right = len(array) -1
    while left<=right:
        mid = (left + right) // 2
        if array[left]<=array[mid]:
            if array[left]<small:
                small=array[left]
                ans=left
            left=mid+1
        elif array[mid]<=array[right]:
            if array[mid]<small:
                small=array[mid]
                ans=mid
            right=mid-1
    return ans
print('The number of rotation is:', numberrotation([3, 4, 5, 1, 2]))                    


#Search in rotated sorted array-I
def searchrotated(array,k):
    left = 0
    right = len(array) -1
    while left<=right:
        mid = (left + right) //2
        if array[mid] == k:
            return mid

        elif array[left]<=array[mid]:   #here we are checking if the left half of the array is sorted or not
            if array[left]<=k and k<=array[mid]:   #and then we are checking if the target number lies in the left sorted array, if yes then we destroy the right half.
                right=mid-1
            else:  #otherwise the target might exists in the right half, so we move the left pointer
                left = mid + 1    
        elif array[mid]<=array[right]:
            if array[mid]<=k and k<=array[right]:   
                left=mid+1
            else:
                right = mid - 1     
    return -1
print(searchrotated( [4, 5, 6, 7, 0, 1, 2],3))                

