# level order traversal
# in the level order traversal,we traverse from left to right of every level in a binary tree
from collections import defaultdict, deque


def levelorder(root):
    n = len(root)
    queue = deque([0])  # storing the very first index
    ans = []
    while queue:
        levelsize = len(queue)  # this stores the size of the level in a binary tree
        levelvalues = []  # this stores the numbers at the current level
        for _ in range(
            levelsize
        ):  # and of course we must loop based on the size of the level
            index = (
                queue.popleft()
            )  # here we are using popleft , cause in levelorder traversal, we always traverse from left to right
            if index < n and root[index] is not None:
                levelvalues.append(root[index])
                leftind = 2 * index + 1
                rightind = 2 * index + 2
                queue.append(leftind)
                queue.append(rightind)
        if len(levelvalues) > 0:
            ans.append(levelvalues)
    return ans


print(levelorder([3, 9, 20, None, None, 15, 7]))
# time complexity : O(N)
# space complexity : O(N)


# preorder traversal
# preorder means the root comes before the left and right respectively
def preordertraversal(root):
    n = len(root)
    stack = []
    stack.append(0)  # storing the first index initially
    ans = []
    while stack:
        index = stack.pop()
        if index < n and root[index] is not None:
            ans.append(root[index])
            stack.append(2 * index + 2)  # storing the right index first
            stack.append(2 * index + 1)  # then storing the left index
    return ans


print(preordertraversal([1, 4, None, 4, 2]))
# time complexity : O(N)
# space complexity : O(N)


# revision of inorder traversal using stack
class Iterativeinorder:
    def __init__(self):
        pass

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def maketree(self, array):  # this function is used for making a binary tree
        root = self.Node(array[0])
        queue = deque([root])  # storing the very first index
        n = len(array)
        i = 1
        while queue:
            current = queue.popleft()
            if i < n and array[i] is not None:
                current.left = self.Node(array[i])
                queue.append(current.left)
            i += 1
            if i < n and array[i] is not None:
                current.right = self.Node(array[i])
                queue.append(current.right)
            i += 1
        return root

    # post order traversal
    # the logic behind the postorder traversal is that , we do the loop of pushing root,then right then left in our stack 2 from stack 1 ,
    # then at last we reverse the stack 2 which gives us left,right and root which is the final post order traversal
    def iterativepostorder(self, root):
        temp = []
        temp.append(root)
        ans = []
        stack = []
        while temp:
            current = temp.pop()  # this is the root
            stack.append((current.data))
            if current.left:  # this is the left
                temp.append(current.left)
            if current.right:  # this is the right
                temp.append(current.right)
        while stack:
            ans.append(stack.pop())
        return ans

    def solveinordertraversal(self, root):
        stack = []
        ans = []
        current = root
        while stack or current:
            while (
                current
            ):  # as long as we have the left of the current root , we append its left to the stack
                stack.append(current)
                current = current.left
            current = (
                stack.pop()
            )  # this will be the root which doesnot has any left children node
            ans.append(current)
            current = (
                current.right
            )  # then we move towards the right of that root whose left nodes are done going through
        return ans


ii = Iterativeinorder()
a = ii.maketree([1, None, 2, 3])
print(ii.solveinordertraversal(a))
print(ii.iterativepostorder(a))
# time complexity : O(N)
# space complexity : O(N)


# post order traversal using one stack
class Iterativepostorder:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        pass

    def buildtree(self, array):
        root = self.Node(
            array[0]
        )  # first of all we are making a node with the first element from an array
        queue = deque([root])
        i = 1
        n = len(array)
        while queue:
            current = queue.popleft()
            if i < n and array[i] is not None:
                current.left = self.Node(array[i])
                queue.append(current.left)
            i += 1
            if i < n and array[i] is not None:
                current.right = self.Node(array[i])
                queue.append(current.right)
            i += 1
        return root

    def solveiterativepostorder(self, root):
        # the logic behind this iterative postorder is that , we go towards the left end ofthe binary tree , and then after reaching a point where there is no left end,
        # we check the right end of the top element in a stack which is the last or recently touched node, then we check its right, if true then we again go towards its left end by using the same loop with current
        # if no then it means this is our first left end node to be appended in our answer , and if its the right node of the new top node in our stack , then
        ans = []
        stack = []
        current = root
        while stack or current:
            if (
                current
            ):  # this condition of a loop is for going to the left end of the node first
                stack.append(current)
                current = current.left
            else:
                temp = stack[
                    -1
                ].right  # then if there is no more left , we move towards the right end of the top element in a tree
                if (
                    temp
                ):  # if there is the right end then we change current to temp so that we can again move towards the left end of this current node which lies at the right end of the previous node
                    current = temp
                else:  # here this else part is reached only when the whole right subtree is reached from the current parent node which is the top most element in a stack currently
                    temp = stack.pop()
                    ans.append(
                        temp.data
                    )  # here we are doing this cause it means now we have the left most children node of a binary tree
                    while (
                        stack and temp == stack[-1].right
                    ):  # and if this is the right child node of the parent node in a stack,which is the top most element in a stack then it means we have also finished with the right subtree of this current parent node or top element in a stack
                        # so we can safely pop this and append this in our ans as we have already appended the left as well as right subtree nodes of this parent node
                        temp = stack.pop()
                        ans.append(temp.data)
        return ans


