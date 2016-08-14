# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4196788670/concepts/49828218950923

print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

################################################################################
# Add your own code and notes here
################################################################################


################################################################################
# First code lesson in 2.4
################################################################################

print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19


print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # what do you think will happen here?
print 7 != 10
print 7 != 7


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20:
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"

################################################################################
# Second code lesson in 2.4
################################################################################

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

# Generic structure
# def some_function(a,b):
#     if <TestExpression>:
#         <Block>
#     else:
#         <Block>

# Simple version
# def bigger(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# Better version with r stored as return variable.
def bigger(a,b):
    if a > b:
        r = a
    else:
        r = b
    return r


print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3

################################################################################
# Third code lesson in 2.4
################################################################################

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

# Simple solution. You do not always need if and else statements.
# def is_friend(a):
#     return a[0] == "D":


def is_friend(a):
    if a[0] == "D":
        r = True
    else:
        r = False
    return r



print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False


################################################################################
# Fourth code lesson in 2.4
################################################################################


# Define a procedure, is_friend2, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

# Provided alternative solution with or
def is_friend2(a):
    return a[0] == "D" or a[0] == "N"


# My solution
def is_friend3(a):
    if a[0] == "D":
        r = True
    elif a[0] == "N":
        r = True
    else:
        r = False
    return r


print is_friend2('Diane')
#>>> True

print is_friend2('Ned')
#>>> True

print is_friend2('Moe')
#>>> False


print is_friend3('Diane')
#>>> True

print is_friend3('Ned')
#>>> True

print is_friend3('Moe')
#>>> False

################################################################################
# Fifth code lesson in 2.4
################################################################################
# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

# Found this solution online at stackoverflow. Simple and elegant.
# http://stackoverflow.com/questions/3090175/python-find-the-greatest-number-in-a-set-of-numbers
# def biggest(a,b,c):
#     return max(a,b,c)

# Procedural thinking solution. Re-using another function or procedure you've already written (bigger).
# def bigger(a,b):
#     if a > b:
#         r = a
#     else:
#         r = b
#     return r

# def biggest(a,b,c):
#     return bigger(bigger(a,b),c)

# Provided solution with a true or false decision making flowchart
# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-3635959067/m-3667168575
def biggest(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9


# Recap procedural thinking
# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/m-3676598573
# The previous video had a lot of good content about procedural thinking. In his second approach to finding the "biggest" number, Dave used the function called bigger which he had written earlier.
# This is an example of one of the things that makes programming so amazing. Once you (or anyone else) has coded something once, you can use that thing again later as a tool!
