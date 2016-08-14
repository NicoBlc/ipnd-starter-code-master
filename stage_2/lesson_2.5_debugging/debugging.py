# Lesson 2.5: debugging

################################################################################
# Add your own code and notes here
################################################################################


################################################################################
# First code lesson in 2.5
################################################################################

# A small change will fix the crashing bug in printInches.
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Comment out what you think does't work. Run code to verify where the problem is.
# Fix the part with the bug. In this case def printInches has the problem.

# Found this online:
# http://stackoverflow.com/questions/2376464/typeerror-unsupported-operand-types-for-str-and-int
# For future reference Python is strongly typed. Unlike other dynamic languages,
# it will not automagically cast objects from one type or the other (say from str to int)
# so you must do this yourself. You'll like that in the long-run, trust me!

def printExample(a, b):
    print a + b

def printInches(n):                    # Comment out what you think does't work.
    #print n + " inches"               # Comment out what you think does't work.
    print str(n) + " inches"           # Convert n to string.

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)                        # Comment out what you think does't work.


################################################################################
# Second code lesson in 2.5
################################################################################

# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

def bracket(text):
    return '[' + text + ']'

def boldwrap(text): # Missed the : after def boldwrap(text)
    return '<b>' + text + '</b>'

print boldwrap('This is an important message.')


################################################################################
# Third code lesson in 2.5
################################################################################

# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

# # Figure out what it does myself with comments.
# # First 3 strings work. Last 2 not.
# def remove(somestring, sub):                        # Function taking in 2 parameters. Looks fine.
#     """Return somestring with sub removed."""       # Weird """ notation. No clue what it does.
#     location = somestring.find(sub)                 # Find parameter sub in somestring parameter. Store in variable.
#     print location                                 # Try printing location to look at output. NOTE problem is location returns -1 if not found.
#     length = len(sub)                               # Store length parameter sub in variable.
#     #print length                                    # Try printing length to look at output.
#     part_before = somestring[:location]             # Store part_before in variable.
#     #print part_before                               # Try printing part_before to look at output.
#     part_after = somestring[location + length:]     # Store part_after in variable.
#     #print part_after                                # Try printing part_after to look at output.
#     #return part_before + part_after                 # Concatinate 2 string variables together.

# Solution try if statement to ignore -1 return fron location variable when not found.
def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location == -1:
        return somestring
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after


#
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"


################################################################################
# Guidelines while writing code. Add usefull comments for debugging later.
################################################################################

#1) Don't comment "obvious code"
#print "Hello" # prints hello
#Simply writing print "Hello" is enough


# 2) Start functions with a comment
# All functions should start with a comment describing the expected input(s) and output(s),
# and explaining what the function does.
# This helps others determine what the intended purpose of your function is. Here's an example:

# def isLeapYear(year):
#     # takes a number as input and outputs True if the number
#     # represents a leap year and False otherwise

# 3) Python has no offical multi-line comments.
#     """Three quotes can be used as multiline comments. Although not recommended!"""
