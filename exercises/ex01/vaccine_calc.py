"""A vaccination calculator."""

__author__ = "730325536"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population = int(input("Population: "))
doses_admin = int(input("Doses administered: "))
doses_per_day = int(input("Doses per day: "))
trgt = int(input("Target percent vaccinated: "))

trgt_percent = trgt / 100

trgt_doses = population * 2 * trgt_percent
remaining_doses = trgt_doses - doses_admin
days_needed = round(remaining_doses / doses_per_day)

today: datetime = datetime.today()
days_away: timedelta = timedelta(days_needed)
date_reached = days_away + today
date_reached.strftime("%B %d, %Y")

print("We will reach " + str(trgt) + "% vaccination in " + str(days_needed)
    + " days, which falls on " + date_reached.strftime("%B %d, %Y"))