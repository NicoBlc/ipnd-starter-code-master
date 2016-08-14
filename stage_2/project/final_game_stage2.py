# Below you can find my final word replacement game for stage2.
# The game has 3 difficulty levels to play.

# I broke down the problem into 6 essential functions. Then put them all together again.
# 1: choose_difficulty
# 2: start_game
# 3: end_game
# 4: check_correct_answer
# 5: ask_user_next_question
# 6: ask_user_for_answer

start_game_message = '''\nWelcome to the very first Python program NicoBlc wrote! \nIt is a word replacement game.
\nHow to play: \nBelow you can find an example. \nThe answer for ___1___ is 'function'. Can you figure out the others?
\nSimply type your answer in the commandline and hit enter. \nYou get 5 tries, make them count. Good luck!\n'''

question_easy = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''

question_normal = '''Python's ___1___  is a general-purpose interpreted, interactive, object-oriented,
and high-level ___2___ language. It was ___3___ by Guido van Rossum during 1985- 1990. Like Perl,
Python ___4___ code is also available under the GNU General Public License (GPL).\n'''

question_hard = '''Required arguments are the arguments passed to a ___1___ in correct positional order.
Here, the number of arguments in the function call should ___2___ exactly with the function definition.
Keyword ___3___ are related to the function calls. When you use keyword ___3___ in a function call,
the caller identifies the arguments by the ___4___ name.\n'''

question_answers_easy = ['function', 'arguments', 'none', 'list']
question_answers_normal = ['function', 'programming', 'created', 'source']
question_answers_hard = ['function', 'match', 'arguments', 'parameter']
question_list = []
number_tries_left = [5]
difficulty = ['easy', 'normal', 'hard']

def choose_difficulty():
    # Presents user with prompt to choose difficulty (input).
    # Selects right questions and answers to start game (output).
    user_difficulty = raw_input("Choose your difficulty: easy, normal or hard?>> ").lower()
    if user_difficulty == "easy":
        question = question_easy
        question_answers = question_answers_easy
        start_game(question, question_answers)
    if user_difficulty == "normal":
        question = question_normal
        question_answers = question_answers_normal
        start_game(question, question_answers)
    if user_difficulty == "hard":
        question = question_hard
        question_answers = question_answers_hard
        start_game(question, question_answers)
    else:
        print "You did not select a valid option. Try again..."
        choose_difficulty()

def start_game(question, question_answers):
    # Starts the game and displays a message on how to play.
    print start_game_message
    print question
    ask_user_for_answer(question, question_answers)

def end_game():
    # Ends game
    exit()

def check_correct_answer(question_answers):
    # Checks the current question and returns correct answer.
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

def ask_user_next_question(question, question_answers):
    # Asks the user the next question.
    if len(question_list) == 1:
        question_asked = question.replace("___1___", question_answers[0])
        print question_asked
        ask_user_for_answer(question, question_answers)
    if len(question_list) == 2:
        second_question_asked = question.replace("___1___", question_answers[0])
        question_asked = second_question_asked.replace("___2___", question_answers[1])
        print question_asked
        ask_user_for_answer(question, question_answers)
    if len(question_list) == 3:
        second_question_asked = question.replace("___1___", question_answers[0])
        third_question_asked = second_question_asked.replace("___2___", question_answers[1])
        question_asked = third_question_asked.replace("___3___", question_answers[2])
        print question_asked
        ask_user_for_answer(question, question_answers)

def ask_user_for_answer(question, question_answers):
    # Ask user to give an answer (input). Check answer. Give user feedback (output).
    user_answer = raw_input("What is your answer?>> ").lower()
    correct_answer = check_correct_answer(question_answers)
    while user_answer != correct_answer and number_tries_left[0] > 1:
        number_tries_left[0] -= 1
        user_answer = raw_input("What is your answer?>> ").lower()
    if number_tries_left[0] > 1 and len(question_list) != 4:
        print '\n"Right answer! Continue..."\n'
        ask_user_next_question(question, question_answers)
    if number_tries_left[0] > 1 and len(question_list) == 4:
        print '\n"You have won!"\n'
        end_game()
    if number_tries_left[0] == 1:
        print '\n"Game over! Try again..."\n'
        end_game()

choose_difficulty()
