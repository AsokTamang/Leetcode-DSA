from collections import defaultdict
import heapq

#task scheduler
#the question is asking us to return the most possible total minimum time interval ,as two different task can be done just next to each other but for the identical tasks the,they must be separated by n intervals
def taskscheduler(array,n):
    freqarray = [0] * 26
    for i in range(len(array)):
        freqarray[ord(array[i])-ord('A')]+=1   #counting the frequency of task from a given array
    heap = []
    for i in range(26):
        if freqarray[i] > 0:
         heapq.heappush(heap,-freqarray[i])  #here we must store in the negative form cause python heapq returns the minimum value or smallest value while popping
    totaltime = 0
    while heap:
        temp = []  #this stores the number of task left for each iteration 
        for i in range(n+1):
            if heap:
                count = heapq.heappop(heap)
                count+=1  #reducing the value which means we are using the task
                temp.append(count)
        for num in temp:
            if num < 0:
                heapq.heappush(heap,num)
        if heap:  #if the heap still exists then it means we have successfully completed n+1 task in the current cycle maintaining n interval between identical tasks if there is sufficient number of task else remained idle if needed
            totaltime+=n+1
        else:
            totaltime+=len(temp)
    return totaltime     
print(taskscheduler( ["A","A","A","B","B","B"], 2))          
#time complexity : O(N)
#space complexity : O(K)  number of distinct elements in a given array     


#hand of straights
from collections import Counter
def handofstraights(hand,n):  #here n is the size of a group consisting of consecutive cards
    m=Counter(hand)
    for num in sorted(m.keys()):
        count = m[num]  
        if count>0:
            for i in range(n):
                if m[num + i] < count:
                    return False  #we return false as soon as the frequency of the next coming number of the current card number is less than the count or freq of the current card number, cause if the condition is like this then
                m[num + i]-=count
                #we cannot form a group of size n with the consecutive numbers
    return True
print(handofstraights( [1,2,3,4,5],  4))        
#time complexity : O(N)
#space complexity : O(M) number of distinct elements from a given array
from collections import defaultdict
#design a twitter
class Twitter:
    def __init__(self):
        self.time = 1 #here self.time represents the time during which the tweet was posted as the question has asked us to return the 10 most recent tweets based on the user
        self.followinglist = defaultdict(set)  #here the default dict represents the set of the users followed by the specific users example userid->[user1,user2,user3]
        self.tweet=defaultdict(list)    #here defaultdict represents the list of the tweets posted by the specific user example: userid->[t1,t2,t3]
    def posttweet(self,userid,tweetid):
        self.tweet[userid].append((self.time,tweetid))  #here we are appending the tweet with given id in the list of the user represented by userid
        self.time+=1
    def follow(self,followerid,followeeid):
        self.followinglist[followerid].add(followeeid)
    def unfollow(self,followerid,followeeid):
        self.followinglist[followerid].discard(followeeid)
    def getnewsfeed(self,userid):  #as the most recent tweets have the higher time , so we must use heapq method to remove the old tweets as they have the lesser time
        heap = []
        ans = []
        for t in self.tweet[userid]:
            heapq.heappush(heap,t)
            if len(heap) > 10:
                heapq.heappop(heap)  #here the pop is based on the time
        for followee in self.followinglist[userid]:
            for t in self.tweet[followee]:
                heapq.heappush(heap,t)
                if len(heap)>10:
                    heapq.heappop(heap)
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans[::-1]  #as the most recent must come before , we are reversing the heap as the tweet goes from most recent to least recent
tw=Twitter()
tw.posttweet(1,2)
tw.posttweet(2,6)
print(tw.getnewsfeed(1))
tw.follow(1,2)
print(tw.getnewsfeed(1))
tw.unfollow(1, 2)
tw.posttweet(1,7)
print(tw.getnewsfeed(1))
#time complexity: O(N)  N is the total  number of tweets
#space complexity : O(N) 


#Minimum Cost to Connect Sticks
def minimumcost(sticks):
    heap=[]
    totalcost = 0
    for num in sticks:
        heapq.heappush(heap,num)
    while len(heap)>1:
        firstsmall = heapq.heappop(heap)
        secondsmall = heapq.heappop(heap)
        pair = firstsmall + secondsmall
        totalcost+=pair
        heapq.heappush(heap,pair)
    return totalcost
print(minimumcost( [1, 8, 3, 5]))    
#time complexity : O(N)
#space complexity : O(N)


        
#maximum sum combination
#brute approach
def brutemaximumsum(nums1,nums2,k):
    ans=[]
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            ans.append(nums1[i]+nums2[j])
    ans.sort(reverse=True)
    return ans[:k]
print(brutemaximumsum([7, 3],  [1, 6],  2))
#time complexity : O(N**2logN)
#space complexity : O(N)
                        

#optimal solution
def optsumcombination(nums1,nums2,k):
    n=len(nums1)
    nums1.sort()
    nums2.sort()
    heap = []
    ans = []
    seen=set()
    heapq.heappush(heap,(-(nums1[n-1]+nums2[n-1]),n-1,n-1))
    seen.add((n-1,n-1))
    c=0
    while heap and c<k:
        s,i,j = heapq.heappop(heap)
        ans.append(-s)
        c+=1
        if (i-1,j) not in seen:
            heapq.heappush(heap,(-(nums1[i-1]+nums2[j]),i-1,j))
            seen.add((i-1,j))
        if (i,j-1) not in seen:
            heapq.heappush(heap,(-(nums1[i]+nums2[j-1]),i,j-1))
            seen.add((i,j-1))
    return ans
