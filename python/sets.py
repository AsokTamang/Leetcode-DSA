#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
print('Eric' in friends and 'John' in my_friends)
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
sameNames=friends.intersection(my_friends)   #here intersection will help to find the elements that are in both friends and my_friends.
print('The names on both sets are:',sameNames)
total=friends.union(my_friends)    #union will get the sum of elements in both friends and my_friends sets.
print('The union of both sets :',total)

onlyFriends=friends.difference(my_friends)  #this prints the name that are only in friends set
onlyMy_friends=my_friends.difference(friends)
print('Names that are  only in  my friends set',onlyMy_friends)
print('names that are only in friends set',onlyFriends)
print(set(cars))  #here we are converting the list into set

