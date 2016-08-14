Unsupported opcode: MAP_ADD
Unsupported opcode: MAP_ADD
Unsupported opcode: MAP_ADD
# Source Generated with Decompyle++
# File: fill-in-the-blanks_decompiled.pyc (Python 2.7)

easy_mad_lib = 'A common first thing to do in a language is display\n\'Hello __1__!\'  In __2__ this is particularly easy; all you have to do\nis type in:\n__3__ "Hello __1__!"\nOf course, that isn\'t a very useful thing to do. However, it is an\nexample of how to output to the user using the __3__ command, and\nproduces a program which does something, so it is useful in that capacity.\n\nIt may seem a bit odd to do something in a Turing complete language that\ncan be done even more easily with an __4__ file in a browser, but it\'s\na step in learning __2__ syntax, and that\'s really its purpose.\n'
easy_answers = [
    'world',
    'Python',
    'print',
    'HTML']
medium_mad_lib = "\nA __1__ is created with the def keyword.  You specify the inputs a\n__1__ takes by adding __2__ separated by commas between the parentheses.\n__1__s by default returns __3__ if you don't specify the value to retrun.\n__2__ can be standard data types such as string, integer, dictionary, tuple,\nand __4__ or can be more complicated such as objects and lambda functions."
medium_answers = [
    'function',
    'arguments',
    'None',
    'list']
hard_mad_lib = "When you create a __1__, certain __2__s are automatically\ngenerated for you if you don't make them manually. These contain multiple\nunderscores before and after the word defining them.  When you write\na __1__, you almost always include at least the __3__ __2__, defining\nvariables for when __4__s of the __1__ get made.  Additionally, you generally\nwant to create a __5__ __2__, which will allow a string representation\nof the method to be viewed by other developers.\n\nYou can also create binary operators, like __6__ and __7__, which\nallow + and - to be used by __4__s of the __1__.  Similarly, __8__,\n__9__, and __10__ allow __4__s of the __1__ to be compared\n(with <, >, and ==)."
hard_answers = [
    'class',
    'method',
    '__init__',
    'instance',
    '__repr__',
    '__add__',
    '__sub__',
    '__lt__',
    '__gt__',
    '__eq__']

def select_game_difficulty():
    """Prompts user for difficulty level, repeats until the user choses one.
    Function returns a string: either 'easy', 'medium', or 'hard'"""
    prompt = 'Please select a game difficulty by typing it in!\n'
    prompt += 'Possible choices include easy, medium, and hard.\n'
    equivalents = lambda .0: pass# WARNING: Decompyle incomplete
(('easy', 'e', '1', '1.'))
    equivalents.update(lambda .0: pass# WARNING: Decompyle incomplete
(('medium', 'm', '2', '2.')))
    equivalents.update(lambda .0: pass# WARNING: Decompyle incomplete
(('hard', 'h', '3', '3.')))
    chosen_difficulty = raw_input(prompt).lower()
    while chosen_difficulty not in equivalents:
        print "That's not an option!"
        chosen_difficulty = raw_input(prompt).lower()
    print "You've chosen " + str(equivalents[chosen_difficulty]) + '!\n'
    return equivalents[chosen_difficulty]


def get_mad_lib_and_answers(difficulty):
    '''Takes a difficulty (easy, medium, or hard) as an argument.
    Returns mad_lib string and answers list'''
    if difficulty == 'easy':
        return (easy_mad_lib, easy_answers)
    if None == 'medium':
        return (medium_mad_lib, medium_answers)
    if None == 'hard':
        return (hard_mad_lib, hard_answers)
    print
    print
    raise ValueError


def ask_question(mad_lib, blank_num, answer, max_attempts = 4):
    '''Takes the current madlib (str), current_question (int), and
    answer (str).  Returns the partially answered madlib (or None if the user
    takes too many guesses) and the number of the next blank.'''
    attempts_left = max_attempts
    to_replace = '__' + str(blank_num) + '__'
    prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
    user_guess = raw_input(prompt).lower()
    while user_guess != answer.lower() and attempts_left > 1:
        attempts_left -= 1
        prompt = make_display(mad_lib, to_replace, attempts_left, max_attempts)
        user_guess = raw_input(prompt).lower()
    if attempts_left > 1:
        print '\nCorrect!\n'
        return (mad_lib.replace(to_replace, answer), blank_num + 1)
    return (None, blank_num + 1)


def make_display(current_mad_lib, to_replace, attempts_left, max_attempts):
    """Returns a string to be printed out to the user based on the user's
    current progress in the game."""
    prompt = '\nThe current paragraph reads as such:\n{}\n\n'
    prompt += 'What should be substituted in for {}? '
    prompt = prompt.format(current_mad_lib, to_replace)
    if attempts_left == max_attempts:
        return prompt
    new_prompt = None
    if attempts_left > 1:
        new_prompt += "Let's try again; you have {} trys left!\n\n"
    else:
        new_prompt += 'You only have {} try left!  Make it count!\n\n'
    return new_prompt.format(attempts_left) + prompt


def find_max_guesses():
    print 'You will get 5 guesses per problem'
    return 5


def play_game():
    '''Plays the reverse mad_libs game.
    Returns True if the user wins, False otherwise'''
    difficulty = select_game_difficulty()
    (mad_lib, answers) = get_mad_lib_and_answers(difficulty)
    max_guesses = find_max_guesses()
    current_blank = 1
    while current_blank <= len(answers):
        (mad_lib, current_blank) = ask_question(mad_lib, current_blank, answers[current_blank - 1], max_guesses)
        if mad_lib is None:
            print "You've failed too many straight guesses!  Game over!"
            return False
    print mad_lib + '\nYou won!\n'
    return True

play_game()
