from collections import defaultdict

# the main function of the default dict is that we donot need to check if the value exists or not before increasing the value of this key


# Sort Characters by Frequency
# You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.
# If two or more characters have same frequency then arrange them in alphabetic order.
def sortfreq(s):
    m = {}
    for char in s:
        m[char] = (
            m.get(char, 0) + 1
        )  # here the default value will be 0 and we are adding 1 as soon as we found the occurence of letter

    return (sorted(m, key=lambda x: m[x]))[
        ::-1
    ]  # here what we are doing is we are sorting our dict called m by using sorted and lambda where x:m[x] means sorting based on the values and using [::-1] to reverse the output


# as the question is asking us to return from highest to lowest
print(sortfreq("cba"))
# time complexity : O(N) + O(K)  #here N is the number of characters in a given string and K is the number of keys in our dictinary m
# space complexity : O(N)


# Maximum Nesting Depth of the Parentheses
# A string s is a valid parentheses string (VPS) if it meets the following conditions:
# It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
# The parentheses are balanced and correctly nested.
# Your task is to compute the maximum nesting depth of parentheses in s. The nesting depth is the highest number of parentheses that are open at the same time at any point in the string.
def nestingdepth(s):
    count = 0
    ans = 0
    for char in s:
        if char == "(":
            count += 1
            ans = max(ans, count)
        elif char == ")":
            count -= 1

    return ans


print(nestingdepth("(1)+((2))+((((3))))"))
# time complelxity : O(N) N is the number of characters in a string
# space complexity : O(1)


# Roman to Integer
# Roman numerals are represented by seven different symbols:
# Roman numerals are typically written from largest to smallest, left to right. However, in specific cases, a smaller numeral placed before a larger one indicates subtraction.
# The following subtractive combinations are valid:
# I before V (5) and X (10) → 4 and 9
# X before L (50) and C (100) → 40 and 90
# C before D (500) and M (1000) → 400 and 900
# Given a Roman numeral, convert it to an integer.


# optimized version
def romanint(s):
    data = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 500,
        "CM": 900,
    }
    i = 0
    ans = 0
    while i < len(s):
        if i < len(s) - 1:
            if s[i : i + 2] in data:
                ans += data[s[i : i + 2]]
                i += 2
        if s[i : i + 1] in data:
            ans += data[s[i : i + 1]]
            i += 1
    return ans


print(romanint("DCCCXC"))
# time complexity : O(N)
# space complexity : O(1) our space complexity is O(1) our dictonary is fixed through out the code loop


# string to integer(atoi)
# Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).
def stringtoint(s):
    ans = 0
    sign = 1
    i = 0
    while i < len(s) and s[i] == " ":
        i += 1
    if i < len(s) and (s[i] == "+" or s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i += 1
    while i < len(s) and s[i].isdigit():
        ans = ans * 10 + int(s[i])
        i += 1
    result = sign * ans
    if result > 2147483647:
        return 2147483647
    elif result < -2147483648:
        return -2147483648
    else:
        return sign * ans


print(stringtoint("0-1"))
# time complexity : O(N)
# space complexity : O(N) in worst case


# Count Number of Substrings
# Given a string s consisting only of characters 'a', 'b', and 'c', return the number of substrings that contain at least one of each character 'a', 'b', and 'c'
# Medium
# here what the question is asking us is to return the number of substrings from the given string


def substring(s):
    n = len(s)
    required = set(
        s
    )  # here we are using set to remove the duplicate data from the comparing variable which is required
    count = 0
    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(s[j])  # here we are adding the current j indexed character in seen
            if required == seen:
                count += (
                    n - j
                )  # here  as soon as we find the index of j at which the substring consists of all the three characters then we just calculate the count which is n-j which gives
                # the total number of substrings including the substrings made after this current index j too.
                break
    return count


print(substring("bbcabc"))
# time complexity : O(N^2)
# space complexity : O(1)


# or for the optimization ,
def optsubstring(s):
    n = len(s)
    count = 0
    left = 0
    m = defaultdict(
        int
    )  # here we are using the default dict instead of the usual dict inorder to make our code shorter and faster
    for i in range(n):
        m[
            s[i]
        ] += 1  # here what we are doing is storing the charcaters of s at every index i in the storage m
        while (
            len(m) == 3
        ):  # if the length of the storage is m , which means we have found a substring consisting of all the characters at the current index i,then we increase the count by n-i
            count += n - i
            m[
                s[left]
            ] -= 1  # then inorder to remove the left most part of the charc of a string which is store in  our storage m , we are doing this calculation
            if m[s[left]] == 0:
                m.pop(s[left])
            left += 1
    return count


print(optsubstring("bbcabc"))
# time complexity : O(N)
# space complexity : O(1)


# Count Vowel Substrings of a String
# Given a string word, return the number of vowel-only substrings—i.e., every character in the substring is a vowel (a, e, i, o, u)
# brute approach, for the brute approach we check vowels for every possible substrings
def countvowel(s):
    n = len(s)
    vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for i in range(n):
        for j in range(
            i, n
        ):  # this inner loop j is for creating an every possible substrings from the given string s
            substring = s[i : j + 1]  # which is this
            if all(
                char in vowels for char in substring
            ):  # then we are checking every values in an obtained substring that if all of them are vowels or not
                count += 1  # if yes then we just increase the count by 1
    return count


print(countvowel("abc"))
# time complexity : O(N^3) in worst case
# space complexity : O(1)  here we arenot using any kind of extra storage.

# optimized solution
# in the optimized solution ,what we do is , we just count the number of vowels presented in the given string , then we use the formula of L*(L+1)//2 which calculates the number of total substrings that consists of the vowels


# find a contiguous subarray whose length is equal to k
def consubarray(s, k):  # the subarray or substring must have a length of a k
    n = len(s)
    left = 0
    storage = []
    ans = 0
    for i in range(n):
        storage.append(s[i])
        while (
            len(storage) == k
        ):  # here if the length of storage is equal to k then we just calculate the average and find the answer
            average = sum(storage) / k
            ans = max(ans, average)
            storage.pop(0)
            left += 1

    return ans


print(consubarray([5], 1))
# time complexity : O(N)
# space complexity : O(1)

# longest palindromic substring
# Given a string s, return the longest palindromic substring in s.


def brutepalindromic(s):
    n = len(s)
    length = 0
    ans = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i : j + 1]
            if (
                substring == substring[::-1]
            ):  # here we are comparing the reverse form of a substring with the substring, if they are same then it means the substring is palindromic, then we need to calcualte the length of the substring
                if len(substring) > length:
                    length = len(substring)
                    ans = substring
    return ans


