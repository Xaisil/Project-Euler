def getNthPrime(n):
    howMany = n
    while True:
        primes = erasto(howMany)
        if len(primes) >= n:
            return primes[n-1]
        howMany *= 2

def erasto(n):
    shouldBe = list(True for i in range(n+1))
    primes = list(range(n+1))
    m = 2
    while (m**2 <= n):
        if shouldBe[m]:
            for i in range(m * 2, n + 1, m):
                shouldBe[i] = False
        m += 1
    
    return [p for (p,b) in zip(primes,shouldBe) if b][2:]




print(getNthPrime(100001))
    
