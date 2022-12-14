import csv
import random

from functions.learning_menu import learning_menu
from functions.terminal import clear_terminal
from pathlib import Path
from functions.user_input import *

# LEARNING MODE

def learning():

    def learning_mode(file_to_open, language_to_practice):
        with open(file_to_open) as readFile:
            open_file = csv.reader(readFile)
            vocabulary = list(open_file)    # convert file to list of lists (per row)
            word_check(vocabulary, language_to_practice)    # pass list and lang to func

    # Initialize empty set to store correct and incorrect values
    correct = set()
    incorrect = set()

    def word_check(vocabulary, language_to_practice):

        list_len = len(vocabulary)-1
        counter = 0

        # statement assigns index of opposite lang word (display practice word)
        if language_to_practice == "english":
            lang_index = 1
        else:
            lang_index = 0

        # statement switches the index to correspond with language of their answer, 
            # to determine if a match (correct)
        if lang_index == 1:
            guessword = 0
        else: guessword = 1

        studying_language = vocabulary[0][lang_index]
        #vocabulary[0][1] gives french value
        #vocabulary[0][0] gives english value
        # these are the header rows in the csv file


        while counter < list_len:
            random_word = random.randint(1,
                                        list_len)

            # generates index of random practice word relative to lang chosen
            practice_word = vocabulary[random_word][lang_index]
            counter+=1

            # tries = 0
            x=3
            for tries in range(1, 4):   # to iterate up to 3 tries (inclusive)
                user_entry = (handleUserInput(
                    f"What is the {language_to_practice} translation of {practice_word}?\n"
                )).lower()
                x-=1 # to show tries left on output of each guess (when wrong)
                if user_entry == (vocabulary[random_word][guessword]).lower():
                    print("Nice work! That's correct. \n")
                    correct.add(practice_word)   # adds correct word to correct set
                    break  # (break loop if correct)
                    
                elif user_entry != (vocabulary[random_word][guessword]).lower():
                    print(
                        f"Incorrect. You have {x} tries remaining! \n"
                    )
                    incorrect.add(practice_word)    # adds incorrect word to incorrect set

        # if user guessed any words right
        if len(correct)>0:
            print("\nAwesome work, here are the words you guessed correctly!\n")
            for word in correct:
                print (word)
        # otherwise they got them all wrong
        else: 
            print ("\nYou didn't get any correct, but more studying can fix this!\n")

        # if user guessed any words wrong
        if len(incorrect)>0:
            print("\nBelow are the words we need to work on: \n")
            for word in incorrect:
                print (word)
        # otherwise they guessed them all correctly
        else: 
            print ("\nMaybe its time for a quiz...\n")
        learning_menu()
        

    clear_terminal() # Clear terminal before user enters file name

    # Learning mode entry greeting message
    print('''\nYou're now in Viper Learning Mode. Please follow the below
    prompts to get started - \n''')

    while True:
            # determine user input to run correct func
            practice_lang = handleUserInput_stringOnly(
                    '''\nIf you wish to study from foreign language translations (note: this 
                    will require you to respond in eng), type English.\n 
                    If you wish to study from english translations (note: this 
                    will require you to respond in foreign lang), type Foreign: \n''')     
                # determine user input to run correct func
            if practice_lang.lower() == "english":
                break
            elif practice_lang.lower() == "foreign":
                break
            else:
                print("\nPlease enter a recognized language.")

    # Allow user to choose which file they wish to study
        # Create path that represents the current directory
    while True:
        try:
            target_dir = Path('.')
            filename = handleUserInput("\nPlease enter the filename you wish to study: \n").lower()
            # searches thru files and returns matching
            filepath = list(Path(target_dir).glob(f"**/{filename}.csv"))[0]
            break
        except IndexError:
            print("\nSorry that file doesn't seem to exist. Please enter a valid file name.\n")

    clear_terminal() # Clear terminal before starting
    # assess user input to run correct func
    if practice_lang.lower() == "english":
        print("\nGreat, let's begin!\n")
        learning_mode(filepath, practice_lang.lower())
    elif practice_lang.lower() == "foreign":
        print("\nGreat, let's begin!\n")
        learning_mode(filepath, practice_lang.lower())
    