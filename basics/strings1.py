#Sort Characters by Frequency
#You are given a string s. Return the array of unique characters, sorted by highest to lowest occurring characters.
#If two or more characters have same frequency then arrange them in alphabetic order.
def sortfreq(s):
    m={}
    for char in s:
        m[char]=m.get(char,0) + 1 #here the default value will be 0 and we are adding 1 as soon as we found the occurence of letter 
    
    return(sorted(m,key=lambda x: m[x]))[::-1]  #here what we are doing is we are sorting our dict called m by using sorted and lambda where x:m[x] means sorting based on the values and using [::-1] to reverse the output 
#as the question is asking us to return from highest to lowest
print(sortfreq("cba"))
#time complexity : O(N) + O(K)  #here N is the number of characters in a given string and K is the number of keys in our dictinary m
#space complexity : O(N)

#Maximum Nesting Depth of the Parentheses
#A string s is a valid parentheses string (VPS) if it meets the following conditions:
#It only contains digits 0-9, arithmetic operators +, -, *, /, and parentheses (, ).
#The parentheses are balanced and correctly nested.
# Your task is to compute the maximum nesting depth of parentheses in s. The nesting depth is the highest number of parentheses that are open at the same time at any point in the string.
def nestingdepth(s):
    count = 0
    ans = 0
    for char in s:
        if char == "(":
            count+=1
            ans=max(ans,count)
        elif char == ")":
            count-=1
        
    return ans
print(nestingdepth("(1)+((2))+((((3))))"))  
#time complelxity : O(N) N is the number of characters in a string
# space complexity : O(1)           
