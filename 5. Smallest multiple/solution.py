import math 
def isPrime(x):
    for i in range(2,math.ceil(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def sqrtIsInt(x):
    s = math.sqrt(x)
    if s.is_integer():
        return True
    return False

primes = [i for i in range(1,21) if isPrime(i)]
sqrts = [i for i in range(1,21) if sqrtIsInt(i)]


shouldBe = []
for i in range(len(sqrts)):
    temp = True
    for j in range(len(sqrts)-1-i):
        if sqrts[j]%sqrts[i]==0:
            temp = False
            break
    shouldBe.append(temp)
filteredSqrts = [sqrt for (sqrt, b) in zip(sqrts, shouldBe) if b]

shouldBe = []
for prime in primes:
    temp = True
    for sqrt in filteredSqrts:
        if sqrt%prime == 0:
            temp = False
            break
    shouldBe.append(temp)
filteredPrimes = [prime for (prime, b) in zip(primes, shouldBe) if b]

print(filteredPrimes)
print(filteredSqrts)
value = math.prod(filteredPrimes)*math.prod(filteredSqrts)
print(value)
            