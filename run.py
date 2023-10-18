
import story
import os
import platform

# Define global variable for username
username = None

def clear_screen():
    """
    When called clears the screen for the user, to enhance user
    experience. 
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
  

def introduction():
    """
    Introduces the game to the user
    """

    print(
        """
Welcome, Detective Extraordinaire, to the grandest caper of them all - 'Murder Mystery'! 
Prepare to embark on a whirlwind adventure filled with more twists and turns than a contortionist on a rollercoaster.

In this puzzling escapade, you'll don the hat of a sharp-eyed investigator determined to untangle a web of secrets, lies, 
and intriguing characters. With the goal of finding the murderer and uncovering the truth! 
        
But do remember that sometimes the path to the truth is not as straightforward as you might think.. 

Do you think you have what it takes to uncover the secrets of Whodunit Manor? 

        """)

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
        start_game()
         
    if valid is False:
        get_username()
    
   
def start_game():
    """
    Asks the user to start the game via pressing Y
    prints message if the user does not press Y. 
    """

    while True:
        print("Press Y to start game")
        start_game = input()
        if start_game == "y":
            clear_screen()
            story.story_welcome()
            first_choice()
            break
        else:
            print("Wrong choice, do you not dare to take on this challenge?")

def first_choice():
    """
    Asking the user for the first choice which takes them down different branches of the story
    """
    while True:
        first_choice = input()
        if first_choice == "1":
            story.story_branch_a()
            enter_front_door()
            break
        elif first_choice == "2":
            story.story_branch_b()
            break
        else:
            print("Invalid choice, please enter 1 or 2")

def enter_front_door():
    enter_front = input()
    if enter_front == "1":
        story.branch_a1()
    elif enter_front == "2":
        story.branch_a2()
    else:
        print("Invalid choice, please enter 1 or 2")
        enter_front_door()


def main():
    introduction()
    get_username()


main()


