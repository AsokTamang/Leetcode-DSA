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




    


       
    
     

