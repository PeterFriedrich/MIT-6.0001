# Problem Set 2, hangman.py
# Name: Peter Friedrich
# Collaborators: The internet
# Time spent: 7 Planck seconds

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters
     are lowercase
    letters_guessed: list (of letters), which letters have been guessed so
     far; assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in
     letters_guessed; False otherwise
    '''
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
     letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
     represents which letters in secret_word have been guessed so far.
    '''
    guess_string = ''
    for i in secret_word:
        if i not in letters_guessed:
            guess_string = guess_string + '_ '
        else:
            guess_string = guess_string + i
    return guess_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which
     letters have not yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    letter_string = ''
    for i in alphabet:
        if i not in letters_guessed:
            letter_string = letter_string + i
    return letter_string


def check_letter(guess,warnings_remaining,secret_word, letters_guessed,
                guesses_remaining):
    '''
    guess: string, the current guess that the user has entered
    warnings_remaining: int of remaining warnings
    secret_word: string that is chosen word for game
    letters_guessed: list of letters already guessed
    guesses_remaining: remaining guesses
    '''

    if not str.isalpha(guess):
        if warnings_remaining > 0:
            warnings_remaining -= 1
            print('Oops! That is not a valid letter. You have {}'
            ' warnings left: {}'.format(warnings_remaining,
            get_guessed_word(secret_word, letters_guessed)))
            return False, guesses_remaining, warnings_remaining
        else:
            guesses_remaining -= 1
            print('Oops! That is not a valid letter. You have no'
            ' warnings left so you lose one guess: {}'.format(
            get_guessed_word(secret_word, letters_guessed)))
            return False, guesses_remaining, warnings_remaining
    else:
        return True, guesses_remaining, warnings_remaining

def is_match(guess, secret_word, letters_guessed, guesses_remaining,
            warnings_remaining):
            '''
            guess: a user inputted variable, has to be a single character
            - this function takes in the user guess, and takes an action, based
            on then aformentioned rules. It returns a tuple with recorded
            warnings, remaining guesses, and the appended list of guessed
            letters
            '''
            if guess in letters_guessed:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! You've already guessed that letter. You have"
                    " {} warnings left: {}".format(warnings_remaining,
                    get_guessed_word(secret_word, letters_guessed)))
                    return (warnings_remaining, guesses_remaining,
                    letters_guessed)
                else:
                    guesses_remaining -= 1
                    print("Oops! You've already guessed that letter. You have"
                    " no warnings left so you lose one guess: {}".format(
                    get_guessed_word(secret_word, letters_guessed)))
                    return (warnings_remaining, guesses_remaining,
                    letters_guessed)
            elif guess in secret_word:
                letters_guessed.append(guess)
                print('Good guess: ', get_guessed_word(secret_word,
                letters_guessed))
                return (warnings_remaining, guesses_remaining,
                letters_guessed)
            else:
                if guess in ['a','e','i','o','u']:
                    letters_guessed.append(guess)
                    print('Oops! That letter is not in my word:',
                            get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining -= 2
                    return (warnings_remaining, guesses_remaining,
                    letters_guessed)
                else:
                    letters_guessed.append(guess)
                    print('Oops! That letter is not in my word:',
                            get_guessed_word(secret_word, letters_guessed))
                    guesses_remaining -= 1
                    return (warnings_remaining, guesses_remaining,
                    letters_guessed)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(" ","")
    # Make sure lengths are identical
    if len(my_word) != len(other_word):
        return False
    # Check if letters in my_word match other_word, or are blank
    for i in range(len(my_word)):
        if (my_word[i] != '_') and (my_word[i] != other_word[i]):
            return False
    # Make hidden letters are not ones that are already revealed
    # I.e "a_ ple" != "apple"
    for j in range(len(my_word)):
        if my_word[j] == '_' and (other_word[j] in my_word):
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # prints out words that could be possible matches
    hintwords = []
    for aword in wordlist:
        if match_with_gaps(my_word,aword):
            hintwords.append(aword)
    count = 0
    for i in hintwords:
        if count == 10:
            print('\n',end='')
        print(i+' ',end='')
        count += 1

    print('\n',end='')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # Declare variables
    swl = len(secret_word)
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    # First announcements code
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is {} letters long.".format(swl))



    while True:
        print("-------------")
        if guesses_remaining == 0:
            print("Sorry, you ran out of guesses."
            " The word was {}.".format(secret_word))
            return
        if is_word_guessed(secret_word, letters_guessed) == True:
            print('Congratulations, you won!')
            score_word = ''
            for i in secret_word:
                if i not in score_word:
                    score_word = score_word + i
            score = guesses_remaining*len(score_word)
            print('Your total score for this game is:',score)
            return

        print("You have {} guesses left.".format(guesses_remaining))
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input('Please guess a letter: ')
        # access hints
        if guess == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word,
            letters_guessed))
            continue

        cl, guesses_remaining, warnings_remaining = check_letter(guess,
        warnings_remaining,secret_word, letters_guessed, guesses_remaining)
        if cl == True:
            guess = str.lower(guess)
            warnings_remaining, guesses_remaining, letters_guessed = is_match(
            guess, secret_word, letters_guessed, guesses_remaining,
            warnings_remaining)
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    #secret_word = 'apple'
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
