def stringtointeger(s):
  s=s.replace(' ','')  #here we are removing the whitespaces in the given string and we have already removed the whitespace character from the left side,right side and also from the middle in a given string
  c=1
  for char in s:
    if char=='-':
      c=-1
      break
  a=''
  for char in s:
    if char!='-' and char.isdigit():  #here we are negleting the negative sign and appending the other characters of the string in a varible called s.
      a+=char
  a=int(a) * c   
  if a < -2147483648:
    return -2147483648
  elif a >2147483647:
    return 2147483647 
  else:
    return a
print(stringtointeger( "4193 with words"))
#time complexity : O(N)
#space complexity : O(N) in the worst case.

