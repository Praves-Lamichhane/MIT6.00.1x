# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for c in secretWord:
        if c not in lettersGuessed:
            return False;
    return True;

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed SO FAR.
    ''' 
    # SHOULD FILL THE BLANK RATHER THAN PRINT
    workList = list(len(secretWord)*'_')
    if lettersGuessed in secretWord:
        # if there are two letters to be the same, only one will be entered
        # need to be fixed!!
        idx_list = findChar(secretWord,lettersGuessed);
        for cnt in idx_list:    
            workList[cnt]= lettersGuessed
    ret_str = ''.join(workList)
    return ret_str
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    allLetters = string.ascii_lowercase;
    ret_str = '';
    for c in allLetters:
        if c not in lettersGuessed:
            ret_str += c;
    return ret_str;

def findChar(s, ch):
    '''
    ch: character, the character to be found
    s: string, string to be searched over
    returns: list, the list of the indexes which shows the appearance of ch.
    '''
    return [i for i, ltr in enumerate(s) if ltr == ch]

def joinLists(updatedList, newList):
    '''
    updatedList: list, what letters have been filled in so far
    newList: list, what letters are guessed in this round
    returns: list, comprised of letters being filled in
    '''
    for i in range (len(newList)):
        if newList[i].isalpha():
            updatedList[i] = newList[i];      
    return updatedList
    
def printWelcomeMessage(secretWord):
    '''
    Print welcome message
    '''
    # Debugging Only...
    #print ("DEBUG: secret word is: %s." %secretWord)
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is %d letters long." %len(secretWord))

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    
    # ******************************
    # Local variables
    totalGuess = 8 # total number of guesses
    guessLeft = 8; # number of guesses remaining
    availableLetters = string.ascii_lowercase;
    prev_str = len(secretWord)*'_'; # dummy string
    updated_str= ''; # updated string (users' guess so far)
    letterEntered = []; # list to collect the letters that have been entered.
    # ******************************

    # print out welcome message
    printWelcomeMessage(secretWord)
    
    for i in range(totalGuess):
        print ("------------");
        print ("You have %d guesses left." %guessLeft);
        print ("Available letters: %s" %availableLetters);
        curr_char_usr = input("Please guess a letter: ")
        curr_char = curr_char_usr.lower();
        letterEntered += curr_char;
        # ******************************
        # DEBUG
        #if (curr_char == 'QUIT'):
        #   break; # Q to quick the program
        # ******************************
        
        temp_str = getGuessedWord(secretWord, curr_char)
        #print (temp_str)
        updated_str = ''.join(joinLists(list(prev_str),list(temp_str)));
        
        if (letterEntered.count(curr_char) > 1):
            print("Oops! You've already guessed that letter: %s" %updated_str)
        elif (curr_char in secretWord):
            print ("Good guess: %s" %updated_str)
        elif (curr_char not in secretWord):
            print ("Oops! That letter is not in my word: %s" %updated_str)
        else:
            pass;
        if(letterEntered.count(curr_char) <= 1):
            guessLeft -= 1;
        
        #if (curr_char in secretWord):
        #    print ("Good guess: %s" %updated_str)
        #else:
        #    print ("Oops! That letter is not in my word: %s" %updated_str)
        
        #print (updated_str);
        # update the required variables
        prev_str = updated_str;
        availableLetters = getAvailableLetters(letterEntered);
        
        # Decide whether users won or not
        if (isWordGuessed(secretWord,updated_str)):
            print ("------------"); # just for matching the grader's output
            print('Congratulations, you won!');
            break;
        if (guessLeft == 0 and not isWordGuessed(secretWord,updated_str)):
            print ("------------"); # just for matching the grader's output
            print("Sorry, you ran out of guesses. The word was %s." %secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'sea';
hangman(secretWord)
