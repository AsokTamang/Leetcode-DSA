def stringtointeger(s):
  s=s.lstrip()  #here we have removed the leftmost whitespaces or the leading whitespaces from the given string
  c=1
  i=0
  if s[0]=='-':
    c=-1   #c denotes the sign for our final string
    i=1
  elif s[0]=='+':
    c=1
    i=1  

  if len(s)>1 and  s[1] in ['+','-']:   #as the first sign is the correct but the thing is the second indexed character must not be the sign
    return 0    
    
  a=''
  for char in s[i:]:  #now ignoring the sign , we are starting the loop from the 1st index of the given string.
    if char.isdigit()==False:  #we stop parsing the given string as soon as the non-digit character is found.
      break
      
    if char.isdigit():  #here we are negleting the negative sign and appending the other characters of the string in a varible called s.
      a+=char
  a=int(a) * c   
  if a < -2147483648:
    return -2147483648
  elif a >2147483647:
    return 2147483647 
  else:
    return a
print(stringtointeger( "04193abc"))
#time complexity : O(N)
#space complexity : O(N) in the worst case.


def optimalstringtointeger(s):
  s=s.lstrip()  #here we have removed the leftmost whitespaces or the leading whitespaces from the given string
  c=1
  i=0
  if s[0]=='-':
    c=-1   #c denotes the sign for our final string
    i=1
  elif s[0]=='+':
    c=1
    i=1  

  if len(s)>1 and  s[1] in ['+','-']:   #as the first sign is the correct but the thing is the second indexed character must not be the sign
    return 0    
    
  j=i
  for char in s[i:]:  #now ignoring the sign , we are starting the loop from the 1st index of the given string.
    if char.isdigit()==False:  #we stop parsing the given string as soon as the non-digit character is found.
      break
      
    if char.isdigit():  #here we are negleting the negative sign and appending the other characters of the string in a varible called s.
      j+=1
  ans=int(s[i:j]) * c   
  if ans < -2147483648:
    return -2147483648
  elif ans >2147483647:
    return 2147483647 
  else:
    return ans
print(optimalstringtointeger("4193 with words"))
#time complexity : O(N)
#space complexity : O(1) 




