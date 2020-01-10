"""
Related to:  https://stackoverflow.com/questions/31350857/find-pair-of-string-without-duplicate-letter-that-has-max-length-product

Problem statement:
    Given a list of words, find two strings S & T such that:

    a. S & T have no common character
    b. S.length() * T.length() is maximized
"""

import itertools
import cProfile


NUMBERS = range(500 + 1)
# NUMBERS = [20, 18, 17, 15, 14, 11, 10, 9]


def path_of_max_product(numbers):
    pairs = itertools.combinations_with_replacement(numbers, 2)
    sorted_pairs = sorted(pairs, key=lambda p: p[0] * p[1], reverse=True)
    return sorted_pairs


def main():
    global NUMBERS
    for p in path_of_max_product(NUMBERS):
        print(tuple(sorted(p, reverse=True)), p[0] * p[1])


if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    pr.print_stats()
