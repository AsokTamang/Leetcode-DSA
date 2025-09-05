from collections import defaultdict


class Node:
    def __init__(self, data, next):
        self.next = next
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def optimalmiddlelist(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    # time complexity : O(N)
    def brutemiddlelist(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        mid = (
            count // 2
        )  # this gives us the middle value or middle index in our doubly linked list
        c = 0
        itr = self.head
        while (
            c < mid
        ):  # here again we are declaring c = 0 which takes us to the mid indexed node , then we return this particular node
            c += 1
            itr = itr.next
        return itr.data

    # time complexity : O(N)
    # space complexity : O(1)

    def adddatas(self, datas):
        self.head = Node(
            datas[0], None
        )  # here we are making the very first element of a given array the head of the linked list
        current = self.head

        for data in datas[1:]:  # then we loop from the index 1 to the last
            current.next = Node(data, None)
            current = current.next
        return self.head


ll = LinkedList()
ll.adddatas([1, 2, 3, 4, 5])
print(ll.brutemiddlelist())
print(ll.optimalmiddlelist())


# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def optimalreversal2(head):
    if head is None or head.next is None:
        return head
    mainhead = optimalreversal2(head.next)
    front = head.next
    front.next = head
    head.next = None
    return mainhead


def printdatas(head):
    itr = head
    value = ""
    while itr:
        value += str(itr.data) + ","
        itr = itr.next
    return value


# recursion output
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
headd = optimalreversal2(head)
print(printdatas(headd))


class Lnkedlst:
    def __init__(self):
        self.head = None

    def adddatas(self, datas):
        self.head = Node(datas[0], None)
        itr = self.head
        for data in datas[1:]:
            itr.next = Node(data, None)
            itr = itr.next
        return self.head

    # brute approach
    def brutereversal(self):
        a = []
        itr = self.head
        while itr:
            a.append(itr.data)
            itr = itr.next
        return ",".join(a[::-1])  # this code reverses the obtained linked list

    # time complexity : O(N)
    # space complexity : O(N)
    # in the optimal approach 1 of reversing the linked list , what we are doing is storing the previous of the itr as prev,
    def optimalreversal1(self):
        itr = self.head
        prev = None
        while itr:
            front = itr.next
            itr.next = prev  # the next of the current node will be the previous
            prev = itr  # And this prev will change to the current node

            itr = front  # and as we need to move to our next node we are doing itr=front as front has stored our original next or inital next of the node
        self.head = prev
        return prev  # here at the last iteration , the head of the linked list will be stored in a prev. So, we are returning the prev.

    # time complexity : O(N)
    # space complexity : O(1)

    # in the second optimal approach of reversing the linked list , what we are doing is using the recusrion method of breaking down the  larger or longer linked list into smaller linked list
    def printdatas(self):
        itr = self.head
        value = ""
        while itr:
            value += str(itr.data) + ","
            itr = itr.next
        return value


ll1 = Lnkedlst()
ll1.adddatas(["a", "b", "c", "d", "e"])
print(ll1.optimalreversal1())
print(ll1.printdatas())


# Detect a loop in a linked list
# Given the head of a singly linked list. Return true if a loop exists in the linked list or return false.
# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index(0-based) of the node from where the loop starts. Note that pos is not passed as a parameter.


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LL:
    def __init__(self):
        self.head = None

    def adddatas(self, datas):
        self.head = Node(datas[0], None)
        itr = self.head
        for data in datas[1:]:
            itr.next = Node(data, None)
            itr = itr.next

    def optimaldetectloop(self):
        if self.head is None:
            return None
        else:
            slow = self.head
            fast = self.head
            while fast or fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
        return False

    def detectloop(self):
        if self.head is None:
            return None
        else:
            itr = self.head
            m = {}
            count = 0
            while itr:
                if itr in m:
                    return m[
                        itr
                    ]  # if the node exists which means the node is reconnected or relinked that tells us there is a loop inside the linked list then ofcourse we return the position at which this loop exists.
                m[itr] = (
                    count  # here what we are doing is storing each and everyy nodes based on their respective positions
                )
                count += 1
                itr = itr.next

        return (
            -1
        )  # here we are returning -1 if the loop doesnot exists in the linked list

    # time complexity : O(N)
    # space complexity : O(1)


if __name__ == "__main__":
    a = LL()
    a.adddatas([1, 2, 3, 4, 5])
    s = a.head
    while s.next:
        s = s.next
    s.next = a.head.next

    # here after the while loop we are at the last node then again we are making the next of this last node to the head , which means we are again linking the last node to the head then ofcourse there exists a loop.
    print(a.optimaldetectloop())
    print(a.detectloop())


# Find the starting point in LL
# Given the head of a singly linked list, the task is to find the starting point of a loop in the linked list if it exists. Return the starting node if a loop exists; otherwise, return null.
# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos denotes the index (0-based) of the node from where the loop starts.
# Note that pos is not passed as a parameter.


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class algolinkedlst:
    def __init__(self):
        self.head = None

    def optiamlstartpoint(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (
                slow == fast
            ):  # now if we come to the point or the node where the slow and the fast meets then we need the node position of fast
                slow = (
                    self.head
                )  # then we are reassigning the slow with the head of the node , then we are start moving by one from both slow as well as fast which is not self.head right now , which is the value we got after detecting a cycle
                while (
                    slow != fast
                ):  # then as long as we donot meet the node where slow is not equal to the fast , then we keep moving both slow and fast by one node
                    slow = slow.next
                    fast = fast.next
                return slow  # then there comes a point or node where the slow meets the fast if there exists a cycle, then we return this current value of slow
        return (
            -1
        )  # if we donot find the cycle and there is no loop then we just return -1

    def brutestartpoint(self):
        itr = self.head
        count = 0
        m = {}
        while itr:
            if (
                itr in m
            ):  # if the itr is already existed in m then it means there exists a cycle so we are returning it's position
                return m[itr]
            m[itr] = (
                count  # here we are storing the itr as the key and its position in the linked list as the value , pair
            )
            count += 1
            itr = itr.next
        return -1  # if the cycle is not detected then we return -1

    # time complexity : O(N)
    # space complexity : O(N)


j = algolinkedlst()
j.head = Node(1, None)
j.head.next = Node(2, None)
j.head.next.next = Node(3, None)
j.head.next = (
    j.head
)  # as we are reconnecting the link or next of our last node to the head of this current linked list , we get the starting point 0
print(j.optiamlstartpoint())

# Length of loop in LL
# Given the head of a singly linked list, find the length of the loop in the linked list if it exists. Return the length of the loop if it exists; otherwise, return 0.
# A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos is used to denote the index (0-based) of the node from where the loop starts.
# Note that pos is not passed as a parameter.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(
        self,
    ):  # this constructor is used to return the node in the form of string by using it's corresponding data
        return str(self.data)


class llst:
    def __init__(self):
        self.head = None

    def brutecountlength(self):
        itr = self.head
        count = 1  # as we are determing the length of the nested loop in a linked list , we must start with the count = 1
        m = {}  # this m stores the length of the nested loop
        while itr:
            if itr in m:
                return (
                    count - m[itr]
                )  # this calculation returns the actual lenght or the number of nodes in a nested loop
            m[itr] = count
            count += 1
            itr = itr.next
        return 0

    # time complexity : O(N)
    # space complexity : O(N)
    # of course in the optimal approach we use tortorise and hare method
    def optimalcountlength(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (
                slow == fast
            ):  # then by using slow and fast method, we comes to a point where slow becomes equal to fast
                length = (
                    1  # then we start calculating the length by assuming it initally 1
                )
                fast = (
                    fast.next
                )  # and we are moving the fast to next iteration or next node , inorder to calculate the length
                while slow != fast:
                    length += 1
                    fast = fast.next
                return length
        return 0

    # time complexity : O(N)
    # space complexity : O(1)

    # in the brure approach down below what we are doing is, we are storing the datas of the linked list in an external storage, then if this is equal to it's reverse form, then of course the linked list is palindrome
    # otherwise , its not palindrome

    # time complexity : O(N)
    # space complexity : O(N)
    def printdatas1(self):
        itr = self.head
        val = ""
        while itr:
            val += str(itr.data) + ","
            itr = itr.next
        return val

    # in the reverselinked list approach what we are doing is using the recursion method inorder to reverse the given linked list by changing the direction of next connecting the nodes
    def reverselinkedlist(self, node=None):
        if node is None:
            node = self.head

        if node is None or node.next is None:
            self.head = node
            return node
        mainhead = self.reverselinkedlist(node.next)
        front = node.next
        front.next = node
        node.next = None
        return mainhead

    def brutepalindrome(self):
        m = []
        itr = self.head
        while itr:
            m.append(
                itr.data
            )  # here we are storing each and every datas of the linked list inside a list called m which is first in last out
            itr = itr.next
        itr = self.head
        while itr:
            if (
                itr.data != m.pop()
            ):  # here m.pop deletes the last most data from the list , and if the linked list is palindrome then of course the head must match with the last data in a linked list
                return False
            # if the first most data matches with the last most data then it is showing that the given linked list might be palindrome so thats why we are moving to the next iteration after deleting the last most element from the list m
            itr = itr.next
        return True  # if the reversed form of a linked list matches with the original linked list then ofcourse the linked list is palindrome.

    # time complexity : O(N)
    # space complexity : O(N)

    def optimalpalindrome(self):
        slow = self.head
        fast = self.head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        m1 = slow  # here m1 represents the last node of the first half of the linked list
        m2 = (
            slow.next
        )  # here m2 represents the first node or the head node of the second half of the linked list

        # the below code is for reversing the second half of the linked list
        prev = None
        while m2 != None:
            front = (
                m2.next
            )  # here we are storing the next of the m2 which is head of the second half right now
            m2.next = prev  # then that front next will be the previous node
            prev = m2
            m2 = front
        a = self.head
        while (
            prev
        ):  # here we are using while prev cause after reversing the second half of the linked list , our last node of the linked list
            # which is the head of the second half of the linked list is stored in a variable prev
            if a.data != prev.data:
                return False
            a = a.next
            prev = prev.next
        return True

    # time complexity : O(N)
    # space complexity : O(1)

    def brutesegregrate(self):
        a = []
        itr = self.head
        while itr and itr.next.next:
            a.append(itr)  # here we are storing the datas of odd indices in the array a
            itr = itr.next.next
        if itr:
            a.append(itr)

        itr = self.head.next
        while itr and itr.next.next:
            a.append(itr)
            itr = itr.next.next
        if itr:
            a.append(itr)
        self.head = a[0]
        main = self.head
        for data in a[1:]:  # here we are looping the data from 1st index
            main.next = data
            main = main.next
        return a

    # time complexity : O(N)
    # space complexity : O(N)

    def optimalsegregrate(self):
        odd = self.head
        even = even_head = self.head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return self.head

    # time complexity : O(N)
    # space complexity : O(1)

    def optimalremove(self, index):
        prev = None  # this first loop is for reversing the original linked list
        itr = self.head
        while itr:
            front = itr.next
            itr.next = prev
            prev = itr
            itr = front
        # then this down below code is for finding the index and removing the node
        self.head = prev
        itr = self.head
        c = 1
        while itr:
            if c == index - 1:
                itr.next = itr.next.next
                itr = itr.next
                c += 1
            else:
                itr = itr.next
                c += 1
        # then this final code is for reversing the obtained list to take it back to the original list
        prev = None
        itr = self.head
        while itr:
            front = itr.next
            itr.next = prev
            prev = itr
            itr = front
        self.head = prev  # after reversing the linked list , we must always assign the new head of the linked list.
        return self.head

    # time complexity : O(N)
    # space complexity : O(1)

    # sort linked list
    # Given the head of a singly linked list. Sort the values of the linked list in non-decreasing order and return the head of the modified linked list.

    def brutesortll(self):
        itr = self.head
        a = []
        while itr:
            a.append(itr.data)
            itr = itr.next
        a = sorted(a)
        self.head = Node(a[0], None)
        itr = self.head
        for data in a[1:]:
            itr.next = Node(data, None)
            itr = itr.next
        return self.head

    # time complexity : O(NlogN)
    # space compleity : O(N)

    # optimal approach of sorting the linked list
    # using merge sort method
    def findmiddle(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, l, r):
        dummynode = Node(-1)  #here we are just making the dummy head of our going to be new sorted linked list
        temp = dummynode
        while l and r:
            if l.data <= r.data:
                temp.next = l
                l = l.next
            else:
                temp.next = r
                r = r.next
            temp = temp.next
        while l:
            temp.next = l
            l = l.next
            temp=temp.next
        while r:
            temp.next = r
            r = r.next
            temp=temp.next

        return dummynode.next  #and as we need to return the head of the linked list , we are using dummynode.next cause dummynode was just the dummy head for our newly created linked list

    def optimalsort(self, head):
        if head is None or head.next is None:
            return head
        mid = self.findmiddle(head)
        right = (
            mid.next
        )  # here right means the head of the right half which is mid.next in our case
        mid.next = None  # then we destroy this mid.next inorder to keep only the left half using the head of the linked list.
        # down below what we are doing is we are recursively splitting the linked list into two halves
        lefthead = self.optimalsort(head)
        righthead = self.optimalsort(right)
        return self.merge(lefthead, righthead)

    def printdatas(self):
        itr = self.head
        val = ""
        while itr:
            val += str(itr.data) + ","

            itr = itr.next
        return val


v = llst()
v.head = Node(10, None)
v.head.next = Node(2, None)
v.head.next.next = Node(11, None)
v.head.next.next.next = Node(4, None)
v.head.next.next.next.next = Node(1, None)
print(v.brutesortll())
print(v.optimalremove(3))
print(v.optimalsort(v.head))
print(v.printdatas())


# Check if LL is palindrome or not
# Given the head of a singly linked list representing a positive integer number. Each node of the linked list represents a digit of the number, with the 1st node containing the leftmost digit of the number and so on. Check whether the linked list values form a palindrome or not. Return true if it forms a palindrome, otherwise, return false.
# A palindrome is a sequence that reads the same forward and backwards.


# Segregate odd and even nodes in LL
# Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list.
# Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.


# Remove Nth node from the back of the LL
# Given the head of a singly linked list and an integer n. Remove the nth node from the back of the linked List and return the head of the modified list. The value of n will always be less than or equal to the number of nodes in the linked list.
