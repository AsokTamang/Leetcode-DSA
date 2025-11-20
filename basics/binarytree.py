# for full a binary tree, all the nodes in a tree must have either 0 node or 2 nodes which are left and right children nodes for a parent node
# complete binary tree is a binary tree whose last level is either full or the children nodes are in the left hand side
# perfect binary tree is a binary tree whose last levels or the last children nodes are in the same level
# balanced binary tree is a binary tree whose maximum height is logN where N is the total number of nodes in a binary tree.


# so in a binary tree , there are two ways to solve a problem and they are :
# BFS - breadth first search , in this search we go through every levels of the binary tree or every breadths of the binary tree
# DFS -depth first search , in this search we go deeper into the depth of the binary tree
# for DFS there are 3 types and they are:
# Inorder traversal
# in the inorder traversal the root node will be in the middle of left and right binary subtree
# Preorder traversal
# in the preorder traversal , the root node will come before the left and right binary subtree
# postorder traversals
# in the postorder traversal, the root node will come after the left and right binary subtree


# Preorder Traversal
# Given root of binary tree, return the preorder traversal of the binary tree.
class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
class Solution:
    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        pass

    def buildtree(self, array, i=0):  # this function is for building the binary tree
        if i >= len(array) or array[i] is None:
            return
        root = self.Node(
            array[i]
        )  # here we are creating a node with the value of element at index i of the given array
        root.left = self.buildtree(array, 2 * i + 1)
        root.right = self.buildtree(array, 2 * i + 2)
        return root

    def preorder(self, root, arr):
        if root is None:
            return
        arr.append(root.data)
        self.preorder(
            root.left, arr
        )  # here we are recursively going to the left children node or lets say left binary subtree
        self.preorder(
            root.right, arr
        )  # here we are recurvisly going to the right binary subtree
        return arr


s = Solution()
r = s.buildtree(
    [5, 1, 2, 8, None, 4, 5, None, 6]
)  # here we are storing the root of the designed binary tree
print(s.preorder(r, []))
# time complexity : O(N)
# space complexity : O(N)

from collections import defaultdict, deque


# Inorder Traversal
class Inorder:
    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        pass

    def buildtree(self, array):
        root = self.Node(array[0])
        queue = deque(
            [root]
        )  # creating the root element by using node and storing it in a queue
        i = 1  # starting from the index 1
        while i < len(array):
            current = (
                queue.popleft()
            )  # this is the main logic of popping the element which was just appended
            if i < len(array) and array[i] is not None:
                current.left = self.Node(
                    array[i]
                )  # only when the i indexed element is not none we make it left
                queue.append(current.left)
            i += 1
            if i < len(array) and array[i] is not None:
                current.right = self.Node(
                    array[i]
                )  # only when the i indexed element is not none we make it right
                queue.append(current.right)
            i += 1

        return root

    def inorder(self, root, arr):
        if root is None:
            return
        self.inorder(
            root.left, arr
        )  # first we are visiting the left subtree based on the current root node
        arr.append(
            root.data
        )  # then only we append the roots data after all the left nodes or subtrees are visisted and their datas are appended
        self.inorder(root.right, arr)
        return arr


i = Inorder()
mainroot = i.buildtree([1, None, 2, 3])
print(i.inorder(mainroot, []))
# time complexity : O(N)
# space complexity : O(N)


# postorder traversal
class Postorder:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def buildtree(self, array):
        root = self.Node(
            array[0]
        )  # first element of an array is the root element of our tree for now
        queue = deque([root])
        i = 1
        while i < len(array):
            current = queue.popleft()
            if i < len(array) and array[i] is not None:
                current.left = self.Node(array[i])
                queue.append(current.left)
            i += 1
            if i < len(array) and array[i] is not None:
                current.right = self.Node(array[i])
                queue.append(current.right)
            i += 1
        return root

    def makepostorder(self, root, arr):
        if root is None:
            return
        self.makepostorder(root.left, arr)  # we first go with the left node
        self.makepostorder(root.right, arr)  # then we go with the right node
        arr.append(root.data)  # then at last we append the root's data
        return arr


