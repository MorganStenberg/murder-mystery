import end_of_game

""" 
This file contains the story for the game. 
The different branches of the story are defined as different functions 
which will be called depending on the choices by the user

"""



def introduction_text():
    print(
        """
Welcome, Detective Extraordinaire, to the grandest caper of them all - 'Murder Mystery'! 

Prepare to embark on a whirlwind adventure filled with more twists and turns than a contortionist on a rollercoaster.

In this puzzling escapade, you'll don the hat of a sharp-eyed investigator determined to untangle a web of secrets, lies, 
and intriguing characters. With the goal of finding the murderer and uncovering the truth! 
        
But do remember that sometimes the path to the truth is not as straightforward as you might think.. 

Do you think you have what it takes to uncover the secrets of Whodunit Manor? 
        """
    )

def welcome():
    print(
        """
You find yourself standing in front of the grand gates of Whodunit Manor, a sprawling estate shrouded in mystery. 
As Detective Extraordinaire, you've been called upon to solve the most perplexing case of the century - a murder most foul!
Inside, you'll encounter a cast of eccentric characters, each with their own secrets and motives.

The atmosphere is thick with tension, but fear not! Your wit, charm, and keen detective skills will be your greatest allies.
Now, it's time to take your first step into the labyrinth of clues and eccentricities that is Whodunit Manor. 
Choose your path wisely, for the fate of this investigation rests squarely on your shoulders.

    A. Enter through the front doors of the manor.
    B. Circumvent the manor and sneak in through a side entrance.

What will you choose?

        """
    )

def branch_a():
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
    
def branch_a1_1():
    print(
        """
Indeed, Lady Genevieve. I'm here to untangle this web of mystery. So, who among you has the most skeletons in their closet?

You decide to start with a bold statement, hoping to shake loose any hidden secrets. The room falls momentarily silent, 
interrupted only by the crackling of the fireplace.

Uncle Reginald, his face turning a shade of crimson, sputters, "This is preposterous! How dare you imply such things?"
Cousin Eliza raises an eyebrow, her expression cool and collected. "Detective, your approach is rather... direct."
Miss Penelope, always quiet, shifts uncomfortably.

However, one person stands out among the reactions. It's Lady Genevieve. Her composure falters for just a moment, 
her eyes darting around the room before she regains her icy demeanor.

In a huff, Uncle Reginald exclaims, "This is outrageous! I won't stand for this!" With that, 
he storms out of the room, closely followed by Eliza and Miss Penelope.

The atmosphere in the room has changed, it seems you've struck a nerve. 
Now, it is only you Lady Genevieve still left in the room..

You have two options:

1. Press Lady Genevieve further about her reaction and any potential secrets.
2. Follow the departing guests into the next room.

What will you choose, Detective?

        """
    )

def branch_a1_1_1():
    print(
        """
Press Lady Genevieve further about her reaction and any potential secrets.

You turn your attention back to Lady Genevieve, who stands with a steely resolve. 
"Lady Genevieve, your reaction was quite telling. Is there something you're not telling me?"

She hesitates for a moment, then sighs. 
"Very well, Detective. There is a family secret, one that has haunted us for years. 
Mortimer, my late brother, had been in a bitter dispute with Miss Penelope. 
It involved a rather... peculiar matter."

The room seems to hold its breath, the weight of the revelation pressing in from all sides.
Lady Genevieve continues, her voice trembling, 
"It was during a stormy night much like this one, years ago. 
Mortimer and Miss Penelope had a heated argument about... believe it or not, 
it was about the never-ending debate between Android and iPhone. 
Mortimer was staunchly in favor of Android, while Miss Penelope, well, 
she was a die-hard iPhone enthusiast."

The gravity of the situation hits you, but in an unexpected way. 
The absurdity of their disagreement juxtaposed with the serious tone 
of Lady Genevieve's revelation is almost surreal.

"And this seemingly trivial argument," she continues, 
"led to a far more serious consequence. You see, the family trust fund, 
set up by our late father, was managed by Mortimer. Despite not being the 
eldest, he was given control due to our father's outdated beliefs. 
He took advantage of this power and cut Miss Penelope off from her 
rightful share, believing she couldn't handle the responsibility."


This revelation adds a new layer to the mystery, one that hints at deeper family tensions and hidden motives.

You have two options:

1. Go into the next room to try and find Miss Penelope and ask her about the argument.
2. Go up to Mortimers study to see if you can find some more clues.

What will be your next move, Detective?
        """
    )

