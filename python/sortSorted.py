#sorted converts anything either string,list or tuples into a sorted version of array or list
my_list = [1,5,3,7,2]
demoList=[1,-2,-3,4,5,6,7,8]

print(sorted(demoList,key=abs))   #here key=abs means we are sorting the list in the ascending order but only based on the absolute values of the list


print(my_list.sort())   #here .sort will only sort the list but doesnt return the new list where as 
print(f'The list after sorting is or after using .sort() is:',my_list)
print(sorted(my_list))   #sorted will provide the new list after sorting the provided list



my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

print(sorted(my_llist,key= lambda item:item[2]))   #here we are sorting the linked list based on it's second value. as lamba is a custom function that can be used for anything 