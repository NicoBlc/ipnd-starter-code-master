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

def start_game():
    # Starts the game and displays a message on how to play.
    print start_game_message
    print question0

start_game()

def ask_user_first_question(question):
    print question1

ask_user_first_question(question1)

#Do something with a question list
#Update this global variable by appending to it
question_list = []

def ask_user_next_question(question):
    count_question = check_count_question()
    if question == 'question2':
        print question2
    if question == 'question3':
        print question3
    if question == 'question4':
        print question4

#Do something with a question list
def check_count_question(count_question):
    if count_question == 1:
        question = 'question1'
        return question
    if count_question == 2:
        question = 'question2'
        return question
    if count_question == 3:
        question = 'question3'
        return question
    if count_question == 4:
        question = 'question4'
        return question

def check_correct_answer():
    count_question = check_count_question(1)
    if count_question == 1:
        correct_answer = 'function'
        return correct_answer
    if count_question == 2:
        correct_answer = 'arguments'
        return correct_answer

def ask_user_for_answer():
    # Ask user to give an answer
    number_tries_left = 5
    user_answer = raw_input("What is your answer?>> ").lower()
    correct_answer = check_correct_answer()
    count_question = []
    while user_answer != correct_answer and number_tries_left > 1:
        number_tries_left -= 1
        user_answer = raw_input("What is your answer?>> ").lower()
    if number_tries_left > 1:
        print '\n"Right answer! Continue..."\n'
        count_question += 'answer_correct'
    ask_user_next_question(count_question)

ask_user_for_answer()
