
import asyncio
import random

BOULDER_FELL = False


async def escape():
    global BOULDER_FELL
    for i in range(3, 0, -1):
        print(f"Player is {i*5} feet from the exit...")
        await asyncio.sleep(1)
    if BOULDER_FELL:
        print("dead :(")
    else:
        print("Escaped! :D")


async def boulder():
    global BOULDER_FELL
    BOULDER_FELL = False
    for i in range(random.randint(2, 4), 0, -1):
        print(f"Boulder is {i*10} feet away...")
        await asyncio.sleep(1)
    BOULDER_FELL = True
    print("*Crash!*")


def play():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(escape(), boulder()))


def main():
    play()


if __name__ == '__main__':
    main()
