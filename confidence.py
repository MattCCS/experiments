
import math


LEVELS = [
    "Absolutely Not",
    "No",
    "Probably Not",
    "Maybe Not",
    "Maybe",
    "Maybe So",
    "Probably",
    "Yes",
    "Absolutely",
]

assert len(LEVELS) % 2  # ensure there's a "middle" value

# TODO: allow even number of terms
# TODO: scale if != +/- 4 terms


def confidence(average: float, samples: int) -> str:
    assert 0.0 <= average <= 1.0
    assert 0 <= samples

    cap = len(LEVELS) // 2  # for 9 levels, 4 is the cap

    if samples <= 1:
        return (cap, LEVELS[cap])

    average_spread = average * 2 - 1
    samples_log = math.log(samples)

    numerators = list(range(-cap, 0)) + list(range(1, cap + 1))
    confidence_thresholds = []
    for numerator in numerators:
        # try:
        confidence_threshold = numerator / samples_log
        # except ZeroDivisionError:
        #     confidence_threshold = float()
        confidence_thresholds.append(confidence_threshold)

    # print(confidence_thresholds)
    # print(average_spread)

    index = 0
    for confidence_threshold in confidence_thresholds:
        if average_spread > confidence_threshold:
            index += 1
        else:
            break

    # print(index, LEVELS[index])
    return (index, LEVELS[index])


print(confidence(0.2, 50))
print(confidence(0.2, 500))
print(confidence(0.2, 5000))


def test():
    SAMPLES = 50
    CONF = 100
    a_set = set()
    s_set = set()
    L = [['' for x in range(CONF)] for y in range(SAMPLES)]
    xf = lambda x: x / CONF
    yf = lambda y: math.floor(y ** 1.2)
    # yf = lambda y: (10 ** ((y - 1) // 9)) * ((y - 1) % 9 + 1) if y else 0
    # yf = lambda y: 2 ** y // 1.5
    import time
    t0 = time.time()
    for x in range(CONF):
        for y in range(SAMPLES):
            a = xf(x)
            s = yf(y)
            a_set.add(a)
            s_set.add(s)
            v = confidence(a, s)
            L[y][x] = dict(zip(range(9), "<=\\. ,/->"))[v[0]]
    t1 = time.time()

    for (y, row) in reversed(list(enumerate(L))):
        print(' '.join(map(str, row)), yf(y))
    print(''.join(str(xf(x) * 2 - 1).lstrip('-')[1:3] for x in range(CONF)))
    print(t1 - t0, SAMPLES * CONF)

    LOOPS = 100000
    t0 = time.time()
    for _ in range(LOOPS):
        confidence(0.75, 5000)
    t1 = time.time()
    print(t1 - t0, LOOPS)


test()
