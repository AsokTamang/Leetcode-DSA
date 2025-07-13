names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

additionalMember1=input('Enter the name you want to add in the first list:')
additionalMember2=input('Enter the name you want to add in the second list:')

names.append(additionalMember1)
names1.append(additionalMember2)

for name in names:
    print(f'{name}! You are invited to the party on saturday')
for name in names1:
     print(f'{name}! You are invited to the party on saturday')


