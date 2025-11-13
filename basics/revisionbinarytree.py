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
            

#revision of inorder traversal using stack
class Iterativeinorder:
    def __init__(self):
        pass
    class Node:
        def __init__(self,data,left=None,right=None):
            self.data=data
            self.left=left
            self.right=right
    def maketree(self,array):  #this function is used for making a binary tree
        root=self.Node(array[0])
        queue=deque([root])   #storing the very first index
        n=len(array)
        i=1
        while queue:
            current = queue.popleft()
            if i<n and array[i] is not None:
                current.left=self.Node(array[i])
                queue.append(current.left)
            i+=1
            if i<n and array[i] is not None:
                current.right=self.Node(array[i])
                queue.append(current.right)
            i+=1
        return root
    #post order traversal
    #the logic behind the postorder traversal is that , we do the loop of pushing root,then right then left in our stack 2 from stack 1 ,
    #then at last we reverse the stack 2 which gives us left,right and root which is the final post order traversal
    def iterativepostorder(self,root):   
        temp = []
        temp.append(root)
        ans = []
        stack = []
        while temp:
            current = temp.pop()  #this is the root
            stack.append((current.data))
            if current.left:      #this is the left
                temp.append(current.left)
            if current.right:      #this is the right
                temp.append(current.right)
        while stack:
            ans.append(stack.pop())
        return ans     
    def solveinordertraversal(self,root):
        stack = []
        ans = []
        current = root
        while stack or current:
            while current:   #as long as we have the left of the current root , we append its left to the stack
                stack.append(current)
                current=current.left
            current=stack.pop()   #this will be the root which doesnot has any left children node 
            ans.append(current)
            current=current.right   #then we move towards the right of that root whose left nodes are done going through
        return ans    
ii=Iterativeinorder()
a=ii.maketree( [1, None, 2, 3])
print(ii.solveinordertraversal(a))
print(ii.iterativepostorder(a))
#time complexity : O(N)
#space complexity : O(N)

  
           

#post order traversal using one stack
class Iterativepostorder:
    class Node:
        def __init__(self,data,left=None,right=None):
            self.data=data
            self.left=left
            self.right=right
    def __init__(self):
        pass
    def buildtree(self,array):
        root=self.Node(array[0])  #first of all we are making a node with the first element from an array
        queue=deque([root])
        i=1
        n=len(array)
        while queue:
            current = queue.popleft()
            if i<n and array[i] is not None:
                current.left=self.Node(array[i])
                queue.append(current.left)
            i+=1
            if i<n and array[i] is not None:
                current.right = self.Node(array[i])
                queue.append(current.right)
            i+=1        
        return root
    def solveiterativepostorder(self,root):
        #the logic behind this iterative postorder is that , we go towards the left end ofthe binary tree , and then after reaching a point where there is no left end,
        #we check the right end of the top element in a stack which is the last or recently touched node, then we check its right, if true then we again go towards its left end by using the same loop with current
        #if no then it means this is our first left end node to be appended in our answer , and if its the right node of the new top node in our stack , then
        ans = []
        stack = []
        current = root
        while stack or current:
            if current:  #this condition of a loop is for going to the left end of the node first
                stack.append(current)
                current=current.left
            else:
                temp=stack[-1].right  #then if there is no more left , we move towards the right end of the top element in a tree
                if temp:   #if there is the right end then we change current to temp so that we can again move towards the left end of this current node which lies at the right end of the previous node
                    current=temp
                else: #here this else part is reached only when the whole right subtree is reached from the current parent node which is the top most element in a stack currently
                    temp=stack.pop()     
                    ans.append(temp.data) #here we are doing this cause it means now we have the left most children node of a binary tree
                    while stack and temp==stack[-1].right:  #and if this is the right child node of the parent node in a stack,which is the top most element in a stack then it means we have also finished with the right subtree of this current parent node or top element in a stack
                        #so we can safely pop this and append this in our ans as we have already appended the left as well as right subtree nodes of this parent node
                        temp=stack.pop()
                        ans.append(temp.data)
        return ans                
ip=Iterativepostorder()
p=ip.buildtree( [1, 4, None, 4, 2])
print(ip.solveiterativepostorder(p))
#time complexity : O(N)
#space complexity : O(N)



#preorder traversal of a binary tree
class Allsolution:
    def __init__(self):
        pass
    class Node:
        def __init__(self,data,left=None,right=None):
            self.data=data
            self.left=left
            self.right=right
    def buildtree(self,array):
        root=self.Node(array[0])
        queue=deque([root])
        n=len(array)
        i=1
        while queue:
            current=queue.popleft()
            if i<n and array[i] is not None:
                current.left=self.Node(array[i])
                queue.append(current.left)
            i+=1
            if i<n and array[i] is not None:
                current.right=self.Node(array[i])
                queue.append(current.right)
            i+=1
        return root
    def solvepreorder(self,root,ans):
        if root is None:
            return
        ans.append(root.data)
        self.solvepreorder(root.left,ans)
        self.solvepreorder(root.right,ans)
        return ans
    def solveinorder(self,root,ans):
        if root is None:
            return
        self.solveinorder(root.left,ans)
        ans.append(root.data)
        self.solveinorder(root.right,ans)
        return ans
    def solvepostorder(self,root,ans):
        if root is None:
            return
        #in the post order first we go to the left subtree then we go right subtree
        self.solvepostorder(root.left,ans)   
        self.solvepostorder(root.right,ans)
        ans.append(root.data)
        return ans
    def levelorder(self,root):
        queue=deque([root])
        ans = []
        while queue:
            levelvalues = []

            for _ in range(len(queue)):  #this for loop is for storing the node values at the current level 
                #And also storing the left as well as right nodes of every nodes at the current level
                current = queue.popleft()
                levelvalues.append(current.data) 
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            if len(levelvalues)>0:
                ans.append(levelvalues)            
        return ans   
        #preorder traversal using iteration
    def preorderiteration(self,root):
        ans=[]
        queue=deque([root])
        while queue:
            current=queue.popleft()
            ans.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return ans    
    def inordertraversal(self,root):
        current = root
        stack=[]
        ans=[]
        while stack or current:
            while current:   #first we go all the way to the left subtree
                stack.append(current)
                current=current.left
                
            current=stack.pop()    #then we append this leftest node value
            ans.append(current.data)  
            current=current.right   #and we change into the right subree
        return ans
    #post order traversal using 2 stacks
    def iterativepostorder(self,root):
        stack1=[]
        stack2=[]
        stack1.append(root)
        while stack1:
            current=stack1.pop()
            stack2.append(current.data)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)    
        return stack2[::-1]     





                    

pr=Allsolution()
z=pr.buildtree([1, 4, None, 4, 2])  
l=pr.buildtree( [3, 9, 20, None, None, 15, 7])
print(pr.levelorder(l))
print(pr.solvepostorder(z,[]))  #time complexity : O(N)  #space complexity : O(N)
print(pr.preorderiteration(z))  #time complexity : O(N)  #space complexity : O(N)
print(pr.inordertraversal(z))
print(pr.iterativepostorder(z))


#level order traversal
#in the level order traversal , we are tasked to return the node values in each level in their own array in a final ans variable





    
