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