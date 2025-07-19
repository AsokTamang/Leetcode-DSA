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