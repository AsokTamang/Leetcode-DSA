#level order traversal
#in the level order traversal,we traverse from left to right of every level in a binary tree
from collections import deque
def levelorder(root):
    n=len(root)
    queue=deque([0])  #storing the very first index
    ans = [ ]
    while queue:
        levelsize = len(queue)  #this stores the size of the level in a binary tree
        levelvalues = []    #this stores the numbers at the current level
        for _ in range(levelsize):   #and of course we must loop based on the size of the level
            index = queue.popleft()  #here we are using popleft , cause in levelorder traversal, we always traverse from left to right
            if index<n and root[index] is not None:
                levelvalues.append(root[index])
                leftind = 2*index + 1
                rightind = 2 * index + 2
                queue.append(leftind)
                queue.append(rightind)
        if len(levelvalues)>0:
            ans.append(levelvalues) 
    return ans
print(levelorder([3, 9, 20, None, None, 15, 7]))               
#time complexity : O(N)
#space complexity : O(N)

#preorder traversal
#preorder means the root comes before the left and right respectively
def preordertraversal(root):
    n=len(root)
    stack=[]
    stack.append(0)  #storing the first index initially
    ans = []
    while stack:
        index = stack.pop()
        if index<n and root[index] is not None:
            ans.append(root[index])
            stack.append(2*index + 2)  #storing the right index first
            stack.append(2*index + 1)  #then storing the left index
    return ans 
print(preordertraversal([1, 4, None, 4, 2]))      
#time complexity : O(N)
#space complexity : O(N)  
            


    
