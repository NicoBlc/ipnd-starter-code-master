# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/


################################################################################
# Add your own code and notes here
################################################################################
# What is the problem I am trying to solve?
# For this project, you'll be building a Fill-in-the-Blanks quiz.

################################################################################
# Standard breakdown of the problem
################################################################################
# 0 What is the problem I am trying to solve? Understand it first! Create a simple mechanical solution then optimze!
# 1 What are my inputs? Make a descriptive list of the inputs.
# 2 What are my outputs? Make a descriptive list of the outputs.
# 3 What are my available tools? Make a descriptive list of the tools.
# 4 Subdivide problem into more easily solvable pieces (if necessary). Make a descriptive list of all the pieces of the problem.
# 5 Solve each piece (prioritize subdivided pieces).
# 6 Reassemble the solved pieces.
# 7 Verify that the results match expectations.

################################################################################
# Standard breakdown of the problem 1
################################################################################
# 1 What are my inputs? Make a descriptive list of the inputs.

# My inputs are:
# 1 User selects game level.
# 2 Answer of the user to the quiz.

# More specific:
# A returned answer typed in the Python terminal.
# This respons is the value of a string variable.

################################################################################
# Standard breakdown of the problem 2
################################################################################
# 2 What are my outputs? Make a descriptive list of the outputs.

# My outputs are:
# 1 Feedback for the user that he selected a specific game level and rules how to play the game.
# 2 Feedback for the user if the provided answer is correct.
# 3 Feedback for the user when he has won or lost the game.

# More specific:
# A returned print statement in the Python terminal. "Right answer!" or "Wrong answer!"
# If "Right answer!" then update blanked out sentence with correct answer keyword and print "Right answer! Continue..."
# If "Wrong answer!" then do not update blanked out sentence with correct answer keyword and print "Wrong answer! Try again... X number of try's left."
# If all answers on a specific game level correct print "You have won the game!"
# If X number of try's left = 0 then print "Game over!"

################################################################################
# Standard breakdown of the problem 3
################################################################################
# 3 What are my available tools? Make a descriptive list of the tools.

# My available tools are:
# 1 The standard Python raw input function for storing user input into a variable.
# 2 The standard Python string find & replace method should be usefull.
# 2 General tools such a functions, variables and loops.

# More specific:
# https://docs.python.org/2/library/string.html
# string.replace(s, old, new[, maxreplace])
# Return a copy of string s with all occurrences of substring old replaced by new. If the optional argument maxreplace is given, the first maxreplace occurrences are replaced.
# string.find(s, sub[, start[, end]])
# Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end]. Return -1 on failure. Defaults for start and end and interpretation of negative values is the same as for slices.

# https://docs.python.org/2/library/functions.html#raw_input
# raw_input([prompt])
# If the prompt argument is present, it is written to standard output without a trailing newline.
# The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised.
# https://www.udacity.com/course/viewer#!/c-nd000/l-4170998786/m-4915289176

################################################################################
# Standard breakdown of the problem 4
################################################################################
# 4 Subdivide problem into more easily solvable pieces (if necessary). Make a descriptive list of all the pieces of the problem.

# My subdivision of the general problem:
# 1 Create a start_game function.
# 2 Create a end_game function.
# 3 Create a continue_game function.
# 4 Create a select_level function.
# 5 Create a start_level function.
# 6 Create a user_input function.
# 7 Create a check_user_input function.
# 8 Create a respons_user_input function.
# 9 Create a respons_update_game_status function.
# 10 Create a continue_game function.

################################################################################
# Standard breakdown of the problem 5
################################################################################
# 5 Solve each piece (prioritize subdivided pieces).
# My solution to each piece in pseudo code:

# 1 Create a start_game function.
# def start_game():
#   If code run start game immediately

# 2 Create a end_game function.
# def end_game(number_correct_answers, number_tries_left):
#   If all 4 answers on a level correct == True
#       print "You have won the game!"
#   Else:
#       call continue_game function
#   If number of try's left == 0
#       print "Game over!"
#   Else:
#       call continue_game function

# 3 Create a continue_game function.
# def continue_game():
#   If user input to answer == True
#       return number_correct_answers + 1
#       call respons_user_input function
#   Else:
#       return number_tries_left - 1
#       call respons_user_input function



################################################################################
# Standard breakdown of the problem 6
################################################################################

################################################################################
# Standard breakdown of the problem 7
################################################################################
