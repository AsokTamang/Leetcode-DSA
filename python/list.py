sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w2.append(int(input('enter the number of lemonades you sold in the week 2: ')))
sales=(sales_w1+sales_w2)  
print('The sorted list is: ',sorted(sales))
best_Day=max(sales)
worst_day=min(sales)
print('profit on best day is:',best_Day*1.5)
print('profit on worst day is:',worst_day*1.5)


