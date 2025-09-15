def countDigit(n):
    print(len(str(n)))
countDigit(15)   

def reverseDigit(n):
    print(str(n)[::-1])  #here we are first converting the digits into a string then we are reversing the order
reverseDigit(1056)    

def palindrome(n):
    if(str(n)==str(n)[::-1]):
        print('palindrome')
    else:
        print('not palindrome')
palindrome(65) 

def greatestComDivisor(n1,n2):
   a=[i for i in range(1,n1+1) if n1 % i ==0]
   b=[i for i in range(1,n2+1) if n2 % i ==0]
   c=set(a).intersection(set(b))
   print(max(c))            
greatestComDivisor(10,40)


def armstrongNumber(n):
    numss=n
    arr=[]
    s=0
    while n > 0:
        digit=n % 10
        arr.append(digit)
        n=n//10
    for num in arr:
        s+=num**len(arr)
    if s == numss:
        print('armstrong')
    else:
        print('not armstrong')            
armstrongNumber(153)        

def arms(n):
    arr= [int(num) for num in str(n)]
    s=0
    for num in arr:
        s+=num ** len(arr)
    if s==n:
        print('armstrong')    
    else:
        print('not armstrong')    
  
arms(153)    


def allDivisors(n):
  a=[int(i) for i in range(1,n+1) if n % i ==0]
  print(sorted(a))
allDivisors(10)  


def prime(n):
    s=True
    if n==2:
        print('prime number')
    else:    
     for i in range(2,n-1):
        if(n % i != 0 and n!=1 and n!=0):
           s=True
        else:
           s=False
    if(s):
        print('prime number')    
    else:
        print('Composite number')       
prime(11)                


def sortastack(array):
    if len(array)==1:
        return array
    else:
        if not array or len(array)==1:  #and our base case is that if only one number remains inside an array we return 
            return 
        top=array.pop()  #we keep on deleting the last element from our array till only one number remains inside an array.
        sortastack(array) #by calling this same function recursively
        insertelement(array,top)     #then after the base case is reached, we insert those popped numbers recursively using another function
        return array
def insertelement(array,element):
    if not array or element<=array[-1]:  #as the question is asking us to sort the array in descending order , thats the passed element must be lesser than the number that is already in an array
        #and in some cases if the only remaining number in an array is lesser than the passed number then we have to use the condition of if not array.
        array.append(element)
        return    
    else:
        top=array.pop()  #if the number which is already inside an array is lesser than the passed element then we pop this number then try inserting the passed number recursivley
        insertelement(array,element)
        array.append(top) #and at last , we insert that deleted number
print(sortastack([1, 2, 5, 10]))
#time complexity : O(N^2)
#space complexity : O(N)
