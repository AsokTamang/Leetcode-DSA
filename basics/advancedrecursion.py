# Sort a Stack
# You are given a stack of integers. Your task is to sort the stack in descending order using recursion, such that the top of the stack contains the greatest element. You are not allowed to use any loop-based sorting methods (e.g., quicksort, mergesort). You may only use recursive operations and the standard stack operations (push, pop, peek/top, and isEmpty).
def sortastack(a):
    if len(a) <= 1:
        return
    top = (
        a.pop()
    )  # we keep on deleting the lastmost element or the top element from the stack a till the base case is reached
    sortastack(a)
    # after the base case is reached then we keep on adding the element but based on recursive sorting method
    insertelem(a, top)
    return a[
        ::-1
    ]  # here we are reversing the list cause the question is asking us to return the list where the top most element is at the leftmost side of an array.


def insertelem(a, element):
    if (
        not a or element >= a[-1]
    ):  # if the passed element is greater than or equal to the topmost element then we append this element to the stack and return
        a.append(
            element
        )  # as the question is asking us to return the top most element at the leftmost side of an array.
        return
    # otherwise  we remove the top most element in a stack which is greater than the passed element
    top = a.pop()
    insertelem(
        a, element
    )  # then we keep on passing the eleemenet till the condition of element > topmost element in the stack is reached

    a.append(top)  # then only we append this popped top most element


print(sortastack([4, 1, 3, 2]))
# time complexity : O(N^2)  in the worst case
# space complexity : O(N)


# Reverse a stack
# You are given a stack of integers. Your task is to reverse the stack using recursion. You may only use standard stack operations (push, pop, top/peek, isEmpty). You are not allowed to use any loop constructs or additional data structures like arrays or queues.
# Your solution must modify the input stack in-place to reverse the order of its elements.


def reverseastack(stack):
    # our base case
    if len(stack) <= 1:
        return
    top = (
        stack.pop()
    )  # we keep on removing the top most or the right most element from the given stack
    reverseastack(stack)
    insertelement(
        stack, top
    )  # when the base case is reached then we keep on inserting the elements based on the reversed way
    return stack


def insertelement(stack, element):
    if not stack:
        stack.append(element)
        return
    else:
        top = (
            stack.pop()
        )  # if there are numbers in a stack then we again remove the topmost element
        insertelement(stack, element)  # then we insert the newly passed element
        stack.append(
            top
        )  # then only  we append the popped top element which was the first element passed


print(reverseastack([4, 1, 3, 2]))
# time complexity : O(N^2)
# space complexity : O(N)


# Generate Binary Strings Without Consecutive 1s
# Given an integer n, return all binary strings of length n that do not contain consecutive 1s. Return the result in lexicographically increasing order.
# A binary string is a string consisting only of characters '0' and '1'.


def genbinary(n):  # n is the length of the string
    numbers = ["0"] * n
    ans = []
    solvebinary(0, True, ans, numbers)  # here we are passing the first index
    return ans


def solvebinary(index, flag, ans, numbers):
    if index >= len(
        numbers
    ):  # this is our base case where if the index becomes greater than or equal to the length of the formed numbers
        ans.append("".join(numbers))
        return
    numbers[index] = (
        "0"  # whether the flag is true or false , we just add 0 at the current index
    )
    solvebinary(index + 1, True, ans, numbers)
    if (
        flag == True
    ):  # onle if the flag is true then we also have a option of adding 1 in the current index, after adding one we just make the flag to false
        numbers[index] = "1"
        solvebinary(
            index + 1, False, ans, numbers
        )  # and again go deeper into our recursion by increasing the index
        numbers[index] = (
            "0"  # then while backtracking , we again make the value at the current index 0
        )


print(genbinary(3))
# time complexity : O(2^N)
# space complexity : O(N)


# Generate Parentheses
# Given an integer n.Generate all possible combinations of well-formed parentheses of length 2 x N.
def generateparentheses(n):  # here n is the number of pair of parenthesis
    ans = []
    datas = []
    solveparenthesis(0, 0, ans, datas, n)
    return ans


