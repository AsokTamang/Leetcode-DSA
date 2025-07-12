msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Eric','John','Michael','Terry','Graham']

  #join helps us to make the array into a string
  #split makes the string into array.


print(msg.split())   #this makes the msg into an array.

print('-'.join(friends_list))   #this joins the string from array to make a string but without no space.




csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']

# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

array=','.join(csv.split(';'))  #this splits the csv at the comma
second=','.join(array.split(':'))  #this is the final array of friends_list
final=second.split(',')
friends_list=(':').join(friends_list).split(':')
friends_list.clear()
friends_list.append(second)
print('The modified data list is: ',friends_list)


