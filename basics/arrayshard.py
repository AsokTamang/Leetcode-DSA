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
#Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
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

#Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.
def var2(r,c):
    res = 1
    for i in range(1,c+1):    #c is the number of columns
        print(res,end=' ')
        res = (res * (r-i))//i
    print()        
var2(6,6)    
#time complexity: O(N)   here N is the number of columns 
#space complexity: O(1)   it is constant


#Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.
def var3(n):   #here n is the number of rows given
    for i in range(1,n+1):   #this outer loop is for printing the number of rows
        #and for each value of i we reset the res to 1 and repeat the process
        res = 1
        for j in range(1,i+1):    #here our i acts as the number of column for each row
            print(res,end=' ')
            res = (res * (i-j))//j
        print()    
var3(5)
#timecomplexity : O(N^2) as we are using outer loop as well as the inner loop
#spacecomplexity : O(1)



#3#Given an integer array nums. Return all triplets such that:
#i != j, i != k, and j != k
#nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. The output and the triplets can be returned in any order.

#bruteapproach
def triplets3sum(array):
    a = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):   #to find the second element we are starting the loop from i+1
            for k in range(j+1,len(array)):  #to find the third element we are starting the loop from j+1
                if array[i] + array[j] + array[k] == 0:
                    a.append([array[i],array[j],array[k]])
    print(a)
  
triplets3sum([2, -2, 0, 3, -3, 5])
#timecomplexity: O(N^3) as we are using 3 nested loops
#spacecomplexity : O(1) constant

#better approach
# now for better approach what we do is we dont use the third loop, we just use the reverse math which is 
# as to get the sum of triplets to 0 then of course the third element is the negative of sum of first and second element
# as an example
# if a + b + c =0 then c = -(a+b)
#so we gonna use this reverse math technique to remove the third loop and get the value of third element
#and also as we cannot randomly insert the required third element as it must be in the array. So waht we do is we use dictionary 
#to store j elements.
def bettertriplet(array):
    s=set()
  
    for i in range(len(array)):
        m={}
        for j in range(i+1,len(array)):
            thirdelement=-(array[i]+array[j])
            if thirdelement in m:   #if the required third element is not in the m then it means that we havenot found the third element to meet the condition right now , but it can be met in the future 
                #if its in the array otherwise not
                s.add(tuple(sorted([array[i],array[j],thirdelement])))   #inorder to prevent the duplicate insertion of the triplet we are usign the set.add method
            m[array[j]]=array[j]   #this code runs whether the if else condition is true or false3
    print(list(s))
bettertriplet([2, -2, 0, 3, -3, 5])            
#timecomplexity: O(N^2 + log(M))
#spacecomplexity: O(M)


#optimal approach
def optimaltriplet(array):
    array=sorted(array)
    s = []
    for i in range(len(array)):
        if i>0 and array[i] == array[i-1]: continue 
        left = i+1  # left most part
        right = len(array) - 1   # right most part
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == 0:
                s.append([array[i],array[left],array[right]])
                left +=1
                right -=1
                while left < right and array[left] == array[left+1]: left+=1  #if the next left element is equal to the previous left element then theres no point in using the current element as left thats why we are incrementing by 1
                
                while left < right and array[right]== array[right-1]: right-=1  #if the next right element is equal to the previous right then theres no point in using the current element as right      


                
            elif sum < 0:
                left+=1
               
                
            else :
                right-=1
                
    print(s)            
optimaltriplet([2, -2, 0, 3, -3, 5])                 


#Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#a, b, c, d are all distinct valid indices of nums.
#nums[a] + nums[b] + nums[c] + nums[d] == target.
def brutea4sum(array,target):
    s= set()
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1,len(array)):
                for l in range(k+1,len(array)):
                    if (array[i] + array[j] + array[k] + array[l] ==target):
                        s.add(tuple([array[i],array[j],array[k],array[l]]))
    print(list(s))  #then we convert the set into the final list
brutea4sum(  [1, -2, 3, 5, 7, 9],7)   
#time complexity is : O(N^4)
# space complexity is : O(1) which is constant

