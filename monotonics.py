
def find_larger_term_index(s, n):
    l = len(str(n))
    for i in range(l, len(s) + 1):
        sl = s[:i]
        print(f"Testing {n} vs {sl}...")
        nn = int(sl)
        if nn > n:
            return i
    return None


def is_monotonic_at_rank(s, rank=1):
    print(s)
    (n, s) = (int(s[:rank]), s[rank:])
    print(n, s)

    while s:
        l = find_larger_term_index(s, n)
        if not l:
            print(f"Expected >{n} but got {s}!")
            return False
        (n, s) = (int(s[:l]), s[l:])
        print(n, s)

    return True


def is_monotonic(s):
    for i in range(1, len(s)):
        if is_monotonic_at_rank(s, rank=i):
            print(f"'{s}' is monotonic at rank {i}!")
            return True
        else:
            print(f"'{s}' is not monotonic at rank {i}.\n")
    return False


# print(is_monotonic_at_rank("247958276574640", rank=1))

print(is_monotonic_at_rank("54106519", rank=1))
print(is_monotonic("4321"))