p = Postorder()
po = p.buildtree([1, 4, None, 4, 2])
print(p.makepostorder(po, []))
# time complexity : O(N)
# space complexity : O(N)


# level order traversal
def levelorder(root):
    n = len(root)
    i = 0
    ans = []
    queue = deque([0])  # here we are storing the root index in our queue
    while queue:
        levelsize = len(queue)
        levelvalues = []
        for _ in range(levelsize):
            index = (
                queue.popleft()
            )  # as we are going from left to right of every level of given tree, we are usign the popleft here to get the left index first
            # as we have appended the left index in our queue storage first
            if index < n and root[index] is not None:
                levelvalues.append(root[index])
                leftind = 2 * index + 1
                rightind = 2 * index + 2
                queue.append(
                    leftind
                )  # here we are storing the left index and right index
                queue.append(rightind)
        if len(levelvalues) > 0:
            ans.append(levelvalues)
    return ans


print(levelorder([3, 9, 20, None, None, 15, 7]))
# time complexity : O(N)
# space compelxity : O(N)


# Preorder Traversal using stack
def preorderstack(root):
    stack = []
    stack.append(0)
    result = []
    n = len(root)

    while stack:
        index = stack.pop()
        if index < n and root[index] is not None:
            result.append(root[index])
            stack.append(
                2 * index + 2
            )  # first we append the right index based on the current index
            stack.append(
                2 * index + 1
            )  # then we append the left index based on the current index

    return result


print(preorderstack([5, 1, 2, 8, None, 4, 5, None, 6]))
# time complexity : O(N)
# space complexity : O(N)


from collections import deque


class Iterativeinorder:
    class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        pass

    def buildtree(self, array):
        root = self.Node(array[0])  # this will be the root element
        queue = deque([root])
        n = len(array)
        i = 1
        while queue:
            current = (
                queue.popleft()
            )  # popping the value that was stored first in a queue
            if i < n and array[i] is not None:
                current.left = self.Node(array[i])
                queue.append(current.left)
            i += 1
            if i < n and array[i] is not None:
                current.right = self.Node(array[i])
                queue.append(current.right)
            i += 1
        return root  # we must return the root element after building the tree

    def getinorder(self, root):
        ans = []
        stack = []
        current = root
        while stack or current:
            while (
                current
            ):  # this loop is for storing all the left node datas a every nodes
                stack.append(current)
                current = current.left
            # once we reach a node that has no left node then we append its value
            current = stack.pop()
            ans.append(
                current.data
            )  # then we append this major node which is the root at a time
            current = current.right  # then we go to the right
        return ans

    # postorder traversal using one stack
    def postorder(self, root):  # post order usign the only one stack
        # the logic behind this solution is we start going to the left most end of the current root ,
        # then if we find its null then we go towards right end , then
        # when it also becomes empty then we append it to the ans which is the right most end,
        # otherwise if we go to the left most of this right node
        current = root
        stack = []
        ans = []
        while stack or current:
            if (
                current
            ):  # when the current element is not null which means it has the left node child then we append it to the stack and we keep on going to the left
                stack.append(current)
                current = current.left
            else:  # but if there is no more left node then we try to go to the right
                temp = stack[-1].right  # we go to the right
                if temp:  # if the right node exists then we change the current to temp
                    current = temp
                else:
                    temp = stack.pop()
                    ans.append(temp.data)  # otherwise we add this right most node
                    while (
                        stack and temp == stack[-1].right
                    ):  # if the popped element is the right node of the top most element of a stack then we  change the temp to stack.pop() and add to the ans
                        temp = stack.pop()
                        ans.append(temp.data)
        return ans


io = Iterativeinorder()
a = io.buildtree([1, 4, None, 4, 2])
print(io.getinorder(a))
print(io.postorder(a))
# time complexity : O(N)
# space complexity : O(N)


