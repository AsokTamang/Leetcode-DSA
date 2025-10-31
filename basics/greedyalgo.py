#Assign Cookies
def assigncookes(student,cookie):
    n=len(student)
    m=len(cookie)
    def helperfunction(studentindex,cookieindex):
        if studentindex>=n or cookieindex>=m:#this is the base case where all the students or the cookies are passed
            return 0
        if cookie[cookieindex]>=student[studentindex]:
            return 1+helperfunction(studentindex+1,cookieindex+1)  #here if the current indexed cookie satisfies the student then we add one to the satisfied number of student and recursivley move to next index of studnet as well as cookie
        else:
            return helperfunction(studentindex,cookieindex+1)  #if the current cookie cannot satisfy this current student then we move to the next cookie for the same student
    return helperfunction(0,0)
print(assigncookes( [1, 2, 3] , [1, 1]))    
#time complexity : O(max(n,m))  due to recursion as we are going into only one way of recursion depth,either through cookies or through both students and cookies
#space complexity : O(max(n,m))  due to the recursion