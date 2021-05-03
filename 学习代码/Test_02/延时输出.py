import sys
from time import sleep


def slow(msg, text):
    print(msg)
    for i in text:
        print(i)
        sys.stdout.flush()
        sleep(0.8)
    return '.'


slow('loginning', '...')
