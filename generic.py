"""
"""

import argparse


DESCRIPTION = ""


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print(args)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Cancelled.")
