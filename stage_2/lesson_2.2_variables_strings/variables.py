# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4192698630/concepts/48904185560923

speed_of_light = 299792458.0
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

# Add your own code and notes here


# First assignment in lecture 2.2
# Given the variables defined here, write Python
# code that prints out the distance, in meters,
# that light travels in one processor cycle.

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0 # meters per second
cycles_per_second = 2700000000.0 # 2.7 GHz processor on iMac
distance_one_processor_cycle = speed_of_light / cycles_per_second # Solution ~0.1 meters
print distance_one_processor_cycle

# cycles_per_second is 2.8 GHz
# Changing a value of a variable will change the output.
cycles_per_second = 2800000000.0 # 2.8 GHz processor on iMac
distance_one_processor_cycle = speed_of_light / cycles_per_second # Solution ~0.1 meters
print distance_one_processor_cycle


# Write python code that defines the variable
# age to be your age in years, and then prints
# out the number of days you have been alive.
age = 33
days = age * 365
print days