# preorder,postorder and inorder in one traversal
class allorder:
    def __init__(self):
        pass

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def buildtree(self, array):
        root = self.Node(array[0])  # this will be the root element
        queue = deque([root])
        n = len(array)
        i = 1
        while queue:
            current = (
                queue.popleft()
            )  # popping the value that was stored first in a queue
            if i < n and array[i] is not None:
                current.left = self.Node(array[i])
                queue.append(current.left)
            i += 1
            if i < n and array[i] is not None:
                current.right = self.Node(array[i])
                queue.append(current.right)
            i += 1
        return root

    def solveallorder(self, root):
        preorder, inorder, postorder = [], [], []
        stack = []
        stack.append(
            (root, 1)
        )  # here we start with appending the root element and the index 1 which means the loop will start from preorder function
        while stack:
            element, state = stack.pop()
            if (
                state == 1
            ):  # here state represents how many time we have visited this current node
                preorder.append(
                    element.data
                )  # if its first time then it means it is in the preorder array
                stack.append((element, 2))  # then we increase its count of visited time
                if (
                    element.left
                ):  # as th preoder means root is at first then comes left-right  ,and as we have already appended the root element
                    stack.append(
                        (element.left, 1)
                    )  # we then append the left of element in the stack
            elif (
                state == 2
            ):  # if the state is 2 then it means the element must be in the inorder and also we must explore its right node
                inorder.append(element.data)
                stack.append((element, 3))
                if element.right:
                    stack.append((element.right, 1))
            else:  # if its already visited 3 times then it means it must be in the postorder and there's no need of exploring the left node and right node
                postorder.append(element.data)
        return [preorder, inorder, postorder]

    # Maximum Depth in BT
    def maximumdepth(self, root):
        depth = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            depth += 1
        return depth

    # diameter of a binary tree
    def diameterbinarytree(self, root):
        self.diameter = float("-inf")

        def checkdiameter(root):
            if root is None:
                return 0
            lh = checkdiameter(root.left)
            rh = checkdiameter(root.right)
            self.diameter = max(self.diameter, lh + rh)
            return (
                max(lh, rh, 0) + 1
            )  # and as to find the longest path from the current node , we must check the max between its left subtree and right subtree

        checkdiameter(root)
        return self.diameter

    def optimalcheckbalanced(self, root):
        def check(root):
            if root is None:  # if there is no root element then we just return 0
                return 0
            lh = check(root.left)
            rh = check(root.right)
            if lh == -1 or rh == -1:
                return (
                    -1
                )  # and at any level of nodes we find -1,we return -1 ending this check function
            if (
                abs(lh - rh) > 1
            ):  # as soon as the difference in height of subtree is greater than 1 we return -1
                return -1
            return (
                max(lh, rh) + 1
            )  # here +1 means the current node itself is counted for calculating the height and max between lh and rh means we determing the longest path from this node

        # and as the height of the subtree is the longest path
        a = check(root)
        return a != -1

    # maximum path sum
    def maximumpathsum(self, root):
        self.maxpathsum = 0

        def checksum(root):
            if root is None:
                return 0
            lh = checksum(root.left)
            rh = checksum(root.right)
            self.maxpathsum = max(
                self.maxpathsum, lh + rh + root.data
            )  # and in every recursuin level we add the current node's data for calculating the maximum path sum
            return (
                max(lh, rh) + root.data
            )  # here we are adding the current node's value with the max between the value of left subtree and right subtree from this current node

        checksum(root)
        return self.maxpathsum

    # Check if two trees are identical or not
    # brute approach
    def checktwotrees(self, root1, root2):
        ans1 = []
        ans2 = []
        queue1 = deque([root1])
        queue2 = deque([root2])
        while queue1:
            current = queue1.popleft()
            ans1.append(current.data)
            if current.left:
                queue1.append(current.left)
            if current.right:
                queue1.append(current.right)
        while queue2:
            current = queue2.popleft()
            ans2.append(current.data)
            if current.left:
                queue2.append(current.left)
            if current.right:
                queue2.append(current.right)
        return ans1 == ans2

    # time complexity : O(N)
    # space complexity : O(N)

    # optimal approach
    def optimalchecktwo(self, root1, root2):
        if not root1 and not root2:  # if both the root values are none we return true
            return True
        elif not root1 or not root2:  # if one of the root value is none we return false
            return False
        return (
            root1.data == root2.data
            and self.optimalchecktwo(root1.left, root2.left)
            and self.optimalchecktwo(root1.right, root2.right)
        )

    # time complexity : O(N)
    # space complexity : O(N)
    def getheight(self, root):
        if root is None:
            return 0
        return (
            max(self.getheight(root.left), self.getheight(root.right)) + 1
        )  # this gives us the height of left as well as right subtree

    # zigzag traversal so the zigzag traversal means we are going from left to right in one level then right to left in another level and we do this as we go to the end of the binary tree
    def spiraltraversal(self, root):
        ans = []
        queuq = deque([root])
        level = 1
        while queuq:
            values = []
            if level % 2 != 0:
                level += 1
                for _ in range(len(queuq)):
                    c = queuq.pop()
                    values.append(c.data)
                    if c.right:
                        queuq.append(c.right)

                    if c.left:
                        queuq.append(c.left)

            else:
                level += 1
                for _ in range(len(queuq)):
                    c = queuq.popleft()
                    values.append(c.data)
                    if c.right:
                        queuq.append(c.right)
                    if c.left:
                        queuq.append(c.left)
            if len(values) > 0:
                ans.append(values)
        return ans

    # time complexity : O(N)
    # space complexity : O(N)

    # optimal approach
    def optimalspiraltraversal(self, root):
        queue = deque([root])
        ans = []
        ltr = True  # left to right
        while queue:
            values = []
            for _ in range(len(queue)):
                c = queue.popleft()
                values.append(c.data)
                if c.left:
                    queue.append(c.left)
                if c.right:
                    queue.append(c.right)
            if ltr:
                ans.append(
                    values
                )  # if the condition of left to right is true then we just append the values as it is in our ans variable
            else:
                values.reverse()  # so we must reverse the values first then we can append it to our answer
                ans.append(
                    values
                )  # otherwise we just append the values but in a reverse way
            ltr = (
                not ltr
            )  # then in each iteration we just switch the direction to the opposite of the current direction in a current loop
        return ans

    def boundarytraversal(self, root):
        ans = []
        ans.append(root.data)

        def isleafnode(node):
            if (
                not node.left and not node.right
            ):  # for the node to be leafnode, it mustnot have a left as well as right child node
                return True
            return False

        def addleaves(node):
            if node is None:
                return
            if isleafnode(node):
                ans.append(node.data)
                return
            addleaves(node.left)  # recursively going towards the left subtree
            addleaves(node.right)  # then to the right subtree

        def leftboundary(node):
            current = node.left
            while current:
                if not isleafnode(current):
                    ans.append(current.data)
                current = current.left if current.left else current.right

        def rightboundary(node):
            current = node.right
            temp = []
            while current:
                if not isleafnode(current):
                    temp.append(current.data)
                current = current.right if current.right else current.left
            ans.extend(reversed(temp))

        leftboundary(root)  # first we must add the left boundary nonleaf node values
        addleaves(root)  # then we add the leaf node values
        rightboundary(root)  # then we must add the right boundary nonleaf node values
        return ans

    # so the logic for this problem is that based on the column index we must obtain the node datas ,and for this we are using the deque method as we must go from left to right while going top to bottom vertically
    from collections import defaultdict, deque

    def verticalordertraversal(self, root):
        q = deque([])
        q.append((root, 0))
        verticalmapdict = defaultdict(
            list
        )  # here we are making a map structure of the column indices as key and the list of node values in this sepcific index as value, and they act as key-value pair
        while q:
            node, column = q.popleft()
            verticalmapdict[column].append(
                node.data
            )  # here based on the column value , we are appending the node's data in the list
            if node.left:
                q.append((node.left, column - 1))
            if node.right:
                q.append((node.right, column + 1))
        return [
            (verticalmapdict[col]) for col in sorted(verticalmapdict.keys())
        ]  # here we are returning the list of node values in their own specific parent list based on the column values in a sorted valuemap dictionary

    # top view of BT
    # so the logic behind this top view solution is that we calculate the horinzontal distance and we store the horizontal distance of the node from the top view and the node as the key value pair in our dict only if there are no any nodes at the same horizontal distance
    def topview(self, root):
        m = (
            {}
        )  # this dict stores the horizontal distance and the node value as the key-value pair
        q = deque([])
        q.append((root, 0))  # as the root index is 0,0
        while q:
            node, distance = q.popleft()
            if (
                distance not in m
            ):  # here only if the current node is not covered by another node which lies at the same horizontal distance from the top view, we store this current node
                m[distance] = node.data
            if node.left:
                q.append((node.left, distance - 1))
            if node.right:
                q.append((node.right, distance + 1))
        return [
            m[distance] for distance in sorted(m.keys())
        ]  # as we have stored the distance as key

    # bottom view of a binary tree
    def bottomview(self, root):
        m = {}
        q = deque([])
        q.append(
            (root, 0)
        )  # the second index value is the horizontal distance from the root
        while q:
            node, distance = q.popleft()
            m[distance] = (
                node.data
            )  # as we are viewing from the bottom , we can override the previous nodes with the later ones
            if node.left:
                q.append((node.left, distance - 1))
            if node.right:
                q.append((node.right, distance + 1))
        return [m[distance] for distance in sorted(m.keys())]

    # right/left view of a binary tree
    def rightview(self, root):
        q = deque([root])
        ans = []
        while q:
            levelsize = len(q)
            for i in range(levelsize):
                curr = q.popleft()
                if (
                    i == levelsize - 1
                ):  # only if the i is at last index , which is the rigt most , we append its value and also we append its left as well as right in the q
                    ans.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return ans

    def leftview(self, root):
        q = deque([root])
        ans = []
        while q:
            levelsize = len(q)
            for i in range(levelsize):
                curr = q.popleft()
                if (
                    i == 0
                ):  # as we are viewing from the left side , only when the current index or position is the first one or 0, we append the data of this current node in our ans
                    ans.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    # as soon as we are the very first index , we append its value in our ans variable and also the left as well as right node in q and then we break out of the loop
        return ans

    # check for symmetrical binary trees
    def checksymmetrical(self, root):
        q = deque([])
        q.append((root.left, root.right))
        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            if (
                not left or not right
            ):  # if any one of the node lying at the opposite adjacent positions is missing, then the half tree is not mirror of the other half
                return False
            if left.data != right.data:
                return False
            q.append((left.left, right.right))
            q.append((left.right, right.left))
        return True

    # recursive nature
    def recurchecksymmetrical(self, root):
        def checksymmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.data != right.data:
                return False
            return checksymmetric(left.left, right.right) and checksymmetric(
                left.right, right.left
            )

        return checksymmetric(root.left, root.right)

    # Print root to node path in BT
    def printroottonode(self, root):
        path = []
        ans = []

        def dfs(node):
            if node is None:  #if the node is empty , we return from the reursion level
                return
            path.append(node.data) #we keep on appending the node data as long as the node is not empty  
            if not node.left and not node.right:  #this means we have reached the leaf node , so the path has been made
                ans.append(path.copy())
            dfs(node.left)
            dfs(node.right)
            path.pop()  # backtracking inorder to remove the older nodes, which has already contributed to make path

        dfs(root)
        return ans
   #LCA in binary tree
    def lca(self,root,p,q):
        if root is None:
            return 
        if root.data==p or root.data==q:  #whenever we find the node's data equal to p or q then it means this current node might be our answer
            return root.data
        #if both p and q are not found then we recursively move towards left as well as right subtree
        left = self.lca(root.left,p,q)  
        right=self.lca(root.right,p,q)
        if not left:
            return right
        elif not right:
            return left
        else:
            return root.data
        
        #time complexity : O(N)
        #space complexity : O(N)
    

    #maximum width of a binary tree
    #so the logic behind this code is that we traverse the bt in a level order and calculate the width using rigthidnex-leftindex + 1 where we calculate the leftindex by 2*index+1 and right index by 2*i+2 which are of the next nodes from the current node
    def maxmwidth(self,root):
        if root is None:
            return
        q=[(root,0)]  #for the root element , we store with the index 0
        ans = float('-inf')
        while q:
            leftmostindex = q[0][1]  #as the left most index is always at the first index
            rightmostindex = q[-1][1]  #where as the right most index is always at the last
            ans = max(ans,rightmostindex-leftmostindex+1)  #rightmost-leftmost+1 is the formula for calculating the width
            newq=[]
            for node,index in q:
                index-=leftmostindex  #here we are doing this inorder to prevernt the overflow of the data if the numbers or the indices are way too big
                if node.left:
                    newq.append((node.left,(2*index) + 1))
                if node.right:
                    newq.append((node.right,(2*index)+2))
            q=newq
        return ans

    #children sum property
    def childrensum(self,root):
        if root is None:
            return
        q=deque([root])
        while q:
            curr=q.popleft()
            if not curr.left and not curr.right:  #if both the left child and the right child is null then it means we are at the leaf node
                continue #so we continue with another iteration
            l=curr.left.data if curr.left else 0
            r=curr.right.data if curr.right else 0
            
            if curr.data!= l + r:
                return False
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            
        return True           
    #binary tree after the children sum
    def btaftersum(self,root):
        if root is None:
            return
        ans = [ ]
        q=deque([root])
        while q:
            curr=q.popleft()
            if not curr.left and not curr.right:  #if we reach the leaf node then we continue with another iteration
                ans.append(curr.data)  #we also must append the leaf node while changing the bt after the children sum
                continue   
            childsum = 0
            l=curr.left.data if curr.left else 0
            r=curr.right.data if curr.right else 0
            childsum = l+r
            if childsum>=curr.data:  #if the child sum is greater than or equal to the current node's data then we change the current node's data to child sum
                curr.data = childsum 
            else:  #if the child sum is smaller then
                if curr.left:
                    curr.left.data = curr.data
                if curr.right:
                    curr.right.data=curr.data
            ans.append(curr.data)  #here we are just appending the node with newly modified or unmodified data 
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return ans

    #print all nodes at a distance of K in BT
    def printallnodes(self,root,target,k):
        m={}
        def mappingparentchild(root):  #this function is used for storing the parent and children nodes as key-value pair where the children are stored as key and the parent nodes are stored as value
            q=deque([root])
            while q:
                curr=q.popleft()
                if curr.left:
                    m[curr.left] = curr
                    q.append(curr.left)
                if curr.right:
                    m[curr.right]=curr
                    q.append(curr.right)
        mappingparentchild(root)    
        iteration = 0
        seen = set()
        seen.add(target)
        q=deque([target])
        while q:
            if iteration==k: #at k distance
                break
            levelsize = len(q)
            for _ in range(levelsize):
                curr=q.popleft()
                if curr.left and curr.left not in seen:
                    seen.add(curr.left)
                    q.append(curr.left)
                if curr.right and curr.right not in seen:
                    seen.add(curr.right)
                    q.append(curr.right)
                if curr in m and m[curr] not in seen:
                    seen.add(m[curr]) #here we are storing the parent in our set data storage
                    q.append(m[curr]) 
            iteration+=1    
        return [node.data for node in q]
                      



        
                 
    
all = allorder()
v = all.buildtree( [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])  # O(N) for both
w = all.buildtree([1, 2, 3])
print(all.solveallorder(v))
print(all.maximumdepth(v))
print(all.optimalcheckbalanced(v))  # TC-O(N**2) and SC-O(N)
print(all.diameterbinarytree(v))
print(all.maximumpathsum(v))
print(all.optimalchecktwo(v, w))
print(all.spiraltraversal(v))
print(all.optimalspiraltraversal(v))
print(all.boundarytraversal(v))
print(all.verticalordertraversal(v))
print(all.topview(v))
print(all.bottomview(v))
print(all.rightview(v))
print(all.leftview(v))
print(all.checksymmetrical(v))
print(all.recurchecksymmetrical(v))
print(all.printroottonode(v))
print(all.lca(v,5,4))
print(all.maxmwidth(v))
print(all.childrensum(v))
print(all.btaftersum(v))
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)
print(all.printallnodes(root,root.left,2))
# time complexity : O(N)
# space complexity : O(N)
