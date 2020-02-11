"""
All-Or-Nothing Transform experiments.
"""

import hashlib


K0 = 118  # public.
K = 26  # random, masked within message package.

print(f"Public K0 = {K0}")

m = list(b'pretty cool!')
print(bytearray(m), m)


def E1(k, p):
    # (Encryption function is arbitrary for our purposes.)
    return (p + k + 3) % 256


def E2(k, p):
    # (Less guessable version.)
    sha = hashlib.sha256()
    sha.update(bytes([k, p]))
    return sha.digest()[0]


E = E1


def H(mi, i):
    global K0
    return E(K0, mi ^ i)


mP = []
mS = K
for (i, mi) in enumerate(m, 1):
    mPi = mi ^ E(K, i)
    mP += [mPi]
    mS ^= H(mPi, i)
mP += [mS]

print(bytearray(mP), mP)


########################

dK = mP[-1]
mP = mP[:-1]
for (i, mPi) in enumerate(mP, 1):
    dK ^= H(mPi, i)
print(dK)

d = [mPi ^ E(dK, i) for (i, mPi) in enumerate(mP, 1)]
print(bytearray(d), d)
