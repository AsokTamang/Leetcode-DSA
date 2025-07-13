print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
a=6
b=5
operator=input('enter an operator: ')
if (operator=='+'):
    print(a+b)
elif (operator=='-'):
    print(a-b)  
elif (operator=='*'):
    print(a*b)  
elif (operator=='/'):
    print(a/b)             

temp=int(input('enter temperature in celsius.'))
print('Temperature in fahrenheit is : ',(temp*9/5)+ 32) 