def better4sum(array,target):
    s=set()
   
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            hasset=set()  #this hasset must be inside the j loop cause we are using this hasset to store the k indexed elements that must be unique for every loop of j
            for k in range(j+1,len(array)):
                fourthelem=target - (array[i]+array[j]+array[k])
                if fourthelem in hasset:
                    s.add(tuple(sorted([array[i],array[j],array[k],array[fourthelem]])))
                hasset.add(array[k])    

    print(s)        
            
   
better4sum([1, -2, 3, 5, 7, 9],7)  
#time complexity is : O(N^3)
# space complexity is : O(M) + O(K)   where M is the unique quadruplets which denotes the set and K is the number of necessary third and fourth elements which denotes the dictionary m                                   
  

#optimal approach
#in this approach what we do is we use four pointers 
#where the two pointers are i and j are made fixed where j = i+1 and the other two pointers k and l are made moving.
def optimalsum(array,target):
    s =set()  #this set s is for storing the final quadruplets
    array=sorted(array)
    for i in range(len(array)): 
        if i > 0 and array[i] == array[i-1]:   #this condition is to prevent the use of same i indexed element or number cause the question is asking for the unique quadruplets
            continue      #if the next i indexed number is also same then we just skip and continue with the next iteration of i
        for j in range(i+1,len(array)):   #same case here for j
            if j >i+1 and array[j] == array[j-1]:
                continue
            k=j+1   
            l=len(array)-1   #it is the last index
            while k < l:    #these two moving pointers mustnot cross eachother or become equal
                suum=array[i] + array[j] +array[k] + array[l]
                if suum == target:
                    #if we found the  sum then we just change value of k by increasing as it goes towars west side and the value of l by decreasing as it move towars east side
                    s.add(tuple(sorted([array[i],array[j],array[k],array[l]])))
                    k+=1
                    l-=1
                    while k < l and array[k] == array[k-1]: k+=1    #Same here the changed value must not be equal to the previous value
                    while k < l and array[l] == array[l+1]: l-=1
                elif suum<target:
                    k+=1
                else:
                    l-=1   
    print('The unique quadruplets using the optimal solution is:',s)
optimalsum( [1, -2, 3, 5, 7, 9],7)                       
#time complexity is : O(N^3)  its N^3 cause we are using the two nested loops and inside them we also have a while loop that runs after every index of J so the time complexity of this particular loop will be O(N)
#space complexity is : O(1) or O(K) where K is the number of unique quadruplets   as we are not using any dicts or sets to store the input variables rather just to give the output


#You are given an integer array arr of size n which contains both positive and negative integers. Your task is to find the length of the longest contiguous subarray with sum equal to 0.
def brutesubarrays(array,n):
    length = 0
    for i in range(n):
        s = 0  #here for every value of i we makes the sum or s = 0 cause the new subarray is being creater in every value of i
        for j in range(i,n):
            s+=array[j]   #then we calculate the sum for every value of i
            if s == 0:   #if we found the sum or s  == 0 then we start calculating the lenght using max between the previous length where we got the sum 0 and the current length as the question is asking us the maximum length
                length = max(length , j-i+1)   #here j-i+1 gives us the number of elements in an array
    if length!=0:
        print(length)
    else:
        print(0)
brutesubarrays([15, -2, 2, -8, 1, 7, 10, 23],8)    
#time complexity is : O(N^2)
# space complexity is : O(1)    

#as the subarray is the continous array inside an array thats why we cant sort the array

#better approach
def bettersubarrays(array,n):
    s=0
    length = 0
    m={}   
    for i in range(n) :
        s+=array[i]
        if s == 0:
            length=max(length,i+1)   #here i+1 gives us the number of elements in a subarray as our i is starting from 0 or we can also write i-0+1
        elif s in m:   #if the same sum exists in the current i index then ofcoure there exists a subarray that gives the sum 0
            length = max(length,i-m[s] )    #here i - m[s] gives us the length of subarray or the number of elements as we are storing the prefix sum with their respective indexes. so the subtraction of the current index with that stored index gives us the length of the required subarray     
        else:  #only if the sum doesnot exists then we store the prfix sum with its current index
         m[s] = i   #here we are storing the current born sum with the current index so that we can use this postion later as shown in the upper code
    print(length)
bettersubarrays([15, -2, 2, -8, 1, 7, 10, 23],8) 
















            








         


         





    


           


            


