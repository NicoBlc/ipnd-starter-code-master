# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4141089439/concepts/50282994840923

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

################################################################################
# Add your own code and notes here
################################################################################
# Procedures, Functions, Methods etc. are synonyms.
# What they basically do is process INPUT (def) to OUTPUT (return).
# Functions take input, do something with it, and then produce output.
# IPUTS are also called operands or arguments.

################################################################################
# First code lesson in 2.3
################################################################################
# Read through the code below. Even if you don't understand it, try to make
# a guess about what it does. What do you think will happen when you press
# "Test Run"? Once you have a prediction, press "Test Run" and compare what
# happens to what you predicted.

def say_hello():
    return "Hello!"

print say_hello()

# say_hello is a function. Or, as Dave would call it, a procedure.
# This procedure isn't particularly interesting because it only does
# one thing.

# Continue to the next example to see a more interesting version of say_hello.


################################################################################
# Second code lesson in 2.3
################################################################################
# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time.
#
# Read through the code and try to predict what the output will be when
# you press "Test Run"

def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting

print say_hello("Miriam")
print say_hello("Andy")


################################################################################
# Third code lesson in 2.3
################################################################################
def say_hello(name):
    greeting = "Hello " + name + '!'
    return greeting
# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
def add_two_numbers(number_1, number_2):
    return number_1 + number_2

print add_two_numbers(4, 3)
print add_two_numbers(2, 6)
print add_two_numbers(0, 9)
# Also works with concatinating strings
print add_two_numbers("Wor", "ks")
# Does not work with concatinating strings and numbers
#TypeError: cannot concatenate 'str' and 'int' objects
#print add_two_numbers("Wor", 7)

# Once you've pressed Test Run, remove the comment characters from the
# code below and then make ONE modification so that the function does
# what the name says it should do.

def subtract_two_numbers(number_1, number_2):
   return number_1 - number_2

print subtract_two_numbers(4, 3)

################################################################################
# Fourth code lesson in 2.3
################################################################################
# You have to return a + b instead of trying to create a variable inside a function
# This code will return a none value
def sum (a,b):
    a= a + b

print sum(4, 3)

# You have to return a + b instead of trying to create a variable inside a function
# This code will return the sum of two inputs (also called arguments)
def sum (a,b):
    a= a + b
    return a

print sum(4, 3)

# This behaviour is caused by the difference in local and global variables
# NOTE try to avoid global variables!!! They will cause issues. Use sparingly.
# There is a difference with mutable and imutable objects, see lecture on Google hangout below.
# https://plus.google.com/events/cpi62usjgpmfb0vn8veq4hok8h4?authkey=CMGn4vyVkrqGwwE
a = 6
def some_function():
    a = 5
    print "Function has local value: " + str(a)

some_function()
print "Assined variable has global value: " + str(a)


################################################################################
# Fifth code lesson in 2.3
################################################################################

# Define a procedure, square, that takes one number
# as its input, and returns the square of that
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    c = a + b
    return c

def square(n):
    s = n**2
    return s


# To test your procedure, uncomment the print
# statement below, by removing the hash mark (#)
# at the beginning of the line.

# Do not remove the # from in front of the line
# with the arrows (>>>). Lines which begin like
# this (#>>>) are included to show the results
# you should see when run your procedure.

print sum(5,5)
print square(5)
#>>> 25


################################################################################
# Sixth code lesson in 2.3
################################################################################

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    return a + b

def sum3(a,b,c):
    return a + b + c





print sum3(1,2,3)
#>>> 6

print sum3(93,53,70)
#>>> 216

################################################################################
# Seventh code lesson in 2.3
################################################################################

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

def abbaize(a,b):
    s = a + b + b + a
    return s







print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'
