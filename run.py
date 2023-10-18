
import story

# Define global variable for username
username = None

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

    if valid is False:
        get_username()

   
def start_game()

def main():
    introduction()
    get_username()


main()


