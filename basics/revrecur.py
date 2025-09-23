#Palindrome partitioning
def palindromepartition(s):
    ans= []
    value = []
    def solvepalind(index):
        if index == len(s):
           
            ans.append(value.copy())
            return
        for i in range(index , len(s)):
            substring=s[index:i+1]
            if substring == substring[::-1]:
                value.append(substring)
                solvepalind(i+1)
                value.pop()   #backtracking

                
    solvepalind(0)
    return ans
print(palindromepartition('aabaa'))
#time complexity : O(N*2^N)  we have only two choices which are whether we want to add this current number or not
#space complexity : O(N*N)  in the worst cases all the substrings are palindrome


#word search
def wordsearch(board,word):
    rows = len(board)
    cols = len(board[0])
    path=set()
    def dfs(r,c,index):
        if index == len(word):  
            return True
        if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[index]:  #if the passed rows or columns become out of bounds and the indexed number of word is not equal to the current passed row and column indexed number then we return false
            return False
        path.add((r,c))   #if the passed row and column index is valid then we add this passed row and column index in our path , cause we can't use the same duplicate row and column index
        result = dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c+1,index+1) or dfs(r,c-1,index+1)
        path.remove((r,c)) #backtracking
        return result
    for i in range(rows):   #we pass every possible row and column indices and check if the dfs function is true for them or not , if its true for every possible row and column indices then we return true
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False    #otherwise we return false     
print(wordsearch( [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] , "ABCCED"))


#N Queen
#The challenge of arranging n queens on a n × n chessboard so that no two queens attack one another is known as the "n-queens puzzle."
#Return every unique solution to the n-queens puzzle given an integer n. The answer can be returned in any sequence.
#Every solution has a unique board arrangement for the placement of the n-queens, where 'Q' and '.' stand for a queen and an empty space, respectively.

def nqueen(n):  #N is the number of queens that we must enter n*n size chessboard
    board=[['.'] * n for _ in range(n)]  #this will produce n*n size board which will be like this [['.','.','.','.']['.','.','.','.']['.','.','.','.']['.','.','.','.']]
    rows = len(board)
    cols=len(board[0])
    ans = []
    def isvalid(row,col):
        for i in range(col): #checking horizontally in the left direction
            if board[row][i] == 'Q':
                return False
        r=row
        c=col
        while r>=0 and c>=0:  #Checking diagonally which goes in upward direction
            if board[r][c] == 'Q':
                return False
            r-=1
            c-=1
        r=row
        c=col     
        while r<rows and c>=0:  #checking diagonally which goes in downward direction
            if board[r][c] == 'Q':
                return False
            r+=1
            c-=1
        return True            
    def solvenqueen(c):
        if c == cols:   #if our column index becomes equal to the value of the number of columns then it means we have successfully inserted n number of queens in n*n size chess board.  
            ans.append([''.join(row) for row in board])
            return
        for i in range(rows):
                if isvalid(i,c):
                    board[i][c]='Q'
                    solvenqueen(c+1)
                    board[i][c] = '.' #backtracking

    solvenqueen(0)
    return ans
print(nqueen(4))
#time complexity : O(N! *N)  here N! is for the algo where with every increase in the row value the chance of inserting the queen decreases due to the horizontal and diagonal checks and N is for appending the N rows in the ans variable
#space complexity : O(N*N)


#Rat in a Maze
def ratinmaze(grid,n):
    ans=[]
    nums=[]
    if grid[0][0] == 0:  #if the very first coordinate of the grid is 0,0 then it means the rat cannot move from the starting position
        return -1
    path=set()
    path.add((0,0))
    def solveratinmaze(r,c):
        if r==n-1 and c == n-1:  #if the passed row and column indeices are at the last coordinates of the maze then it means the rat has reached the end of the maze
            ans.append(''.join(nums.copy()))
            return
         #looping through rows
        if c+1<n and grid[r][c+1] == 1 and (r,c+1) not in path:
            nums.append('R')
            path.add((r,c+1))

            solveratinmaze(r,c+1)
            nums.pop()
            path.remove((r,c+1))
        if r+1<n and grid[r+1][c] ==1 and (r+1,c) not in path:
            nums.append('D')
            path.add((r+1,c))
            solveratinmaze(r+1,c)
            nums.pop()
            path.remove((r+1,c))
        if c-1>=0 and grid[r][c-1] == 1 and (r,c-1) not in path:
            nums.append('L')
            path.add((r,c-1))

            solveratinmaze(r,c-1)
            nums.pop()
            path.remove((r,c-1))
        if r-1>=0 and grid[r-1][c] ==1 and (r-1,c) not in path:
            nums.append('U')
            path.add((r-1,c))
            solveratinmaze(r-1,c)
            nums.pop()
            path.remove((r-1,c))

    solveratinmaze(0,0)
    return ans
print(ratinmaze( [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ],4))
#time complexity : O(4^N*N)  all possible 4 choices are correct for the current co-ordinate of N*N grid
#space complexity : O(N*N)   

#wordbreak
#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
#Note that the same word in the dictionary may be reused multiple times in the segmentation.

