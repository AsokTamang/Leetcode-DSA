def convertintobinary(num):
    res = ""
    if num == 0:
        return "0"
    while num > 0:
        if num % 2 == 0:
            res += "0"
        else:
            res += "1"

        num = num // 2
    return res[
        ::-1
    ]  # here we are adding the '1' at the beginning cause our while loop condition is while num!=1


print(convertintobinary(13))
# time complexity : O(log2N)
# space complexity : O(log2N)


def convertintodecimal(s):
    ans = 0
    p = 0
    for i in range(len(s) - 1, -1, -1):
        ans += int(s[i]) * (2**p)  # ** denotes the power
        p += 1
    return ans


print(convertintodecimal("1101"))
# time complexity : O(N)
# space complexity : O(N)

# 1s compliment
# while doing the 1s compliment, we just switch 0 with 1 and 1 with 0

# 2s compliement
# while doing the 2s compliment , we just add 1 to the value of 1s compliment


# XOR
# while doing the xor which is like this ^ , if the number of ones is odd then the result of xor operation will be 1.
# but if the number of ones is even while doing the xor operation then the result of xor operation will be 0.

# right shift >>
# while doing the right shift we just shift the elements of the given digit to right side


# so while storing the negative number , computer stores the 2s compliment of this negative number
# as the - sign is denoted by 1 and the positive sign is denoted by 0

# the right shift of a number means the value of a number will be smaller compared to the original value or original number so it's formula is num // 2 ** k where k denotes the power or position of a number from the very last index.
# the left  shift of a number means the value of a number will be greater compared to the original value , so its formula is num * (2**k)

# for the not operation of a positive number
# and for the not operation example(~5) what we do is we first flip the digits 0 and 1 then we check if its negative or positive based on the sign at the very beginning , if its a negative which is denoted by 1 then we make the 2s compliment of it, if its a positive then we stop , as the flipped output will be our answer.

# for the not operation of a negative number
# first of we should make a 2s compliment of this negative number then we again repeat the same process which is first flipping then checking if it's a negative number or not,
# if it's negative then we should make a 2s compliment of this output again otherwise we must stop.


# problem1
# Check if the i-th bit is Set or Not
# Given two integers n and i, return true if the ith bit in the binary representation of n (counting from the least significant bit, 0-indexed) is set (i.e., equal to 1). Otherwise, return false.
# brute approach
def checkibit(n, indexx):
    if n == 0:
        return False
    res = ""
    while n > 0:
        res += "0" if n % 2 == 0 else "1"
        n = n // 2

    if int(res[indexx]) == 1:
        return True
    return False


print(checkibit(10, 1))
# time complexity : O(log2N)
# space complexity : O(log2N)


# for the optimal approach we do the and operation between the given number and the left shift of 1 from the given comparing index , and check whether the output is true or false
def optimalcheckibit(n, indexx):
    return (
        n & (1 << indexx)
    ) != 0  # here we are doing the and operation which is . or multiplication between n and the left shift of 1 by the given comparing index.


# because in the add operation , most of the time the output will be false or 0 except only when both of the inputs are true
print(optimalcheckibit(10, 1))
# time complexity : O(1)
# space complexity : O(1)


# xor fact - the xor of the same number will be 0
# swap two numbers
def swaptwonums(a, b):
    a = a ^ b
    b = a ^ b  # making b equals to a
    a = a ^ b  # making a equals to b
    return (a, b)


print(swaptwonums(5, 6))
# time complexity : O(1)
# space complexity : O(1)


# set i-th bit a 1
# brute approach
def setibnit(n, indexx):
    res = ""
    while n > 0:
        res += "0" if n % 2 == 0 else "1"
        n = n // 2
    res = list(res)
    if indexx >= len(
        res
    ):  # if the given index is way greater than the length of the obtained binary digit, then we must add 0s in the obtained binary digit so that we can manipulate the data of the given index.
        res += ["0"] * (indexx - len(res) + 1)
    res[indexx] = "1"
    ans = 0
    for i in range(len(res)):
        ans += int(res[i]) * (2**i)
    return ans


