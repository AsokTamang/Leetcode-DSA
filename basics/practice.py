import math
import heapq
from collections import defaultdict


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
def optimalapproach(array, index, ans):
    if index == len(array) - 1:
        ans.append(array[:])
        return
    for i in range(index, len(array)):
        array[index], array[i] = array[i], array[index]
        optimalapproach(array, index + 1, ans)
        array[index], array[i] = array[i], array[index]


ans = []
optimalapproach([1, 2, 3], 0, ans)
print(ans)


# permutation
def permutation(array, index, ans):
    if index == len(array) - 1:
        ans.append(array[:])
        return
    for i in range(index, len(array)):
        array[index], array[i] = array[i], array[index]
        permutation(array, index + 1, ans)
        array[index], array[i] = array[i], array[index]


ans = []
permutation([1, 2, 3], 0, ans)
print(ans)


# longest consecutive number
def linearsearch(array, num):
    for i in range(len(array)):
        if array[i] == num:
            return True
    return False


def consec(array):
    length = 1
    for i in range(len(array)):
        x = array[i]
        count = 1  # for every value of x we make the count to 1
        while linearsearch(
            array, x + 1
        ):  # then for every value of x we are trying to find x+1 using linear search function
            # if found we increase the count by 1
            x += 1
            count += 1
        length = max(length, count)
    print(length)


consec([5, 4, 3, 2, 1, 100, 200, 101, 201])


# n is the number of rows and m is the number of columns
# or n is the number of elements in an outer array while m is the number of elements in an inner arrays
def matrixzero(array, n, m):
    rows = [
        0
    ] * n  # here we are making the zero matrices called rows having n number of elements
    cols = [0] * m  # same with this one but with m number of elements
    # we are running the loop below to find the index on both row based as well as column based to make its corresponding elements 0
    for i in range(n):  # looping through outer loop or outer array
        for j in range(m):  # looping through inner loop
            if (
                array[i][j] == 0
            ):  # here we are checking for each and every element inside the matrix that if they are equal to 0 or not
                # if yes then
                rows[i] = 1
                cols[j] = (
                    1  # then we find that particular index from row based index as well as column based index
                )
    for i in range(n):
        for j in range(m):
            if rows[i] == 1 or cols[j] == 1:
                array[i][j] = 0
    print(array)


