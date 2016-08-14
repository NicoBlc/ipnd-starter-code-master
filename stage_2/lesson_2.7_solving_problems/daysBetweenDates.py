# Lesson 2.7: How to Solve Problems - Days Between Dates

# In this lesson, you'll be working on solving a much
# bigger problem than those you've seen so far. If you
# want, you can use this starter code to write your
# quiz responses and then copy and paste into the
# Udacity quiz nodes.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4184188665/concepts/49934588850923

# Simple Mechanical Algorithm
# days = 0
# while date1 is before date2:
#     date1 = advance to next day
#     days += 1

# Fill in the functions below to solve the problem.

# def isLeapYear(year):
#     return True
#
# def daysInMonth(year, month):
#     return 30
#
# def nextDay(year, month, day):
#     if day < daysInMonth(year, month):
#         return year, month, day + 1
#
# def dateIsBefore(year1, month1, day1, year2, month2, day2):
#     if year1 < year2:
#         return True
#
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     days = 0
#     while dateIsBefore(year1, month1, day1, year2, month2, day2):
#         days += 1
#     return days
#
# # Below is a testing script that will check if your code is doing
# # what it is supposed to. Don't change it! The test will run
# # when you execute the file.
# # Bonus: Can you figure out how the test works?
#
# def test():
#     test_cases = [((2012,1,1,2012,2,28), 58),
#                   ((2012,1,1,2012,3,1), 60),
#                   ((2011,6,30,2012,6,30), 366),
#                   ((2011,1,1,2012,8,8), 585 ),
#                   ((1900,1,1,1999,12,31), 36523)]
#
#     for (args, answer) in test_cases:
#         result = daysBetweenDates(*args)
#         if result != answer:
#             print "Test with data:", args, "failed"
#             print result
#         else:
#             print "Test case passed!"
#
# test()


################################################################################
# Add your own code and notes here
################################################################################
# https://www.udacity.com/course/viewer#!/c-nd000/l-4184188665/m-108325402
# https://www.youtube.com/watch?v=uQDk8euwyDI
# Pythonista's Guide to all problems in the galaxy.
# 0 Don't panic!
# 1 What are the inputs?
# 2 What are the outputs?
# 3 Work through some examples by hand.
# 4 Find a simple mechanical solution.

################################################################################
# First code lesson in 2.6
################################################################################

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

# # Provided code in lecture with my notes on how how it works.
# def nextDay(year, month, day):
#     """
#     Returns the year, month, day of the next day.
#     Simple version: assume every month has 30 days.
#     """
#     # YOUR CODE HERE
#     if day < 30:                        #Check if day < 30.
#         return year, month, day + 1     #If True, return current year, month value and increment day +1. (1999, 12, 29) will become (1999, 12, 30)
#     else:                               #If False, check if month < 12 to continue
#         if month < 12:                  #Check if month < 12.
#             return year, month + 1, 1   #If True, return current year and increment month +1. Reset day to 1. (1999, 11, 30) will become (1999, 12, 1)
#         else:                           #If False, increment year, month and day with 1
#             return year + 1, 1, 1       #Return incremented year +1. Reset month and day with 1. (1999, 12, 30) will become (2000, 1, 1)


################################################################################
# Second code lesson in 2.6
################################################################################

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
#

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    # YOUR CODE HERE!
    # My pseudo code
    # 1 My inputs are: 2 dates. More specific: 1 tuple containing 6 variables, representing 2 dates.
    # 2 My outputs are: 1 number. More specific: 1 integer, representing the number of days between dates.
    # 3 Example pseudo code
    # days = o
    # while date1 is before date2:
        #date1 = day after date 1   <--nextDay
        #days += 1
    # return days
    return

################################################################################
# Third code lesson in 2.6
################################################################################

# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    # assert not dateIsbefore(year2, month2, day2, year1, month1, day1)
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30),
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)
test()

################################################################################
# Fourth code lesson in 2.6
################################################################################

# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