print(setibnit(5, 3))
# time complexity : O(log2N)+M), M is the length of the obtained binary form
# space complexity : O(M)


def optimalsetibit(n, indexx):
    return (
        n | 1 << indexx
    )  # doing the OR operation between the given digit and value obtained by shifting 1 to the leftside to the given index, sets the i-th bit to set.


print(optimalsetibit(5, 3))
# time complexity : O(1)
# space complexity : O(1)


# clear the i-th bit
# which means turning the 1 to 0 if its 1 otherwise let it be 0 at the given index
# brute approach
def bruteclearithbit(n, indexx):
    res = ""
    ans = 0
    while n > 0:
        res += "0" if n % 2 == 0 else "1"
        n = n // 2
    res = list(res)
    if indexx >= len(res):
        res += ["0"] * (indexx - len(res) + 1)
    if res[indexx] == "1":
        res[indexx] = "0"
    for i in range(len(res)):
        ans += int(res[i]) * (2**i)
    return ans


print(bruteclearithbit(13, 3))
# time complexity : O(log2N + M)  where M is the length of the obtained binary form of the given digit
# space complexity : O(M)


# optimal approach
def optimalclearithbit(n, indexx):
    return n & ~(
        1 << indexx
    )  # as the and operation always gives us false except both the values are true  and doing the not operation on shifting the 1 to the left side of the given index


print(optimalclearithbit(13, 3))
# time complexity : O(1)
# space complexity : O(1)


# toggle the ith bit
def toggleithbit(n, indexx):
    return n ^ (
        1 << indexx
    )  # here we are using the xor cause xor changes the value only when both of the values are same which means


# it changes into 1 when there is odd number of 1, it changes into 0 when is even number of 1s.
print(toggleithbit(5, 5))
# time complexity : o(1)
# space complexity : O(1)


# remove the last setbit which is turn the last 1 into 0
# brute approach
def removelastsetbit(n):
    res = ""
    while n > 0:
        res += "0" if n % 2 == 0 else "1"
        n = n // 2
    res = list(res)
    for i in range(len(res)):
        if res[i] == "1":
            res[i] = "0"
            break
        else:
            continue
    ans = 0
    for i in range(len(res)):
        ans += int(res[i]) * (2**i)
    return ans


print(removelastsetbit(13))
# time complexity : O(log2N+M)
# space complexity : O(M+N)


# optimal solution
def optimallastsetbit(n):
    return n & (n - 1)


print(optimallastsetbit(13))
# time complexity : O(1)
# space complexity : O(1)


# check if the given number is a power of 2 or not
def checkpower(n):
    return (
        n & (n - 1) == 0
    )  # if the and operation between the given number and the number lesser than just 1 compared to the given number , gives us the value 0 then , the given number is a power of 2, otherwise its not the power of 2


print(checkpower(9))
# time complexity : O(1)


# count the number of setbits
# brute-wise approach
def countsetbits(n):
    c = 0
    while n > 0:
        if n % 2 == 1:
            c += 1
        n = n // 2
    return c


print(countsetbits(9))
# time complexity : O(N)
# space complexity : O(1)


# brute-bit-wise approach
# the bit-wise operation is much faster and effective than the normal brute approach
def bitwisecountset(n):
    c = 0
    while n > 0:
        c += (
            n & 1
        )  # if the given number is odd then it always gives us 1 while doing the and operation with value 1 otherwise false or 0
        n = (
            n >> 1
        )  # right shifting which means n/2**k , also means decreasing the number or value
    return c


print(bitwisecountset(8))
# time complexity : O(N)
# space complexity : O(1)


# using the and operation between n and n-1
def countset(n):
    c = 0
    while n > 0:
        n = n & (n - 1)
        c += 1
    return c


