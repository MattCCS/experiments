
import random
import time

t0 = time.time()
VALUES = [random.randint(0, 1) for _ in range(3000000)]
t1 = time.time()
print(t1 - t0)


class S():
    __slots__ = ["x"]

    def __init__(self, x):
        self.x = x


class D():
    def __init__(self, x):
        self.x = x


t0 = time.time()
slist = list(map(S, VALUES))
stotal = sum(s.x for s in slist)
print(stotal)
t1 = time.time()
print(t1 - t0)

t0 = time.time()
dlist = list(map(D, VALUES))
dtotal = sum(d.x for d in dlist)
print(dtotal)
t1 = time.time()
print(t1 - t0)