ip = Iterativepostorder()
p = ip.buildtree([1, 4, None, 4, 2])
print(ip.solveiterativepostorder(p))
# time complexity : O(N)
# space complexity : O(N)


# preorder traversal of a binary tree
class Allsolution:
    def __init__(self):
        pass

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def buildtree(self, array):
        root = self.Node(array[0])
        queue = deque([root])
        n = len(array)
        i = 1
        while queue:
            current = queue.popleft()
            if i < n and array[i] is not None:
                current.left = self.Node(array[i])
                queue.append(current.left)
            i += 1
            if i < n and array[i] is not None:
                current.right = self.Node(array[i])
                queue.append(current.right)
            i += 1
        return root

    def solvepreorder(self, root, ans):
        if root is None:
            return
        ans.append(root.data)
        self.solvepreorder(root.left, ans)
        self.solvepreorder(root.right, ans)
        return ans

    def solveinorder(self, root, ans):
        if root is None:
            return
        self.solveinorder(root.left, ans)
        ans.append(root.data)
        self.solveinorder(root.right, ans)
        return ans

    def solvepostorder(self, root, ans):
        if root is None:
            return
        # in the post order first we go to the left subtree then we go right subtree
        self.solvepostorder(root.left, ans)
        self.solvepostorder(root.right, ans)
        ans.append(root.data)
        return ans

    def levelorder(self, root):
        queue = deque([root])
        ans = []
        while queue:
            levelvalues = []

            for _ in range(
                len(queue)
            ):  # this for loop is for storing the node values at the current level
                # And also storing the left as well as right nodes of every nodes at the current level
                current = queue.popleft()
                levelvalues.append(current.data)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if len(levelvalues) > 0:
                ans.append(levelvalues)
        return ans
        # preorder traversal using iteration

    def preorderiteration(self, root):
        ans = []
        queue = deque([root])
        while queue:
            current = queue.popleft()
            ans.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return ans

    def inordertraversal(self, root):
        current = root
        stack = []
        ans = []
        while stack or current:
            while current:  # first we go all the way to the left subtree
                stack.append(current)
                current = current.left

            current = stack.pop()  # then we append this leftest node value
            ans.append(current.data)
            current = current.right  # and we change into the right subree
        return ans

    # post order traversal using 2 stacks
    def iterativepostorder(self, root):
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            current = stack1.pop()
            stack2.append(current.data)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        return stack2[::-1]

    # post traversal using one stack
    def onepostorder(self, root):
        stack = []
        ans = []
        current = root
        lastvisited = None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peeknode = stack[-1]
                if (
                    peeknode.right and peeknode.right != lastvisited
                ):  # if the right child node of the current peeknode exists then we go to the left subtree from this right child node
                    current = peeknode.right
                else:
                    lastvisited = stack.pop()
                    ans.append(lastvisited.data)

        return ans

    def preinpo(self, root):
        stack = []
        pre, po, ino = [], [], []
        stack.append(
            (root, 1)
        )  # initially we always start with root node and as it is being visited for the very first time , we start with 1
        while stack:
            node, time = stack.pop()
            if time == 1:
                pre.append(node.data)
                stack.append((node, 2))
                if node.left:
                    stack.append(
                        (node.left, 1)
                    )  # as its left node is also being visited for the very first time
            elif time == 2:
                ino.append(node.data)
                stack.append((node, 3))
                if node.right:
                    stack.append((node.right, 1))
            else:
                po.append(node.data)
        return pre, ino, po

    # maximum depth in a binary tree
    def maxdepth(self, root):
        q = deque([root])
        depth = 0
        while q:
            for _ in range(
                len(q)
            ):  # this for loop appends the left as well as right child of every nodes at the current level
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            depth += 1
        return depth

    def checkheightbalanced(self, root):
        def checkheight(node):
            if node is None:
                return 0
            lh = checkheight(node.left)
            rh = checkheight(node.right)
            if (
                lh == -1 or rh == -1
            ):  # if from any side of the subtree we get -1 , we just return -1
                return -1
            if abs(lh - rh) > 1:
                return -1
            return (
                max(lh, rh) + 1
            )  # here +1 means we are also assuming this current node in the height

        return checkheight(root) != -1

    def diameterofbt(self, root):
        self.diameter = 0

        def checkdiameter(node):
            if node is None:
                return 0
            lh = checkdiameter(node.left)
            rh = checkdiameter(node.right)
            self.diameter = max(
                self.diameter, lh + rh
            )  # as the diameter means the sum of height of left subtree as well as right subtree
            return max(lh, rh) + 1  # +1 means the current node is also counted

        checkdiameter(root)
        return self.diameter

    def maximpathsum(self, root):
        self.maximsum = 0

        def checksum(node):
            if node is None:
                return 0
            lh = checksum(node.left)
            rh = checksum(node.right)
            self.maximsum = max(self.maximsum, lh + rh + node.data)
            return (
                max(lh, rh) + node.data
            )  # we only take the path from where we can get the maximum sum

        checksum(root)
        return self.maximsum

    def boundarytraversal(self, root):
        ans = []
        ans.append(root.data)

        def isleafnode(node):
            if not node.left and not node.right:
                return True
            return False

        def addleftboundary(node):
            if node is None:
                return
            curr = node.left
            while curr:
                if not isleafnode(
                    curr
                ):  # if the current node isnot a leafnode in the left subtree, then only we can append it to our ans
                    ans.append(curr.data)
                curr = curr.left if curr.left else curr.right

        def addrightboundary(node):
            if node is None:
                return
            curr = node.right
            temp = []
            while curr:
                if not isleafnode(
                    curr
                ):  # if the current node isnot a leafnode in the right subtree, then only we can append it to our ans
                    temp.append(curr.data)
                curr = curr.right if curr.right else curr.left
            ans.extend(reversed(temp))

        def addleaves(node):
            if node is None:
                return
            if isleafnode(node):  # here as we are adding the leafnodes
                ans.append(node.data)
                return
            addleaves(node.left)  # then we recursively go to the left subtree
            addleaves(node.right)  # and then to the right subtree

        addleftboundary(root)
        addleaves(root)
        addrightboundary(root)
        return ans

    # check whether the given binary tree is symmetrical or not
    ##recursion method
    def recurchecksymmetric(self, root):
        def checksymmetric(left, right):
            if (
                not left and not right
            ):  # if both of the left and right nodes are none then its true for this first recursion depth
                return True
            if not left or not right:
                return False
            if left.data != right.data:
                return False
            return checksymmetric(left.left, right.right) and checksymmetric(
                left.right, right.left
            )

        return checksymmetric(root.left, root.right)

    def iterativechecksymmetric(self, root):
        def checksymmetric(left, right):
            q = deque([])
            q.append(left)
            q.append(right)
            while q:
                curr1 = q.popleft()
                curr2 = q.popleft()
                if not curr1 and not curr2:
                    continue
                if not curr1 or not curr2:
                    return False
                if curr1.data != curr2.data:
                    return False
                if curr1.left:
                    q.append(curr1.left)
                if curr2.right:
                    q.append(curr2.right)
                if curr1.right:
                    q.append(curr1.right)
                if curr2.left:
                    q.append(curr2.left)
            return True

        return checksymmetric(root.left, root.right)

    # check if two trees are identical or not
    def checkidentical(self, p, q):
        def checkone(first, second):
            if not first and not second:
                return True
            if not first or not second:
                return False
            if first.data != second.data:
                return False
            return checkone(first.left, second.left) and checkone(
                first.right, second.right
            )

        return checkone(p, q)

    def spiraltraversal(self, root):
        q = deque([root])
        ans = []
        ltr = True
        while q:
            levelvalues = []
            for _ in range(len(q)):
                current = q.popleft()
                levelvalues.append(current.data)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            if not ltr:
                levelvalues.reverse()
                ans.append(levelvalues)
            else:
                ans.append(levelvalues)
            ltr = not ltr  # just switching the ltr condition in each while loop
        return ans

    # boundary traversal
    def btraversal(self, root):
        ans = []

        def isnotleaf(node):
            if node.left and node.right or node.left or node.right:
                return True
            return False

        def addleftboundary(node):
            if node is None:
                return
            if isnotleaf(node):
                ans.append(node.data)
            addleftboundary(node.left)

        def addrightboundary(node):
            if node is None:
                return
            if isnotleaf(node):
                ans.append(node.data)
            addrightboundary(node.right)

        def addleavesnode(node):
            if node is None:
                return
            if not isnotleaf(node):
                ans.append(node.data)
            addleavesnode(node.left)  # first we go from left side
            addleavesnode(node.right)  # then we go to the right subtree

        ans.append(root.data)
        addleftboundary(root.left)
        addleavesnode(root)
        addrightboundary(root.right)
        return ans

    from collections import defaultdict

    def vordertraversal(self, root):
        q = deque([(root, 0)])
        distancemap = defaultdict(
            list
        )  # we must make a default dict having the distance as a key and the list of node values appearing at that distance as values
        ans = []
        while q:
            curr, index = q.popleft()
            distancemap[index].append(curr.data)
            if (
                curr.left
            ):  # in the left side , the node index will always be decreasing by 1 as we go more to the left side
                q.append((curr.left, index - 1))
            if (
                curr.right
            ):  # where as towards the right side, the node index will go on increasing by 1 , as we move more towards the right side
                q.append((curr.right, index + 1))
        for distance in sorted(
            distancemap.keys()
        ):  # and inorder to return the answer from leftmost , we are using sorting the keys of default dict
            ans.append(distancemap[distance])
        return ans

    # top view of a binary tree
    def topviewofbt(self, root):
        q = deque([(root, 0)])
        m = {}
        while q:
            curr, index = q.popleft()
            if index not in m:
                m[index] = (
                    curr.data
                )  # storing the index and the node data as key-value pair
            if curr.left:
                q.append((curr.left, index - 1))
            if curr.right:
                q.append((curr.right, index + 1))
        ans = []
        for position in sorted(
            m.keys()
        ):  # here we are using sorted inorder to move from left to right
            ans.append(m[position])
        return ans

    # bottom view of a binary tree
    def bottomviewofbt(self, root):
        q = deque([(root, 0)])
        m = {}
        ans = []
        while q:
            curr, index = q.popleft()
            m[index] = curr.data  # storing the index and node data as key-value pair
            if curr.left:
                q.append((curr.left, index - 1))
            if curr.right:
                q.append((curr.right, index + 1))
        for position in sorted(m.keys()):
            ans.append(m[position])
        return ans

    # right view of a binary tree
    def rightview(self, root):
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if (
                    i == size - 1
                ):  # as we  are viewing from the right side , the index or the position of the targeted node must be the last index
                    ans.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans

    # left view of a binary tree
    def leftview(self, root):
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                if i == 0:
                    ans.append(curr.data)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans

    # check for symmetrical BTs
    def checksymmetric(self, root):
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.data != right.data:
                return False
            return check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right)

    # Print root to node path in BT
    def printroottonode(self, root):
        ans = []
        path = []

        def dfs(node):
            if node is None:
                return
            path.append(node.data)
            if (
                not node.left and not node.right
            ):  # if we reach the leaf node then it means our one of the path has been reached
                ans.append(path.copy())
            dfs(node.left)
            dfs(node.right)
            path.pop()  # here we are backtracking

        dfs(root)
        return ans


pr = Allsolution()
z = pr.buildtree([1, 2, 3, None, 5, None, 4])
l = pr.buildtree([1, 2, 2])
print(pr.levelorder(l))
print(pr.solvepostorder(z, []))  # time complexity : O(N)  #space complexity : O(N)
print(pr.preorderiteration(z))  # time complexity : O(N)  #space complexity : O(N)
print(pr.inordertraversal(z))
print(
    pr.iterativepostorder(z)
)  # time complexity : O(N) + O(logN) as we are also using the reverse method
print(pr.onepostorder(z))  # time complexity : O(N) space complexity : O(N)
print(pr.preinpo(z))
print(pr.maxdepth(z))
print(pr.checkheightbalanced(z))
print(pr.diameterofbt(z))
print(pr.maximpathsum(z))
print(pr.checkidentical(z, l))
print(pr.spiraltraversal(z))
print(pr.btraversal(z))
print(pr.vordertraversal(z))
print(pr.topviewofbt(z))
print(pr.bottomviewofbt(z))
print(pr.rightview(z))
print(pr.leftview(z))
print(pr.checksymmetric(z))
print(pr.printroottonode(z))