print(optsumcombination( [3, 4, 5],  [2, 6, 3], 2))    
#time complexity : O(NlogN + klogK) here NlogN is for sorting the given array and KlogK is for the heaping as well as appending the sum 
#space complexity : O(k+N)  K denotes the heap and N denotes the total number of values in both of these lists      






#Find Median from Data Stream
class MedianFInder:
    def __init__(self):
      self.small = []  #this array stores the smaller half of the array and it uses maxheap property 
      self.large = []  #this array stores the larger half of the array and it uses minheap property
    def addnum(self,val):
        heapq.heappush(self.small,-val)
        if self.small and self.large and -self.small[0] > self.large[0]:  #the elements in the smaller half must be smaller than or equal to the elements in the larger half
            v=heapq.heappop(self.small)
            heapq.heappush(self.large,-v)
        if len(self.small) > len(self.large) + 1:
            v=heapq.heappop(self.small)   
            heapq.heappush(self.large,-v)
        if len(self.large) > len(self.small)+1:
            v=heapq.heappop(self.large)
            heapq.heappush(self.small,-v)     



    def findmedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2   #as in the smaller half array or heap , we have stored the number in a negative form
mf=MedianFInder()
mf.addnum(1)
mf.addnum(2)
mf.addnum(3)
print(mf.findmedian())
#time complexity : 
#addnum- O(logN)
#findmedian - O(1)
#space complexity : O(N)



#Kth largest element in a stream of running integers   
#so in this question we have to find the kth ranked larger element from our given array
#for this we can use the min-heap , and inorder to find the kth largest element, we can pop elment if the length of our array becomes greater than k
#so the root element in our array is the kth ranked larger element      
class Kthlargest:
    def __init__(self,array,k):  #here we have to return the kth largest element from the given array
        self.array =array
        self.k=k   
        heapq.heapify(self.array)   
    
    def add(self,val):
        heapq.heappush(self.array,val)
        if len(self.array)>self.k:
            heapq.heappop(self.array)
    def findkthlargest(self): 
        return self.array[0]
    
kl=Kthlargest([1, 2, 3, 4],3)
(kl.add(5))
(kl.add(2))
(kl.add(7))
print(kl.findkthlargest())
#time complexity :
# add: O(logk)
#findkthalargest : O(1) 


#minimum cost to connect sticks
def minimumcost(sticks):
    heap = []
    for num in sticks:
        heapq.heappush(heap,num)
    total=0
    while len(heap)>1:  #as long as we are not forming one total stick , we continue this loop
        stick1=heapq.heappop(heap)
        stick2=heapq.heappop(heap)
        formedstick = stick1+stick2  #this is the stick formed from the minimum length possible from every sticks
        heapq.heappush(heap,formedstick)
        total+=formedstick
    return total
print(minimumcost([1, 8, 3, 5]))
#time complexity :  O(NlogN)
#space complexity : O(N)


#design twitter
class Tweeter:
    def __init__(self):
      self.tweets=defaultdict(list)   #this list is of the tweets having their own unique ids uploaded by the specific users having their own id ,
      #example : user1:[t1,t2,t3]
      self.following  =defaultdict(set)
      #this is the set of all the users represented by their own unique ids followed by the specific user id 
      #example: user1:[u1,u2,u3]
      self.time = 0  #we have initialized this time just for the clarification of finding the recent tweets
    def posttweet(self,userid,tweetid):
        self.tweets[userid].append((self.time,tweetid))
        self.time+=1
    def followe(self,followerid,followeeid):
        self.following[followerid].add(followeeid)
    def unfollowe(self,followerid,followeeid):
        self.following[followerid].discard(followeeid)
    def getnewsfeed(self,userid):
        ans = []
        heap=[]
        for t in self.tweets[userid]:
            heapq.heappush(heap,t)
            while len(ans)>10:
                heapq.heappop(heap)  #this will pop the old tweets which is based on the smaller time or earlier times
        for user in self.following[userid]:
            for t in self.tweets[user]:
                heapq.heappush(heap,t)
                while len(heap)>10:
                    heapq.heappop(heap)
        while heap:
            ans.append(heapq.heappop(heap)[1])  #here we are only appending the value only not the time 
             #as the actual tweet id is the second indexed value cause the first indexed value is the time of insertion
        return ans[::-1]     #and we are reversing the ans cause we need to return the 10 most recent tweets 
tw=Tweeter()
tw.posttweet(1,2)
tw.posttweet(2,6)
print(tw.getnewsfeed(1))    
#time complexity :
#follow,unfollow,posttweet:O(1)
#getnewsfeed : O(NlogN)  N is the total number of tweets
#space complexity : O(1)  cause it is always constant as we are storing at most 10 number of tweets in our heap as well as ans


#kth largest element in an array
def medkthlargest(nums,k):
    heap =[]
    for num in nums:
        heapq.heappush(heap,num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
print(medkthlargest( [-5, 4, 1, 2, -3], k = 5))    
#time complexity : O(NlogK)  logk is for popping the elements until the length of the heap is equal to k
#space complexity : O(k)














                 





