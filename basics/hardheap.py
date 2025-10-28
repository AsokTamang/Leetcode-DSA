#design twitter
#Create a simplified version of a social media platform similar to Twitter. Users should be able to post tweets, follow or unfollow other users, and view the 10 most recent tweets in their news feed.Implement the Twitter class as follows:
from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.time = 0
        self.twitters=defaultdict(list)  #here this twitters is the list of twitter ids related to the specific user its
        #example userid->[(time,twitter1),(time,twitter2)]  and so on and here time denotes the time at which the twitter is posted
        self.following=defaultdict(set)  #here this self.following is the list of ids of the users followed by one specific user
        #example : userid -> [user1,user2,user3]
    def posttwitt(self,userid,twittid):
        self.twitters[userid].append((self.time,twittid))  #here as you can see, we are appending both the time as well as the twitt id based on the given user id 
        self.time+=1
        #in our default dict
    def follow(self,followerid,followeeid):
        self.following[followerid].add(followeeid)
    def unfollow(self,followerid,followeeid):
        self.following[followerid].discard(followeeid)  
    def getnewsfeed(self,userid):  #now for this function we need to retrieve the 10 most recent twitts either posted by this user himself or the persons he follows
        ans = []
        heap = []
        for t in self.twitters[userid]:
            heapq.heappush(heap,(t))  
            while len(heap)>10:
                heapq.heappop(heap)
        for followee in self.following[userid]:
            for t in self.twitters[followee]:
                heapq.heappush(heap,(t))  
                while len(heap)>10:
                    heapq.heappop(heap)
        while heap:
            ans.append(heapq.heappop(heap)[1])   #here we are using index 1 cause we have also inserted the time while inserting the tweet 
        return ans[::-1]        #as the recent twitts has the higher counts or time so we are reversing the ans as the heap always returns the minimum value while we are using pop
t=Twitter()
t.posttwitt(1,2)  #time complexity : O(1) space complexity : O(T)  total number of tweets
t.posttwitt(2,6)
t.getnewsfeed(1)  #time complexity : O(Tu + Tf)  here Tf is the total number of tweets of the user or follower and Tf is the total number of tweets of the followed users
t.follow(1,2)     #time complexity : O(1)
t.getnewsfeed(1)
t.unfollow(1, 2)  #time complexity : O(1)
t.posttwitt(1,7)  #time complexity : O(1)
print(t.getnewsfeed(1))
                    

#minimum cost to connect sticks
def minimumcost(sticks):
    heap = []
    for num in sticks:
        heapq.heappush(heap,num)
    totalcost=0    
    while len(heap)>1:
        firstcost = heapq.heappop(heap)  
        secondcost = heapq.heappop(heap)
        cost = firstcost+secondcost
        totalcost+=cost
        heapq.heappush(heap,cost)
    return totalcost    

print(minimumcost([1, 8, 3, 5]))
#time complexity : O(NlogN) 
#space complexity : O(N)
