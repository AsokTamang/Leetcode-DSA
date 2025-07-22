def recursiveinsertion(array,n):
     if n==1:
            print(array)
            return
     for i in range(n):
       
        j=i
        while j>0 and array[j-1]>array[j]:
            array[j-1],array[j]=array[j],array[j-1]
            j-=1
        recursiveinsertion(array,n-1)
recursiveinsertion([4,1,5,2,3],5)