print(countset(9))
# time complexity : O(number of set bits in a given digit)
# space complexity : O(1)


# check if the given number is odd or even
def checkevenodd(n):
    if n & 1 == 0:
        return "even"
    elif n & 1 == 1:
        return "odd"


print(checkevenodd(13))
# time complexity : O(1)
# space complexity : O(1)


def setrightmostunsetbit(n):
    return n | (
        n + 1
    )  # here doing the OR operation between the given digit n and n+1 helps to set the unset bit


print(setrightmostunsetbit(9))
# time complexity : O(1)
# space complexity : O(1)


def unsettherightmostsetbit(n):
    return n & (n - 1)


print(unsettherightmostsetbit(8))
# time complexity : O(1)
# space complexity : O(1)

# Divide two numbers without multiplication and division
# Given the two integers, dividend and divisor. Divide without using the mod, division, or multiplication operators and return the quotient.


def dividenums(dividend, divisor):
    sign = 1

    if dividend < 0 and divisor < 0:
        sign = 1
    elif dividend < 0 or divisor < 0:
        sign = -1

    ans = 0
    for i in range(32, -1, -1):
        calculation = (
            divisor << i
        )  # this means divisor * 2 **i  #left shifting means increasing the value while right shifting means decreasing the value
        if calculation <= dividend:
            ans += 1 << i  # this means 2**i as 1<<i means in the binary form
            dividend -= calculation
    if ans < -231:
        return -231
    elif ans > 231 - 1:
        return 231 - 1
    else:
        return sign * int(
            ans
        )  # the question is asking us to return our answer in an integer format not in a float or decimal


print(dividenums(15, 3))
# time complexity : O(number of calculation)
# space complexity : O(1)


# brute approach
def brutedividenums(divided, divisor):
    sign = 1

    if divided < 0 and divisor < 0:
        sign = 1
    elif divided < 0 or divisor < 0:
        sign = -1
    ans = 0
    while divisor < divided:
        divided -= divisor
        ans += 1
    if ans < -(2**31):
        return -(2**31)
    elif ans > 2**31 - 1:
        return 2**31 - 1
    else:
        return sign * int(ans)


print(brutedividenums(22, 3))
# time complexity : O(number of divisor to reach the divided)
# space complexity : O(1)


# Minimum Bit Flips to Convert Number
# Given two integers start and goal. Flip the minimum number of bits of start integer to convert it into goal integer.
# A bits flip in the number val is to choose any bit in binary representation of val and flipping it from either 0 to 1 or 1 to 0.


def minimumflips(start, goal):
    target = (
        start ^ goal
    )  # this gives us the value where if there is no difference between the numbers then there would be 0 but if there is difference then there would be 1
    # and our trick here is to calculate the number of 1s in this target.
    count = 0
    while target > 0:
        count += (
            target & 1
        )  # here we are checking if the 1 exists or not and as the and operation only provide when both of the comparing values are 1   otherwise it provides 0
        target = (
            target >> 1
        )  # right shifting the target value by 1 inorder to compare other remaining digits
    return count


print(minimumflips(3, 4))
# time complexity : O(logN)
# space complexity : O(1)


# revision of minimum bit flips to convert a number from start to end
def minimumflips(start, end):
    target = (
        start ^ end
    )  # here xor gives us the value where we can identify the number of bits that must be changed which is denoted by the number of 1s
    # cause in xor operation , if the values are same then it gives 0, if the values are different or odd number of 1s, then it gives the digit 1
    count = 0
    while target > 0:
        count += target & 1  # this operation helps us to count the number of 1s
        target = target >> 1  # then we right shift the target by 1
    return count


print(minimumflips(10, 7))
# time complexity : O(number of distinct bits between the start and end)
# space complexity : O(1)


# Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.
# brute-force approach
def singlenumber(nums):
    m = {}
    for num in nums:
        m[num] = m.get(num, 0) + 1
    for data in m:
        if m[data] == 1:
            return data


