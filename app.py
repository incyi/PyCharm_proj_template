from __future__ import print_function
import sys

def hello_world():
    return 'Hello (virtual) World! =)'

def version():
    print("version:")
    version_text = "Running app with Python :", sys.version + " and api_version", sys.api_version
    print("") #Print an empty line at the end of this function.
    return version_text

def friends_list():
    print("friends_list:")
    friends = ["Muhammad", "Ali", "Ebu Bekir", "Omar"]
    friends.append("Hassan")
    friends.append("Huseyin")
    friends.sort()
    print(friends)
    print("")  # Print an empty line at the end of this function.

def lucky_numbers_list():
    print("lucky_numbers_list:")
    lucky_numbers = [4, 8, 15, 16, 23, 42]
    print(lucky_numbers)
    print(lucky_numbers.reverse())
    print("") #Print an empty line at the end of this function.

def coordinates_tuples():
    print("coordinates_tuples:")
    coordinates = (2, 3, 4, 56, 674, 53, 7, 456, 9876)
    print(coordinates)
    print(coordinates[0])
    print(coordinates[6])
    print("") #Print an empty line at the end of this function.

def main():
    print(hello_world())
    print(version())
    friends_list()
    lucky_numbers_list()
    coordinates_tuples()
    return 0

if __name__ == '__main__':
    sys.exit(main())
