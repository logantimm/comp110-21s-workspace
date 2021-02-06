"""An exercise in remainders and boolean logic."""

__author__ = "730325536"


# Begin your solution here...

number = int(input("Enter an int: "))

if number % 2 == 0 or number % 7 == 0:
    if number % 2 != 0:
        print("HEELS")
    if number % 7 != 0:
        print("TAR")
    if number % 2 == 0 and number % 7 == 0:
        print("TAR HEELS")
else:
    print("CAROLINA")