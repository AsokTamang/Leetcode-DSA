class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)

    # Delete all occurrences of a key in DLL


class doublell:
    def __init__(self):
        self.head = None

    def removekey(self, k):
        # first of all , we are checking the head of our double linked list and removing the k from it.
        if self.head.data == k:
            self.head = self.head.next
            self.head.prev = None
        itr = self.head
        while itr:
            if (
                itr.data == k
            ):  # first of all we are checking if the current node consits of the data k
                if (
                    itr.next
                ):  # then we check if its not the last node which consists of k then
                    itr.prev.next = itr.next
                    itr.next.prev = itr.prev
                else:  # if its the last node then we destroy the current node by pointing the next of the previous node to none
                    itr.prev.next = None
            itr = (
                itr.next
            )  # as usual we always move to the next node after all the calculation and comparisons.
        return self.head

    # time complexity : O(N)
    # space complexity : O(1)
    def bruteremovekey(self, k):
        a = []
        itr = self.head
        while itr:
            a.append(str(itr.data))
            itr = itr.next
        a = [
            num for num in a if num != str(k)
        ]  # this loop is for removing the target k from a and as our datas are stored as string, we are comparing the string version of k with the datas
        self.head = Node(a[0], None, None)
        itr = self.head
        for data in a[1:]:
            itr.next = Node(data, itr, None)
            itr = itr.next
        return self.head

    # time complexity : O(N)
    # space complexity : O(N)

    # Find Pairs with Given Sum in Doubly Linked List
    # brute appeoach
    def brutefindsum(self, k):
        itr = self.head
        a = []
        while itr:
            a.append(int(itr.data))
            itr = itr.next
        n = len(a)  # length of the total datas
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                if a[i] + a[j] == k:
                    ans.append([min(a[i], a[j]), max(a[i], a[j])])
        return ans

    # time complexity : O(N+M)  here N is the length of the given double linked list and M is the length of the answer
    # space complexity : O(N^2)
    def optimalalfindsum(self, k):
        itr = self.head
        a = []
        while itr:
            a.append(int(itr.data))
            itr = itr.next
        n = len(a)
        # here a is the collection of datas of nodes of a double linked list
        left = 0  # this is our first index
        right = n - 1  # this is our last index
        ans = []
        while left <= right:
            if a[left] + a[right] == k:
                ans.append([a[left], a[right]])
                left += 1
                right -= 1
            elif a[left] + a[right] > k:
                right -= 1
            elif a[left] + a[right] < k:
                left += 1
        return ans

    # time complexity : O(N)
    # space complexity : O(N+M)

    # Remove duplicated from sorted DLL
    def bruteremoveduplicates(self):
        itr = self.head
        s = set()
        while itr:
            s.add(itr.data)
            itr = itr.next
        s = list(s)
        self.head = Node(s[0], None, None)
        itr = self.head
        for data in s[1:]:
            itr.next = Node(data, itr, None)
            itr = itr.next
        return self.head

    # time complexity : O(N)
    # space complexity : O(N)

    def optimalremoveduplicates(self):
        itr = self.head
        while (
            itr and itr.next
        ):  # here we are running the loop till we have a node and the next node of the current node
            if itr.data == itr.next.data:
                itr.next = (
                    itr.next.next if itr.next.next else None
                )  # if its not the last second last node then we can move to next.next else none only if the datas of second last node and last node are same
                if itr.next:
                    itr.next.prev = itr  # if the next node of the current node exists then we set the previous of this next node to the current node otherwise it will be just none or empty node.

            else:
                itr = itr.next
        return self.head

    # time complexity : O(N)
    # space complexity : O(1)
    

    # reverse LL in a group of given size k
    def optimalreversal(self,head, k):
        if head is None or  head.next is None:
            return head
        c=0
        itr=head
        while itr and c<k:
            itr=itr.next
            c+=1
        if c<k:  #if the count or the length of the linked list is still lesser than k then we just return the head , inorder to preserve this linked list as it was before, by returning the head
            return head      
        itr=head
        prev=None
        c=0
        while itr and c<k:
            front=itr.next
            itr.next=prev
            prev=itr
            itr=front
            c+=1
        if self.head is head:
            self.head=prev
        if front:  #if the next node still exists then we use the recursion
            head.next=self.optimalreversal(front,k)  #and for the recursion, we use the next node of the current node as the head in our main function inorder to link the previous head and the current next node
        return prev            
        #time complexity : O(N)
        #space complexity : O(1)
    

    def bruterotatell(self,k):
        c=0
        
        while c<k:
            itr=self.head
            while itr.next:
                prev=itr
                itr=itr.next
            lastnode=itr   #so this is the last node of the current shifted linked list
            prev.next=None   #then we just destroy the  last node  
            #and first of all we must destroy the previous node's next 
            lastnode.next=self.head  #then the next of the last node will be the  current head of the linked list
            self.head=lastnode  #then this last node will be the new head of the linked list.
            
            c+=1
        return self.head 
    #time complexity : O(N*k)
    #space complexity : O(1)
    def countlength(self):
        c=0
        itr=self.head
        while itr:
            itr=itr.next
            c+=1
        return c  #this is the total number of nodes or the length of the linked list    
    def optimalrotatell(self,k):
        k=int(k)
        length=self.countlength() # this gives us the length of the linked list
        if k>length and k%length==0:  #if the value of k is exactly divisible by the length of the linked list then the linked list will stay original as before
            return self.head
        elif k> length and k%length>0:
            k=k%length
        itr=self.head
        target=length-k #this is our target node which must be the tail of the new linked list
        while itr:
            prev=itr
            itr=itr.next
        prev.next=self.head #now we connected the tail of the original linked list to the head of the original linked list
        c=0
        itr=self.head
        while itr and c<target:
            temp=itr
            itr=itr.next  #as the next node is already stored here in itr, we must make this itr the head of the new linked list after the completion of the loop with c variable
            c+=1
        temp.next=None  
        self.head=itr
        return self.head
    #time complexity : O(N)
    #space complexity : O(1)








    def printdatas(self):
        itr = self.head
        v = []
        while itr:
            v.append(str(itr.data))
            itr = itr.next
        return ",".join(v)


c = doublell()
c.head = Node(1, None, None)
c.head.next = Node(2, c.head, None)
c.head.next.next = Node(3, c.head.next, None)
c.head.next.next.next = Node(4, c.head.next.next, None)
c.head.next.next.next.next = Node(5, c.head.next.next.next, None)
print(c.optimalrotatell(4))
print(c.printdatas())