def branch_a1_1_1_1():
    print(
        """
Go into the next room to try and find Miss Penelope and ask her about the argument.


With newfound determination, you decide to seek out Miss Penelope to get her side of the story. 
You make your way to the next room, your footsteps echoing in the silent halls.

As you enter, you're enveloped in the warm glow of a roaring fire. 
The room is a hunter's den, adorned with the spoils of countless 
expeditions - deer heads, antlers, and an array of taxidermied creatures.

In the dimly lit corner, a figure sits shrouded in shadow. 
You strain your eyes to see, but before you can make out who it is, a shot pierces the air.

The sound reverberates through the room, followed by the smell of gunpowder. 
Your senses heighten, and for a moment, time seems to stand still. Then, a searing pain courses through you.

You stagger, trying to comprehend what just happened. You catch a glimpse 
of the figure rising from the shadows, but it's too late. Darkness claims you.

---

The story comes to a sudden, tragic end. Your pursuit of the truth met an untimely 
demise in the heart of Whodunit Manor. The secrets of the manor, along with 
the identity of Mortimer's killer, remain locked away forever.
        """
    )
    end_of_game.end_game()

def branch_a1_1_1_2():
    print(
        """
You decide to head to Mortimer's study, hoping to uncover any additional clues 
that might shed light on the situation. The mansion's long corridors seem 
to stretch endlessly, and the silence is palpable.

As you ascend the grand staircase, the weight of anticipation 
hangs heavy in the air. The study's door looms ahead, imposing 
and enigmatic. You push it open, revealing a room filled with 
bookshelves, parchment, and the faint scent of aged leather.

Suddenly, you hear faint but distinct footsteps approaching. 
Your heart quickens as you scan the room, 
searching for a place to take cover.

Then, a noise startles you. You turn, only to come 
face-to-face with a shadowy figure. Before you can react, 
a gunshot echoes through the room.

Pain rips through your side, and you crumple to the ground.
Your vision blurs, and the room seems to spin. 
The figure steps forward, emerging from the shadows, 
and for a brief moment, you see their face. 
But it's the last thing you'll ever see.

---

The story takes a tragic turn as the detective's pursuit 
of the truth ends in a sudden and violent demise. 
The secrets of Whodunit Manor remain buried, 
and the identity of Mortimer's killer remains a mystery.
        """
    )
    end_of_game.end_game()

def branch_a1_1_2():
    print("testing branch_a1_1_2")

def branch_a1_2():
    print("Testing branch_a1_2")

def branch_a1_2_1():
    print("testing branch_a1_2_1")

def branch_a1_2_2():
    print("testing branch_a1_2_2")

def branch_a2():
    print("Testing branch a2")

def branch_a2_1():
    print("Testing branch a2_1")

def branch_a2_1_1():
    print("Testing branch a2_1_1")

def branch_a2_1_2():
    print("Testing branch a2_1_2")

def branch_a2_2():
    print("Testing branch a2_2")

def branch_a2_2_1():
    print("Testing branch a2_2_1")

def branch_a2_2_2():
    print("Testing branch a2_2_2")


def branch_b():
    print("testing branch b")

def branch_b1():
    print("testing branch b1")

def branch_b2():
    print("testing branch b2")


#testing putting functions in dictionary for refactoring decision function
map_of_functions = {
    'a': branch_a,
    'aa': branch_a1,
    'aaa': branch_a1_1,
    'aaaa': branch_a1_1_1,
    'aaaaa': branch_a1_1_1_1,
}