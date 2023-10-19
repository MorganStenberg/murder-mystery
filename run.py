
import story
import os
import platform

# Define global variables for decisions by the user
first_decision = None
second_decision = None
third_decision = None
fourth_decision = None
fifth_decision = None


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
    story.introduction_text()


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
            story.welcome()
            first_choice()
            break
        else:
            print("Wrong choice, do you not dare to take on this challenge?")

def first_choice():
    """
    Asking the user for the first choice which takes them down different branches of the story
    and calls the function for the chosen branch.
    """
    global first_decision
    while True:
        first_decision = input()
        if first_decision == "a":
            clear_screen()
            story.branch_a()
            second_choice()
            break
        elif first_decision == "b":
            clear_screen()
            story.branch_b()
            second_choice()
            break
        else:
            print("Invalid choice, please enter a or b")
    return  first_decision


def second_choice():
    """
    Ask the user for the second choice, calling the function for the chosen branch of the story
    """
    global second_decision
    while True:
        second_decision = input()
        if first_decision == "a":
            if second_decision == "1":
                clear_screen()
                story.branch_a1()
                third_choice()
                break
            elif second_decision == "2":
                clear_screen()
                story.branch_a2()
                third_choice()
                break
            else: 
                print("Invalid choice, please enter 1 or 2")
        elif first_decision == "b":
            if second_decision == "1":
                clear_screen()
                story.branch_b1()
                third_choice()
                break
            elif second_decision == "2":
                clear_screen()
                story.branch_b2()
                third_choice()
                break
            else: 
                print("Invalid choice, please enter 1 or 2")
    return second_decision


def third_choice():
    """
    Ask the user for the third choice, calling the function for the chosen branch of the story
    """
    global third_decision
    while True:
        third_decision = input()
        if first_decision == "a":
            if second_decision == "1":
                if third_decision == "1":
                    clear_screen()
                    story.branch_a1_1()
                    fourth_choice()
                    break
                elif third_decision == "2":
                    clear_screen()
                    story.branch_a1_2()
                    fourth_choice()
                    break
                else: 
                    print("Invalid choice, please enter 1 or 2")
        elif first_decision == "a":
            if second_decision == "2":
                if third_decision == "1":
                    clear_screen()
                    story.branch_a2_1()
                    fourth_choice()
                    break
                elif third_decision == "2":
                    clear_screen()
                    story.branch_a2_2()
                    fourth_choice()
                    break
                else: 
                    print("Invalid choice, please enter 1 or 2")
        elif first_decision == "b":
            if second_decision == "1":
                if third_decision == "1":
                    clear_screen()
                    story.branch_b1_1()
                    fourth_choice()
                    break
                elif third_decision == "2":
                    clear_screen()
                    story.branch_b1_2()
                    fourth_choice()
                    break
                else: 
                    print("Invalid choice, please enter 1 or 2")
        elif first_decision == "b":
            if second_decision == "2":
                if third_decision == "1":
                    clear_screen()
                    story.branch_b2_1()
                    fourth_choice()
                    break
                elif third_decision == "2":
                    clear_screen()
                    story.branch_b2_2()
                    fourth_choice()
                    break
                else: 
                    print("Invalid choice, please enter 1 or 2")
    return third_decision


def fourth_choice():
    """
    Ask the user for the fourth choice, calling the function for the chosen branch of the story
    """
    global fourth_decision
    while True:
        fourth_decision = input()
        if first_decision == "a":
            if second_decision == "1":
                if third_decision == "1":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_a1_1_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_a1_1_2()
                        fifth_choice()
                        break
                    else: 
                        print("Invalid choice, please enter 1 or 2")
                elif third_decision == "2":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_a1_2_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_a1_2_2()
                        fifth_choice()
                        break
                    else:
                        print("Invalid choice, please enter 1 or 2")
            elif second_decision == "2":
                if third_decision == "1":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_a2_1_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_a2_1_2()
                        fifth_choice()
                        break
                    else:
                        print("Invalid choice, please enter 1 or 2")
                elif third_decision == "2":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_a2_2_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_a2_2_2()
                        fifth_choice()
                        break
                    else:
                        print("Invalid choice, please enter 1 or 2")
        elif first_decision == "b":
            if second_decision == "1":
                if third_decision == "1":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_b1_1_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_b1_1_2()
                        fifth_choice()
                        break
                elif third_decision == "2":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_b1_2_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_b1_2_2()
                        fifth_choice()
                        break
                    else: 
                        print("Invalid choice, please enter 1 or 2")
            elif second_decision == "2":
                if third_decision == "1":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_b2_1_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_b2_1_2()
                        fifth_choice()
                        break
                elif third_decision == "2":
                    if fourth_decision == "1":
                        clear_screen()
                        story.branch_b2_2_1()
                        fifth_choice()
                        break
                    elif fourth_decision == "2":
                        clear_screen()
                        story.branch_b2_2_2()
                        fifth_choice()
                        break
                    else: 
                        print("Invalid choice, please enter 1 or 2")
    return fourth_decision
                




   


def main():
    introduction()
    get_username()


main()

