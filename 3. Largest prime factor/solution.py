import math

def isPrime(x):
    i=2
    while(i<math.ceil(math.sqrt(x))+1):
        if x%i==0:
            return False
        i += 1
    return True

def getBiggestPrimeFactor(x):
    divisor=2
    biggestPrimeFactor = 0
    while divisor<(math.ceil(math.sqrt(x))+1):
        while x%divisor==0:
            x /= divisor
            if isPrime(divisor):
                biggestPrimeFactor = divisor
        divisor += 1
    
    if isPrime(x) and x>biggestPrimeFactor:
        return x
    return biggestPrimeFactor

print(getBiggestPrimeFactor(600851475143))
