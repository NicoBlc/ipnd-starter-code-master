# Work Session 2.4: Preperation Mat Lib game

################################################################################
# First code worksession 4
################################################################################

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if day == "Saturday":
        return True
    if day == "Sunday":
        return True
    else:
        return False

print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

print weekend('Sunday')
#>>> True


################################################################################
# Second code worksession 4
################################################################################

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

# First try. This was not the asignment.
# Use while loop instead and print Blastoff!
# def countdown(n):
#     sec_to_launch = ""
#     if n == 3:
#         print 3
#         print 2
#         print 1
#         print "Blastoff!"

def countdown(n):
    while n > 0:
        print n
        n = n-1
    print "Blastoff!"

countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

################################################################################
# Third code worksession 4
################################################################################

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

#print bigger(2,5)                  #Checked: this returns biggest number

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

#print biggest(2,5,7)               #Checked: this returns biggest number

def median(a,b,c):
    big3 = biggest(a,b,c)            #Store biggest number in a variable big3
    if big3 == a:                    #Compare remaining numbers to biggest of 3 numbers
        return bigger(b,c)
    if big3 == b:
        return bigger(a,c)
    else:
        return bigger(a,b)


print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7


################################################################################
# Fourth code worksession 4
################################################################################

# Write code for the function random_noun, which takes in no inputs but outputs
# one of two nouns randomly. Use the randint function to generate a number
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different nouns, but for submission purposes return
# the string "sofa" if the number is 0, else return "llama".

# from random import randint
#
# def random_noun():
#     # your code here
#     num = randint(0,1)
#     if num == 0:
#         return "sofa"
#     else:
#         return "llama"
#
# print random_noun()


################################################################################
# Fifth code worksession 4
################################################################################

# Write code for the function random_verb, which takes in no inputs but outputs
# one of two verbs randomly. Use the randint function to generate a number from 0-1
# and return a verb depending on whether the number is equal 0 or 1. Feel free to
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

# from random import randint
#
# def random_verb():
#     # your code here
#     num = randint(0,1)
#     if num == 0:
#         return "run"
#     else:
#         return "kayak"
#
# print random_verb()


################################################################################
# Sixth code worksession 4
################################################################################

# Write code for the function word_transformer, which takes in a string word as input.
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB",
# return a random verb, else return the first character of word.

# from random import randint
#
# def random_verb():
#     random_num = randint(0, 1)
#     if random_num == 0:
#         return "run"
#     else:
#         return "kayak"
#
# def random_noun():
#     random_num = randint(0,1)
#     if random_num == 0:
#         return "sofa"
#     else:
#         return "llama"
#
# def word_transformer(word):
#     # your code here
#     if word == "NOUN":
#         return random_noun()
#     if word == "VERB":
#         return random_verb()
#     else:
#         return word[0]

################################################################################
# Seventh code worksession 4
################################################################################

# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]

def process_madlib(mad_lib):
    processed = ""
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    # Own basic psudo code:
    # 1) Check 4 characters at a time if string == "NOUN" or "VERB"
    # 2) If True: call function word_transformer(). If False: move over 1 character to left.
    # 3) Continue till entire string is processed.
    # This will work, still sloppy work in progress though.
    output1_string_1 = mad_lib.replace("NOUN", random_noun())
    output2_string_1 = output1_string_1.replace("VERB", random_verb())
    return output2_string_1

test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)

# This will work, still sloppy work in progress though.
# Trying string replace method: str.replace(old, new[, max])
# output1_string_1 = test_string_1.replace("NOUN", random_noun())
# output2_string_1 = output1_string_1.replace("VERB", random_verb())
# print output2_string_1


### NOTE Provided solution ###

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]

# provided solution
def process_madlib(mad_lib):
    processed = ""
    index = 0
    box_lenght = 4
    while index < len(mad_lib):
        frame = mad_lib [index:index + box_lenght]
        to_add = word_transformer(frame)
        processed += to_add
        if len(to_add) == 1:
            index += 1                              #+= is shorthand for incrementing a variable.
        else:
            index += 4
    return processed





test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
