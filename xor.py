
import math
import os
import random
import struct
import time


DIFFICULTY = 22
BASE = 8  # bits per unit of work


def to64(bytez):
    assert not len(bytez) % 8
    total = len(bytez) // 8
    return struct.unpack("L" * total, bytez)


def from64(ints):
    return struct.pack("L" * len(ints), *ints)


def toN(bytez, exp=128):
    assert exp >= 128
    assert not exp % 64
    grouping = exp // 64
    packed = to64(bytez)
    for i in range(math.ceil(len(packed) / grouping)):
        pack = packed[i * grouping:(i + 1) * grouping]
        yield sum(e << (i * 64) for (i, e) in enumerate(pack))


def downconvert(num, exp, mod, grouping):
    for i in range(grouping):
        # (num, out) = divmod(num, mod)
        # yield out
        yield num % mod
        num >>= exp


def fromN(ints, exp=128):
    assert exp >= 128
    assert not exp % 64
    grouping = exp // 64
    mod = 2**64
    for num in ints:
        yield from from64(list(downconvert(num, 64, mod, grouping)))


def calculate_challenge(exp):
    scale = exp // BASE  # 8 bits = scale of 0, 32 bits = scale of 3
    challenge = int(2**DIFFICULTY / scale)
    return challenge


def generate(exp, total):
    if exp == 8:
        return os.urandom(total)
    return [random.randint(0, 2**exp) for _ in range(total)]


def test(l1, l2):
    t0 = time.time()
    lo = [a ^ b for (a, b) in zip(l1, l2)]  # noqa
    t1 = time.time()
    return t1 - t0


def fair_test(l1, l2, exp):
    lt = [a ^ b for (a, b) in zip(l1, l2)]

    t0 = time.time()

    l1 = list(toN(l1, exp=exp))
    # l1 = toN(l1, exp=exp)
    t1 = time.time()

    l2 = list(toN(l2, exp=exp))
    # l2 = toN(l2, exp=exp)
    t2 = time.time()

    lo = [a ^ b for (a, b) in zip(l1, l2)]  # noqa
    # lo = (a ^ b for (a, b) in zip(l1, l2))  # noqa
    t3 = time.time()

    lo = list(fromN(lo, exp=exp))
    t4 = time.time()

    assert lt == lo

    return (t4 - t0, (t1 - t0, t2 - t1, t3 - t2, t4 - t3))


def run_test(exp):
    print(f"Testing: 2^{exp}")
    total = calculate_challenge(exp)
    print(f"Generating lists of {total:,} random numbers in [0, 2^{exp}):")
    print("    Generating adjusted list 1...")
    l1 = generate(exp, total)
    print("    Generating adjusted list 2...")
    l2 = generate(exp, total)
    # print(f"    (Sample: {str(l1[:10])[:-1]}, ...])")
    print(f"Running {total:,} rounds of XOR...")
    dt = test(l1, l2)
    print(f"Time: {dt:.2f} sec\n")


def run_fair_test(exp):
    print(f"Fairly testing: 2^{exp}")
    total = calculate_challenge(8)
    print(f"Generating lists of {total:,} random bytes in [0, 255]:")
    print("    Generating list 1...")
    l1 = os.urandom(total)
    print("    Generating list 2...")
    l2 = os.urandom(total)
    # print(f"    (Sample: {str(l1[:10])[:-1]}, ...])")
    print(f"Running {total:,} rounds of XOR, while up/down converting...")
    (dt, stats) = fair_test(l1, l2, exp)
    stats = ", ".join(f"{s:.2f}" for s in stats)
    print(f"Time: {dt:.2f} sec")
    print(f"    (Other stats: {stats})\n")


# run_test(2048)
# run_test(1024)
# run_test(512)
# run_test(256)
# run_test(128)
# run_test(64)
# run_test(32)
# run_test(16)
run_test(8)

# run_fair_test(2048)
# run_fair_test(1024)
# run_fair_test(512)
# run_fair_test(256)
# run_fair_test(128)
