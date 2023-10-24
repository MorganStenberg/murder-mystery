
import story
import end_of_game
import os
import platform
import time #To delay printing of text for user

# Define global variables for decisions by the user
list_of_decision = []
decisions = None


def clear_screen():
    """
    When called clears the screen for the user, to enhance user
    experience. 
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def get_username():
    """
    Gets username from user
    """
    print("Please select your detective name..")
    username = input("Enter your name here: \n")
    validate_username(username)
  

def validate_username(username):
    """
    Validates username by checking that the user does not leave it blank,
    that it is atleast 2 characters and no longer than 10 characters. 
    """
    valid = True

    try:
        if len(username) == 0:
            raise ValueError(
                "You need to enter a name")
        if len(username) < 2:
            raise ValueError(
                "Your name needs to be at least 2 characters")
        if len(username) > 10:
            raise ValueError(
                "Your name can not be longer than 10 characters"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        valid = False
       
    if valid:
        print(f"Welcome detective {username}")
        initialize_game()

    if valid is False:
        get_username()
    
   
def initialize_game():
    """
    Asks the user to start the game via pressing Y
    Calls correct functions to start game
    """

    while True:
        print("Press Y to start game\n")
        initialize_game = input().lower()
        if initialize_game == "y":
            clear_screen()
            time.sleep(1)
            story.welcome()
            make_choice()
            break
        else:
            print("Wrong choice, do you not dare to take on this challenge?")



def make_choice():
    """
    Handles the main logic for the game and all the user choices. 
    Traverses through the different branches depending on the user input. 
    When the end of a branch is reached, asks the user if they want to restart the game.
    Sets global variables needed for game. 
    """
    global decisions
    global list_of_decision

    list_of_decision = []
    decisions = None
   
    while True:
        available_paths = [key for key in story.map_of_functions.keys() if len(key) == (len(list_of_decision)+1)]
        print(f"available paths here: {available_paths}")

        if available_paths > list_of_decision:
            decisions = input("Enter choice \n").lower()
            if decisions in {"a", "b"}:
                list_of_decision.append(decisions)
                function_call = ''.join(list_of_decision)
                if function_call in story.map_of_functions:
                    clear_screen()
                    time.sleep(0.5)
                    story.map_of_functions[function_call]()
                    print(f"list of decisions here:{list_of_decision}")
            else:
                print("Invalid choice, please input A or B")
        elif available_paths < list_of_decision:
            end_or_restart = input("Do you want to play again? Y for yes N for no\n").lower()
            if end_or_restart == "y":
                    clear_screen()
                    story.welcome()
                    make_choice()
                    break
            elif end_or_restart == "n":
                    clear_screen()
                    story.end_of_game_text()
                    break



def main():
    print(story.INTRODUCTION_TEXT)
    get_username()

main()

