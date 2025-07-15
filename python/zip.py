nums = '1234' 
letters = ['a','b','c','d']
names =['John','Eric','Michael','Graham','Joe']

combo = zip(nums,letters,names)  #here we are zipping the datas called nums , letters and names inside a combo.


numbers,letterss,namess=zip(*combo)  #here * means we are unzipping the data using zip
print('The unzipped variables are: ',numbers,letterss,namess)


keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keyList=keys.split(' ')     #here we are spliting the keys at the space which convertes the sentence into an array
valueList=values.split(' ')
dictzipped=(dict(zip(keyList,valueList)))
print(dictzipped)
print('The unzipped keys and values are: ',list(dictzipped.keys()),list(dictzipped.values()))
print('The unzipped key and values from a dict is: ',list(zip(*dictzipped.items())))


