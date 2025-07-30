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


    
