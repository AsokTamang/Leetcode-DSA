#Rotate a LL
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)
class linkedlist:
    def __init__(self):
        self.head=None
    def countlength(self):   #here this function counts the number of nodes or calculate the length of the given linked list
        itr=self.head
        c=0
        while itr:
            itr=itr.next
            c+=1
        return c    
    def rotatell(self,k):  #here k is the number of rotations that we must do for the given linked list
     length=self.countlength()
     if k>length and k%length==0:  #if the value of k is the multiple of the length of the given linked list then the linked will stay unchanged after k number of rotations
         return self.head
     elif k>length:   #if the value of k is way greater and k is not exactly divided by the length of the linked list then the remainder that we get by dividing k with the length of the linked list is the required number of rotations
         k=k%length  
     k=int(k)
     tailnode=length-k
     itr=self.head
     while itr.next:
         itr=itr.next
     itr.next=self.head
     itr=self.head
     c=1
     while itr and c< tailnode:
         itr=itr.next
         c+=1
     self.head=itr.next
     itr.next=None
     return self.head 
    def printdatas(self):
        itr=self.head
        v=[]
        while itr:
            v.append(str(itr.data))
            itr=itr.next
        return ','.join(v)        

c=linkedlist()
c.head=Node(1,None)
c.head.next=Node(2,None)
c.head.next.next=Node(3,None)
c.head.next.next.next=Node(4,None)
c.head.next.next.next.next=Node(5,None)
c.rotatell(4)
print(c.printdatas())



         
#word search
#the question has given us the board of size n*m and we must check if the given target word exists in the board or not.
def wordsearch(board,target):
    rows = len(board)   #number of rows
    cols=len(board[0]) #number of columns
    path=set()
    def dfs(r,c,index):
     if index==len(target):  #if the column index gets out of range
         return True
     if r<0 or c<0 or r>=rows or c>=cols or target[index]!=board[r][c] or (r,c) in path:
         return False
     #if the above conditions have not met or reached without going false then
     path.add((r,c))
     res= dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1)
     path.remove((r,c)) #backtracking
     return res
     
         
     


    

    #this loop is for going through every row and column indexed and if any one of the row and column position returns true after going through complete recursion , then it means we have found the word
    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):   #if this recursion algo is true then we return true
                return True
    return False        
print(wordsearch( [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] , "SEE"))
#time complexity : O(N*2^N)
#space complexity : O(N*2^N)

#rat in maze
#the question is asking us to find every possible way that a rat can reach from the first row and column position [0,0] upto the last row and column position which is [n-1,n-1]
def ratinmaze(grid):
    rows = len(grid)  #number of rows
    cols=len(grid[0])  #number of columns
    ans = []
    nums = []
    path=set()
    if grid[0][0] == 0:  #if the very first row and column index is 0 then it means the rat cannot even move from this very first index
        return -1
    def solveratinmaze(r,c):
        if r==rows-1 and c==cols-1:  #if our r and c index reaches the very last index of the grid which is rows-1 and cols-1, then it means the rat has reached the ending of the grid. 
            ans.append(''.join(nums.copy()))
            return
        path.add((r,c))
        
        if r-1>=0 and grid[r-1][c]==1 and (r-1,c) not in path:
            nums.append('U')
            solveratinmaze(r-1,c)
            nums.pop()
        if c-1>=0 and grid[r][c-1]==1 and (r,c-1) not in path:
            nums.append('L')
            solveratinmaze(r,c-1)
            nums.pop()    
        if r+1<rows and grid[r+1][c] == 1 and (r+1,c) not in path:  #if the very next downward position in the same column has value 1 then it means the rat can move in this downward position
            nums.append('D')
            solveratinmaze(r+1,c)  #then we recursively go towards this next row
            nums.pop()
        if c+1<cols and grid[r][c+1] == 1 and (r,c+1) not in path:  #if the very next right position in the same row has the value 1 then it means the rat can move in this right position
            nums.append('R')
            solveratinmaze(r,c+1)  #then we recursively go towards this next column
            nums.pop()
        path.remove((r,c)) #backtracking for removing this path
    solveratinmaze(0,0)  
    return ans if ans else -1
print(ratinmaze([ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]))
#time complexity : O(4^N*M)  as we have 4 options of going left-right-up-down at each indices and N is the number of rows and M is the number of columns
#space complexity : O(N*M)   as for the space too in the worst case the space complexity will be O(N*M) for every indices


            