
import story
import end_of_game
import os
import platform
import time #To delay printing of text for user
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('murder_mystery')

user_path = SHEET.worksheet('userpath')
data = user_path.get_all_values()
print(data)


# Define global variables for decisions by the user
list_of_decisions = []
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


def start_game_get_username():
    """
    Starts the game by asking the user for a username
    """
    print("Please select your detective name..\n")
    username = input("Enter your name below: \n")
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
        print(f"\nWelcome detective.. {username}\n")
        initialize_game()

    if valid is False:
        start_game_get_username()
    
   
def initialize_game():
    """
    Asks the user to start the game via pressing Y
    Calls correct functions to start game
    """

    while True:
        print("Press Y to start game. Q to quit the game\n")
        initialize_game = input().lower()
        if initialize_game == "y":
            clear_screen()
            time.sleep(1)
            story.welcome()
            user_choices()
            break
        elif initialize_game == "q":
            clear_screen()
            time.sleep(1)
            story.end_of_game_text()
            break
        else:
            print("Wrong choice, do you not dare to take on this challenge?")



def user_choices():
    """
    Handles the main logic for the game and all the user choices. 
    Traverses through the different branches depending on the user input. 
    When the end of a branch is reached, asks the user if they want to restart the game.
    Sets global variables needed for game. 
    """
    global decisions
    global list_of_decisions

    list_of_decisions = []
    decisions = None
   
    while True:
        decisions = input("Enter your choice here: \n").lower()
        if decisions in {"a","b"}:
            list_of_decisions.append(decisions)
            function_call = ''.join(list_of_decisions)  
            if function_call in story.map_of_functions:
                clear_screen()
                time.sleep(0.5)
                story.map_of_functions[function_call]()
        else:
                print("Invalid choice, please input A or B")

        if (function_call + "a") not in story.map_of_functions or (function_call + "b") not in story.map_of_functions:
            end_or_restart = input("Do you want to play again? Y for yes N for no\n").lower()
            if end_or_restart == "y":
                    clear_screen()
                    story.welcome()
                    user_choices()
                    break
            elif end_or_restart == "n":
                    clear_screen()
                    story.end_of_game_text()
                    break
            else:
                print("Invalid choice, please input Y or N")





def main():
    """
    Starts the game by printing introduction text and then calling function to start
    game via asking the user for username.
    """
    print(story.INTRODUCTION_TEXT)
    username = start_game_get_username()

#if __name__ == "__main__":
    #main()

