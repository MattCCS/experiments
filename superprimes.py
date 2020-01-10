"""
Fun with super-primes, and my extension concept, "hyper-primes".

Super-primes are primes whose position (starting with 1)
within the set is, itself, prime.

Hyper-primes are primes whose position (starting with 1)
appears in the set itself.

https://en.wikipedia.org/wiki/Super-prime
"""


def isprime(n):
    return n > 1 and all(n % i for i in range(2, n - 1))


PRIMES = list(filter(isprime, range(1000)))


def super(nums):
    return [n for (i, n) in enumerate(nums, 1) if isprime(i)]


def hyper(nums):
    return [n for (i, n) in enumerate(nums, 1) if i in nums]


p = PRIMES
sp = super(p)
ssp = super(sp)

print(p)
print(sp)
print(ssp)

hp = hyper(p)
hhp = hyper(hp)

print(p)
print(hp)
print(hhp)
