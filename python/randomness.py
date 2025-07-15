import random
for i in range(5):
 print(random.uniform(1,10))   #random.uniform will help to provide the random numbers between given two params

friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))    #random.choice will only provide one random name
a=(random.sample(friends_list,3))    #random.sample will provide random names based on the quantity provided and .sample wont provide a duplicate value
print(random.choices(friends_list,k=3))  #random.choices will also do the same as .sample but will provide the duplicate value
print(''.join(a))