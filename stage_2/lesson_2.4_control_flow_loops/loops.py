# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4196788670/concepts/50222508420923

def count():
    i = 0
    while i < 10:
        print i
        i = i + 1

count()

################################################################################
# Add your own code and notes here
################################################################################


################################################################################
# First code lesson in 2.4
################################################################################

# This code demonstrates a while loop with a "counting variable"
i = 0
while i < 10:
    print i
    i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")

################################################################################
# Second code lesson in 2.4
################################################################################
# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(n):
    count = 1
    while count != n+1:
        print count
        count = count +1



print_numbers(3)
#>>> 1
#>>> 2
#>>> 3
