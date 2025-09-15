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
    numbers=['0'] * n  
    ans=[]
    solvebinary(0,True,ans,numbers)  #here we are passing the first index
    return ans
def solvebinary(index,flag,ans,numbers):
    if index>=len(numbers):  #this is our base case where if the index becomes greater than or equal to the length of the formed numbers
        ans.append(''.join(numbers))
        return 
    numbers[index] = '0'      #whether the flag is true or false , we just add 0 at the current index  
    solvebinary(index+1,True,ans,numbers)
    if flag==True:   #onle if the flag is true then we also have a option of adding 1 in the current index, after adding one we just make the flag to false
        numbers[index]='1'
        solvebinary(index+1,False,ans,numbers)  #and again go deeper into our recursion by increasing the index
        numbers[index]='0'  #then while backtracking , we again make the value at the current index 0
print(genbinary(3))
#time complexity : O(2^N)
#space complexity : O(N)

#Generate Parentheses
#Given an integer n.Generate all possible combinations of well-formed parentheses of length 2 x N.
def generateparentheses(n):#here n is the number of pair of parenthesis
    ans=[]
    datas=[]
    solveparenthesis(0,0,ans,datas,n)
    return ans
def solveparenthesis(opentag,closetag,ans,datas,n):  #here opentag represents the number of opening tag used and closetag represents the number of closing tag used
    if opentag==closetag==n:
        ans.append(''.join(datas))
        return
    if opentag<n:
        datas.append('(')
        solveparenthesis(opentag+1,closetag,ans,datas,n)
        datas.pop()  #backtracking 
    if closetag<opentag:
        datas.append(')')
        solveparenthesis(opentag,closetag+1,ans,datas,n)
        datas.pop() #backtracking
print(generateparentheses(3))
#time complexity : O(2^N)
#space complexity : O(N)
    




        




