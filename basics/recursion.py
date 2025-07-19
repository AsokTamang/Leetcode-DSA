def printNumbers(n,current=1):
    if current<= n:
     print(current)
    else:
       return 
    printNumbers(n,current+1)
printNumbers(10)    