"""
Example of nice logging.
"""

import functools
import logging
import sys
import traceback


FORMATTER = logging.Formatter(fmt='[{asctime}] {levelname:<8} | {filename}:{lineno}:{funcName}() | {message}', style="{")
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(FORMATTER)
LOGGER = logging.getLogger()
LOGGER.addHandler(CONSOLE_HANDLER)
LOGGER.setLevel(0)


def color(n):
    return f"{ESC}[{n}m"


ESC = "\033"
BOLD = f"{ESC}[1m"
RESET = f"{ESC}[0m"

BLACK = color(30)
RED = color(31)
WHITEONRED = f"{ESC}[37;41m"
GREEN = color(32)
YELLOW = color(33)
BLUE = color(34)
MAGENTA = color(35)
CYAN = color(36)
WHITE = color(37)


def colorize(logmsg, ansi):
    pre = ''.join(ansi)
    if sys.stderr.isatty():
        return f'{pre}{logmsg}{RESET}'
    return logmsg


i = functools.partial(colorize, ansi=[GREEN])
w = functools.partial(colorize, ansi=[BOLD, YELLOW])
e = functools.partial(colorize, ansi=[BOLD, RED])
c = functools.partial(colorize, ansi=[BOLD, WHITEONRED])


def fib(n):
    LOGGER.debug(f"got n = {n}")
    if not n:
        raise RuntimeError("oops")
        return 1
    return n * fib(n - 1)


def test2():
    LOGGER.debug("boring")
    LOGGER.info(i(f"interesting!"))
    LOGGER.warn(w(f"this might be bad..."))
    LOGGER.info(i(f"fib(5) = {fib(5)}"))


def main():
    LOGGER.error(e(f"something bad"))
    test2()


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        LOGGER.critical(c(f"Got an uncaught error:\n{traceback.format_exc()}"))
