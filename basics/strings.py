#Remove Outermost Parentheses
#A valid parentheses string is defined by the following rules:
#It is the empty string "".
#If A is a valid parentheses string, then so is "(" + A + ")".
# If A and B are valid parentheses strings, then A + B is also valid.
#A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.
#Given a valid parentheses string s, your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.

def remoutermost(s):
    counter = 0
    ans = []
    for char in s :
        if char == '(':  
            if counter>0:      #here even though the char is ( , we arenot appending the char until we check whehter the counter is > 0 cause at the first index the char is ( but the counter is 0 so if we append it char as soon as we found the ( then we cannot remove this opening parenthesis 
                ans.append(char)
            counter+=1  
        elif char == ')':
            counter-=1  #then as soon as we found out that the char is equal to ) then we just decrease the counter by 1  
            if counter > 0:      #then we check after the decrement of counter by 1 , if its still greater than 0 then we just append this char to ans
                ans.append(char)
    return ''.join(ans)            
print(remoutermost("()(()())(())"))
#time complexity : O(N)
#space complexity : O(N)