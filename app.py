from __future__ import print_function
import sys


def hello_world():
    return 'Hello (virtual) World! =)'


def version():
    version_text = "Running app with Python :", sys.version + " and api_version", sys.api_version
    return version_text


def main():
    print(hello_world())
    print(version())
    return 0


if __name__ == '__main__':
    sys.exit(main())
