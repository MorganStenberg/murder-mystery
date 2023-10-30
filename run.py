
import story
import os
import platform
import time
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


def start_game_get_username():
    """
    Starts the game by asking the user for a username
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
        initialize_game()
    if valid is False:
        start_game_get_username()


def initialize_game():
    """
    Asks the user to start the game via pressing Y
    Calls correct functions to start game
    """
    while True:
        initialize_game = input("Y to start. Q to quit the game\n").lower()
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
    When the end of a branch is reached, asks the user if they want to
    restart the game and displays information on what number of player
    the user is. Sets global variables needed for game.
    """
    global decisions
    global list_of_decisions
    global username

    list_of_decisions = []
    decisions = None
    selected_path = ''

    while True:
        decisions = input("Enter your choice here: \n").lower()
        if decisions in {"a", "b"}:
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
            while True:
                end_or_restart = input("Do you want to play again?"
                                        " Y for yes N for no\n").lower()
                if end_or_restart == "y":
                    clear_screen()
                    story.welcome()
                    user_choices()
                    break
                elif end_or_restart == "n":
                    clear_screen()
                    story.end_of_game_text()
                    return
                else:
                    print("Invalid choice, please input Y or N")


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
    Compares the current path chosen by the user with previous paths taken by
    other users. And tells the user how many, if any, has chosen their
    specific path before them.
    """
    player_path = user_path.col_values(2)[1:]
    compare_paths = player_path.count(selected_path)
    print(f"You have reached the end of the game.\nYou are the {compare_paths}"
            f" player that has chosen this path: {selected_path}")


def main():
    """
    Starting the game by calling the correct functions
    """
    story.introduction_text()
    username = start_game_get_username()


if __name__ == "__main__":
    main()
