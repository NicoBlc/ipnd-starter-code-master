# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

start_game_message = '''Welcome to the very first Python program NicoBlc wrote! It is a word replacement game.
How to play: Below you can find an example. The answer for ___1___ is 'function'. Can you figure out the others?
Simply type your answer in the commandline and hit enter. You get 5 tries, make them count. Good luck!\n'''

question = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''

question1 = '''A function is created with the def keyword. You specify the inputs a function takes by
adding ___2___ separated by commas between the parentheses. functions by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''

question_answers = ['function', 'arguments', 'none', 'list']

question_asked = question.replace("___1___", question_answers[0])

print question
print question_asked

number_tries_left = [5]

print number_tries_left[0]
