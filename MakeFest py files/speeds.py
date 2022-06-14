import sys
from time import sleep

def fast_text(words):
    for char in words:
        sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()


def wait_text(words):
    for char in words:
        sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()
