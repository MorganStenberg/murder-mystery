

""" 
This file contains the story for the game. 
The introduction text is declared as a variable.
The different branches of the story are defined as different functions 
which will be called depending on the choices by the user

This file is imported in to the run.py file. 

"""



INTRODUCTION_TEXT = """
Welcome, Detective Extraordinaire, to the grandest caper of them all - 'Murder Mystery'! 

Prepare to embark on a whirlwind adventure filled with more twists and turns than a contortionist on a rollercoaster.

In this puzzling escapade, you'll don the hat of a sharp-eyed investigator determined to untangle a web of secrets, lies, 
and intriguing characters. With the goal of finding the murderer and uncovering the truth! 
        
But do remember that sometimes the path to the truth is not as straightforward as you might think.. 

Do you think you have what it takes to uncover the secrets of Whodunit Manor? 
"""
    

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

    A. Follow the butler to the drawing room.
    B. Politely decline and explore the manor on your own.

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

A. Indeed, Lady Genevieve. I'm here to untangle this web of mystery. So, who among you has the most skeletons in their closet?
B. Exchange pleasantries and ask about the events leading up to the unfortunate incident?

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

A. Press Lady Genevieve further about her reaction and any potential secrets.
B. Follow the departing guests into the next room.

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

A. Go into the next room to try and find Miss Penelope and ask her about the argument.
B. Go up to Mortimers study to see if you can find some more clues.

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


def branch_a1_1_2():
    print(
    """
You swiftly decide to follow the departing family members. Each takes a different 
direction, leaving you with a moment of decision. The person closest to you, 
their silhouette disappearing into the dimly lit chamber, catches your attention. 
There's something about the way they glance back, a hint of suspicion in their eyes, 
that makes you believe they may be holding onto some crucial information.

Without further hesitation, you choose to tail them. They walk briskly down the corridor, 
their steps purposeful. The echo of their heels against the polished floor seems to 
reverberate through the silent mansion.

Just as you round a corner, you catch sight of them disappearing into the room. 
You quicken your pace, determined not to lose them.

As you step into the room, the scene unfolds before you in an alarming tableau. 
They stand with their back to you, their figure silhouetted against a large ornate mirror. 
In their hand, you catch a glint of steel—a gun.

Before you can react, they turn to face you, their expression a chilling mix of 
determination and desperation. Without a word, they raise the gun..

The world seems to slow for a heartbeat, and then everything happens at once. 
The room fills with the echo of a gunshot, your instincts kicking into overdrive.

But it's too late. In a single, fatal shot, they hit their mark.

The room falls silent once more, the only sound the soft patter of rain against the window. 
The truth of Mortimer's demise, along with the answers you sought, remain locked within the walls of Whodunit Manor.

---

The detective's pursuit of the truth takes an unforeseen turn, culminating in a deadly encounter. 
The enigma of Whodunit Manor remains unsolved.

    """)


def branch_a1_2():
    print(
        """
 You decide to take a more diplomatic approach and engage in some small talk before delving into the heart of the matter. 
 After exchanging pleasantries with the gathered family members, you ask about the events leading up to Mortimer's untimely demise.

Lady Genevieve takes a deep breath, her gaze distant. "It was a stormy night, much like tonight. We were all 
gathered in the drawing room, discussing family matters. Mortimer seemed... on edge."

Before she can continue, a voice from the other side of the room cuts in sharply. 
"Nonsense, Genevieve! Mortimer was perfectly fine! He was in high spirits, excited about an upcoming business venture."

The speaker, Uncle Reginald, a stern-looking man with a no-nonsense air, stands tall, challenging Lady Genevieve's account. 
Tension fills the room as the rest of the family looks on, divided.

Miss Penelope, with a glint of mischief in her eyes, interjects, "Oh, come now! Let's not rehash old arguments. 
It won't do anyone any good."

With a gracious smile, she turns to you. 
"Detective, might I trouble you for a glass of champagne? I believe it's high time we toast to Mortimer's memory."

She leaves the room, her footsteps echoing down the hallway. The family members exchange uneasy glances, 
leaving an air of anticipation in her wake.

You now have two options:

A. Press Lady Genevieve to continue her account of the events.
B. Turn your attention to the stern-looking man and ask for his version of what happened.

How would you like to proceed, Detective?
        """

    )

