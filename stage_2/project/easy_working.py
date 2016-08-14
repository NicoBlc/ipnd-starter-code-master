# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

start_game_message = '''\nWelcome to the very first Python program NicoBlc wrote! \nIt is a word replacement game.
\nHow to play: \nBelow you can find an example. \nThe answer for ___1___ is 'function'. Can you figure out the others?
\nSimply type your answer in the commandline and hit enter. \nYou get 5 tries, make them count. Good luck!\n'''

question = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''


question_answers = ['function', 'arguments', 'none', 'list']

question_list = []

number_tries_left = [5]

difficulty = ['easy', 'normal', 'hard']


def start_game():
    # Starts the game and displays a message on how to play.
    print start_game_message
    print question

start_game()

def end_game():
    # Ends game
    exit()


def check_correct_answer():
    # Checks the corresponding question (input) and returns correct answer (output).
    if len(question_list) == 0:
        correct_answer = question_answers[0]
        question_list.append(0)
        return correct_answer
    if len(question_list) == 1:
        correct_answer = question_answers[1]
        question_list.append(1)
        return correct_answer
    if len(question_list) == 2:
        correct_answer = question_answers[2]
        question_list.append(2)
        return correct_answer
    if len(question_list) == 3:
        correct_answer = question_answers[3]
        question_list.append(3)
        return correct_answer

def ask_user_next_question():
    # Asks the user the next question.
    if len(question_list) == 1:
        question_asked = question.replace("___1___", question_answers[0])
        print question_asked
        ask_user_for_answer()
    if len(question_list) == 2:
        second_question_asked = question.replace("___1___", question_answers[0])
        question_asked = second_question_asked.replace("___2___", question_answers[1])
        print question_asked
        ask_user_for_answer()
    if len(question_list) == 3:
        second_question_asked = question.replace("___1___", question_answers[0])
        third_question_asked = second_question_asked.replace("___2___", question_answers[1])
        question_asked = third_question_asked.replace("___3___", question_answers[2])
        print question_asked
        ask_user_for_answer()

def ask_user_for_answer():
    # Ask user to give an answer (input). Check answer. Give user feedback (output).
    user_answer = raw_input("What is your answer?>> ").lower()
    correct_answer = check_correct_answer()
    while user_answer != correct_answer and number_tries_left[0] > 1:
        number_tries_left[0] -= 1
        user_answer = raw_input("What is your answer?>> ").lower()
    if number_tries_left[0] > 1 and len(question_list) != 4:
        print '\n"Right answer! Continue..."\n'
        ask_user_next_question()
    if number_tries_left[0] > 1 and len(question_list) == 4:
        print '\n"You have won!"\n'
        end_game()
    if number_tries_left[0] == 1:
        print '\n"Game over! Try again..."\n'
        end_game()

ask_user_for_answer()
