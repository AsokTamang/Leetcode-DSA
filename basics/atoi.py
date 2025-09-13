def stringtointeger(s):
    s = (
        s.lstrip()
    )  # here we have removed the leftmost whitespaces or the leading whitespaces from the given string
    c = 1
    i = 0
    if s[0] == "-":
        c = -1  # c denotes the sign for our final string
        i = 1
    elif s[0] == "+":
        c = 1
        i = 1

    if len(s) > 1 and s[1] in [
        "+",
        "-",
    ]:  # as the first sign is the correct but the thing is the second indexed character must not be the sign
        return 0

    a = ""
    for char in s[
        i:
    ]:  # now ignoring the sign , we are starting the loop from the 1st index of the given string.
        if (
            char.isdigit() == False
        ):  # we stop parsing the given string as soon as the non-digit character is found.
            break

        if (
            char.isdigit()
        ):  # here we are negleting the negative sign and appending the other characters of the string in a varible called s.
            a += char
    a = int(a) * c
    if a < -2147483648:
        return -2147483648
    elif a > 2147483647:
        return 2147483647
    else:
        return a


print(stringtointeger("04193abc"))
# time complexity : O(N)
# space complexity : O(N) in the worst case.


def optimalstringtointeger(s):
    s = (
        s.lstrip()
    )  # here we have removed the leftmost whitespaces or the leading whitespaces from the given string
    c = 1
    i = 0
    if s[0] == "-":
        c = -1  # c denotes the sign for our final string
        i = 1
    elif s[0] == "+":
        c = 1
        i = 1

    if len(s) > 1 and s[1] in [
        "+",
        "-",
    ]:  # as the first sign is the correct but the thing is the second indexed character must not be the sign
        return 0

    j = i
    for char in s[
        i:
    ]:  # now ignoring the sign , we are starting the loop from the 1st index of the given string.
        if (
            char.isdigit() == False
        ):  # we stop parsing the given string as soon as the non-digit character is found.
            break

        if (
            char.isdigit()
        ):  # here we are negleting the negative sign and appending the other characters of the string in a varible called s.
            j += 1
    ans = int(s[i:j]) * c
    if ans < -2147483648:
        return -2147483648
    elif ans > 2147483647:
        return 2147483647
    else:
        return ans


print(optimalstringtointeger("4193 with words"))
# time complexity : O(N)
# space complexity : O(1)

# Pow(x,n)
# Implement the power function pow(x, n) , which calculates the x raised to n i.e. xn.
# Note : In output print 6 digits places after decimal point.


def powerxn(x, n):
    ans = 1
    isnegative = False
    if n < 0:
        isnegative = True
        n = (
            n * -1
        )  # if the power value is negative then we make it positive by multiplying this by -1
    for i in range(
        n
    ):  # as we just need to find the power of the given digit upto n times, we are multiplying the digit by n times
        ans = ans * x
    if (
        isnegative
    ):  # if the power value is negative then we divide 1 by the  actual answer
        return 1 / ans
    else:  # otherwise we just return the actual answer.
        return ans


def optimalpow(x, n):
    nn = n  # here we are storing the copy of n to nn
    ans = 1
    if nn < 0:  # if the base power is negative then we make it positive
        nn = -1 * nn
    while nn > 0:
        if (
            nn % 2 == 0
        ):  # if the base power is even then we multiply the given number with the given number which is x^2 and divide the basepower n by 2
            x = x * x
            nn = nn // 2
        else:  # but if the base power becomes odd then we make the ans to multiply by the
            ans = ans * x
            nn = nn - 1
    if n < 0:
        ans = 1 / ans
    return ans


print(optimalpow(2, 10))


def countgoodnumbers(n):  # here n is the length of the string of good numbers
    c = 0
    ans = ""
    while c < n:
        if c % 2 == 0:  # here we are just checking at which index we are at
            ans += str(
                5
            )  # here 5 denotes the number of even digits which can be placed at the even index and they are : 0,2,4,6,8
            # and they must be under digit 10
        else:
            ans += str(
                4
            )  # if the current index is odd then there are 4 number of prime digits which can be placed at this current index , and all of them must be within the range 0- 9 and they are
            2, 3, 5, 7
        c += 1

    final = 1
    for char in ans:
        final *= int(
            char
        )  # this gives us the total number of good digits for the given length n
    return final


print(countgoodnumbers(2))


# time complexity : O(N)  N is the given length of the digit string
# space complexity : O(N)
def bettercountgoodnumbers(n):
    c = 0
    ans = 1
    while c < n:
        if c % 2 == 0:
            ans *= 5  # here we can place 5 even digits at the even indices
        else:
            ans *= 4  # at the odd indices , we can place about 4 digits which are the prime digits under 10
        c += 1
    return ans


print(bettercountgoodnumbers(2))
# time complexity : O(N)
# space complexity : O(1)


def optimalcountgoodnumbers(n):
    if n == 1:
        return 5  # if the length of the required digit string is just one then we return 5 as we can place 5 even digits at this only one index
    else:
        oddindices = (
            n // 2
        )  # if the length of the digit string is more than 1 then of course the odd indices as well as the even indices will be equal which is n//2 , only
        # if the length of the digit string is even but if the length of the digit string is odd then, the even indices will be one value greater than the odd indices
        # so we have coded evenindices=(n+1) // 2
        evenindices = (n + 1) // 2
        return oddindices * 4 * evenindices * 5


print(powerxn(2.0000, -2))
print(optimalcountgoodnumbers(2))

# Sort a Stack
# You are given a stack of integers. Your task is to sort the stack in descending order using recursion, such that the top of the stack contains the greatest element. You are not allowed to use any loop-based sorting methods (e.g., quicksort, mergesort). You may only use recursive operations and the standard stack operations (push, pop, peek/top, and isEmpty).
def sortastack(a):
    if len(a) <= 1:
        return a
    top=a.pop()  #we keep on deleting the lastmost element or the top element from the stack a till the base case is reached
    sortastack(a)
    #after the base case is reached then we keep on adding the element but based on recursive sorting method
    insertelem(a,top)
    return a[::-1]   #here we are reversing the list cause the question is asking us to return the list where the top most element is at the leftmost side of an array.
def insertelem(a,element):
    if not a or element>=a[-1]:  #if the passed element is greater than or equal to the topmost element then we append this element to the stack and return
        a.append(element)   #as the question is asking us to return the top most element at the leftmost side of an array.
        return 
    #otherwise  we remove the top most element in a stack which is greater than the passed element
    top=a.pop()      
    insertelem(a,element)  #then we keep on passing the eleemenet till the condition of element > topmost element in the stack is reached

    a.append(top)  #then only we append this popped top most element

print(sortastack( [4, 1, 3, 2]))
#time complexity : O(N^2)  in the worst case
#space complexity : O(N)


    
    
    

# time complexity : O(N)
# space complexity : O(1)