print(singlenumber([1, 2, 2, 4, 3, 1, 4]))
# time complexity : O(N+M)   M represents the total number of unique digits from the given array
# space complexity : O(M)


# optimal solution
# using xor
# the xor of a same number will gives us 0
def optimalsinglenum(nums):
    ans = 0
    for num in nums:
        ans ^= num
    return ans


print(optimalsinglenum([1, 3, 10, 3, 5, 1, 5]))
# time complexity : O(N)
# space complexity : O(1)


# backtracking
# power set bit manipulation
def powerset(nums):
    ans = []
    output = []

    def solvepowerset(index):
        if index >= len(nums):

            ans.append(output.copy())
            return

        output.append(nums[index])  # appending the current indexed number
        solvepowerset(index + 1)
        output.pop()  # backtracking
        solvepowerset(index + 1)  # ignoring the current indexed number

    solvepowerset(0)
    return ans


print(powerset([1, 2, 3]))
# time complexity : O(2^N)
# space complexity : O(N*M) M is the length of the output in each recursion level.


# power set
# optimal bit manipulation
def powersetbit(nums):
    n = len(nums)
    subsets = 1 << n  # an array having a length n always has a subsets of size 2**n
    ans = []
    for i in range(subsets):
        output = []
        for j in range(n):  # looping through the bits or index in simple language
            if i & (
                1 << j
            ):  # if the bit-mask and with 1 << j gives us true then we can include the j indexed or j-bit number from an array
                output.append(nums[j])
        ans.append(output)  # appending the formed output in ans varible
    return ans


print(powersetbit([1, 2, 3]))
# time complexity : O(N*2**n) we are looping for every possible subsets which is 2**n and N is the number of numbers in a given array
# space complexity : O(N*2**n) number of formed subsets and those subsets has N length in the worst case.


# xor of a numbers in a given range
def xor(l, r):
    def calculatexor(
        N,
    ):  # this is the logic of xor using 4 as a divisor and depending upon the ramainder , we change the xor value , as this calculates the xor from 1 upto N
        if N % 4 == 1:
            return 1
        elif N % 4 == 2:
            return N + 1
        elif N % 4 == 3:
            return 0
        elif N % 4 == 0:
            return N

    return calculatexor(l - 1) ^ calculatexor(r)


# as the calculatexor function calculates the xor of a number from 1 to n
# and we are using l-1 cause if we include l then it will get cancel cause if we are doing calculatexor(l) ^ calculatexor(r)  l^l will cancel eachother , thats why for the first function
# we are passing only l-1
print(xor(3, 5))
# time complexity : O(1)
# space complexity : O(1)


# brute approach
def brutesinglenumberiii(nums):
    m = {}
    ans = []
    for num in nums:
        m[num] = m.get(num, 0) + 1
    for num in m:
        if m[num] == 1:
            ans.append(num)
    return ans


print(brutesinglenumberiii([1, 2, 1, 3, 5, 2]))
# time complexity : O(N+M) N is the length of given array and M is the number of unique numbers in a given array
# space complexity : O(M)  number of unique characters or O(N) in the worst case


# optimal singlenumberiii
# so the logic of the solution of this problem is that
# first of all , we are doing the xor of the numbers in a given array, which gives us the xor between those required two different number
# then what we do is , we find the set bit of that number using and between that number and it's two's compliment
# then we again loop through the given array and check if the set bit at the bit of the obtained number is same as the current looped number or not , if yes then we group in one side
# and for the numbers having unset bit at the bit of the obtained number, we group in the next side
# then we find the xors of the numbers of those groups separately , which finally provide us those two required values.
def optimalsinglenumber(nums):
    initial = 0
    for num in nums:
        initial ^= num
    # inorder to find the rightmost or the setbit which is at the end compared to other setbits, we must calculate the and operation between the number and the two's compliment of the number
    bitposition = (
        initial & -initial
    )  # and operation between the initial and it's two's compliment to find the right most set bit
    a = 0
    b = 0
    for num in nums:
        if (
            num & bitposition
        ):  # if the current number has the bit set at the bit of the bitposition, then we start doing the xor in a variable
            a ^= num
        else:
            b ^= num  # if the current number has an unset bit compared to the bit of the bitposition then we start doing the xor in b variable
    return [a, b]


