"""
Contains function to be called when the game is over for the user.
Resets variables and asks the user if they want to play again, 
and calling correct function depending on input

This file is imported in both run.py and story.py

"""


def end_game():
    
    
    end_or_restart = input("Do you want to play again? Y for yes N for no\n").lower()
    if end_or_restart == "y":
        clear_screen()
        start_game()
    elif end_or_restart == "n":
        clear_screen()
        end_of_game_text()

def end_of_game_text():
    print("testing end of game text")