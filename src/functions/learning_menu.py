from functions.terminal import clear_terminal
from functions.quiz import quiz
from functions.user_input import handleUserInput

# MENU ONCE IN LEARNING MODE

def learning_menu():
    print('''\nWould you like to continue?
            Press 1 to Continue in Learning Mode
            Press 2 for Translator Mode 
            Press 3 for Quiz Mode
            Type \home to return Home
            Type \exit to Exit at any time \n''')
    while True:
        option = handleUserInput("What would you like to do? \n")
        if option == "1":
            clear_terminal()
            print("\nWelcome Back!\n")
            from functions.learning_mod import learning
            learning()
        elif option == "2":
            clear_terminal()
            from functions.translator import translator
            translator()
        elif option == "3":
            clear_terminal()
            quiz()
        else: 
            print('''\nThat's not a valid menu option. Please try again
            from the selection above.''')