#assign cookies
def assigncookies(student,cookie):
    student.sort()  #here we are sorting both student and cookie so that the least greedy stident can be satisfied easily by the smallest amount of cookie
    cookie.sort()
    i=0  #for student
    j=0  #for cookie
    n=len(student)
    number = 0
    while i<n:
        if cookie[j]>=student[i]:
            number+=1  
            i+=1          
        j+=1  
        
    return number          
print(assigncookies([4, 5, 1] , [6, 4, 2]))
#time complexity : O(NlogN+MlogM)
#space complexity : O(1)