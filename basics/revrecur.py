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