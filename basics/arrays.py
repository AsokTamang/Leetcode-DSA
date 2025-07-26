# Given an array of integers nums, return the value of the largest element in the array
def maxelem(array):
    max = array[0]
    for i in range(len(array)):
        if max < array[i]:
            max = array[i]

    print(max)


maxelem([5, 4, 10, 2, 1])

# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


# better approach
# its time complexity will be O(N) and space complexity will also be O(2) which is constant
def secondLargest(array):
    largest = float(
        "-inf"
    )  # here we are just assigning the positive inf float value to the largest variable
    seclarge = float("-inf")  # same with the seclarge variable
    for i in range(len(array)):
        if array[i] > largest:
            largest = array[i]
    for i in range(len(array)):
        if array[i] > seclarge and (array[i] != largest or array[i] < largest):
            seclarge = array[i]
        elif array[i] > seclarge and array[i] > largest:
            largest = array[i]
            seclarge = largest
    print(largest)
    print(seclarge)


secondLargest([10, 11, 4, 2, 1, 11, 9])

# optimal approach


def seclrgest(array):
    largest = float("-inf")
    seclargests = float("-inf")
    for i in range(len(array)):
        if (
            array[i] > seclargests and array[i] > largest
        ):  # here when the i index array value is greater than seclargest and also greater than the largest
            seclargests = largest  # then ofcourse the largest will be the seclargest and the  array[i] will be the largest
            largest = array[i]

        elif array[i] > seclargests and (
            array[i] != largest or array[i] < largest
        ):  # and if the value is greater than the seclargest and is not equal to the largest or lesser than the largesst then
            seclargests = array[i]  # the sec largest will be the array[i] value
    print(largest)
    print(seclargests)


seclrgest([10, 11, 4, 2, 1, 11, 9])


def secondsmallest(array):
    smallest = float("inf")
    secsmallest = float("inf")
    for i in range(len(array)):
        if (
            array[i] < smallest and array[i] < secsmallest
        ):  # here if the indexed i array elem is lesser than both smallest and the secsmallest then of course the smallest will be array[i] and the second smallest will be the smallest
            secsmallest = smallest
            smallest = array[i]
        elif (array[i] > smallest or array[i] != smallest) and array[i] < secsmallest:
            secsmallest = array[
                i
            ]  # then if the array[i] element is greater than the smallest and smaller than the second smallest then ofcourse the second elem will change to the index array elem
    print(smallest)
    print(secsmallest)


secondsmallest([10, 11, 4, 2, 1, 11, 9])


# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


def sorting(array, n):

    for i in range(n):
        if array[i] > array[i + 1]:
            return False
        else:
            return True


print(sorting([9, 1, 6, 11, 7, 8], 6))

# Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.


# If the number of unique elements be k, then,#Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness.
def sorting2(array):
    storage = list(set(array))
    tempo = [0] * len(array)
    for i in range(len(tempo)):
        if i < len(storage):
            tempo[i] = storage[i]
        else:
            tempo[i] = "_"
    print(tempo[0:])


sorting2([0, 0, 3, 3, 5, 6])


# Given an integer array nums, rotate the array to the left by one.
def rotatearray(array, n):
    first = array[0]
    for i in range(n):
        if i == n - 1:
            array[i] = first
        else:
            array[i] = array[i + 1]
    print(array)


rotatearray([10, 0, 3, 3, 5, 6], 6)


def rotatentimes(array, n):
    for i in range(n):
        first = array[0]
        for j in range(len(array)):
            if j == len(array) - 1:
                array[j] = first
            else:
                array[j] = array[j + 1]
        print(array)


rotatentimes([10, 0, 3, 3, 5, 6], 2)


# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same. This must be done in place, without making a copy of the array.
def movezeros(array):
    j = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[j] = array[j], array[i]
            j += 1
    print(array)


movezeros([10, 0, 3, 3, 5, 6])


# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1


