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
    #post traversal using one stack
    def onepostorder(self,root):
        stack = []
        ans = []
        current=root
        lastvisited = None
        while stack or current:
            if current:
                stack.append(current)
                current=current.left
            else:
                peeknode=stack[-1]
                if peeknode.right and peeknode.right !=lastvisited:  #if the right child node of the current peeknode exists then we go to the left subtree from this right child node
                    current=peeknode.right
                else:
                    lastvisited=stack.pop()
                    ans.append(lastvisited.data)    

        return ans
    def preinpo(self,root):
        stack = []
        pre,po,ino=[],[],[]
        stack.append((root,1))  #initially we always start with root node and as it is being visited for the very first time , we start with 1
        while stack:
            node,time=stack.pop()
            if time == 1:
                pre.append(node.data)
                stack.append((node,2))
                if node.left:
                    stack.append((node.left,1))  #as its left node is also being visited for the very first time
            elif time == 2:
                ino.append(node.data)
                stack.append((node,3))
                if node.right:
                    stack.append((node.right,1))
            else:
                po.append(node.data)     
        return pre,ino,po   
    #maximum depth in a binary tree    
    def maximumdepth(self,root):
        d=0  
        queue=deque([root])
        while queue:
            for _ in range(len(queue)):  #this for loop checks the whole left and right child nodes at the current level
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            d+=1
        return d    
    def checkheight(self,root):
        if root is None:
            return 0
        return max(self.checkheight(root.left),self.checkheight(root.right)) + 1   #here +1 represents the addition of this current node
    def checkbalanced(self,root):
        if root is None:  #if there is no root or we reach a point of no nodes as all the above level condition of balance is true,then finally we return true
            return True
        leftheight = self.checkheight(root.left)
        rightheight=self.checkheight(root.right)
        if abs(leftheight-rightheight) > 1:  #if the difference in height between leftsubtree and right subtree from current node is greater than 1 then we return false
            return False
        return self.checkbalanced(root.left) and self.checkbalanced(root.right)  #checking for both left and right subtree
    #optimal approach
    def optimalcheckbalanced(self,root):
      def check(root):
        if root is None:
            return 0
        lh=check(root.left)
        rh=check(root.right)
        if lh==-1 or rh == -1:
            return -1
        if abs(lh-rh)>1:  #whenever we find that the difference between left height and right height is greater than 1 we return -1
            return -1
        return max(lh,rh) + 1 
      return check(root)!=-1  #here we are checking if the check function returns -1 or not
    def diameterbinarytree(self,root):
        self.diameter=0
        def calculatediameter(root):
            if root is None:
                return 0
            leftheight=calculatediameter(root.left)
            rightheight=calculatediameter(root.right)
            self.diameter=max(self.diameter,leftheight+rightheight)  #diameter is the sum of the leftsubtree and rightsubtree at every parent node at every level
            return max(leftheight,rightheight) + 1  
            
            
        calculatediameter(root)   
        return self.diameter     
pr=Allsolution()
z=pr.buildtree(  [1, 2, 3, None, 4, None, 5])  
l=pr.buildtree( [3, 9, 20, None, None, 15, 7])
print(pr.levelorder(l))
print(pr.solvepostorder(z,[]))  #time complexity : O(N)  #space complexity : O(N)
print(pr.preorderiteration(z))  #time complexity : O(N)  #space complexity : O(N)
print(pr.inordertraversal(z))
print(pr.iterativepostorder(z))  #time complexity : O(N) + O(logN) as we are also using the reverse method
print(pr.onepostorder(z)) #time complexity : O(N) space complexity : O(N)
print(pr.preinpo(z))
print(pr.maximumdepth(z))
print(pr.checkbalanced(z))
print(pr.optimalcheckbalanced(z))
print(pr.diameterbinarytree(z))  #time complexity : O(N)  #space complexity : O(N)



           




    
