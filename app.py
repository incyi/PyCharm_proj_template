from __future__ import print_function
import sys

def hello_world():
    print("Hello (virtual) World! =)")

def version():
    print("Running app with Python :", sys.version + " and api_version", sys.api_version)

def main():
    hello_world()
    version()
    return 0

if __name__ == '__main__':
    sys.exit(main())
