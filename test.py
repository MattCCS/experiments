"""
Testing the speed of BINARY if-else statements vs BINARY dict
lookups with different data types/lengths/conditions.
"""

import time
import random


KEY_0 = "0"
KEY_1 = "1"
LOOPS = 10_000_000
KEYS = (random.choice([KEY_0, KEY_1]) for _ in range(LOOPS))

d = {
    KEY_0: 0,
    KEY_1: 1,
}

_ = None
k = None
t0 = None
t1 = None

print("Generating keys...")
KEYS = list(KEYS)

print("Test 1...")
t0 = time.time()
for k in KEYS:
    _ = d[k]
t1 = time.time()
print(f"{LOOPS:,} loops with 2-dict: {t1 - t0}")


print("Test 2...")
t0 = time.time()
for k in KEYS:
    if k == KEY_0:
        _ = 0
    else:
        _ = 1
t1 = time.time()
print(f"{LOOPS:,} loops with 2-branch: {t1 - t0}")
