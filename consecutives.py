
def is_consecutive_at_rank(s, rank=1):
    print(s)
    (n, s) = (int(s[:rank]), s[rank:])
    print(n, s)

    while s:
        n += 1
        l = len(str(n))
        (nn, s) = (int(s[:l]), s[l:])
        if (n != nn):
            print(f"Expected {n} but got {nn}!")
            return False
        print(n, s)

    return True


def is_consecutive(s):
    for i in range(1, len(s) // 2 + 1):
        if is_consecutive_at_rank(s, rank=i):
            print(f"'{s}' is consecutive at rank {i}!")
            return True
        else:
            print(f"'{s}' is not consecutive at rank {i}.\n")
    return False


# print(is_consecutive_at_rank("91011", rank=1))

print(is_consecutive("420422420423"))
