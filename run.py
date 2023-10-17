

def introduction():
    """
    Introduces the game to the user and asks for username
    """

    print("Welcome to Whodunit Manor!\n")
    print("You find yourself standing in front of the grand gates of Whodunit Manor, a sprawling estate shrouded in mystery.")
    print("As Detective Extraordinaire, you've been called upon to solve the most perplexing case of the century - a murder most foul!")
    print("Inside, you'll encounter a cast of eccentric characters, each with their own secrets and motives. The atmosphere is thick with tension, but fear not!")
    print("Your wit, charm, and keen detective skills will be your greatest allies. Now, it's time to take your first step into the labyrinth of clues and eccentricities that is Whodunit Manor.")
    print("Choose your path wisely, for the fate of this investigation rests squarely on your shoulders.\n")

username = None

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

   


def main():
    introduction()
    get_username()


main()