def findnum(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


print(findnum([10, 0, 3, 3, 5, 6], 3))


# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.


def sum(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = [num for num in array[1:] if num < pivot]
    right = [num for num in array[1:] if num >= pivot]
    return sum(left) + [pivot] + sum(right)


def union(array1, array2):
    tempo = list(set(array1 + array2))
    print(sum(tempo))


(union([1, 2, 3, 4, 5], [1, 2, 7]))


# next solution of union of two sorted arrays
def union2(array1, array2):
    i = 0
    j = 0
    l1 = len(array1) - 1
    l2 = len(array2) - 1
    tempo = []
    while (
        i <= l1 and j <= l2
    ):  # here we are using the two pointers method to append the smaller value in the tempo var by comparing the value between the two arrays
        if array1[i] < array2[j]:
            if len(tempo) == 0 or tempo[-1] != array1[i]:
                tempo.append(array1[i])
            i += 1
        else:
            if len(tempo) == 0 or tempo[-1] != array2[j]:
                tempo.append(array2[j])
            j += 1
    while i <= l1:

        if len(tempo) == 0 or tempo[-1] != array1[i]:
            tempo.append(array1[i])
        i += 1
    while j <= l2:

        if len(tempo) == 0 or tempo[-1] != array2[j]:
            tempo.append(array2[j])
        j += 1
    print(tempo)


union2([1, 2, 3, 4, 5], [1, 2, 7])


# Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.


def findmiss(array, n):
    for i in range(n + 1):
        if i not in array:
            print(i)


findmiss([0, 5, 3, 1, 4], 5)

# Given a binary array nums, return the maximum number of consecutive 1s in the array.


def findconsecutive(array):
    count = 0
    maximum = 0
    for i in range(len(array)):
        if array[i] == 1:
            count += 1  # for every found of element 1 , we increase the count by 1
        else:
            count = 0
        maximum = max(
            count, maximum
        )  # then for every loop we calculate the maximum even if the count is 0 or greater than 0
    print("The maximum consecutives of 1 is:", maximum)


findconsecutive([1, 1, 0, 0, 1, 1, 1, 0])


# Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.
def findonce(array, n):  # here n is the length of an array
    tempo = [0] * (
        max(array) + 1
    )  # as for the hass map the length of an array must be greater than 1 value of the maximum digit in an array
    for i in range(n):
        tempo[array[i]] += 1
    for j in range(len(tempo)):
        if tempo[j] == 1:
            print(j)


findonce([1, 2, 3, 4, 3, 1, 4], 7)


# but the most optimal method to find the number which appears only one time in an array can be found using xor cause xor means the a ^ a is 0 but 0 ^ a is a so if we use xor for every numbers in an array only the number left will be the number which appears only one time in an array
def optimalonce(array):
    x = 0
    for num in array:
        x ^= num  # this code will run xor or ^ for every numbers in an array
    print("The number in an array which appears only one time in an array is:", x)


optimalonce([1, 2, 3, 4, 3, 1, 4])


# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
def summing(
    array, n, k
):  # here n is the length of an array and k is the target element
    s = 0
    sub_Array = []
    for i in range(n):
        if (
            array[i] <= k / 2 and s < k
        ):  # here to find the longest subarrays we need to have more nums inside a subarray so for that the numbers inside this subarray must be certainly very low compared with the target value
            s += array[i]
            sub_Array.append(array[i])
    if s == k:
        print(sub_Array)
        print(len(sub_Array))
    else:
        print(0)


summing([10, 5, 2, 7, 1, 9], 6, 15)


# sliding window approach
def slider(array, k):
    left = 0
    subarray = []
    max_len = 0
    s = 0
    for right in range(
        len(array)
    ):  # this right goes through every elements in an array.

        s += array[right]

        if (
            s > k
        ):  # but if the sum is too big then we subtract the sum with the arrays left most element and we move the left pointer towards right
            s -= array[left]
            left += 1
            max_len = (
                right - left + 1
            )  # here we are calculating the length of a subarray as suppose when the window's length is decreased
        elif s == k:
            if (
                right - left + 1 > max_len
            ):  # and if the sum is equal to the target element and the valeu of current lenght which is right - left +1 is greater than the previous max lenght then we assign the current one to the max length
                subarray = array[
                    left : right + 1
                ]  # so that the new sub array becomes the array from array[left:right+1]
                max_len = right - left + 1

    if (
        max_len > 0
    ):  # and ofcourse if the final max_length is greater than 0 we print the maximum length as well as the subarray otherwise we print 0
        print(max_len)
        print(subarray)
    else:
        print(0)


slider([10, 5, 2, 7, 1, 9], 15)


# brute approach
def bruteapp(array, k):
    max_len = 0

    subarray = []

    for i in range(len(array)):
        s = 0
        for j in range(i, len(array)):
            s += array[j]
            if (
                s == k and j - i + 1 > max_len
            ):  # we will check the sum for every possible sub arrays and if the sum is equal to k and the length is greater than the maximum length then we take that specific max lenght and that sub array
                max_len = j - i + 1
                subarray = array[i : j + 1]

    print(subarray)
    print(max_len)


bruteapp([10, 5, 2, 7, 1, 9], 15)


# better approach
def betterapp(array, k):
    s = 0
    j = 0
    length = 0  # this calculates the length  of an array
    for i in range(len(array)):
        s += array[i]
        if s > k:
            s -= array[j]
            j += 1

        elif s == k and i - j + 1 > length:
            length = i - j + 1
            subarray = array[j : i + 1]  # this calculates the subarray

    print(subarray)
    print(length)


betterapp([10, 5, 2, 7, 1, 9], 15)
# so for the optimal approach to find the target element from the longest subarrays, what we can do is use the dictionary and store the prefix sum of all the subarrays with the corresponding index and if we ever find the prefix sum at any index which is  the value that we can get by subtracting a k from it in a map then we find the maximum length
# by comparing its curreent index with the index at that specific index in a map or dict then we keep on running this loop till we hit the next maximum length.


def betterapproach(array, k):
    s = 0  # this variable stores the sum of all the possible subarrays
    m = {}  # this variable stores the prefix sums and its corresponding indexes

    length = 0
    for i in range(len(array)):
        s += array[i]

        if s == k:
            length = (
                i + 1
            )  # as the loop is starting from 0 the length is ofcourse index+1
        if s not in m:
            m[s] = i  # we are storing the sum as a key and the current index as a value

        if (
            s - k in m
        ):  # in any possible cases if we ever find the number which can give us the value of k by subtracting this particluar number inside our map which is the collection of the prefix sums then we calcualte the lenght here
            length = max(length, i - m[s - k])
            subarrays = array[i - m[s - k] : i + 1]
    print(length)
    if length > 0:
        print(length)
        print(subarrays)


betterapproach([1, -1, 5, -2, 3], 3)


# Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.
def twosum(array, k):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == k:
                return [i, j]


print(twosum([1, 3, 5, -7, 6, -3], 0))


# better approach
def bettwosum(array, k):
    m = {}
    for i in range(len(array)):
        if array[i] not in m:
            m[array[i]] = (
                i  # we are storing the number as the key and the index as the value of the key
            )
        if (
            array[i] - k in m
        ):  # here we are checking if the required number which adds to the current indexed value to get k is stored in our dict as key or not.
            return (
                i,
                m[array[i] - k],
            )  # if yes then we return the current index and that particular index


bettwosum([1, 3, 5, -7, 6, -3], 0)


# optimal approach
def optitwosum(array, k):
    sa = [(num, index) for index, num in enumerate(array)]
    sortedarray = sorted(
        sa
    )  # while sorting the list consiting of tuples sorted will automatically sort the list based on the first value inside a tuple of the list
    # here we are sorting the array first in an ascending order
    left = 0  # this is the lefthand side pointer which starts at the 0 index
    right = (
        len(array) - 1
    )  # this is the right hand side pointer which starts at the end of the array
    s = 0
    while left < right:
        s = sortedarray[left][0] + sortedarray[right][0]
        if s == k:
            return sorted([sortedarray[left][1], sortedarray[right][1]])
        elif (
            s < k
        ):  # if the sum is smaller than k then we move the left pointer towards the right direction or greater indexed value
            left += 1
        elif (
            s > k
        ):  # if the sum is greater than k then we move the left pointer towards the right direction or greater indexed value
            right -= 1
        else:
            return 0


print(optitwosum([1, 3, 5, -7, 6, -3], 0))


# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
# betterapproach
def bettersort(array):
    count0 = 0
    count1 = 0
    count2 = 0
    for num in array:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        elif num == 2:
            count2 += 1
    for i in range(
        count0
    ):  # for the range of count0 excluding the count0 index , it fills with the number 0
        array[i] = 0
    for i in range(
        count0, count0 + count1
    ):  # as the part of index before count0 index is already passed so we add the index of count1 to count0 to fill with 1s
        array[i] = 1
    for i in range(
        count0 + count1, len(array)
    ):  # as the part of index just before the sum of  both count 0 and count 1 is already passed or used then we start from that sum to the length of an array
        array[i] = 2
    print(array)


bettersort([1, 0, 2, 1, 0])


# better approach
def sorting01(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    left = [num for num in array[1:] if num < pivot]
    right = [num for num in array[1:] if num >= pivot]
    return sorting01(left) + [pivot] + sorting01(right)  # recursion


print(sorting01([1, 0, 2, 1, 0]))


# optimal approach or known as dutch national flag algorithm
def dutchalgo(array):
    high = (
        len(array) - 1
    )  # as the high is the last index in an array so we are doing this
    low = 0
    mid = 0  # in dutch algo mid to high is the part where the unsorted algo sits. so , as the whole given array is unsorted , we are setting the mid to 0
    while (
        mid <= high
    ):  # in dutch algo if the mid overlaps the high then it is garaunted that the whole array is sorted
        if array[mid] == 0:
            array[low], array[mid] = (
                array[mid],
                array[low],
            )  # then we swap the low index with the mid index
            mid += 1  # then we move the comparing pointer towards inclination
            low += 1  # as the most left part is already sorted cause it only consists of series of 0
        elif array[mid] == 1:
            mid += 1  # as the series from low+1 to mid consists of only the series of 1 so if the current indexed value is 1 then we decrease the range from mid+1
        elif array[mid] == 2:
            array[mid], array[high] = (
                array[high],
                array[mid],
            )  # if the current index number is 2 then we push it to the end of an array as the extreme right only consists of 2
            high -= 1  # as the extreme right already consists of 2 after swapping so it is already sorted so thats why we are decreasing the range of mid+1 to high
    print(array)


dutchalgo([1, 0, 0, 2, 2, 1, 1, 0])


# Given an integer array nums of size n, return the majority element of the array.
# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

#brute approach 1
def brutemajority(array,n):      
    for i in range(n):   #n is the length of an array
        count = 0
        for j in range(i,n):
            if array[i] == array[j]:
                count+=1
        if count > n//2:
            print(array[i])
            return
        else:
            continue
    print('No such majority element')    
brutemajority([7, 0, 0, 1, 7, 7, 2, 7, 7], 9)    
#timecomplexity: O(N^2)
#spacecomplexity: O(1)
                    





# brute approach2
def majority(array, n):
    tempo = [0] * (
        max(array) + 1
    )  # here we are making a temporary array with all elements of 0 upto the lenght of just one value greater than the maximum value in an array
    for i in range(len(array)):
        tempo[
            array[i]
        ] += 1  # this counts the total number of appearance of a number of an array but using temporary array
    for i in range(len(tempo)):
        if (
            tempo[i] > n // 2
        ):  # then we are comparing each  of tempo with the half of length of an array
            print(
                i
            )  # and as the index is the actual value of an array in a tempo we are printing the index when we find the number
            return
    print("no such majority numbers")


majority([7, 0, 0, 1, 7, 7, 2, 7, 7], 9)

# timecomplexity:  O(N+M)
# spacecomplexity: O(M)


# better approach
def bettermajority(array, n):
    m = {}
    for i in range(len(array)):
        if array[i] not in m:
            m[array[i]] = 1
        else:
            m[array[i]] += 1
    for key, value in m.items():
        if value > n // 2:
            print(key)   #as the key is the actual denotion of a number so thats why we are printing the key
            return
    print("no such majority numbers")
#timecomplexity: O(N)
#spacecomplexity: O(N)
bettermajority([7, 0, 0, 1, 7, 7, 2, 7, 7], 9)


#optimal approach for finding the element which has a majority occurence in an array.
#Moore's voting algorithm
#in this algorithm what we do is we make the count to 1, as  we take a number from an array and consider it as an element then if the next element is the same numebr then we increase the value of count .
#if the next element is the different number then we decrease the count by 1.
#while doing so , if in any case the count becomes 0, then we change the element which means we take the next number as an element and repeat the process, then we get the last man standing number as an element.
#then for that particular number we must count its occurence in an array cause in some cases its occurence might be lesser than n//2.
def optimalmajority(array,n):
    element = 0
    count = 0    
    #this first loop gives us the number which is the potential majority element 
    for i in range(n):
        if count == 0:
            count = 1 
            element = array[i]
        elif array[i] == element:
            count+=1
        else:
            count-=1        
    


    count2=0
    for i in range(n):
        if array[i] == element:
            count2+=1
    if count2 > n//2:
        print(element)
    else:
        print(-1)    

optimalmajority([7, 0, 0, 1, 7, 7, 2, 7, 7], 9)   
       