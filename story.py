""" 
This file contains the story for the game. 
The different branches of the story are defined as different functions 
which will be called depending on the choices by the user

"""

def story_welcome():
    print(
        """
You find yourself standing in front of the grand gates of Whodunit Manor, a sprawling estate shrouded in mystery. 
As Detective Extraordinaire, you've been called upon to solve the most perplexing case of the century - a murder most foul!
Inside, you'll encounter a cast of eccentric characters, each with their own secrets and motives.

The atmosphere is thick with tension, but fear not! Your wit, charm, and keen detective skills will be your greatest allies.
Now, it's time to take your first step into the labyrinth of clues and eccentricities that is Whodunit Manor. 
Choose your path wisely, for the fate of this investigation rests squarely on your shoulders.

    1. Enter through the front doors of the manor.
    2. Circumvent the manor and sneak in through a side entrance.

What will you choose?

        """
    )

def story_branch_a():
    print(
        """
    Enter through the front doors of the manor

You stride confidently up to the massive oak doors and give them a firm push. They creak open to reveal a grand foyer adorned with portraits of stern-faced ancestors and glittering chandeliers.

As you step inside, a butler, impeccably dressed, approaches with a polite bow. "Good evening, Detective. The family is in the drawing room. May I show you the way?"

You have two options:

    1. Follow the butler to the drawing room.
    2. Politely decline and explore the manor on your own.

What will you choose?

        """
    )
    

def branch_a1():
    print(
        """
Follow the butler to the drawing room

You decide to accept the butler's offer. He leads you through a series of ornate hallways, 
each more opulent than the last, until you reach a set of double doors. With a flourish, the butler announces your arrival, 
"Ladies and gentlemen, a detective has graced us with their presence."

The room is filled with an assortment of characters. There's the aloof matriarch, Lady Genevieve, the boisterous Uncle Reginald, the enigmatic cousin Eliza, and the withdrawn niece, Miss Penelope.

Lady Genevieve, her gaze piercing, steps forward, "Detective, you're here to solve the unfortunate incident regarding my late brother Mortimer, aren't you?"

As she speaks, you notice a flicker of something in her eyes - a mix of sorrow and perhaps something else, something harder to place.

You have two options:

1. Indeed, Lady Genevieve. I'm here to untangle this web of mystery. So, who among you has the most skeletons in their closet?
2. Exchange pleasantries and ask about the events leading up to the unfortunate incident?

What will be your next move, Detective?

        """
    )

def branch_a2():
    print("Testing branch a2")

def story_branch_b():
    print("testing branch b")