def solveparenthesis(
    opentag, closetag, ans, datas, n
):  # here opentag represents the number of opening tag used and closetag represents the number of closing tag used
    if opentag == closetag == n:
        ans.append("".join(datas))
        return
    if opentag < n:
        datas.append("(")
        solveparenthesis(opentag + 1, closetag, ans, datas, n)
        datas.pop()  # backtracking
    if closetag < opentag:
        datas.append(")")
        solveparenthesis(opentag, closetag + 1, ans, datas, n)
        datas.pop()  # backtracking


print(generateparentheses(3))
# time complexity : O(2^N)
# space complexity : O(N*2^N)


# Power Set
# Given an array of integers nums of unique elements. Return all possible subsets (power set) of the array.
# Do not include the duplicates in the answer.


def powerset(array):
    ans = []
    nums = []
    solvepowerset(0, ans, nums, array)
    return ans


def solvepowerset(index, ans, nums, array):
    if index >= len(
        array
    ):  # if the passed index becomes greater than or equal to the length of an array then we append the nums in our ans variable
        ans.append(
            nums.copy()
        )  # here we are appending the copy of nums instead not the nums itself
        return
    nums.append(
        array[index]
    )  # for creating the subset we keep on appending every numbers from  an array one at a time and go deep into recursion
    solvepowerset(index + 1, ans, nums, array)
    # while also by deleting the appended number and going into recursion
    nums.pop()
    solvepowerset(index + 1, ans, nums, array)


print(powerset([1, 2, 3]))
# time complexity : O(n*2^n)
# space complexity : O(n) + O(n*2^n)
# so the main logic behind backtracking is finding that edge or the condition where we come with two ways and we choose both the ways but in recursive approach


# print all the subsequences of the given array
def getsubsequence(
    a, k
):  # here a is the array given of which we need to find the subsequence
    ans = []
    nums = []
    getsubse(0, 0, ans, nums, a, k)

    return len(ans)


def getsubse(index, currentsum, ans, nums, a, k):
    if index >= len(a):
        if currentsum == k:
            ans.append(nums.copy())
        return
    nums.append(a[index])
    getsubse(
        index + 1, currentsum + a[index], ans, nums, a, k
    )  # only if we append the indexed number , the sum will increase
    nums.pop()
    getsubse(
        index + 1, currentsum, ans, nums, a, k
    )  # otherwise the sum will remain same


print(getsubsequence([4, 9, 2, 5, 1], 10))
# time complexity : O(n*2^n )  M is the length of the list of the subsequent arrays
# space complexity :  O(n*2^n )

# Check if there exists a subsequence with sum K
# Given an array nums and an integer k. Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.


def checksubse(array, k):
    def solvesubsek(index, summ, k):
        if index >= len(array):  # the base case
            return summ == k

        if solvesubsek(
            index + 1, summ + array[index], k
        ):  # if any of the function or the branch recursion of including the numbers at the given index satisfies the condition , then immediately we return True
            return True

        if solvesubsek(
            index + 1, summ, k
        ):  # if any of the function of excluding the number at the given index satisfies the condition after hitting the base case , then we return true
            return True
        return False  # after all the recursion of every possible branches , if it still doesnot satisfy the condition then we return false

    return solvesubsek(
        0, 0, k
    )  # here we are passing the 0 for the first index and ofcourse the pre sum of an array will be 0 at first


print(checksubse([4, 3, 9, 2], 10))
# time complexity : O(2^N)  where N is the length of the array
# space complexity : O(N) due to the recursive nature


# Combination Sum
# the given question is asking us to use the number at the given index multiple times
def combinationsum(array, k):
    nums = []
    ans = []

    def solvecombination(index, presum, ans, nums):
        if index >= len(array) or presum > k:
            return
        if presum == k:
            ans.append(["".join(nums.copy())])
            return
        nums.append(str(array[index]))
        solvecombination(index, presum + array[index], ans, nums)
        nums.pop()

        solvecombination(index + 1, presum, ans, nums)

    solvecombination(0, 0, ans, nums)
    return ans


print(combinationsum([2, 3, 5, 4], 7))


# Combination Sum II
# Given collection of candidate numbers (candidates) and a integer target.Find all unique combinations in candidates where the sum is equal to the target.There can only be one usage of each number in the candidates combination and return the answer in sorted order.


