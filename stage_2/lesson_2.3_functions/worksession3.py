# Work Session 2.3: Functions, Methods and Procedures.

################################################################################
# First code worksession 2.3
################################################################################

# Define a procedure, udacify, that takes as
# input a string, and returns a string that
# is an uppercase 'U' followed by the input string.
# for example, when you enter

# print udacify('dacians')

# the output should be the string 'Udacians'


def udacify(a):
    s = "U" + a
    return s




# Remove the hash, #, from infront of print to test your code.

print udacify('dacians')
#>>> Udacians

print udacify('turn')
#>>> Uturn

print udacify('boat')
#>>> Uboat