def wordbreak(s,worddict):
    worddict=set(worddict)  #removing the duplicate words from  the given word dictionary
    n=len(s)  #length of the given string
    d=[False] * (n+1)  #making n+1 length of string consisting of false values  which denotes whether we can break the given string at the particular indices or not
    d[n] =True  #making the very last index true cause this very last index is out of the bound of the given string.
    for i in range(n-1,-1,-1):
        for word in worddict:
         if i+ len(word)<=len(s) and  s[i:i+len(word)]== word:  #the first condition check whether the length of the given word is way greater or not compared to the substring from the given string
             d[i] = d[i+len(word)]   #if the substring matches with any of the word from the word dict then we make the boolean at this particular index which is equal to the boolean of i+len(word) which is matched
         if d[i] == True:   #then if the match comes true then we break out of the for-loop of word and goes to next iteration
             break 
    return d[0]        
print(wordbreak("leetcode", ["leet","code"])) 
#time complexity : O(N*K*W)  N is the number of length of the given string and K is the number of words in the worddict and W is the length of the word as we have used the slicing method inside the two for-loop. 
#space complexity : O(N+K)  where N is the denotion variable size and K is the set of worddict  


#M coloring problem
def mcolor(M,N,graph):  #M is the number of colors we must use and N is the number of vertices
    colorset=[0] *  N  #here we store the color used for each vertex
    neighbourvertex = [[] for _ in range(N)]   #here we store the neighbours of every index
    for u,v in graph:
        neighbourvertex[u].append(v)
        neighbourvertex[v].append(u)
    def isvalid(color,vertex):   #this function checks whether the passed color is valid for the passed index or not.
        for index in neighbourvertex[vertex]:
            if colorset[index] == color:
                return False
        return True    
    def solvemcolor(index):
        if index==N:  #means all the vertices are colored
            return True
        for i in range(1,M+1):  #here we are starting the loop for color from 1 cause initially we have made the color storage from 0 index
          
                if isvalid(i,index):
                    colorset[index]=i  #here i is denoting the color
                    if solvemcolor(index+1):
                        return True
                    
                    colorset[index] = 0  #backtracking  #if the recursion returns false then we remove that inserted color and go with another color
        return False  #if the index doesnot reach the N then it means the for loop has ended without returning true so 
    #we obviously return false.
    return solvemcolor(0)            
print(mcolor(2,3,[ (0, 1) , (1, 2) , (0, 2) ]))        
#time complexity : O(N*M)
#space complexity : O(N)


#sudoku solver
def sudokusolver(board):
    def isvalid(row,col,digit):
        for i in range(9):
            if board[i][col] == str(digit):
                return False
            if board[row][i] == str(digit):
                return False
            if board[3*(row//3) + (i//3)][3*(col//3) + (i%3) ] == str(digit):
                return False
        return True
    def solvesudoku():
     for i in range(9):
        for j in range(9):
            if board[i][j]=='.':  #first of all we go through every indices and check if the current index has no digit or just .
             for c in range(1,10):
                 if isvalid(i,j,c):
                     board[i][j]=str(c)
                     if solvesudoku():
                         return True   
                     board[i][j]='.'  #backtracking
             return False  #if the recursion doesnot work then we just return false
     return True        #if there was no any error then we return true        
    solvesudoku()  #we must call the solve function inorder to print the final board
    return board
solved=(sudokusolver( [ [ ".", ".", ".", ".", ".", ".", "7", ".", ".", ], [ "7", ".", "5", ".", ".", ".", "9", ".", ".", ], [ ".", ".", ".", "9", "7", "5", "4", "3", "1", ], [ "9", ".", ".", ".", "4", "1", ".", ".", "7", ], [ ".", "5", ".", "8", ".", "7", "6", "4", ".", ], [ ".", "7", ".", ".", "2", ".", ".", ".", ".", ], [ ".", "4", ".", ".", ".", ".", ".", "6", "9", ], [ "1", "6", ".", "4", "3", ".", ".", ".", ".", ], [ ".", ".", ".", ".", "6", "2", "3", ".", "4", ] ]))                 
for row in solved:
    print(row)    
#time complexity : O(9^M)  here M is the number of empty spaces or in the worst case O(9^N^2)  where all the N indices has empty spaces
#space complexity : O(N)                 


#expression add operators
def addoperators(nums,target):
    ans=[]
    def solveoperators(index,presum,prev,path):
        if index == len(nums):
            if presum == target:
                ans.append(''.join(path))
            return
        for i in range(index,len(nums)):
            substring=nums[index:i+1]    
            currvalue=int(substring)
            if len(substring) > 1 and substring[0] == '0':
                break
            if index == 0:
                solveoperators(i+1,presum + currvalue,currvalue,path+[substring])

            else:              
                solveoperators(i+1,presum + currvalue,currvalue,path+['+']+[substring])
                solveoperators(i+1,presum - currvalue,-currvalue,path+['-']+[substring])
                solveoperators(i+1,presum-prev+prev*currvalue,prev*currvalue ,path+['*']+[substring])

    solveoperators(0,0,0,[])
    return ans
print(addoperators('0232',8))
#time complexity : O(3^N) as we have 3 signs to use for each index
# space complexity : O(N) 


                


