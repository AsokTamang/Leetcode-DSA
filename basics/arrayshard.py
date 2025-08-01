#1#Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.
#brute approach
def bruteeleme(array,n): #here n is the length of an array
    a = []
    for i in range(n):
        if array[i] in a:    #what we do here is , if the current i indexed element is already a target element or inside a list called a then we dont need to count this again so 
            #by using continue we are skipping this index and moving onto the next index i
            continue
        count = 1
        for j in range(i+1,n):
            if array[i] == array[j]:
                count+=1
        if count > (n/3):
             a.append(array[i])  #as we are appending the required element in an array called a.
    print(a)
bruteeleme( [1, 2, 1, 1, 3, 2],6)  
#time complexity is O(N^2)
# space complexity is O(1) in worst case if all the elements appear more than n//3 times          

#better approach
def bettereleme(array,n):
    m={}
    a=[]
    for num in array:
        m[num] = m.get(num,0) + 1 #default is 0 and we add one if we keep finding the same number
    for key,value in m.items():
        if value > n/3:

            a.append(key)
    print(a)
bettereleme([1, 2, 1, 1, 3, 2,2,2],6) 
#time complexity is O(N) + O(N)  so O(N) is the space complexity
# space complexity is O(N) for worst case + O(1) this one is of list

#optimal approach
#the below function will be appropriate for the element which appears more than n/2 times 
def optimaleleme(array): #here n is the size of an array
    candidate = 0
    count = 0
    for num in array:
        if num == candidate:
            count+=1
        elif count == 0:    #and whenever the count becomes 0, we change the candidate as only the element which has a higher range survives
            candidate = num
            count = 1
        else:
            count -=1   #if there is different number than the canditate then we subtract the count by 1.
    print('The candidate element is :',candidate ,'having a range of',array.count(candidate))
optimaleleme([1,1,1,2,0]) 
#but for the element which appear more than n/3 times , we have to make two candidates cause in most cases , n/3 means about the one-third part of an array is filled with that element and 
#there is a higher chance that more than one element is  suitable here.

def optimalelem2(array):
    candidate1=0
    count1=0
    candidate2=0
    count2=0
    a = []
    for num in array:
        if num == candidate1:
            count1+=1
        elif num == candidate2:
            count2+=1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1-=1
            count2+=1
    if candidate1!=candidate2:
        a.append(candidate1)
        a.append(candidate2)
        print(array.count(candidate1)) 
        print(array.count(candidate2))

    else:
        a.append(candidate1)
        print(array.count(candidate2))
        
    print(a)
optimalelem2([1,1,1,2,2,2,2,0])    



#2#This problem has 3 variations. They are stated below:
#Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
#variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
#Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.

#variation 1 answer
#brute approach
#here the formula we are using is NcR 
#which is factorial of N divided by (N-R) factorial and R factorial where N is the number of rows - 1 and R is the number of columns - 1.
def var1(r,c):  #here r is the number of rows and c is the number of columns
    res=1
    for i in range(0,c):
        res = res * (r-i) // (i+1)   #here i acts c value
    print(res)
var1(10,3) 
#time complexity is O(C)
# space complexity is O(1)   

def var2(r,c):
    res = 1
    for i in range(1,c+1):    #c is the number of columns
        print(res,end=' ')
        res = (res * (r-i))//i
    print()        
var2(6,6)    
#time complexity: O(N)   here N is the number of columns 
#space complexity: O(1)   it is constant






         


         





    


           


            


