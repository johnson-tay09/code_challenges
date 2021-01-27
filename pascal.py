

def printPascal(n):
    # for each value in 1 to 3+1
    for row in range(1, n+1):
        # the first value is always 1
        constant = 1
        # for each value in 1 to row +1
        for i in range(1, row+1):
            print(constant, end=" ")
            constant = int(constant * (row-i)/i)
        print("")


n = 3
printPascal(n)
