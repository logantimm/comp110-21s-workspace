"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730325536"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

fortune: int = int(randint(1, 100))

if fortune <= 50:
    if fortune <= 25:
            print("Brighter days are ahead.")
    else:
            print("You got this!")
else:
    if fortune <= 75:
            print("Good things are coming your way.")
    else:
            print("Soon your life will become richer.")

print("Now, go spread positive vibes!")