def primeNumber(n):
    if n <= 1:
        print("The checking number must be greater than 1.")
        return
    for i in range(
        2, int(n ** 0.5) + 1
    ):  # here we are making the loop from 2 to the square root of a number +1 
        #cause the square root of the number acts as a mid-point or a boundary, 
        #which means if we found any number before this mid-point which can divide the number and get remainder 0 
        # then obviously the numebr after this also can give same result.
        #so this loop runs O(√n) times
        if n % i == 0:
            print("The number is a composite number.")
            return
    print('The number is a prime number')
    return

(primeNumber(10))
