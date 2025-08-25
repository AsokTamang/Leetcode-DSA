# Remove Outermost Parentheses
# A valid parentheses string is defined by the following rules:
# It is the empty string "".
# If A is a valid parentheses string, then so is "(" + A + ")".
# If A and B are valid parentheses strings, then A + B is also valid.
# A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.
# Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.


def remoutermost(s):
    counter = 0
    ans = []
    for char in s:
        if char == "(":
            if (
                counter > 0
            ):  # here even though the char is ( , we arenot appending the char until we check whehter the counter is > 0 cause at the first index the char is ( but the counter is 0 so if we append it char as soon as we found the ( then we cannot remove this opening parenthesis
                ans.append(char)
            counter += 1
        elif char == ")":
            counter -= 1  # then as soon as we found out that the char is equal to ) then we just decrease the counter by 1
            if (
                counter > 0
            ):  # then we check after the decrement of counter by 1 , if its still greater than 0 then we just append this char to ans
                ans.append(char)
    return "".join(ans)


print(remoutermost("()(()())(())"))
# time complexity : O(N)
# space complexity : O(N)


# Reverse every word in a string
# Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.
# Return a string with the words in reverse order, concatenated by a single space.

#the given question is asking us to reverse the words in the given string
def reversewordins(s):  
 initial = s[::-1]  #here we are reversing the whole letters and words' position of the given string
 ans = []
 i = 0
 n = len(s)
 while i<n:
  word=[]
  while i<n and initial[i]!=' ':
     word.append(initial[i])
     i+=1
 #if we get the ' ' at the current index i then its clear than one word is formed so we store this one word's reverse form in our answer variable called ans
  i+=1
  if len(word)>0:
   ans.append(''.join(word[::-1]))
  
 return ' '.join(ans)
print(reversewordins("welcome to the jungle"))
#time complexity : O(N)
# space complexity : O(N) 


#Largest Odd Number in a String
#Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
#The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)


#brute approach 
#in the brute approach what we did was looping through every possible numbers which are odd and finding the maximum among them
def largestodd(s):
   n=len(s)  
   maxim=float('-inf')
   for i in range(n):
      for j in range(i+1,n):
         num=int(s[i:j+1] )   #here we are using j+1 cause in slicing the last index is always ignored , so we are using j+1
         if num % 2 !=0:
            maxim=max(maxim,num)
   return str(maxim)   
print(largestodd("0214638"))      
#time complexity : O(N^2)
#space complexity :O(1)

#in the optimal approach what we will do is
#we loop from the last index or the last digit of the given string cause ofcourse it will give us the largest possible number in the given string if we just start from the last index
#and as soon as we find the largest odd number from the last index , this will be our answer

def optimallargestodd(s):
   n = len(s)
   for i in range(n-1,-1,-1):
      if int(s[i]) % 2 !=0:  #as soon as we found the last digit from the last index which is odd then this will be our answer. 
         return int(s[:i+1])   #here to include this odd digit i we are using i+1
   return -1
print(optimallargestodd("0214638"))  
#time complexity : O(N)
#space complexity : O(1) 
      
#Longest Common Prefix
#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#here what the question is asking us is to find the common or matching letters or prefix among the given words in an array
def commonprefix(a): #here a is the array which consists of all the strings from which we need to find the prefix
   ans = ""
   for i in range(len(a[0])):
      for str in a[1:]:
         if i==len(str) or str[i]!=a[0][i]:   #here why we are checking i==len(str) cause the first letter in the array might have the longest length whereas the other strings might have the shortest length, so as soon as i exceeds the length of the other string , then
            #there is no point in comparing the common prefix . so we just return the ans
            return ans
      ans+=a[0][i]  
print(commonprefix( ["dog" , "cat" , "animal", "monkey" ]))        
#time complexity : O(M*N)  here M is the length of the first string
# space complexity : O(M)  in the worst case all of the strings in the first word can be a common prefix     

#Isomorphic String
#Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


#so here what the question is asking us is to check whether the given string is isomorphic or not
#and for the two strings to be isomorphic, if  the letters of first string s is all replaced by the letters of the second string t and those letters replaced are mapped to their unique replacing number then only the condition is true otherwise false 
def isomorphicstring(s,t):
   m1={}  #here this is a map1
   m2={}   #here this is a map2
   #first condition, as soon as we find that the length of two strings are unequal then we return false
   if len(s)!=len(t):
      return False
   for i in range(len(s)):#looping through every characters of any string among the two
      word1=s[i]  #then assiging the given i indexed character of word s in word1 and of word t in word2
      word2=t[i]
      #at first the below two conditions will always be false , so it wont return false or return anything 
      if (word1 in m1 and m1[word1]!=word2) or  (word2 in m2 and m2[word2]!=word1):  #then we check if the word1 has already a value which is not equal to the current word2 then we just return false
         return False
      #so we reach here , which stores the first letter of the word s as a key and first letter of the word t as a value in a dict called m1
     
      m1[word1]=word2 
      m2[word2]=word1 
   return True   
print(isomorphicstring( "apple", "bbnbm"))   
#time complexity : O(N)  where N is the length of the given strings
#space complexity : O(N)
          

#rotate string
#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#A shift on s consists of moving the leftmost character of s to the rightmost position.
#For example, if s = "abcde", then it will be "bcdea" after one shift.

def rotatestr(s,goal):  #the best approach will be as s+s consists of all the s string which can be obtained after every rotations possible
   #the string can be rotated only upto the length of any string
   if (len(s)!=len(goal)):
      return False
   return goal in (s+s)
print(rotatestr( "abcde" ,"abcde"))  
#time complexity : O(N) here N is the length of the string
#space compelxity : O(1)
   
        
#Valid Anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#here what we are doing is we are checking the count 
def validanagram(s,t):
   m1={}
   m2={}
   for char in s:
      m1[char]=m1.get(char,0) + 1  #here 0 is the default
   for char in t:
      m2[char]=m2.get(char,0) + 1  
   if m1==m2:
      return True
   else:
      return False
print(validanagram( "anagram" ,"nagaram"))       
#time complexity : O(N+M) where N is the lenght of the first string and M is the length of the second string
# space complexity : O(N+M)
