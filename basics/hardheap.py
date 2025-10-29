# design twitter
# Create a simplified version of a social media platform similar to Twitter. Users should be able to post tweets, follow or unfollow other users, and view the 10 most recent tweets in their news feed.Implement the Twitter class as follows:
from collections import defaultdict
import heapq


class Twitter:
    def __init__(self):
        self.time = 0
        self.twitters = defaultdict(
            list
        )  # here this twitters is the list of twitter ids related to the specific user its
        # example userid->[(time,twitter1),(time,twitter2)]  and so on and here time denotes the time at which the twitter is posted
        self.following = defaultdict(
            set
        )  # here this self.following is the list of ids of the users followed by one specific user
        # example : userid -> [user1,user2,user3]

    def posttwitt(self, userid, twittid):
        self.twitters[userid].append(
            (self.time, twittid)
        )  # here as you can see, we are appending both the time as well as the twitt id based on the given user id
        self.time += 1
        # in our default dict

    def follow(self, followerid, followeeid):
        self.following[followerid].add(followeeid)

    def unfollow(self, followerid, followeeid):
        self.following[followerid].discard(followeeid)

    def getnewsfeed(
        self, userid
    ):  # now for this function we need to retrieve the 10 most recent twitts either posted by this user himself or the persons he follows
        ans = []
        heap = []
        for t in self.twitters[userid]:
            heapq.heappush(heap, (t))
            while len(heap) > 10:
                heapq.heappop(heap)
        for followee in self.following[userid]:
            for t in self.twitters[followee]:
                heapq.heappush(heap, (t))
                while len(heap) > 10:
                    heapq.heappop(heap)
        while heap:
            ans.append(
                heapq.heappop(heap)[1]
            )  # here we are using index 1 cause we have also inserted the time while inserting the tweet
        return ans[
            ::-1
        ]  # as the recent twitts has the higher counts or time so we are reversing the ans as the heap always returns the minimum value while we are using pop


t = Twitter()
t.posttwitt(
    1, 2
)  # time complexity : O(1) space complexity : O(T)  total number of tweets
t.posttwitt(2, 6)
t.getnewsfeed(
    1
)  # time complexity : O(Tu + Tf)  here Tf is the total number of tweets of the user or follower and Tf is the total number of tweets of the followed users
t.follow(1, 2)  # time complexity : O(1)
t.getnewsfeed(1)
t.unfollow(1, 2)  # time complexity : O(1)
t.posttwitt(1, 7)  # time complexity : O(1)
print(t.getnewsfeed(1))


# minimum cost to connect sticks
def minimumcost(sticks):
    heap = []
    for num in sticks:
        heapq.heappush(heap, num)
    totalcost = 0
    while len(heap) > 1:
        firstcost = heapq.heappop(heap)
        secondcost = heapq.heappop(heap)
        cost = firstcost + secondcost
        totalcost += cost
        heapq.heappush(heap, cost)
    return totalcost


print(minimumcost([1, 8, 3, 5]))
# time complexity : O(NlogN)
# space complexity : O(N)