def branch_a1_2_1():
    print(
        """
You turn your attention back to Lady Genevieve, encouraging her to share more about the fateful night. 
She takes a deep breath and begins, her voice steady yet tinged with sadness.

"As I said.. It was a stormy night, much like tonight. We were all gathered in the drawing room, 
discussing family matters. Mortimer seemed... on edge."

Just as she's about to reveal the nature of the heated argument, 
a sudden crash resounds through the mansion, followed by the sound of shattering glass. 
The family members jump in their seats, their faces pale with shock.

You rush to the window and see a shattered vase, its remnants scattered across the floor. 
Lady Genevieve gasps, clutching her chest.

"What in the world..." she begins, her voice trembling.

Before anyone can react, the lights flicker and then go out entirely. 
The room is plunged into darkness, and a collective gasp sweeps through the family.

In the chaos that follows, as everybody is trying to get the lights back on
from the shadows, a voice whispers in your ear. 

"I know what happened that night, meet me in the basement.."

As you try to grab hold of whoever that whispered, you realise that they are already gone..

You have two options:

A. Head to the basement to meet the mysterious informant.
B. Stay in the drawing room and try to restore order amidst the chaos. Ask the family who it was that whispered? 

What will be your next move, Detective?

        """
    )

def branch_a1_2_1_1():
    print(
        """
With a sense of urgency, you make your way through the darkened mansion, guided only by your flashlight. 
The air grows colder as you descend the narrow staircase leading to the basement.

As you approach the bottom of the surprisingly steep stairs, just as you start to make out 
that there are candles lit along the wall below the stairs, an unseen force slams into your back. 
You lose your balance, tumbling forward into the abyss.

Pain surges through your body as you collide with the ground, a searing agony that leaves you breathless. 
In the dim light of your flashlight, you glimpse strange symbols and eerie markings adorning the walls.

Gasping for air, you lay there, your vision fading, the symbols etched into your memory. 
You realize, too late, the sinister truth hidden within Whodunit Manor.

---

The detective's pursuit of the truth ends in a chilling and untimely demise. 
The secrets of Whodunit Manor, particularly the sinister activities in the basement, 
remain forever shrouded in mystery.

        """
    )

def branch_a1_2_1_2():
    print(
        """
You choose to remain in the drawing room, determined to bring some semblance of order to the chaos. 
Just as you're about to shout, "Who was it that just whispered?" the lights flicker back on, bathing 
the room in a sudden, startling brightness. Simultaneously, you've already begun to shout, 
creating a bizarre contrast of noise and light.

The room falls into a stunned silence. The family members exchange concerned looks, 
clearly taken aback by this unexpected turn of events. You can almost feel their unease radiating from them.

Lady Genevieve clears her throat, breaking the silence. 
"I think... perhaps we've all had enough excitement for one evening."

There's a murmur of agreement among the family members. It's clear that they're now 
convinced that you've, for lack of a better term, lost it. They exchange glances, 
and you catch snippets of conversation about hiring someone else, perhaps that famous detective, Benoit Blanc.

You nod, feeling a strange mixture of embarrassment and bewilderment. 
As you are make your way to the door, you can't help but wonder how you ended up as the star of this peculiar show.

---

The detective's attempt at restoring order takes an unexpected turn, leading to the family losing confidence in your ability to solve the case. With the decision made to seek the assistance of another detective, you make your exit from Whodunit Manor.


        """
    )

def branch_a1_2_1_1_2():
    print(
        """

        """
    )

def branch_a1_2_2():
    print(
    """
You decide to engage with Uncle Reginald, the stern-looking man who challenges 
Lady Genevieve's account of the events. With a firm but polite tone, 
you ask him to share his perspective on that fateful night.

Reginald straightens his posture, his expression determined. 
"It's important to set the record straight. Mortimer was in high spirits, 
excited about an upcoming business venture. There was no sign of distress in him."

Before he can continue, a sudden crash resounds through the mansion, 
followed by the sound of shattering glass. The family members jump in 
their seats, their faces pale with shock.

You rush to the window and see a shattered vase, its remnants scattered 
across the floor. Lady Genevieve gasps, clutching her chest.

"What in the world..." she begins, her voice trembling.

Before anyone can react, the lights flicker and then go out entirely. 
The room is plunged into darkness, and a collective gasp sweeps through the family.

In the chaos that follows, as everybody is trying to get the lights back on
from the shadows, a voice whispers in your ear. 

"I know what happened that night, meet me in the basement.."

As you try to grab hold of whoever that whispered, you realise that they are already gone..

---

You now have two options:

A. Head to the basement to meet the informant.
B. Stay in the drawing room and try to restore order amidst the chaos. Ask the family who it was that whispered?

How would you like to proceed, Detective?

    """)


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


def end_of_game_text():
    print("testing end of game text")

#testing putting functions in dictionary for refactoring decision function
map_of_functions = {
    'a': branch_a,
    'aa': branch_a1,
    'aaa': branch_a1_1,
    'aaaa': branch_a1_1_1,
    'aaaaa': branch_a1_1_1_1,
    'aaaab': branch_a1_1_1_2,
}