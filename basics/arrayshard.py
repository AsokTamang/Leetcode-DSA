#Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.
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
           


            