matrixzero([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 3, 3)


def optimalapproach(
    array, n, m
):  # here n is the number of rows and m is the number of columns
    first_row_haszero = False
    first_col_haszero = False

    for j in range(m):
        if array[0][j] == 0:
            first_row_haszero = True
    for i in range(n):
        if array[i][0] == 0:
            first_col_haszero = True
    # then we make a mark in the first row and first column  based on the zero element which lies inside the matrix
    for i in range(1, n):
        for j in range(1, m):
            if array[i][j] == 0:
                array[0][j] = 0
                array[i][0] = 0
    # then based on the marker on the first row or first column, we start making elements zero in the inside matrix
    for i in range(1, n):
        for j in range(1, m):
            if array[i][0] == 0 or array[0][j] == 0:
                array[i][j] = 0

    # then based on the first row and first column, we start making its other elements 0l

    if first_col_haszero:
        for i in range(n):
            array[i][0] = 0

    if first_row_haszero:
        for j in range(m):
            array[0][j] = 0
    print(array)


optimalapproach([[1, 0, 1], [0, 1, 1], [1, 1, 0]], 3, 3)


outer = []
n = 3
for i in range(n):
    outer.append([0] * 3)
print(outer)


def rotatematrrix(array, n, m):
    outer = []
    for i in range(n):
        outer.append([0] * m)

    for i in range(n):
        k = 2
        for j in range(m):
            outer[i][j] = array[k][i]
            k -= 1
    print(outer)


rotatematrrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
# time complexity: O(N*M)
# space complexity: O(N*M)


def betterapproach(array, k):
    m = {
        0: 1
    }  # and here we are using the first prefix sum of 0 with repition 1 cause there might be a case where the first continuous subarray gives us the result k
    count = 0
    s = 0
    for num in array:
        s += num
        if s - k in m:
            count += (
                m.get(s - k, 0) + 1
            )  # what we are doing is finding the number of subarrays until the current index which  has a sum of s-k because those subarray's gives the target k
        m.get(s, 0) + 1
    print(count)


betterapproach([1, 1, 1], 2)
# timecomplexity is : O(N)
# spacecomplexity is : O(N) for worst case if all the subarrays give the target k


def practice(r, c):  # r is the number of rows and c is the number of columns
    res = 1
    for i in range(1, c + 1):
        print(res, end=" ")
        res = (res * (c - i)) // i


practice(5, 5)


# brute approach
def majorityeleme(array, n):
    s = []
    for i in range(len(array)):
        if (
            array[i] in s
        ):  # if the majority element is already in the list then we just continue or move into the another loop or another value of i
            continue
        count = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
        if count > n / 3:
            s.append(array[i])
    print(s)


majorityeleme([1, 2, 1, 1, 3, 2, 2], 7)
# timecomplexity is O(N^2) as we are using the two nested loops
# space complexity is O(1) which is constant


# better approach
def betterapproach(array, n):
    m = {}
    ans = []
    for num in array:
        m[num] = m.get(num, 0) + 1  # here the default value of the key in m is 0
    for key, value in m.items():
        if value > n / 3:
            ans.append(key)
    print(ans)


betterapproach([1, 2, 1, 1, 3, 2, 2], 7)
# time complexity is : O(N) + O(M)
# space complexity is : O(M)


# optimal approach
# for the optimal approach what we do is use booyer's algorithm which is based on the last man standing
# as the question is asking to find the numbers which appear more than n/3 times where n is the length of an array. so , there must be or there is higher chance that alteast 2 elements satisy this condition
def optimalapproach(array, n):
    count1 = 0
    count2 = 0
    can1 = 0
    can2 = 0
    for num in array:
        if num == can1:
            count1 += 1
        elif num == can2:
            count2 += 1
        elif count1 == 0:
            count1 = 1
            can1 = num
        elif count2 == 0:
            count2 += 1
            can2 = num
        else:
            count1 -= 1
            count2 -= 1
    print([can1, can2])


optimalapproach([1, 2, 1, 1, 3, 2, 2], 7)
# time complexity is : O(N)
# spacecomplexity is :O(1)  which is constant


# Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
def var1(r, c):  # here r is the row position and c is the column postion
    res = 1
    for i in range(c):
        res = (res * (r - i)) / (c - i)
    print(int(res))


var1(5, 2)
# time complexity is : O(N)
# space complexity is : O(1)


# Given the row number n. Print the n-th row of Pascal’s triangle.
def var2(
    n,
):  # here n is the rowth number and the question is asking us to print all the elements of n
    res = 1
    for i in range(n + 1):
        print(res, end=" ")
        res = res * (n - i)
        res = res // (i + 1)
    print()


var2(5)
# timecomplexity : O(N+1)  or O(N) here N is the row number
# spacecomplexity : O(1)


# var3 Given the number of rows n. Print the first n rows of Pascal’s triangle.
def var3(n):  # here instead of printing the nth row we are printing the first n rows

    for i in range(n):
        res = 1
        for j in range(
            i
        ):  # here i acts as the rowth number and j acts as the number of columns
            print(res, end=" ")
            res = res * (i - j)
            res = res // (j + 1)
        print(res)


var3(5)
# time complexity : O(N^2)
# space complexity : O(1)


# brute approach
def brutetriplet(array):
    a = set()
    # here we are using set so that there wont be duplicate triplets
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == 0:
                    a.add(tuple(sorted([array[i], array[j], array[k]])))
    print(list(a))


brutetriplet([2, -2, 0, 3, -3, 5])
# time complexity O(N^3)
# space complexity O(1) or O(N) in worst case


# better approach for which we use hash map or dictionary
def betterapproach(array):

    a = set()
    for i in range(len(array)):
        m = (
            {}
        )  # we must include the m inside the for loop of i as for every value of i , there must be new hasmap so it wont repeat the previously used elements
        for j in range(i + 1, len(array)):
            thirdelem = -(array[i] + array[j])
            if thirdelem in m:
                a.add(tuple(sorted([array[i], array[j], thirdelem])))
            m[array[j]] = (
                m.get(array[j], 0) + 1
            )  # here if the array j exist we increase by one otherwise the initial value will become 1
    print(list(a))


betterapproach([2, -2, 0, 3, -3, 5])
# time complexity : O(N^2)
# space complexity :  O(k) where k is the number of unique triplets as we are using the dictionary


# optimal approach where we use two pointers
def optimaltriplet(array):
    s = set()
    array = sorted(array)
    for i in range(len(array)):
        if (
            i > 0 and array[i] == array[i - 1]
        ):  # if the next i indexed number is equal to the previous one then we just go with the next iteration of i
            continue
        left = i + 1
        right = len(array) - 1

        while left < right:
            total = array[i] + array[left] + array[right]
            if total == 0:
                s.add(tuple([array[i], array[left], array[right]]))
                left += 1
                right -= 1
                while array[left] == array[left - 1]:
                    left += 1
                while array[right] == array[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
                while array[left] == array[left - 1]:
                    left += 1

            elif total > 0:
                right -= 1
                while array[right] == array[right + 1]:
                    right -= 1

    print(list(s))


optimaltriplet([2, -2, 0, 3, -3, 5])
# time complexity : O(N)
# space complexity :  O(1)


def bettersubarray(array, n):
    s = 0
    m = {}
    length = 0
    for i in range(n):
        s += array[i]
        if s == 0:
            length = max(length, i + 1)  # here we are coding i+1 as the i starts from 0
        elif (
            s in m
        ):  # if the sum is not zero but the same sum is seen previously or in the previous subarray then we calculate the subtraction of current index where we get this common sum and the index where we saw this common sum, as
            # this subtraction gives us the length of the subarray which gives us the sum 0
            length = max(length, i - m[s])
        else:
            m[s] = i  # we are storing the index
    print(length)


bettersubarray([15, -2, 2, -8, 1, 7, 10, 23], 8)


# Given an array of integers nums and an integer k, return the total number of subarrays whose XOR equals to k.


def xork(array, k):
    count = 0
    ans = []
    for i in range(len(array)):
        xor = 0
        for j in range(i, len(array)):
            xor ^= array[j]
            if xor == k:
                count += 1
                ans.append(array[i : j + 1])
    print("The count is :", count)
    print(ans)


xork([4, 2, 2, 6, 4], 6)
# time complexity : O(N^2)
# space complexity : O(1)


# better approach
def betterxork(array, k):
    m = {
        0: 1
    }  # here we are making the base case of 0 whose count is 1 cause there might be the first subarray whose xor can gives us the value k
    count = 0
    xor = 0
    for i in range(len(array)):
        xor ^= array[i]
        if xor ^ k in m:
            count += m.get(xor ^ k)
        m[xor] = m.get(xor, 0) + 1
    print(count)


betterxork([4, 2, 2, 6, 4], 6)
# time complexity : O(N)
# space complexity : O(N) in worst case3
# 3

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.


# brute approach
def merging(array):
    array = sorted(array)
    ans = []
    for i in range(len(array)):
        start, end = array[i][0], array[i][1]
        if (
            ans and end <= ans[-1][1]
        ):  # if the current i index scond postion or the current end is lesser than or equal to the end of the last element of ans , then we just continue with another iteration of i.
            continue
        for j in range(i + 1, len(array)):
            if array[j][0] <= array[i][1]:
                end = max(
                    end, array[j][1]
                )  # in this j loop what we are doing is comparing the first index number of the second array with the last index of the first array, make the necessry changes in the end index element.
            else:
                break  # here we are breaking the loop if the condition doesnot meet because we sorted the array in an ascending order and if the first comparison doesnot meet then ofcourse the later condition also won't meet.
        ans.append([start, end])
    print(ans)


merging([[5, 7], [1, 3], [4, 6], [8, 10]])
# time complexity : O(N^2)  because there are two nested loops
# space complexity : O(N) for the worst case because the answer might be very close to the number of N


# betterapproach
def optimalmerging(array):
    array = sorted(array)
    ans = [
        array[0]
    ]  # we are making the first array of the original array a comparing array at first
    for i in range(1, len(array)):
        if array[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], array[i][1])
        else:
            ans.append(array[i])
    print(ans)


optimalmerging([[5, 7], [1, 3], [4, 6], [8, 10]])
# time complexity : O(NlogN+N)
# space complexity : O(N) for worst case.


# Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
# Merge both the arrays into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1 and it should be done in-place.
# #nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
# nums2 has a length of n.
def mergetwosortedarrays(
    array1, array2, m, n
):  # here m is the length of the first array1 and n is the length of the second array2
    left = right = 0
    ans = []
    while left < m and right < n:
        if array1[left] <= array2[right]:
            ans.append(array1[left])
            left += 1
        else:
            ans.append(array2[right])
            right += 1
    while left < m:
        ans.append(array1[left])
        left += 1
    while right < n:
        ans.append(array2[right])
        right += 1
    print(ans)


mergetwosortedarrays([-5, -2, 4, 5], [-3, 1, 8], 4, 3)
# time complexity : O(N + M)
# space complexity : O(N + M)


# better approach
def bettermerging(array1, array2, m, n):
    left = len(array1) - 1  # here we are taking the last index of the first array1
    right = 0
    while (
        left >= 0 and right < n
    ):  # this loop is for making the two arrays array1 and array2 to have a specific numbers as array1 will have the first half of numbers and array2 will have the second half of nummbers.
        if array1[left] > array2[right]:
            array1[left], array2[right] = array2[right], array1[left]
            left -= 1
            right += 1
        else:
            left -= 1
            right += 1
    print(sorted(array1) + sorted(array2))


bettermerging([-5, -2, 4, 5], [-3, 1, 8], 4, 3)
# time complexity : O(NlogN)
# space complexity : O(1)  which is constant.


# find the missing and repeating number from an array
def bruteapp(array):
    A = B = 0
    for i in range(1, len(array) + 1):
        count = 0
        for j in range(len(array)):
            if i == array[j]:
                count += 1
        if count == 2:
            A = i  # A is the repeating number
        elif count == 0:
            B = i  # B is the missing number
    print([A, B])


bruteapp([3, 5, 4, 1, 1])
# time complexity : O(N^2)
# space complexity : O(1)


# better approach
# in this better approach we will use hashmap
def betterapp(array):
    m = {}
    A = B = 0
    for (
        num
    ) in (
        array
    ):  # this first loop is for calculating the number of occurences of number of an array
        m[num] = m.get(num, 0) + 1
    for i in range(
        1, len(array) + 1
    ):  # this loop is for calculating the number of occurences of number between the range of 1 and n which is the length of an array.
        if (
            i not in m
        ):  # and ofcourse if the count is 0 or no i is in m,then this i is the missing number.
            B = i
        elif (
            m[i] == 2
        ):  # else if this particular i occurs more than 1 times then it is the repeating number
            A = i
    print([A, B])


betterapp([3, 5, 4, 1, 1])
# time complexity : O(N)
# space complexity : O(N) in the worst case


# optimal approach
# for the optimal appr(oach of finding the repeating number and the missing number , what we will do is use the mathematical equations.
def optimalapp(array, n):
    s = (n * (n + 1)) // 2
    s2 = n * (n + 1) * (2 * n + 1) // 6
    s1 = 0
    s2n = 0
    for num in array:
        s1 += num
        s2n += num * num
    val1 = s - s1
    val2 = (s2 - s2n) // val1
    x = (val1 + val2) // 2
    y = x - val1
    print([y, x])
    # here x is the missing number and y is the repeating number


optimalapp([3, 5, 4, 1, 1], 5)
# time complexity : O(N)
# space complexity : O(1)


# counting the inversion where a[i] > a[j] as i < j


def merge(array, low, mid, high):
    left = low
    right = mid + 1
    tempo = []
    count = 0
    while left <= mid and right <= high:
        if array[left] <= array[right]:
            tempo.append(
                array[left]
            )  # this code is sorting the array in ascending order
            left += 1
        else:
            tempo.append(array[right])
            count += (
                mid - left + 1
            )  # as the array is sorted in an ascending order , if the first preceding number in the left half is greater than the number in the right half then it is sure that
            right += 1
            # the rest of the numbers in the left half is also greater than the numbers in the right half
    while left <= mid:
        tempo.append(array[left])
        left += 1
    while right <= high:
        tempo.append(array[right])
        right += 1
    array[low : high + 1] = tempo
    return count


def mergesort(array, low, high):
    mid = (low + high) // 2
    if low >= high:
        return 0
    cl = mergesort(array, low, mid)  # we are splitting the left half of an array
    cr = mergesort(array, mid + 1, high)  # we are splitting the right half of an array
    # then if the all of the splitted arrays are splitted into single element array then we just merge them which has its own function
    cm = merge(array, low, mid, high)
    return (
        cl + cr + cm
    )  # we are returning the count of left half ,right half and merging


a = [2, 3, 7, 1, 3, 5]
print(mergesort(a[:], 0, len(a) - 1))

# time complexity : O(NlogN)
# space compelxity : O(1)


def insertpos(array, k):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == k:
            return mid
        elif (
            k > array[mid]
        ):  # if the target number is way greater then we just make our range within the right half
            left = mid + 1
        else:
            right = mid - 1
    return left  # if the target number is not found then the destination  index will be left


print(insertpos([1, 3, 5, 6], 2))


def practicesearch(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif (
            array[left] < array[mid]
        ):  # here we are checking whethter the subarray before the index mid is sorted or not
            if (
                array[left] <= x and x <= array[mid]
            ):  # here we are checking whether the target number exists in this preceding sorted array or not
                right = (
                    mid - 1
                )  # if the target number lies then we just move the right half into the left half
            else:
                left = (
                    mid + 1
                )  # if it doesnot lie then of course it will lie in the right half
        else:
            if (
                array[mid] <= x and x <= array[right]
            ):  # then if the target number lies in the later sorted subarray which lies after index mid then
                left = mid + 1  # then we just move the left half into right
            else:
                right = mid - 1
    # then this whole sequence keeps on repeating till we find the target number in the mid index
    return -1


print(practicesearch([4, 5, 6, 7, 0, 1, 2], 3))


# the question is asking us to find the number of rotation of the array consisting of the distinct numbers
# and this array is also sorted in ascending order
# now to determine the number of rotations of an array
# waht we need to do is find the smallest number in an array and determine its index which will gives us the number of rotation of an array
def rotation(array):
    left = 0
    right = len(array) - 1
    mini = float("inf")
    while left <= right:
        mid = (left + right) // 2
        if (
            array[left] < array[mid]
        ):  # here we are checking if the left most number is lesser than the mid indexed nnumber then of course the most smallest number in the subarray before the mid index will be the first number in an array
            if array[left] < mini:
                index = left  # as we need the index of the smallest number , we are retrieving the index here
            left = (
                mid + 1
            )  # as we have already determined the smallest number from the left subarray now we move the left pointer towards the right half.
        elif array[mid] < array[right]:  # now what if the right half is sorted
            # then of course the mid indexed number will be the smallest here in this right half
            # then we check the current smallest with the last smallest numebr that we found out
            if array[mid] < mini:
                index = mid  # then if the current smallest number is smaller than the last one then of course we change the value of index also
            right = (
                mid - 1
            )  # as we already found out the smallest fromn the right half there is no point in dealing with this half now , so we move the right pointer to the left half
    return index


print("The number of rotation in an array is :", rotation([3, 4, 5, 1, 2]))
# time complexity : O(logN)
# space complexity : O(1)


def oneelem(array):
    ans = 0
    if (
        len(array) == 1
    ):  # if the length of an array is just one then the answer will be that single element
        ans = array[0]
        return ans
    elif array[0] != array[1]:
        ans = array[0]
        return ans
    elif array[len(array) - 1] != array[len(array) - 2]:
        ans = array[len(array) - 1]
        return ans

    left = 1
    right = len(array) - 2
    while left <= right:
        mid = (left + right) // 2
        if array[mid] != array[mid - 1] and array[mid] != array[mid + 1]:
            ans = array[mid]
            return ans
        elif (
            mid % 2 == 0
            and array[mid] == array[mid + 1]
            or array[mid] == array[mid - 1]
        ):  # if the mid index is at even index and the next element from the mid is equal to the mid index then our
            # answer lies in the right half so , we move the left pointer to right half
            left = mid + 1
        elif (
            mid % 2 != 0
            and array[mid] == array[mid + 1]
            or array[mid] == array[mid - 1]
        ):  # if the mid index is at odd index and the next elemnt is equal to the midindex element then
            # our answer lies in the left half
            right = mid - 1


print(oneelem([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
# time complexity : O(logN)
# space complexity : O(1)


# peak element
def peakeleme(array):
    ans = 0
    if len(array) == 1:
        ans = array[0]
        return ans
    elif array[0] > array[1]:
        ans = array[0]
        return ans
    elif array[len(array) - 1] > array[len(array) - 2]:
        ans = array[len(array) - 1]
        return ans
    left = 1
    right = len(array) - 2
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
            ans = mid
            return ans
        elif (
            array[mid] < array[mid + 1]
        ):  # else if the mid index number is smaller than the later number then of course the peak number is in the right half
            left = mid + 1
        elif (
            array[mid] > array[mid + 1]
        ):  # else if the mid index number is greater than the later number then of course the peak number lies in the left half
            right = mid - 1


print(peakeleme([1, 2, 1, 3, 5, 6, 4]))


# Find minimum in Rotated Sorted Array
def minimumro(array):
    left = 0
    right = len(array) - 1
    small = 0
    while left <= right:
        mid = (left + right) // 2
        if array[left] < array[mid]:
            small = min(small, array[left])
            left = mid + 1
        elif array[mid] < array[right]:
            small = min(small, array[mid])
            right = mid - 1
    return small


print(minimumro([4, 5, 6, 7, 0, 1, 2, 3]))
# time complexity : O(logN)
# space complexity : O(1)


# Find out how many times the array is rotated
def numberrotation(array):
    small = float("inf")
    ans = 0
    if len(array) == 1:
        ans = 0
        return ans
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[left] <= array[mid]:
            if array[left] < small:
                small = array[left]
                ans = left
            left = mid + 1
        elif array[mid] <= array[right]:
            if array[mid] < small:
                small = array[mid]
                ans = mid
            right = mid - 1
    return ans


print("The number of rotation is:", numberrotation([3, 4, 5, 1, 2]))


# Search in rotated sorted array-I
def searchrotated(array, k):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == k:
            return mid

        elif (
            array[left] <= array[mid]
        ):  # here we are checking if the left half of the array is sorted or not
            if (
                array[left] <= k and k <= array[mid]
            ):  # and then we are checking if the target number lies in the left sorted array, if yes then we destroy the right half.
                right = mid - 1
            else:  # otherwise the target might exists in the right half, so we move the left pointer
                left = mid + 1
        elif array[mid] <= array[right]:
            if array[mid] <= k and k <= array[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(searchrotated([4, 5, 6, 7, 0, 1, 2], 3))


def brutekoko(array, h):
    for i in range(
        1, max(array) + 1
    ):  # As the required answer which is the minimum number of bananas to be eaten lie between 1 and the maximum number in an array,
        total = 0
        for num in array:
            total += math.ceil(
                num / i
            )  # we are calculating the time taken to finish all bananas in each pile if we take i as the number of banans eaten by monkey in 1 hr.
        if total == h:
            return i
    return -1


print(brutekoko([7, 15, 6, 3], 8))
# time complexity : O(N * max(array))
# space complexity : O(1)


def optimalkoko(array, h):
    left = 1
    right = max(array)
    ans = max(array)
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for (
            num
        ) in (
            array
        ):  # here we are doing the same assuming mid as the requireed number of bananas to be eaten by monkey in 1 hr so that the monkey can finish all the bananas in h hours

            total += math.ceil(num / mid)
        if (
            total <= h
        ):  # if our total is way lesser then we just decrease the value of dividor
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    return ans


print(optimalkoko([25, 12, 8, 14, 19], 5))
# time complexity : O(N * max(array))
# space complexity : O(1)


# bouquets
def brutebloom(
    array, m, k
):  # here m is the number of bouquets and k is the required number of adjacent roses to make one bouquet
    # as our required minimum number of days lie between the smallest and the largest number of day in an array, we use this range of loop
    if len(array) < m * k:
        return -1
    for i in range(min(array), max(array) + 1):
        roses = 0
        bouquets = 0
        for num in array:
            if i >= num:
                roses += 1  # if the taken number of day is greater than the given days in an array then it means the flower is already bloomed and we increase the count of roses by 1
                if roses == k:
                    bouquets += 1
                    roses = 0
            else:
                roses = 0
        if bouquets >= m:
            return i
    return -1


print(brutebloom([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
# time complexity : O(N * (max(array)-min(array)+1))
# space complexity : O(1)


# optimal approach
def optimalbloom(array, m, k):
    if len(array) < m * k:
        return -1
    left = min(array)
    right = max(array)
    ans = 0
    while left <= right:
        roses = 0
        bouquets = 0
        mid = (left + right) // 2
        for num in array:
            if mid >= num:
                roses += 1
                if (
                    roses == k
                ):  # as soon as we found out that there are k adjacent roses then
                    # we can make one bouquets ,
                    bouquets += 1  # so we increase the bouquets by 1 and again make the count of roses to 0
                    roses = 0
            else:
                roses = 0
        if (
            bouquets >= m
        ):  # if the obtainer bouquets is greater than or equal to the given number of bouquets then we move the right pointer towards left side to decrease the number of days
            # as we need to find the minimum number of days
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


print(optimalbloom([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))


# divisor
def brutedivisor(array, l):
    for i in range(
        1, max(array) + 1
    ):  # the main loop runs from 1 to the maximum value in an array
        s = 0
        for num in array:
            s += math.ceil(num / i)
        if s <= l:
            return i


print(brutedivisor([1, 2, 3, 4, 5], 8))
# time complexity : O(max(array) * O(N))
# space complexity : O(1)


# optimal approach
def optimaldivisor(array, l):
    left = 1
    right = max(array)
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        s = 0
        for num in array:
            s += math.ceil(num / mid)
        if s <= l:
            ans = mid
            right = mid - 1  # we need to find the smallest possible interger
        else:
            left = mid + 1
    return ans


print(optimaldivisor([8, 4, 2, 3], 10))
# time complexity : O(logMax(array) * O(N))
# space complexity :O(1)


# bouquets question
def brutebouquet(
    array, m, k
):  # here m is the number of bouquets and k is the number adjcanet roses to make one bouquet.
    # our main loop runs between the range of minimum and the maximum in an array
    for i in range(min(array), max(array) + 1):
        bouquets = 0
        counts = 0  # the count of roses must be adjacents or side by side
        for num in array:
            if i >= num:
                counts += 1
                if (
                    counts == k
                ):  # as soon as we found the three adjacent bloomed roses then we can make one bouquets using these roses ,
                    # after making a bouquet we again make the counts 0 , inorder to make new bouquet
                    bouquets += 1
                    counts = 0
            else:  # as soon as we found the number of day which is lesser than the given day , then it means the flower is not bloomed in that day
                counts = 0
        if bouquets == m:
            return i
    return -1


print(brutebouquet([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
# time complexity : O(max(array)-min(array)+1 * O(N))
# space complexity : O(1)


# optimal approach
def optimalbouquets(array, m, k):
    left = min(array)
    right = max(array)
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        roses = 0
        bouquets = 0
        for num in array:
            if mid >= num:
                roses += 1
                if roses == k:
                    bouquets += 1
                    roses = 0
            else:
                roses = 0
        if bouquets >= m:
            ans = mid
            right = (
                mid - 1
            )  # to find the smallest number possible pr minimum number of days
        else:  # if the made number of  bouquet is lesser compared to the required value then we just move our left pointer towards right half
            left = mid + 1
    return ans


print(optimalbouquets([1, 10, 3, 10, 2], 3, 2))
# time complexity : O(log(max(array)-min(array)+1 * O(N)))
# space complexity : O(1)


# shipping the weights
def bruteshipp(
    array, d
):  # here our array consists of the packages having their own respective weights and d is the number of days limit within which we must
    # shipp all the weights represented in an array
    # the thing is we can shipp any number of packages in 1 day as long as the total weight of the shipped package doesnot exceed the weight which we have targeted to ship per day
    # and we need to find that minimum weight capacity which can be used as target weight capacity to shipp all these packages within given number of days
    s = sum(array)
    # our outer loop runs within the range of the maximum value in an array and the total sum of weights in the given array
    # cause if we take the smaller value than the max value of an array , then of course we cannot shipp the package which has the max weight in an array
    # so we start our loop from the maximum value in an array until the sum of an array
    for i in range(max(array), s + 1):
        day = 1
        totalweights = 0  # for one day
        for num in array:
            if (
                totalweights + num <= i
            ):  # if the taken package can be included in the totalweights if the total weights is still lesser than the target weight then we shipp the package in the same day
                totalweights += num
            else:
                totalweights = num  # if the total weight exceeds the target weight then we take that current package which makes the total weight exceeded after including it in the total packages,
                day += 1
        if day <= d:
            return i
        else:
            continue  # otherwise we start with next iteration of i


print(bruteshipp([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# time complexity : O((sum-max(arraay))) * O(N)
# space complexity : O(1)


def optimalshipp(array, d):
    left = max(array)
    right = sum(array)
    ans = max(array)
    while left <= right:
        mid = (left + right) // 2
        totalweights = 0
        day = 1
        for num in array:
            if totalweights + num <= mid:
                totalweights += num
            else:
                totalweights = num
                day += 1
        if day <= d:
            ans = mid
            right = (
                mid - 1
            )  # inorder to find the minimum capacity we move the right pointer towards the left half if the condition is met
        else:
            left = mid + 1  # otherwise we move the left pointer towards right half
    return ans


print(optimalshipp([3, 2, 2, 4, 1, 4], 3))
# time complexity : O(log(sum-max(array)) * O(N)
# space complexity : O(1)


# stallments of cows
# the question has given us the position of the stalls
# the question is asking us to place the aggressive cows in such a way that the minimum distance between the two adjacent cows is the maximum
def brutecows(array, k):
    array = sorted(array)
    ans = 0
    for i in range(
        1, (max(array) - min(array)) + 1
    ):  # this outer loop is for assuming the minimum distance between two adjacent cows is i
        laststall = array[0]
        cows = 1
        for j in range(1, len(array)):
            if (
                i <= array[j] - laststall
            ):  # if the taken distance is lesser than the distance between the consecutive stalls from the given array then we just place the cow in this current j stall and increase the number of cows which are already placed in the stall
                laststall = array[j]
                cows += 1

        if (
            cows >= k
        ):  # if we have placed all the cows in the stalls then we calculate our ans
            ans = max(i, ans)
        else:  # if we reach such value of i , in which the number of cows become lesser than the k , then we just break out of the loop
            break
    return ans


print(brutecows([0, 3, 4, 7, 10, 9], 4))
# time complexity :  O((max(array)-(min(array))) * O(N))
# space complexity : O(1)


# optimal approach
def optimalcows(array, k):
    array = sorted(array)
    ans = 0
    left = 1
    right = max(array) - min(array)
    while left <= right:
        laststall = array[0]
        mid = (left + right) // 2  # this will be our assumed minimum distance taken
        cows = 1
        for i in range(1, len(array)):
            if mid <= array[i] - laststall:
                laststall = array[i]
                cows += 1
        if cows >= k:
            ans = max(ans, mid)
            left = mid + 1
        else:  # if the number of cows is lesser than we just decrease the distance between the two adjacent cows , by moving the right pointer towards left half
            right = mid - 1
    return ans


print(optimalcows([4, 2, 1, 3, 6], 2))
# time complexity : O(log(max(array)-min(array)) * O(N))
# space complexity : O(1)


# gas station
def maximumdis(array, k):
    howmany = [0] * (
        len(array) - 1
    )  # this howmany denotes the number of new gas station that are placed at the certain gaps or index
    for i in range(
        1, k + 1
    ):  # As there are k number of new gas stations to be placed , we are running the loop from 1 to k
        maxdis = -1
        maxindex = -1
        for i in range(
            len(array) - 1
        ):  # as our loop starts from 0 and we are using the second last index as the end of the loop
            diff = array[i + 1] - array[i]
            dis = diff / (
                howmany[i] + 1
            )  # here we are calculating the distance between the gas stations or more precisely the distance obtained from placing new the gas staion
            if diff > maxdis:
                maxdis = dis
                maxindex = i
            howmany[
                maxindex
            ] += 1  # then after finding the index at which the maximum distance is found , we place the new gasstation at that gap
    maxans = -1
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        dis = diff / (howmany[i] + 1)
        maxans = max(maxans, dis)
    return maxans


print(maximumdis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
# time complexity : O(k * N)
# space complexity : O(1)


# optimal approach
def optimalmaximdis(array, k):
    pq = []
    howmany = [0] * (len(array) - 1)
    for i in range(len(array) - 1):
        dis = array[i + 1] - array[i]
        heapq.heappush(
            pq, (-1 * dis, i)
        )  # then we push the negative value of the distance and the index
    for i in range(k):
        maxim = heapq.heappop(
            pq
        )  # here heapq.heappop(pq) removes or delete the most smallest value , which is the maximum distance in the array
        maxindex = maxim[
            1
        ]  # then we find the index at which the maximum gap is occured
        howmany[
            maxindex
        ] += 1  # as we got the index where the maximum distance or gap is then we place the new gas station at that index
        diff = array[maxindex + 1] - array[maxindex]
        gap = diff / (howmany[maxindex] + 1)
        heapq.heappush(pq, (-1 * gap, maxindex))
    return (
        pq[0][0] * -1
    )  # here we are returning the first value of the pq to return the maximum gap which is the minimum possible by multiplying by -1 to make it into positive


print(optimalmaximdis([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
# time complexity : O(NlogN) + O(KlogN)
# space complexity : O(N-1)


# bruteappeoach of gasstaions
def brutenewgas(
    array, k
):  # here array is the number of initial gas stations and k is the number of new gasstations to be placed.
    howmany = [0] * (
        len(array) - 1
    )  # here howmany represents the number of gaps where the k gas stations can be placed
    # as we need to place k new gas stations , we are running the loop from 0 to k
    for i in range(k):
        maxindex = (
            -1
        )  # this stores the index at which the maximum distance is found at the current loop
        maxdis = -1  # this stores the maximum distance found at the current loop
        for j in range(
            len(array) - 1
        ):  # here we are only running the loop until len(array)-1 cause we need to calculate the difference of array[i+1] - array[i]
            diff = array[j + 1] - array[j]
            dist = diff / (
                howmany[j] + 1
            )  # the formula for the distance is this cause if we place one gas station between the initial position of gas stations then of course there will be two more new gaps and the distance will also be new
            if (
                dist > maxdis
            ):  # then in every loop of calculating the distance or gaps ,
                # we also compare the maximum distance, and input the new maximum distance as well as the index at which we found the maximum gap or maximum distance
                maxdis = dist
                maxindex = j
        howmany[maxindex] += 1  # then we place the new gas station at that maxindex
    # after the completion of the upper loop we have obtained the index or the gap having the number of new gas stations which total upto k
    maxans = -1
    for i in range(
        len(array) - 2
    ):  # then by running this loop , we calculate the maximum distance based on the number of new gas stations placed on these indexes.
        diff = array[i + 1] - array[i]
        dist = diff / (howmany[i] + 1)
        maxans = max(maxans, dist)
    return maxans


print(brutenewgas([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
# time complexity : O(k * N)
# space complexity : O(N)   #as we are using the set called howmany that nearly takes upto N so space complexity is O(N)


def betternewgas(array, k):
    pq = []
    howmany = [0] * (len(array) - 1)
    for i in range(len(array) - 1):
        diff = array[i + 1] - array[i]
        heapq.heappush(
            pq, (-1 * (diff / (howmany[i] + 1)), i)
        )  # here what we are doing is we are pushing the distance between the adjacent gas stations from the given gas stations and their corresponding indexes, and
        # the reason we are multiplying the value of distance by -1 is so that while we use pop to delete the maximum distance value from pq , heapq reduces the most smallest

    for i in range(k):
        tp = heapq.heappop(
            pq
        )  # this removes the most smallest value from pq , which is the most maximum distance at the given  array
        maxindex = tp[
            1
        ]  # then we retrieve that index at which the maximum distance is found
        howmany[maxindex] += 1  # then we insert the new gas station at that index
        diff = (
            array[maxindex + 1] - array[maxindex]
        )  # then we again calculate the difference and the distance
        heapq.heappush(
            pq, ((-1 * diff / (howmany[maxindex] + 1)), maxindex)
        )  # then we again insert that obtained distance after placing the new gas stations
    return pq[0][0] * -1  # then the one remaining at the top is our required distance


print(betternewgas([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
# time complexity : O(k+logN)
# space complexity : O(N)


# better approach of median of 2 sorted arrays
def bettermedian(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    n = n1 + n2
    mainindex = (
        n // 2
    )  # this gives us the main index from the total array at which we can find the median of the two sorted arrays if the total length of the array is odd
    secindex = (
        mainindex - 1
    )  # this gives us the secondary index which can be used to find the median of the two sorted arrays if the total length is odd ,
    count = 0
    mainelem = 0  # this is the number at the main index which we need to find
    secelem = 0  # this is the number at the  secondary index which we need to find if the total length is even
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if count == mainindex:
                mainelem = arr1[
                    i
                ]  # if the count at the current index i is equal to the main index then ofcourse the number at current index i is the  main elem
            if count == secindex:
                secelem = arr1[i]  # same reason here for the secondary index
            i += 1
            count += 1
        else:
            if count == mainindex:
                mainelem = arr2[
                    j
                ]  # if the count at the current index j is equal to the main index then ofcourse the number at current index j is the  main elem
            if count == secindex:
                secelem = arr2[j]  # same reason here for the secondary index
            j += 1
            count += 1
    while i < len(arr1):
        if count == mainindex:
            mainelem = arr1[
                i
            ]  # if the count at the current index i is equal to the main index then ofcourse the number at current index i is the  main elem
        if count == secindex:
            secelem = arr1[i]  # same reason here for the secondary index
        i += 1
        count += 1
    while j < len(arr2):
        if count == mainindex:
            mainelem = arr2[
                j
            ]  # if the count at the current index i is equal to the main index then ofcourse the number at current index i is the  main elem
        if count == secindex:
            secelem = arr2[j]  # same reason here for the secondary index
        j += 1
        count += 1
    if n % 2 != 0:
        return mainelem
    else:
        return (
            mainelem + secelem
        ) / 2  # this gives us the median which is the average of two middle numbers in a total array if the total length is even


print(bettermedian([2, 4, 6], [1, 3, 5]))


# optimal median
def optimalmedian(array1, array2):
    n1 = len(array1)
    n2 = len(array2)
    n = n1 + n2
    if n1 > n2:
        return optimalmedian(
            array2, array1
        )  # if the length of the array1 is greater than that of array2 then we just switch the array1 and array2
    low = 0
    high = len(
        array1
    )  # here anyhow we are making the array1 as the primary array which has the smallest length
    total = (
        n1 + n2 + 1
    ) // 2  # this is the size of the left half of the symmetric or sorted array
    l1 = l2 = float(
        "-inf"
    )  # here the left half elements or numbers must be the smallest so we are making them as the most smallest number possible
    r1 = r2 = float(
        "inf"
    )  # here we are making the r1 and r2 as the most largest number possible initially as the right half numbers must be greater than the left half
    while low <= high:
        mid1 = (
            low + high
        ) // 2  # this gives us the number of elements that must be caught from our main array to fill the left half of the symmetric array
        mid2 = (
            total - mid1
        )  # this gives us the number of elements that must be caught from our secondary array to fill the left half of the symmetric array
        r1 = array1[mid1]
        r2 = array2[mid2]
        l1 = array1[mid1 - 1]
        l2 = array2[mid2 - 1]
        if l1 < r2 and l2 < r1:
            if n % 2 == 0:
                median = (max(l1, l2) + min(r1, r2)) / 2
                return median
            else:
                return max(l1, l2)
        elif (
            l1 > r2
        ):  # if the last element from our main array or array1 is greater than the first element from array2 then it means we need to remove this number from main array so what we need to do is decrease the range of array1 so we make high = mid -1
            high = mid1 - 1
        elif (
            l2 > r1
        ):  # but if the last element from our secondary array or array2 is greater than the first element from array1 then it means we need to remove this number which is of array2 so we increase the range of main array but decrease that of secondary array
            low = mid1 + 1
    return 0  # if the median is not found


print(optimalmedian([2, 4, 6], [1, 3, 5]))
# time complexity : O(log(min(array1,array2)))
# space complexity : O(1)


def optmedian(array1, array2):
    n1 = len(array1)
    n2 = len(array2)
    n = n1 + n2  # here n is the total length of a sorted array
    if (
        n1 > n2
    ):  # if the length of an array 1 is greater than the length of an array2 then we just put the array2 inplace of array1 and vice versa
        return optmedian(array2, array1)
    total = (
        n1 + n2 + 1
    ) // 2  # this gives the total length of the left half of the symmetric array by taking the array1 or the array which has the smallest length
    l1 = l2 = float(
        "-inf"
    )  # here the left side of the elements of both the arrays must be smaller than the right half elements of both arrays
    r1 = r2 = float(
        "inf"
    )  # here the right half elements or the numbers must be always greater than the left half elements or numbers
    low = 0  # here we are declaring low as 0 which means we might also take 0 element from array1
    high = len(
        array1
    )  # and high is declared as len(array1) which means we might also take all the elements from array1
    while low <= high:
        mid1 = (
            low + high
        ) // 2  # this value tell us how many numbers should be taken from array1
        mid2 = (
            total - mid1
        )  # this value tell us how many numbers should be taken from array2
        r1 = array1[mid1]
        r2 = array2[mid2]
        l1 = array1[mid1 - 1]
        l2 = array2[mid2 - 1]
        if l1 < r2 and l2 < r1:
            if (
                n % 2 == 0
            ):  # if the total length of a symmetric array is even then we need to calculate the average of two middle numbers to get the median
                return (max(l1, l2) + min(r1, r2)) / 2
            else:  # else if the total length is odd then we need to return the maximum of l1 and l2
                return max(l1, l2)
        elif (
            l1 > r2
        ):  # if the l1 is greater than the r2 then we need to remove this greater number from array1 by making high a mid1-1
            high = mid1 - 1
        elif (
            l2 > r1
        ):  # else if the l2 is greater than r1 then we need to include more numbers from array1 and less from array2 inorder to remove this current l2 which is the greater value
            low = mid1 + 1
    return 0


print(optmedian([2, 4, 6], [1, 3, 5]))
# time complexity : O(log(min(len(array1),len(array2))))
# space complexity : O(1)


def optimalrow(array):  # this is the main or parent array
    n = len(array)  # this is the length of the parent array
    m = len(array[0])  # this is the length of the child array
    row = 0  # we start from the  first row
    col = (
        m - 1
    )  # we start checking from the last index as the arrays are already sorted
    ans = -1
    while (
        row < n and col >= 0
    ):  # the columns must be greater than or equal to 0 otherwise it will get out of index or range
        if (
            array[row][col] == 1
        ):  # if we encounter number 1 at current row and column then the answer might be the row as our child rows are already sorted

            ans = row
            col -= 1  # then we decrease the value of col
        else:
            row += 1
        # and as we need to find the smaller index of row , we are checking the condition from first row or 0 indexed row
    return ans


print(optimalrow([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1]]))
# time complexity : O(N + M)  here N is the length of the parent row and M means approximately equal to the length of child row
# space complexity : O(1)


# Find row with maximum 1's
def optimalmax(array):
    n = len(array)  # here n is the length of a parent array
    m = len(array[0])  # m is the length of the child array
    row = 0
    col = m - 1
    ans = -1
    while row < n and col >= 0:
        if (
            array[row][col] == 1
        ):  # we are checking the 1 from the first row and the last column or the last element of the first row
            ans = row  # as our answer is sorted in ascending order , we are assuming the answer the current row as soon as we found the number 1 at the current row and column index
            col -= 1
        else:  # if at the current row as soon as we found the number 0 we change the row by keeping the column same,
            row += 1
    return ans


print(optimalmax([[0, 0, 1], [0, 0, 1], [0, 1, 1]]))
# time complexity : O(N + M)
# space complexity : O(1)


def optimal2dmatrix(array, k):
    n = len(array)  # here n is the total length of the parent array
    m = len(array[0])  # here m is the length of the child array
    left = 0  # this is our first index of the flatten array
    right = n * m - 1  # this is the last index of the flatten array
    while left <= right:
        mid = (
            left + right
        ) // 2  # this mid value gives the index of the flatten array which we use to check if its equal to the target k or not
        if array[mid // m][mid % m] == k:
            return True
        elif (
            array[mid // m][mid % m] > k
        ):  # if the current mid indexed number is greater than k then we just move the right pointer to left half
            right = mid - 1
        else:
            left = mid + 1
    return False


print(optimal2dmatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 12))
# time complexity : O(logN*M)
# space complexity : O(1)


# peak number in 2d matrix
def findpeakrow(
    array, mid
):  # here mid is the column index now based on that column we need to find the peak element comparing among each rows on this column mid
    ans = 0
    maxvalue = float('-inf')
    for i in range(len(array)):  # here we are looping through each rows
        if array[i][mid] > maxvalue:
            maxvalue = array[i][mid]  #previously the code was wrong here
            ans = i
    return ans


def optimalpeak2d(array):
    low = 0
    high = len(array[0]) - 1
    while low <= high:
        mid = (low + high) // 2
        row = findpeakrow(array, mid)
        # now as we found out the row having the peak number based on the mid index, we dont need to worry about top and bottom ,we only need to worry about left and right
        left = (
            array[row][mid - 1] if mid - 1 >= 0 else -1
        )  # if the mid-1 index is not 0 or greater than 0 then we give the value of left to -1
        right = (
            array[row][mid + 1] if mid + 1 < len(array[0]) else -1
        )  # if the mid+1 index is not within the range of length of a child array then we give the value of left to -1
        if left < array[row][mid] and right < array[row][mid]:
            return (
                row,
                mid,
            )  # if the condition of peak is met then we return the row index as well as the column index
        elif (
            left > array[row][mid]
        ):  # if the left indexed number is greater than the mid indexed number then our answer lies in the left half
            high = mid - 1
        elif (
            right > array[row][mid]
        ):  # same here but in the opposite direction
            low = mid + 1
    return -1  # if we dont find any peak number


print(
    optimalpeak2d(
        [
            [3, 8, 12, 15, 20],
            [5, 10, 14, 18, 25],
            [7, 13, 17, 22, 28],
            [9, 16, 21, 26, 30],
            [11, 19, 40, 27, 35],
        ]
    )
)
#time complexity : O( logM * N) here M is the number of columns and N is the number of rows
#space complexity : O(1)

#matrix median 
#in the naive approach what we can do is we can store all the numbers of the 2d matrix in a single array in a sorted way then we can easily find the median by calulating the number at the index (N*M) //2  which is the median position in an array
#but in the optimal approach what we can do is , we can calculate the number of numbers smaller than or equal to the mid value which is obtained between the minimum and the maximum number in an array,
#this number of smaller than or equal to the mid value is taken as a comparison value which is compared with  the median, if its lesser than the median then we move to the right half,
#otherwise we move to the left half,
#we can see this in the code below
def upperbound(array,mid):  #we are using only one specific row here passed from smallequal function
    low = 0
    high = len(array)-1
    ans = len(array)   #we are assuming that all the values in the array might be greater than the  value mid
    while low<=high:
        mid2=(low + high) // 2
        if array[mid2] > mid:   #here what we are doing is we  are checking if the mid2 indexed number is greater than the mid in param, if it is then we assume this might be our answer which is mid2 ,
            #that gives us the number of numbers smaller than or equal to mid, and as our array is sorted in ascending order, rather than going to the right half , we are moving to the left half as shown here 
            ans = mid2
            high = mid2-1
        else:
            low=mid2+1
    return ans            



def smallequal(array,mid):
    count = 0
    for i in range(len(array)):
        count+=upperbound(array[i],mid)  #this count is used for counting the numbers in an array which are lesser than or equal to the mid 
    return count    


def optimalmedian2d(array):
    n=len(array)  #number of rows
    m=len(array[0])  #number of columns 
    low = float('inf')  
    high = float('-inf')
    req = (n * m )// 2 
    #as our rows are arranged or sorted in ascending order,
    for i in range(n):
        low = min(low,array[i][0])  #as the first element of every arrays is the smallest in their corresponding rows
        high = max(high,array[i][m-1])  #and as the last element of every arrays is the largeest in their corresponding rows
    #from the above loop, we got the value of low and high
    while low<=high:
        mid=(low + high) // 2 
        smallerequal=smallequal(array,mid)    #this smallequal function is used for calculating all the numbers in the array which are smaller than or equal to the obtained mid
        if smallerequal<=req:
            low = mid + 1
        else:
            high = mid - 1
    return low   #and the value of smaller equal must be just slightly greater than the  median indexed value in an array , which will be the low value in our case , as high will move beyond the mid value but in left direction
print(optimalmedian2d([ [1, 3, 8], [2, 3, 4], [1, 2, 5] ] ))    
#time complexity : O(log(maxm-minm)*NlogM)  #here N is the number of rows and M is the number of columns
# space complexity : O(1)         


#Remove Outermost Parentheses
#A valid parentheses string is defined by the following rules:
#It is the empty string "".
# If A is a valid parentheses string, then so is "(" + A + ")".
#If A and B are valid parentheses strings, then A + B is also valid.
#A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.
#Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.

def removeouter(string):
    counter = 0
    ans = []
    for char in string:  
        if char == '(':  #here our approach is as soon as we found the char ( , we check if the count is greater than 0 , if it is then it means its not the first ( so we append otherwise we just increase the count by 1 by ignoring the first (.
            if counter>0:
                ans.append(char)
            counter+=1    
        elif char == ')':   #but in the case of ), we first decrease the count by 1, then check whether the count is 0 or not , if its 0 then it means this current ) is the last ) that cancel the first ( , if its not then it means its still not the last closing ) char.
            counter-=1
            if counter > 0:
                ans.append(char)
    return ''.join(ans)
print(removeouter("((()))"))   
#time complexity : O(N)
# space complexity : O(1)                 


#reverse the word from a given string
def reverseword(s):
    s=s[::-1]
    i = 0
    ans=[]
    while i<len(s):
        word=[]
        while i<len(s) and s[i]!=" ":  #this is inside loop will only end when the i is greater than or equal to the length of the string and char is equal to the space
            word.append(s[i])
            i+=1
        ans.append(''.join(word[::-1]))
        i+=1  #here we are also adding i to pass behind the index where we found the space
        
    return ' '.join(ans)
print(reverseword("welcome to the jungle"))
#time complexity : O(N) 
#space complexity : O(N)


#string to atoi
def stringatoi(s):
    i = 0
    n = len(s)
    sign=1
    ans=0
    while i<n and s[i] == " ":  #this loop is for checking the whitespaces before the digits or integers
        #as long as we find the whitespaces , we keep on skipping this by increasing the value of i
        i+=1
    if i<n and (s[i] == "-" or s[i]=="+"):  #this condition is for checking the sign and determining whether the given sign in a string is - or +, then we just increase the value of i based on that
        if s[i] == "-":
            sign=-1
        i+=1    
    while i<n and s[i].isdigit():
        ans=(ans*10)+int(s[i])
        i+=1
    final = sign * ans
    if final<-2147483648:
        return -2147483648
    elif final>2147483647:
        return 2147483647
    else:
        return final
print(stringatoi(" -12345"))     

#count substrings consisting of all the vowels and k consonants
#brute approach ,
#in the brute approach , what we can do is we can just go through the nested loops and then check if all the vowels are presented in the substrings or not and also k number of consonants
def brutevowel(s,k):
    vowels = ['a','e','i','o','u']
    n=len(s)
    c=0
    for i in range(n):
        for j in range(i,n):
            count = 0
            substring =s[i:j+1]  #here we are making the every possible substrings from the given string
            for char in substring:
                if char not in vowels:
                    count+=1
            if len(substring)-count>=len(vowels) and count==k:#here the first condition checks if the total number of consonants subtracting the length of the obtained substring is greater than or equal to 0 then of course all the remaining elements are vowels and count==k:  #if the total number of consonants is equal to k , and the other nnumbers except these count elements are vowels then we get our answer
              c+=1
    return c   #here c is the total number of substrings which has k number of consonants and all the remaining elements are the vowels
print(brutevowel('aeiou',0))   
#time complexity : O(N^3) in the worst case
# space complexity : O(1)     


#optimal approach
#in the optimal approach what we gonna do is , we gonna use the sliding window approach where we calculate the subarray or substring from index 0 to n where n is the length of the string
#and we also decrease the length of the window by subtracting the index from left side
def optimalatleastk(s,k):
    left = 0
    n=len(s)
    consonants=0
    vowel=defaultdict(int)
    ans = 0
    for i in range(n):
        if s[i] in "aeiou":  #here what we are doing is , we are adding the i indexed character in vowel if it is one of the vowel letter
         vowel[s[i]]+=1
        else:  #otherwise , we increase the number of consonants , if its not the vowel
            consonants+=1 
        #this below while loop is the main loop for calculating the number of subarrays that matches the condition and for moving the left pointer towards the end to decrease the size of a window
        while len(vowel) == 5 and consonants>=k:  #as long as the length of our dict is 5 which shows all 5 vowels are present in the current i index and the number of consosnants is greater than or equal to k
            ans+=n-i   #counting the number of substrings which has all 5 vowels and atleats k consonants
            if s[i] in "aeiou":
                vowel[s[i]]-=1

            else:
                consonants-=1
            if vowel[s[i]]==0:
                vowel.pop(s[i])          
            left+=1
    return ans   
def optimalvowel(s,k):
    return optimalatleastk(s,k) - optimalatleastk(s,k+1)  #this trick uses the approach where we assume k+1 value and find the substrings which has the all the 5 vowels and at leats k+1 consosnants , then we subtract this substrings count with the count of substrings which has atleast k consonants , then we get the number of substrings having exactly k consonants and all 5 vowels in it
print(optimalvowel('aeiou',0))
#time complexity : O(N) where N is the length of the string
#space complexity : O(1)  which is constant as the vowel var is also constant which will have atmost length of 5 in most cases
     



    


        
