import math

def sumOfSquares(n):
    s = 0
    for i in range(1,n+1):
        s += i**2
    return s

def squareOfSum(n):
    return sum(list(range(1,n+1)))**2

x = 100
print(squareOfSum(x)-sumOfSquares(x))