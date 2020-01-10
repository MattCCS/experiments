"""
Fun with primes in different bases
"""

import math
import string


def is_prime_slow(p, d=False):
    if p == 2:
        return True
    for n in range(2, math.ceil(math.sqrt(p))):
        if math.gcd(p, n) != 1:
            if d:
                print(f"Falsed GCD with {n}")
            return False
    else:
        return True


def is_composite(c):
    return not is_prime_slow(c)


def prime_factors(n):
    return [
        i for i in range(2, n)
        if (n % i == 0) and is_prime_slow(i)
    ]


def composite_lsds_from_factors_in_base(factors, base):
    composite_lsds = set([0])
    for factor in factors:
        for i in range(1, base // factor):
            composite_lsds.add(factor * i)
    return composite_lsds


class Base(object):
    DIGITS = string.digits + string.ascii_uppercase + string.ascii_lowercase

    def __init__(self, value):
        self.value = value
        # self.digits = Base.DIGITS[:value]
        self.prime_factors = frozenset(prime_factors(value))
        self.lsds_indicating_compositeness = frozenset(
            composite_lsds_from_factors_in_base(self.prime_factors, self.value)
        )
        self.lsds_indicating_primeness = frozenset(
            i for i in range(self.value)
            if i not in self.lsds_indicating_compositeness
        )

    # def least_significant_digit(self, n):
    #     return self.digits[n % self.value]

    def is_possible_prime_number(self, n):
        return (n % self.value) in self.lsds_indicating_primeness or \
               (n in self.prime_factors)

    def __repr__(self):
        return "<Base({} -> {})>".format(self.value, list(self.lsds_indicating_primeness))


BASES = sorted([
    Base(i) for i in range(4, 1000) if is_composite(i)
], key=lambda e: len(e.lsds_indicating_primeness))


def custom_primality_test(n, d=False):
    if d:
        print(f"Testing primality of {n}...")

    if n in {0, 1}:
        return False

    if n in {2, 3}:
        return True

    for base in BASES:
        val = base.value
        modded = n % base.value
        if not base.is_possible_prime_number(n):
            if d:
                print(f"Base {base} rejected it, since n mod {val} is {modded}, and {modded} is "
                      "not in the base's prime-possible list!")
            return False
        else:
            if d:
                print(f"Base {val} says maybe...")

    if d:
        print("All bases approved -- probably!  Must run exhaustive test...")
    return None


import functools


@functools.lru_cache(1024)
def fib2(N):
    if N == 0:
        return (0, 1)

    (half_N, is_odd) = divmod(N, 2)
    (f_n, f_n_plus_1) = fib2(half_N)

    # required
    f_n_squared = f_n ** 2
    f_n_plus_1_squared = f_n_plus_1 ** 2
    f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
    f_2n_base = 2 * f_n * f_n_plus_1

    if is_odd:
        f_2n_plus_2 = f_2n_base + f_n_plus_1_squared
        return (f_2n_plus_1, f_2n_plus_2)
    else:
        f_2n = f_2n_base - f_n_squared
        return (f_2n, f_2n_plus_1)


def fib(N):
    return fib2(N)[0]
