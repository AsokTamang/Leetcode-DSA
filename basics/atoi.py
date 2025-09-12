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

#Pow(x,n)
#Implement the power function pow(x, n) , which calculates the x raised to n i.e. xn.
#Note : In output print 6 digits places after decimal point.

def powerxn(x,n):
  ans=1
  isnegative=False
  if n<0:   
    isnegative=True
    n=n*-1    #if the power value is negative then we make it positive by multiplying this by -1
  for i in range(n):  #as we just need to find the power of the given digit upto n times, we are multiplying the digit by n times
    ans=ans*x
  if isnegative:  #if the power value is negative then we divide 1 by the  actual answer 
   return 1/ans   
  else:    #otherwise we just return the actual answer.
    return ans

def optimalpow(x,n):
  nn=n  #here we are storing the copy of n to nn
  ans=1
  if nn<0:  #if the base power is negative then we make it positive 
    nn=-1 * nn
  while nn>0:
    if nn % 2 ==0:  #if the base power is even then we multiply the given number with the given number which is x^2 and divide the basepower n by 2
      x=x*x
      nn=nn//2
    else:   #but if the base power becomes odd then we make the ans to multiply by the 
      ans=ans*x
      nn=nn-1  
  if n<0:
    ans= 1/ans 
  return ans     
print(optimalpow(2,10))







print(powerxn( 2.0000,-2))
#time complexity : O(N)
#space complexity : O(1)





