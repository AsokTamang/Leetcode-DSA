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



#Roman to Integer
#Roman numerals are represented by seven different symbols:
#Roman numerals are typically written from largest to smallest, left to right. However, in specific cases, a smaller numeral placed before a larger one indicates subtraction.
#The following subtractive combinations are valid:
#I before V (5) and X (10) → 4 and 9
#X before L (50) and C (100) → 40 and 90
#C before D (500) and M (1000) → 400 and 900
#Given a Roman numeral, convert it to an integer.
 
                
#optimized version
def romanint(s):
    data = {
        "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":500,"CM":900
    }
    i = 0
    ans=0
    while i < len(s):
        if i < len(s)-1:
            if s[i:i+2] in data:
                ans+=data[s[i:i+2]]
                i+=2
        if s[i:i+1] in data:
            ans+=data[s[i:i+1]]
            i+=1
    return ans
print(romanint("DCCCXC"))        
#time complexity : O(N)
#space complexity : O(1) our space complexity is O(1) our dictonary is fixed through out the code loop


#string to integer(atoi)
#Implement the function myAtoi(s) which converts the given string s to a 32-bit signed integer (similar to the C/C++ atoi function).
def stringtoint(s):
    ans =0
    sign = 1
    i = 0
    while i < len(s) and  s[i] == " ":
            i+=1
    if i < len(s) and (s[i]=="+" or s[i] == "-"):
            if s[i] == "-":
                sign=-1
            i+=1
    while i < len(s) and s[i].isdigit():
        ans=ans*10 + int(s[i])
        i+=1
    result = sign * ans
    if result > 2147483647:
         return 2147483647 
    elif result < -2147483648:
         return -2147483648     
    else:
     return sign * ans    
                    

print(stringtoint("0-1")) 
#time complexity : O(N)
# space complexity : O(N) in worst case 

    

