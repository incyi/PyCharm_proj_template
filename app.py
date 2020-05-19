from __future__ import print_function
import sys


def hello_world(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'Hello (virtual) World! =)'


def main():
    hello_world(say_what())
    return 0


if __name__ == '__main__':
    sys.exit(main())
