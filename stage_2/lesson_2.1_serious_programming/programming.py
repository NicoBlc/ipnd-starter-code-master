# Lesson 2.1: Introduction to Serious Programming

# Programming is grounded in arithmetic, so it's important
# to know how programming languages do simple math.
# Thankfully, Python follows the same math rules people do.
# See if you can predict the output of this code.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4180729266/concepts/49786550990923

print 3
print 1 + 1
# Adding my own code to follow along with the course.
print 52 * 3 + 12 * 9
print (52 * 3) + (12 * 9)
print 52 * (3 + 12) * 9
print 365 * 24 * 60 * 60

# Add your own code and notes here

# Write a Python program that prints out the number of minutes in seven weeks.
# Remember: 7 weeks 7 days in a week, 24 hours in a day, and 60 mins in an hour.
# Multiplying these numbers together will give you the result
print 7 * 7 * 24 * 60

# Learned about Backus - Naur Form and how syntax is validated by a computer.
# Backus was the lead programmer for IBM Foretran https://nl.wikipedia.org/wiki/John_Backus
# Analogy with english grammar is used to explain it in simple terms.
# Sentence grammar rules -> subject verb object
# Computer grammar rules (syntax rules) -> program specific rules.
# Key concepts are: <non-terminal> -> replacement -> <terminal>.
# Python arithmetic expression rules (syntax rules):
# expression -> expression (1) operator (+) expression (1).
# expression -> number
# operator -> +, *, -...etc.
# number -> 0,1...etc.
# 1 + * 1 would be invalid syntax because: expression operator operator expression is not valid.

# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the values
# defined below.
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second
print 299792458 * (100) * (1.0/1000000000)


###### Work session 1 ######

# What do you think the programmer who wrote the following code WANTED it to do?
# Do you think this code will work? Why or why not?
# My awnser: No. IndentationError: unexpected indent (print 7 was indented)

print 1
print 2
print 3
print 4
print 5
print 6
 #print 7
print 8
print 9

# Once you have a guess, press the "Test Run" button below.
# Tip: Read the LAST line of the error message first.



# What do you think the programmer who wrote the following code WANTED it to do?
# Do you think this code will work? Why or why not?
# My awnser: Yes. Space is ignored in Python.

print 1
print  2
print   3
print     4
print        5
print              6
print                       7
print                                     8
print                                                          9

# Once you have a guess, press the "Test Run" button below.


# What do you think the programmer who wrote the following code WANTED it to do?
# Do you think this code will work? Why or why not?
# My awnser: Yes. It did not work. SyntaxError: invalid syntax. Strange capital P not allowed.

print 1
print 2
print 3
print 4
print 5
#Print 6
print 7
print 8
print 9

# Once you have a guess, press the "Test Run" button below.
# Tip: Read the LAST line of the error message first.