# combination sum II
def combinationsumii(array, target):
    array.sort()  # we must sort the array first inorder to prevent the use of the duplicates.
    ans = []
    nums = []

    def solvecombinationsumii(index, presum):
        # base case
        if presum == target:
            ans.append(
                nums.copy()
            )  # if the sum of the obtained array is equal to the target number then ofcourse we append the copy of nums to our ans variable
            return
        if index >= len(array) or presum > target:
            return
        for i in range(index, len(array)):
            if (
                i > index and array[i] == array[i - 1]
            ):  # if we are at the iteration of i which is greater than the index value and if the elements at index i-1 and i are same,then we cannot use this same element or number at same recursive level at same index twice
                # inorder to prevent the duplicate, so we are continuing with the next iteration
                continue
            nums.append(array[i])
            solvecombinationsumii(
                i + 1, presum + array[i]
            )  # then for each i level iteration, we go deep into recursion by making the index i+1, where we insert the number
            nums.pop()  # this is the backtracking which is for getting the nums to the same state after completing all the recursive level iteration, which makes the nums ready for i iteration

    solvecombinationsumii(0, 0)
    return ans


print(combinationsumii([2, 1, 2, 7, 6, 1, 5], 8))
# time complexity : O(N*2^N)  we have N number of options for every index and as the number can be choosen or skipped based on the duplicate condition, we are assuming the time complexity to be N*2^N here N* is for the for loop
# space complexity : O(N*2^N)


# subsets-I
# Given an array nums of n integers. Return array of sum of all subsets of the array nums.
# Output can be returned in any order.


def subsetsI(array):
    totalsum = []

    def solvesubsetsI(index, presum):
        if index >= len(array):
            totalsum.append(presum)
            return
        solvesubsetsI(
            index + 1, presum + array[index]
        )  # here we are including the number
        solvesubsetsI(index + 1, presum)  # here we are excluding the number

    solvesubsetsI(0, 0)
    return totalsum


print(subsetsI([5, 2, 1]))
# time complexity : O(2^N)
# space complexity : O(2^N) + O(N)


# subsetsII
# Given an integer array nums, which can have duplicate entries, provide the power set.
# Duplicate subsets cannot exist in the solution set. Return the answer in any sequence.
# the question is asking us to print the power set of given array which can have duplicate entries ,
def subsetsII(array):
    ans = []
    nums = []
    array.sort()

    def solvesubsetsii(index):
        # we don't need the base case here cause we are using the for loop recursion where the index will go until one value lesser than the length of an array.

        ans.append(nums.copy())

        for i in range(index, len(array)):
            if (
                i > index and array[i] == array[i - 1]
            ):  # this condition is used to remove
                continue
            nums.append(array[i])
            solvesubsetsii(i + 1)
            nums.pop()  # backtracking

    solvesubsetsii(0)
    return ans


print(subsetsII([1, 2]))
# time complexity : O(N*2^N)
# space complexity : O(N*2^N)


# combination iii
def combinationIII(k, target):
    ans = []
    nums = []

    def solvethirdcombination(index, presum):
        if len(nums) == k:  # the question is asking us to determine the set of length k
            if (
                presum == target
            ):  # only if the sum of the formed array is equal to the target number, then we append the copy of nums in our ans variable
                ans.append(nums.copy())
            return
        for i in range(index, 10):

            nums.append(i)
            solvethirdcombination(i + 1, presum + i)
            nums.pop()  # backtracking

    solvethirdcombination(
        1, 0
    )  # as the question is asking us to use the numerals 1 through 9, and no duplicate numbers or values are allowed while making the subset
    return ans


print(combinationIII(3, 9))
# time complexity : O(2^N*9)
# space complexity : O(2^N*9)

# letter combinations of a phone number
# Given a string consisting of digits from 2 to 9 (inclusive). Return all possible letter combinations that the number can represent.
# Mapping of digits to letters is given in first example.


def lettercombination(digits):
    m = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    ans = []
    nums = []

    def solvelettercombination(index):
        if index >= len(
            digits
        ):  # if the passed index becomes greater or equal to the length of the given digits then we just append the copy of nums to our ans
            ans.append("".join(nums.copy()))
            return
        for char in m[digits[index]]:
            nums.append(char)
            solvelettercombination(
                index + 1
            )  # this recursion goes to start the for loop for the next number in the given digit
            nums.pop()  # backtracking

    solvelettercombination(0)
    return ans


