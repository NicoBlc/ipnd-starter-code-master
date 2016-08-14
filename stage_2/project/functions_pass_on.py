# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

start_game_message = '''Welcome to the very first Python program NicoBlc wrote! It is a word replacement game.
How to play: Below you can find an example. The answer for ___1___ is 'function'. Can you figure out the others?
Simply type your answer in the commandline and hit enter. You get 5 tries, make them count. Good luck!\n'''

question0 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''

question1 = '''A function is created with the def keyword. You specify the inputs a function takes by
adding ___2___ separated by commas between the parentheses. functions by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''

question2 = '''A function is created with the def keyword. You specify the inputs a function takes by
adding arguments separated by commas between the parentheses. functions by default return ___3___ if you
don't specify the value to return. Arguments can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''

question3 = '''A function is created with the def keyword. You specify the inputs a function takes by
adding arguments separated by commas between the parentheses. functions by default return none if you
don't specify the value to return. Arguments can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''

question4 = '''A function is created with the def keyword. You specify the inputs a function takes by
adding arguments separated by commas between the parentheses. functions by default return none if you
don't specify the value to return. Arguments can be standard data types such as string, number, dictionary,
tuple, and list or can be more complicated such as objects and lambda functions.\n'''

question_answers = ['function', 'arguments', 'none', 'list']

difficulty = 'easy'

question_list = []


def some_function(some_list):
    some_list.append(1)
    print "Local question_list: " + str(some_list)
    some_function2(question_list)

def some_function2(some_list):
    some_list.append(1)
    print "Local2 question_list: " + str(some_list)
    some_function3(question_list)

def some_function3(some_list):
    if len(some_list) == 2:
        some_list.append(1)
    print "Local3 question_list: " + str(some_list)

some_function(question_list)
print "Global question_list: " + str(question_list)
#Prints:
#>>>Local: [1, 2, 3, 1]
#>>>Global: [1, 2, 3, 1]
