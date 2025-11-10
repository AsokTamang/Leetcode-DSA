#for full a binary tree, all the nodes in a tree must have either 0 node or 2 nodes which are left and right children nodes for a parent node
#complete binary tree is a binary tree whose last level is either full or the children nodes are in the left hand side
#perfect binary tree is a binary tree whose last levels or the last children nodes are in the same level
#balanced binary tree is a binary tree whose maximum height is logN where N is the total number of nodes in a binary tree.




#so in a binary tree , there are two ways to solve a problem and they are :
#BFS - breadth first search , in this search we go through every levels of the binary tree or every breadths of the binary tree
#DFS -depth first search , in this search we go deeper into the depth of the binary tree
#for DFS there are 3 types and they are:
#Inorder traversal
#in the inorder traversal the root node will be in the middle of left and right binary subtree
#Preorder traversal 
#in the preorder traversal , the root node will come before the left and right binary subtree  
#postorder traversals 
#in the postorder traversal, the root node will come after the left and right binary subtree


#Preorder Traversal
#Given root of binary tree, return the preorder traversal of the binary tree.
class Solution:
    class Node:
        def __init__(self,data=0,left=None,right=None):
         self.data=data
         self.left=left
         self.right=right
    def __init__(self):
       pass
    def buildtree(self,array,i=0):  #this function is for building the binary tree
       if i>=len(array) or array[i] is None:
          return 
       root = self.Node(array[i])  #here we are creating a node with the value of element at index i of the given array
       root.left=self.buildtree(array,2*i+1)
       root.right = self.buildtree(array,2*i+2)
       return root
    
    def preorder(self,root,arr):
        if root is None:
           return
        arr.append(root.data)
        self.preorder(root.left,arr)  #here we are recursively going to the left children node or lets say left binary subtree
        self.preorder(root.right,arr)  #here we are recurvisly going to the right binary subtree
        return arr
s=Solution()
r=s.buildtree( [5, 1, 2, 8, None, 4, 5, None, 6])  #here we are storing the root of the designed binary tree
print(s.preorder(r,[]))
#time complexity : O(N)
#space complexity : O(N)

from collections import deque
#Inorder Traversal
class Inorder:
    class Node:
       def __init__(self,data=0,left=None,right=None):
          self.data=data
          self.left=left
          self.right=right
    def __init__(self):
      pass
    def buildtree(self,array):
       root = self.Node(array[0])
       queue=deque([root])  #creating the root element by using node and storing it in a queue
       i = 1  #starting from the index 1
       while i<len(array):
          current = queue.popleft()  #this is the main logic of popping the element which was just appended 
          if i<len(array) and array[i] is not None:
             current.left=self.Node(array[i])
             queue.append(current.left)
          i+=1
          if i<len(array) and array[i] is not None:
             current.right=self.Node(array[i])
             queue.append(current.right)
          i+=1

       return root
       

       
       
    def inorder(self,root,arr):
        if root is None:
           return 
        self.inorder(root.left,arr)  #first we are visiting the left subtree based on the current root node
        arr.append(root.data)        #then only we append the roots data after all the left nodes or subtrees are visisted and their datas are appended
        self.inorder(root.right,arr)
        return arr
i = Inorder()
mainroot = i.buildtree([1, None, 2, 3])
print(i.inorder(mainroot,[]))    
#time complexity : O(N)
#space complexity : O(N)

   
#postorder traversal
class Postorder:
    class Node:
      def __init__(self,data,left=None,right=None):
         self.data=data
         self.left=left
         self.right=right
    def buildtree(self,array):
       root = self.Node(array[0])  #first element of an array is the root element of our tree for now
       queue=deque([root])
       i = 1
       while i<len(array):
          current = queue.popleft()
          if i<len(array) and array[i] is not None:
             current.left=self.Node(array[i])
             queue.append(current.left)
          i+=1
          if i<len(array) and array[i] is not None:
             current.right = self.Node(array[i])
             queue.append(current.right)
          i+=1
       return root
    def makepostorder(self,root,arr):
       if root is None:
          return
       self.makepostorder(root.left,arr)  #we first go with the left node 
       self.makepostorder(root.right,arr) #then we go with the right node
       arr.append(root.data)  #then at last we append the root's data
       return arr
p=Postorder()
po=p.buildtree( [1, 4, None, 4, 2]) 
print(p.makepostorder(po,[]))   
#time complexity : O(N)
#space complexity : O(N)
    
                 
#level order traversal
def levelorder(root):
   n=len(root)
   i=0
   ans=[]
   queue=deque([0])  #here we are storing the root index in our queue
   while queue:
      levelsize = len(queue)
      levelvalues = []
      for _ in range(levelsize):
         index = queue.popleft()  #as we are going from left to right of every level of given tree, we are usign the popleft here to get the left index first
         #as we have appended the left index in our queue storage first
         if index < n and root[index] is not None:
            levelvalues.append(root[index])
            leftind=2*index + 1
            rightind = 2*index + 2
            queue.append(leftind)  #here we are storing the left index and right index
            queue.append(rightind)
      if len(levelvalues)>0:
          ans.append(levelvalues)       
   return ans         
print(levelorder([3, 9, 20, None, None, 15, 7]))       
#time complexity : O(N)
#space compelxity : O(N)   


#Preorder Traversal using stack
def preorderstack(root):
   stack =[]
   stack.append(0)
   result = []
   n=len(root)
   
   while stack :
      index = stack.pop()   
      if index<n and root[index] is not None:
         result.append(root[index])
         stack.append(2*index+2)  #first we append the right index based on the current index
         stack.append(2*index+1)  #then we append the left index based on the current index
   
   return result
print(preorderstack( [5, 1, 2, 8, None, 4, 5, None, 6])) 
#time complexity : O(N)
#space complexity : O(N)  


                 
    


       
    
     