print(lettercombination("34"))
# time complexity : O(M^N) here M is the maximum number of characters of the given numbers in the given digit and N is the length of the digits
# space complexity : O(N)+O(M^N) here O(N) is for the recursion depth and O(M^N) is for the ans variable


# Palindrome partitioning
# Given a string s partition string s such that every substring of partition is palindrome. Return all possible palindrome partition of string s.
def palindromepartition(s):
    ans = []
    nums = []

    def checkpalindrome(stri):
        return stri == stri[::-1]

    def solvepalindromepartition(index):

        if index >= len(s):
            ans.append(nums.copy())
            return
        for i in range(index, len(s)):
            substring = s[
                index : i + 1
            ]  # here we are trying to form every possible substring from the given string, and check if they are palindrome.
            if checkpalindrome(
                substring
            ):  # if the checkpalindrome is true only then we append this substring into our nums and then recurse
                nums.append(s[index : i + 1])
                solvepalindromepartition(i + 1)
                nums.pop()  # backtracking

    solvepalindromepartition(0)

    return ans


print(palindromepartition("aabb"))
# time complexity : O(N*2^N) here N is the length of the string and M is the length of the palindrome substring
# space complexity : O(N*2^N)


# word search
# Given a grid of n x m dimension grid of characters board and a string word.The word can be created by assembling the letters of successively surrounding cells, whether they are next to each other vertically or horizontally. It is forbidden to use the same letter cell more than once.
# Return true if the word exists in the grid otherwise false.


def wordsearch(board, word):
    rows = len(board)  # number of rows
    cols = len(board[0])  # number of columns
    path = (
        set()
    )  # here this path is for storing the used or truthy row and column position

    def dfs(
        r, c, index
    ):  # here r represents the row position and c represents the column position
        if index == len(
            word
        ):  # if the index becomes equal to the length of the word then we return true
            return True
        if (
            r < 0 or c < 0 or r >= rows or c >= cols or word[index] != board[r][c]
        ):  # if the rows becomes out of bounds or the character at the current index of the target word is not equal to the character at the row and column position of board then we return false.
            return False
        # if the edge condition is true then it means the character at r and c postion matches with the character at the current index of word, then we add this current row and column position in our set
        path.add((r, c))
        res = (
            dfs(r + 1, c, index + 1)
            or dfs(r - 1, c, index + 1)
            or dfs(r, c + 1, index + 1)
            or dfs(r, c - 1, index + 1)
        )
        path.remove((r, c))  # backtracking
        return res

    for i in range(
        rows
    ):  # this loop is used for using the recursion or dfs for every row and column indexed number from the given board
        for j in range(cols):
            if dfs(
                i, j, 0
            ):  # and if the dfs keeps on returning true until the last  recursion level then we return true
                return True
    # even after going through every loop , if the condition is not true then we return false
    return False


print(
    wordsearch(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
    )
)


# N-queen
# The challenge of arranging n queens on a n × n chessboard so that no two queens attack one another is known as the "n-queens puzzle."
# Return every unique solution to the n-queens puzzle given an integer n. The answer can be returned in any sequence.
# Every solution has a unique board arrangement for the placement of the n-queens, where 'Q' and '.' stand for a queen and an empty space, respectively.