# Kth largest element in a stream of running integers
class Kthlargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums

    def maxheapify(
        self, i, size, array
    ):  # this function is used for designing the maxheapify tree
        leftind = 2 * i + 1
        rightind = 2 * i + 2
        maximum = i
        if leftind < size and array[leftind] > array[maximum]:
            maximum = leftind
        if rightind < size and array[rightind] > array[maximum]:
            maximum = rightind
        if maximum != i:
            array[maximum], array[i] = array[i], array[maximum]
            self.maxheapify(maximum, size, array)

    def add(
        self, val
    ):  # here val is jsut a random number and we must add this val in our nums array and then return the kth largest number
        self.nums.append(val)
        a = self.nums[:]  # here we are making a copy of the self.nums array
        n = len(a)
        size = n
        for i in range(
            (n // 2) - 1, -1, -1
        ):  # here we are designing the maxheap tree using the heapify function
            self.maxheapify(i, n, a)
        for i in range(1, self.k):
            a[0] = a[size - 1]
            size -= 1

            self.maxheapify(0, size, a)
        return a[0]


k = Kthlargest(2, [5, 5, 5, 5])
print(k.add(6))
print(k.add(60))
print(k.add(2))

# time complexity : O(N+klogN) as we are making a copy of a self.nums
# space complexity : O(N)


class Optkthlargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # here we are designing a min-heap tree
        while (
            len(self.nums) > self.k
        ):  # so the logic behind this is that whenever the heap tree's size goes beyound the k then we start popping the most minimum element in the tree
            heapq.heappop(self.nums)

    def add(self, val):
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[
            0
        ]  # as we have removed the most minimum numbers while the length of the nums is greater than k , the remaining number at the root after this operation is the kth largest number in an array


ok = Optkthlargest(2, [5, 5, 5, 5])
print(ok.add(6))
print(ok.add(60))
print(ok.add(2))
# time complexity : O(logK)
# space complexity : O(K)  as we are always storing at most k number of elements ,cause we are popping the number from our array whenever the size of an array goes beyound k


# maximum sum combinations
# Given two integer arrays nums1 and nums2 and an integer k, return the maximum k valid sum combinations from all possible sum combinations using the elements of nums1 and nums2.
# A valid sum combination is made by adding one element from nums1 and one element from nums2. Return the answer in non-increasing order.
def brutemaxsumcomb(a, b, k):
    n = len(a)
    ans = []
    for i in range(n):

        for j in range(n):
            ans.append(a[i] + b[j])
    ans.sort(reverse=True)  # here we are sorting the given array in descending order
    return ans[:k]


print(brutemaxsumcomb([7, 3], [1, 6], 2))
# time complexity : O(N**2 + logN)  here logN is due to the sorting and n**2 is due to the for loop
# space complexity : O(1)


#optimal approach
def optimalmaxsumcomb(a,b,k):
    a=sorted(a)
    b=sorted(b)
    n=len(a)  #as the length of a and b is same, we can take length of any of the array
    heap = []
    heapq.heappush(heap,(-(a[n-1] + b[n-1]),n-1,n-1))  #here we are appending the negative value of the sum as well as the indices in a heap
    seen = set()
    seen.add((n-1,n-1))
    ans = []
    while k>0 and heap:
        currentsum,i,j = heapq.heappop(heap)  #as we have stored the sum,as well as the indices , 
        ans.append(-currentsum)  #here we are appending the current sum directly cause 
        #we have sorted the arrays and pushed the sum of the last numbers from each array which are the greater numbers along with their indices
        k-=1   
        if i-1>=0 and (i-1,j) not in seen:
            heapq.heappush(heap , (-(a[i-1]+b[j]),i-1,j))
            seen.add((i-1,j))
        if j-1>=0 and (i,j-1) not in seen:
            heapq.heappush(heap,(-(a[i]+b[j-1]),i,j-1))
            seen.add((i,j-1))    
    return ans
print(optimalmaxsumcomb([7, 3], [1, 6],2))        
#time complexity : O(klogk)
#space complexity : O(k)


#find Median from Data Stream
# Implement a class that finds the median from a data stream. The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#Implement the MedianFInder class as follows:
#MedianFinder() initializes the MedianFinder object.
#void addNum(int num) adds the integer num to the data structure.
#double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted. 

class MedianFinder:
    def __init__(self):
        self.array = []
    def addnum(self,num):
             self.array.append(num)
    def findMedian(self):
        self.array.sort()
        n=len(self.array)
        if n%2 !=0:
            median = self.array[n//2]
        else:
            firstvalue = self.array[(n//2)-1]
            secondvalue = self.array[(n//2)]
            median=(firstvalue + secondvalue) / 2
        return median
brutemf=MedianFinder()
brutemf.addnum(1)
brutemf.addnum(2)
brutemf.addnum(3)
print(brutemf.findMedian())
#time complexity : O(nlogn)
#space complexity : O(n)  number of elements in an array



                     