print(brutepalindromic("babad"))
# time complexity : O(N^3)
# space complexity : O(1)


# better approach
# so for the optimal approach inorder to find the longest palindromic substring, we need to take the current i indexed element as the centre of the string and then expand this in both left side as well as the right side as long as the condition of left side and right side elements are same or equal to eachother.
# and during this while loop , we also need to compare the length of the current substring with the previous one,if only its greater we change our answer otherwise its always the same.
def betterpalindrome(s):
    n = len(s)
    ans = ""
    length = 0
    for i in range(n):

        left, right = i, i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > length:
                length = right - left + 1
                ans = s[left : right + 1]
            left -= 1  # as we need to find the most longest substring which is palindromic , we are decreasing the value of left and increasing the value of right
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > length:
                length = right - left + 1
                ans = s[left : right + 1]
            left -= 1  # as we need to find the most longest substring which is palindromic , we are decreasing the value of left and increasing the value of right
            right += 1
    return ans


print(betterpalindrome("babad"))
# time complexity : O(N^2)
# space complexity : O(1)

#optimal palindrome
#in the optimal palindrome we are gonna use the manacher's algorithm
def optimalpalindrome(s):
    tempo = '^#' + '#'.join(s) + '$'    #here we are just inserting the ^ and $ at the starting and ending position to make our string length of odd so it will be easier to calculate whether the centre position is at index odd or even
    n = len(tempo)
    c=r=0  #here c is the centre of the palindromic substring and r is the right boundary of the substring
    p=[0] * n    
    for i in range(1,n-1):  #here we are avoiding the first and the last element cause we have used ^ and $ at the first and last index which acts as a boundary of a string
        mirror = c-(i-c)  #mirror is the postion at the left side of the centre of a palindromic substring which has the same number of radius compared to that at index i
        if i < r :  #if the i index is with in the palindromic substring right border then
            p[i] = min(r-i,p[mirror])   #then the palindromic radius at index i is atleast the palindromic radius of its mirror or the distance of i from r
        while tempo[i-1-p[i]] == tempo[i+1+p[i]]:   #this loop is for expanding the radius of the palindromic substring
            p[i]+=1
        if i + p[i] > r:    #but if our palindromic radius exceeds beyound the right border of our previous palindromic centre having centre at c then we must change the index of c and r
            c=i
            r=i+p[i]
    maximumlen = max(p)    #here we are calculating the maximum radius of the palindromic substring
    centralindex=p.index(maximumlen)   #this gives us the centre which is the central index having the maximum palindromic radius
    start = (centralindex - maximumlen) // 2        #as the difference of  centralindex and the maximum length gives us the starting index and here we are dividing by 2 casue our original strings length is almost half of the length of the tempo string        
    return s[start:start+maximumlen]   #and as start + maximumlen gives us the ending index   
#here we are not using centralindex + maximumlen cause centralindex + maximumlen would give us the ending index based on the tempo string whose length is nearly double than the length of our original string
print(optimalpalindrome('babad'))
#time complexity : O(N)
#space complexity : O(N) cause we are using p whose length is almost N which is the length of the temporary string


#Sum of Beauty of All Substrings
#The beauty of a string is defined as the difference between the frequency of the most frequent character and the least frequent character (excluding characters that do not appear) in that string.
#Given a string s, return the sum of beauty values of all possible substrings of s.

#so the question is asking us to return the total sum of the beauty values of  all the substring

#brute approach
#so in the most brute or naive approach , what we can do is we go through each and every elements to make the substring and we count the frequency and we find the difference 
#then  finally we add those values for every substrings

def calculatebeauty(s):
    v=defaultdict(int)
    for str in s:    
        v[str]+=1
    return max(v.values()) - min(v.values())  #here as the beauty means the differnce between the frequency of the most frequent word and the frequency of the most least appearing word    
def brutebeauty(s):
    n=len(s)
    total = 0
    for i in range(n):
        for j in range(i,n):
            count=calculatebeauty(s[i:j+1])
            total+=count
    return total        
print(brutebeauty('aabcbaa'))
#time complexity : O(N^3)
#space complexity : O(N) cause we are using the storage called v which stores the character and its frequency as a key-value pair in the form of a dictonarys 


def optimalbeauty(s):
    n=len(s)
   
    total=0
    for i in range(n):
        m=defaultdict(int)
        for j in range(i,n):
            m[s[j]]+=1
            currentbeauty=max(m.values()) - min(m.values())
            total+=currentbeauty
    return total        
print(optimalbeauty('aabcbaa'))
#time complexity : O(N^2)
#space complexity : O(1)