def nqueen(
    n,
):  # n being the lenght of rows and columns and we also must insert n number of queens in our n*n board
    ans = []

    nums = [
        ["."] * n
        for i in range(
            n
        )  # we must make the separate arrays for n times so that the value of a certain specific array won't be affected by the value of another specific array.
    ]  # here we are inserting this colvalue n times inside nums

    def isvalid(row, column):
        r = row
        c = column
        for i in range(
            column
        ):  # this loop is for checking whether the queen is placed horizontally before the given column index
            if nums[row][i] == "Q":
                return False
        # now for checking the queen in diagonally and vertically upward position
        while r >= 0 and c >= 0:
            if nums[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        # now for checking whether the queen is in diagonally and vertically downward position
        r = row
        c = column
        while r < n and c >= 0:
            if nums[r][c] == "Q":
                return False
            r += 1
            c -= 1
        # if all of the conditions are true , then it means we can insert the queen at the current row and column position
        return True

    def solvenqueen(column):
        if (
            column == n
        ):  # if we get the conditions true or valid and we are at the index whose value is equal to n, then it means we have inserted the queens in every possible valid positions in our nums
            solution = ["".join(row) for row in nums]
            ans.append(solution)
            return
        for i in range(n):  # going through every rows and there are n rows
            if isvalid(i, column):
                nums[i][column] = "Q"
                solvenqueen(
                    column + 1
                )  # only if the row and column position is valid , we go to the recursion by adding one to the value of column
                nums[i][column] = "."  # backtracking

    solvenqueen(0)  # initially we are passing 0 index row and 0 index column
    return ans


print(nqueen(4))


# rat in maze
# Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1).
# Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).
# The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.
# Note :
# In a path no cell can be visited more than once.
# If there is no possible path then return empty vector.


def ratinmaze(array):
    n = rows = len(array)
    cols = len(array[0])

    ans = []
    nums = []
    if (
        array[0][0] == 0
    ):  # if the very first row and column position number is 0 then it means the rat cannot move to anyother cell from the starting position
        return -1

    def dfs(r, c):
        if (
            r == rows - 1 and c == cols - 1
        ):  # if we are at the last row and last column position then we append the copy of nums in our ans variable
            ans.append("".join(nums.copy()))
            return

        if c + 1 < cols and array[r][c + 1] == 1:
            nums.append("R")
            dfs(r, c + 1)
            nums.pop()  # backtracking
        if r + 1 < rows and array[r + 1][c] == 1:
            nums.append("D")
            dfs(r + 1, c)
            nums.pop()  # backtracking

    dfs(0, 0)
    if ans:
        return ans
    else:
        return -1


print(ratinmaze([[1, 0], [1, 0]]))
# time complexity : O(2^N) only have two options at every index of a given array whether to go right or go left
# space complexity :  O(N+2^N)


# M-coloring
# Given an integer M and an undirected graph with N vertices and E edges. The goal is to determine whether the graph can be coloured with a maximum of M colors so that no two of its adjacent vertices have the same colour applied to them.
# In this context, colouring a graph refers to giving each vertex a different colour. If the colouring of vertices is possible then return true, otherwise return false.


def mcolorproblem(
    n, m, graph
):  # here n means the number of corners and m is the total number of colors that we must use and graph is the graphical representation of the adjacent nodes or the corners
    colorstore = [0] * n
    s = [
        [] for _ in range(n)
    ]  # here we are creating the list to store the adjacent nodes or neighbours of n nodes from the given graph
    for u, v in graph:   #this loop is for storing the corresponding neighbours or the adjacent nodes for every nodes based on the graph.
        s[u].append(v)
        s[v].append(u)

    def ispossible(node, color):
        for neighbour in s[
            node
        ]:  # then we go through the very neighbours of the current node or current edge if they have this same color or not
            if colorstore[neighbour] == color:  #if we find any of the adjacent node to have the same color then we just return false immediately
                return False

        return True  # otherwise we return true

    def solvemcolor(index):
        if (
            index == n
        ):  # if the index value that we pass becomes equal to the number of nodes or corners then it means the condition of using all m colors is possible
            return True
        for i in range(1, m + 1):  # passing every possible m number of colors
            if ispossible(
                index, i
            ):  # here we are using a separate function that checks whether the current passed color for the current node or corner which is index in our case is possible or not
                colorstore[index] = (
                    i  # if its possible then we add the current color i to this current node index
                )
                if solvemcolor(
                    index + 1
                ):  # if the next node or corner also becomes true when we have used the color i in the current node index
                    return True  # then we return true
                colorstore[index] = (
                    0  # if the next node condition becomes false then we just remove that specific color from that index which is backtracking
                )
        return False

    return solvemcolor(0)


print(mcolorproblem(3, 2, [(0, 1), (1, 2), (0, 2)]))
#time complexity : O(N^M)  for each nodes we have M number of color choices
#Space complexity : O(N) + O(N)
