# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4152219158/concepts/50376191640923

p = ['y', 'a', 'b', 'b', 'a', '!']
print p
print p[0]
print p[2:4]

################################################################################
# Add your own code and notes here
################################################################################


################################################################################
# First code lesson in 2.6
################################################################################

# Here's a chance to play around with lists for a bit before you continue
# Take a look at what the following code does and try to guess how it works.

print "EXAMPLE 1: Lists can contain strings"
string_list = ['HTML', 'CSS', 'Python']
print string_list

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi

print "EXAMPLE 4: Lists can contain strings AND numbers"
mixed_list = ['Hello!', 42, "Goodbye!"]
print mixed_list

print "Example 5: Lists can even contain other lists"
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print list_with_lists


################################################################################
# Second code lesson in 2.6
################################################################################

# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    #substract 1 because index start at 0 and month Jan at 1
    return days_in_month[month_number - 1]  #calls upon input variable month_number - 1


print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

################################################################################
# Third code lesson in 2.6
################################################################################

# Every entry in the following list is itself a list
nested_list = [['HTML', 'Hypertext Markup Language forms the structure of webpages'],
               ['CSS' , 'Cascading Style Sheets give pages style'],
               ['Python', 'Python is a programming language'],
               ['Lists', 'Lists are a data structure that let you organize information']]

first_concept = nested_list[0]

print "What do you think this will print?"
print first_concept

print "Since first_concept was itself a list, we can access its elements"
first_title = first_concept[0]
first_description = first_concept[1]


print "What will this print?"
print first_title
print first_description

################################################################################
# Fourth code lesson in 2.6
################################################################################

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list
print countries[1][1]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.

#population_china = countries[0][2]
#population_romania = countries[2][2]
print countries[0][2] / countries[2][2]

################################################################################
# Fifth code lesson in 2.6
################################################################################

# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'
print stooges

################################################################################
# Sixth code lesson in 2.6
################################################################################

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]

def replace_spy(list_three_numbers): #passing in a list of 3 numbers.
    list_three_numbers[2] = list_three_numbers[2]+1 #mutating 3rd number in list [2]


# In the test below, the first line calls your
# procedure which will change spy, and the
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print spy
#>>> [0,0,8]

################################################################################
# Sixth code lesson in 2.6
################################################################################

# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print thing


print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country

################################################################################
# Seventh code lesson in 2.6
################################################################################

# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

# # My working solution.
# def sum_list(list_of_numbers):
#     for elements in list_of_numbers:
#         element1 = list_of_numbers[0]
#         element2 = list_of_numbers[1]
#         element3 = list_of_numbers[2]
#         return element1 + element2 + element3

# Provided working solution in lecture.
def sum_list(p):
    result = 0
    for e in p:
        result = result + e
    return result



print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134

################################################################################
# Eight code lesson in 2.6
################################################################################

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase
# letter 'U'.

def measure_udacity(U):
    count = 0
    for e in U:
        if e[0] == "U":
            count = count + 1
    return count





print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2


################################################################################
# Ninth code lesson in 2.6
################################################################################

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# Looking if target exists in some list
# With a while loop
def find_element_while(some_list,target):
    i = 0
    while i < len(some_list):
        if some_list[i] == target:
            return i
        i = i + 1
    return -1

# Looking if target exists in some list
# With a for loop
def find_element_for(some_list,target):
    i = 0
    for element in some_list:
        if element == target:
            return i
        i = i + 1
    return -1

# Looking if target exists in some list
# With a standard list index method
def find_element_index(some_list,target):
    if target in some_list:
        return some_list.index(target)
    else:
        return -1


print find_element_while([1,2,3],3)
#>>> 2

print find_element_while(['alpha','beta'],'gamma')
#>>> -1

print find_element_for([1,2,3],3)
#>>> 2

print find_element_for(['alpha','beta'],'gamma')
#>>> -1

print find_element_index([1,2,3],3)
#>>> 2

print find_element_index(['alpha','beta'],'gamma')
#>>> -1