print(optimalsinglenumber([1, 9, 1, 2, 8, 2]))
# time complexity : O(N)
# space complexity : O(1)
# First, diff_bit = initial & -initial isolates the bit.
# Second, num & diff_bit checks if that specific bit is set in each number, which allows us to split the array.


# Prime factorisation of a Number
# You are given an integer array queries of length n.
# Return the prime factorization of each number in array queries in sorted order.


def primefactorization(array):
    ans = []
    for num in array:
        output = []
        for i in range(2, num + 1):
            while num % i == 0:
                output.append(i)
                num = num // i
        ans.append(output)
    return ans


print(primefactorization([2, 3, 4, 5, 6]))
# time complexity : O(N * M)  N is the length of an array and M is the range between 2 and the number at the current loop
# space complexity : O(N)  number of prime factorials


# Divisors of a Number
# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.
# A number which completely divides another number is called it's divisor.
# brute approach
def divisorofnum(n):
    ans = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i not in ans:
                ans.append(i)
        if n % (n // i) == 0:
            if (n // i) not in ans:
                ans.append(n // i)
    return sorted(ans)


print(divisorofnum(8))
# time complexity : O(√n + O(logM))
# space complexity : O(M)


# Prime factorisation of a Number
# You are given an integer array queries of length n.
# Return the prime factorization of each number in array queries in sorted order.


def primefactorials(array):
    ans = []
    for num in array:
        output = []
        for i in range(2, num + 1):
            while (
                num % i == 0
            ):  # we keep on appending the divisor if the divisor exactly divides the current number of an array
                output.append(i)
                num = num // i
        ans.append(output)
    return ans


print(primefactorials([2, 3, 4, 5, 6]))
# time complexity : O(N * M)   N is the number of numbers in a given array and M is the prime numbers which exactly divides the current number.
# space complexity : O(N)  in the worst case


# Count primes in range L to R
# You are given an 2D array queries of dimension n*2.
# The queries[i] represents a range from queries[i][0] to queries[i][1] (include the end points).
# Return the count of prime numbers present in between each range in queries array.


# brute approach
def countprimes(array):
    rows = len(array)  # number of rows
    endindex = len(array[0]) - 1
    ans = []

    def checkprime(
        number,
    ):  # this is the function for checking whether the given passed number is prime or not
        if number < 2:
            return False
        for i in range(
            2, (int(number**0.5) + 1)
        ):  # as the prime numbers are those numbers that can be divisible by only themselves or the digit 1
            if number % i == 0:
                return False
        return True  # if it's not divisible then we return true which is a prime number

    for i in range(rows):
        count = 0
        for k in range(
            array[i][0], array[i][endindex] + 1
        ):  # here we are using array[i][cols] +1 so that we can also include this ending number of the range, as
            # we need to find the prime numbers between the start and the end range
            if checkprime(k):
                count += 1
        ans.append(count)
    return ans


print(countprimes([[2, 5], [4, 7]]))
# time complexity : O(N*K*√M)  N is the number of rows and K is range between the starting and ending index at each each rows , and M is the number of checks done on a number which takes upto √M times.
# space complexity : O(N)


# better solution
# in the better solution what we do is ,we create an array ,lets sat primestore which stores the numbers from


def cprimes(array):
    ans = []
    rows = len(array)  # number of rows

    def createarray(start, end):
        primestore = [1] * (
            end + 1
        )  # here we are making the primestore starting from 2 to the ending number which has all the value 1 initially that denotes it is the prime number
        primestore[0] = primestore[1] = (
            0  # as the numbers 0 and 1 are composite , we declare these numbers to have value 0 from the way start.
        )
        for i in range(
            2, int(end**0.5) + 1
        ):  # then we again run the loop to convert the composite numbers in a prime store to have a value 0
            if primestore[i] == 1:
                for j in range(
                    i * i, end + 1, i
                ):  # here why we are doing i+j is to find the multiples of the current number i
                    primestore[j] = (
                        0  # the multiple of prime number will always be composite
                    )
        count = 0
        for i in range(start, end + 1):
            if (
                primestore[i] == 1
            ):  # if the numbers between the range start and end+1 has a value 1 in the primestore
                count += 1
        return count

    for i in range(rows):
        c1 = createarray(array[i][0], array[i][1])
        ans.append(c1)
    return ans


print(cprimes([[2, 5], [4, 7]]))
# time complexity : O(N*logM)  where N is the number of rows in a given array and M is the range between start and end  , and we are using log cause we are also using the if condition inside the for-loop of create array
# space complexity : O(N)


#Sieve of Eratosthenes  theorem

def cprimes(array):
    maximum = max(max(q) for q in array)
    primestore = [1] * (
        maximum + 1
    )  # here we are making the primestore starting from 2 to the maximuming number which has all the value 1 initially that denotes it is the prime number
    primestore[0] = primestore[1] = (
        0  # as the numbers 0 and 1 are composite , we declare these numbers to have value 0 from the way start.
    )
    for i in range(
        2, int(maximum**0.5) + 1
    ):  # then we again run the loop to convert the composite numbers in a prime store to have a value 0
        if primestore[i] == 1:
            for j in range(
                i * i, maximum + 1, i
            ):  # here why we are doing i+j is to find the multiples of the current number i
                primestore[j] = (
                    0  # the multiple of prime number will always be composite
                )

    count = 0
    primecount = [0] * (
        maximum + 1
    )  # here we are making a primecount array which stores the number of prime numbers upto the indexes

    for i in range(2, maximum + 1):
        if primestore[i] == 1:
            count += 1

        primecount[i] = (
            count  # even though the current indexed number is not a prime number which is denoted as 0 in the prime store but upto this indexed number there might be the prime numbers ,so we coded like this
        )
    ans = []
    for q in array:
        start, end = q  # here q is the single array in the given array
        if start > end:
            start, end = end, start
        if start > 0:
            ans.append(
                primecount[end] - primecount[start - 1]
            )  # inorder to count the number of primes between start and end including the start we are substracting the count at index end from the index just before the start
        else:
            ans.append(primecount[end])
    return ans


print(cprimes([[2, 5], [4, 7]]))
# time complexity : O(N*logM * logM)  where N is the number of rows in a given array and M is the maximum value of a given array.
# space complexity : O(maximum)



#Prime factorisation of a Number using sieve theorem
def prmefacto(array):
    maximum= max(array)  #this gives us the maximum value from a given array
    primenums = [1] * (maximum+1)  #creating the primenums array initially
    for i in range(maximum+1):
        primenums[i]  = i
    primenums[0] = primenums[1] = 0  #as 0 and 1 are composite numbers so we are making it's value 0    
    
    #building SPF sieve
    for i in range(2,int(maximum**0.5)+1):
        if primenums[i] == i:   #if the current index has the same value as that of i then 
            for j in range(i*i,maximum+1,i):
                if primenums[j] > i:  #only if the current j indexed value is lesser than the current prime factorial then we change the value at the index j
                 primenums[j] = i  #making the composite indices or the numbers to have value i , which gives us the value from where we should start dividing the number
    ans = []
    for num in array:
        output = []
        for i in range(primenums[num],num+1):
            while num > 1:
                output.append(primenums[num])
                num //= primenums[num]

        ans.append(output)  
    return ans
print(prmefacto([7, 12, 18]))   
#time complexity : O(M*logM)  M is the maximum value of a given array.
#space complexity : O(N)       

