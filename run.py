
import story
import os
import platform
import time
import gspread
from google.oauth2.service_account import Credentials
import sys


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


# Define global variables for decisions by the user
list_of_decisions = []
decisions = None
username = ''


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
    Asking the user to input a username.
    """
    global username
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
    if valid is False:
        get_username()


def initialize_game():
    """
    Asks the user to start the game via input, provides option to quit game.
    """
    while True:
        initialize_game = input("Y to start. Q to quit the game\n").lower()
        if initialize_game == "y":
            time.sleep(1)
            return True
        elif initialize_game == "q":
            return False
        else:
            print("Invalid choice, please input Y or Q.\n")


def user_choices():
    """
    Handles the main logic for the game and all the user choices.
    Traverses through the different branches depending on the user input.
    When the end of a branch is reached, updates worksheet with path by
    user and then displays information on what number of
    player the user is.
    Sets global variables needed for game.
    """
    global decisions
    global list_of_decisions
    global username

    list_of_decisions = []
    decisions = None
    selected_path = ''

    while True:
        decisions = input("Enter your choice here: \n").lower()
        if decisions in {"a", "b"}:  # Validating user input
            list_of_decisions.append(decisions)
            selected_path = ''.join(list_of_decisions)
            if selected_path in story.map_of_functions:
                clear_screen()
                time.sleep(0.5)
                story.map_of_functions[selected_path]()
        else:
            print("Invalid choice, please input A or B")

        if ((selected_path + "a") not in story.map_of_functions
            or (selected_path + "b") not in story.map_of_functions):
            update_worksheet(username, selected_path)
            compare_selected_paths(selected_path)
            print((f"And you are the {retrieve_player_number()}"
                    " player to play the game! \n"))
            return


def retrieve_player_number():
    """
    Gets the number of players that has played the game from the google
    sheet by counting the total number of rows and subtracting for the header
    """
    number_of_rows = len(user_path.get_all_values())
    return number_of_rows - 1


def update_worksheet(username, selected_path):
    """
    Updates google sheet with username and the users chosen path in the game,
    aswell as the player number for the user.
    """
    player_count = retrieve_player_number()
    user_path.append_row([username, selected_path, player_count + 1])


def compare_selected_paths(selected_path):
    """
    Compares the current path chosen by the user with previous paths
    taken by the same user or other users. And tells the user how many,
    if any, has chosen their specific path before them.
    """
    player_path = user_path.col_values(2)[1:]
    compare_paths = player_path.count(selected_path)
    print(f"You have reached the end of the game.\nYou are the {compare_paths}"
            f" player that has chosen this path: {selected_path}")


def start_game():
    """
    Starting the game by calling correct the correct functions.
    """
    clear_screen()
    story.welcome()
    user_choices()


def main():
    """
    Calling functions for introduction and initializing game,
    exits if user decides to not play
    Also asks the user if they want to play again and calls
    correct function depending on input
    """
    story.introduction_text()
    username = get_username()
    init = initialize_game()
    if not init:
        story.end_of_game_text()
        sys.exit(1)

    start_game()
    while True:
        end_or_restart = input(
            "Do you want to play again?" " Y for yes N for no\n").lower()
        if end_or_restart == "y":
            start_game()
        elif end_or_restart == "n":
            clear_screen()
            story.end_of_game_text()
            break
        else:
            print("Invalid choice, please input Y or N")


if __name__ == "__main__":
    main()
