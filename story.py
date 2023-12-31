"""
This file contains the story for the game.
The different branches of the story are defined as different functions

The functions are also mapped to keys in a dictionary, which is used
to call the correct function based on the user input.

This file is imported in to the run.py file.

"""


def introduction_text():
    print(
        """
'                ____    ____                        __                
'               |_   \  /   _|                      |  ]               
'                 |   \/   |  __   _   _ .--.   .--.|  | .---.  _ .--.  
'                 | |\  /| | [  | | | [ `/'`\]/ /'`\ ' |/ /__\ \[ `/'`\] 
'                _| |_\/_| |_ | \_/ |, | |    | \__/  || \__., | |     
'               |_____||_____|'.__.'_/[___]    '.__.;__]'.__.'[___]    
'   ____    ____                  _                                    
'  |_   \  /   _|                / |_                                  
'    |   \/   |    _   __  .--. `| |-'.---.  _ .--.  _   __            
'    | |\  /| |   [ \ [  ]( (`\] | | / /__\ \ [ `/'`\][ \ [  ]           
'   _| |_\/_| |_   \ '/ /  `'.'. | |,| \__.,  | |     \ '/ /            
'  |_____||_____|[\_:  /  [\__) )\__/ '.__.'  [___]  [\_:  /             
'                 \__.'                             \__.'              


Welcome, Detective Extraordinaire, to 'Murder Mystery'! 

--------------------------------------------------------------------------------

Prepare to embark on a whirlwind adventure filled with more twists and turns
than a contortionist on a rollercoaster.

In this puzzling escapade, you'll don the hat of a sharp-eyed investigator
determined to untangle a web of secrets, lies, and intriguing characters. With
the goal of finding the murderer and uncovering the truth!

But do remember that sometimes the path to the truth is not as straightforward
as you might think..

Do you think you have what it takes to uncover the secrets of Whodunit Manor?
        """
    )


def welcome():
    print(
        """
You find yourself standing in front of the grand gates of Whodunit Manor,
a sprawling estate shrouded in mystery. As Detective Extraordinaire, you'
ve been called upon to solve a perplexing case, a murder most foul!

Inside, you'll encounter a cast of eccentric characters, each with
their own secrets and motives.

The atmosphere is thick with tension, but fear not! Your wit, charm,
and keen detective skills will be your greatest allies.
Now, it's time to take your first step into the labyrinth of clues
and eccentricities that is Whodunit Manor. Choose your path wisely,
for the fate of this investigation rests squarely on your shoulders.

A. Enter through the front doors of the manor.
B. Circumvent the manor and sneak in through a side entrance.

What will you choose?
        """
    )


def branch_a():
    print(
        """
Enter through the front doors of the manor

You stride confidently up to the massive oak doors and give them a firm push.
They creak open to reveal a grand foyer adorned with portraits of stern-faced
ancestors and glittering chandeliers.

As you step inside, a butler, impeccably dressed, approaches with a polite bow.

"Good evening, Detective. The family is in the drawing room.
May I show you the way?"

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

You decide to accept the butler's offer. He leads you through a series of
ornate hallways, each more opulent than the last, until you reach a set
of double doors. With a flourish, the butler announces your arrival,

"Ladies and gentlemen, a detective has graced us with their presence."

The room is filled with an assortment of characters. There's the aloof
matriarch, Lady Genevieve, the boisterous Uncle Reginald, the enigmatic
cousin Eliza, and the withdrawn niece, Miss Penelope.

Lady Genevieve, her gaze piercing, steps forward, "Detective,
you're here to solve the unfortunate incident regarding my late
brother Mortimer, aren't you?"

As she speaks, you notice a flicker of something in her eyes -
a mix of sorrow and perhaps something else, something harder to place.

You have two options:

A. Start with a bold statement - "Indeed, Lady Genevieve. I'm here to
   untangle this web of mystery. So, who among you has the most skeletons
   in their closet?"
B. Exchange pleasantries and ask about the events leading up to
   the unfortunate incident?

What will be your next move, Detective?
        """
    )


def branch_a1_1():
    print(
        """
You decide to start with a bold statement.

Hoping to shake loose any hidden secrets. The room falls momentarily silent,
interrupted only by the crackling of the fireplace.

Uncle Reginald, his face turning a shade of crimson, sputters,
"This is preposterous! How dare you imply such things?"

Cousin Eliza raises an eyebrow, her expression cool and collected.
"Detective, your approach is rather... direct." Miss Penelope, always quiet,
shifts uncomfortably.

One person stands out among the reactions. It's Lady Genevieve.
Her composure falters for just a moment, her eyes darting around the
room before she regains her icy demeanor.

In a huff, Uncle Reginald exclaims, "This is outrageous! I won't
stand for this!" With that, he storms out of the room, closely
followed by Eliza and Miss Penelope.

The atmosphere in the room has changed, it seems you've struck a nerve.
Now, it is only you Lady Genevieve still left in the room..

You have two options:

A. Press Lady Genevieve further about her reaction and
   any potential secrets.
B. Follow the departing guests into the next room.

What will you choose, Detective?

        """
    )


def branch_a1_1_1():
    print(
        """
Press Lady Genevieve further about her reaction and any potential secrets.

You turn your attention back to Lady Genevieve.
"Lady Genevieve, Is there something you're not telling me?"

She hesitates for a moment, then sighs.
"Very well, Detective. There is a family secret, one that has
haunted us for years. Mortimer, my late brother, had been in a bitter
dispute with Miss Penelope. It involved a rather... peculiar matter."

Lady Genevieve continues, her voice trembling,

"It was during a stormy night much like this one, years ago.
Mortimer and Miss Penelope had a heated argument about... believe it or not,
the merits of using different programming languages than Python..

Miss Penelope was staunchly in favor Pythons supremacy, while Mortimer, well,
he was open to other languages."

The gravity of the situation hits you, but in an unexpected way.
The absurdity of their disagreement juxtaposed with the serious tone
of Lady Genevieve's revelation is almost surreal.

This revelation adds a new layer to the mystery, one that hints at
deeper family tensions and hidden motives.

You have two options:

A. Go into the next room to try and find Miss Penelope and ask her
   about the argument.
B. Go up to Mortimers study to see if you can find some more clues.

What will be your next move, Detective?
        """
    )


def branch_a1_1_1_1():
    print(
        """
Go into the next room to try and find Miss Penelope and ask her about
the argument.

With newfound determination, you decide to seek out Miss Penelope to get
her side of the story. You make your way to the next room, your footsteps
echoing in the silent halls.

As you enter, you're enveloped in the warm glow of a roaring fire.
The room is a hunter's den, adorned with the spoils of countless
expeditions - deer heads, antlers, and an array of taxidermied creatures.

In the dimly lit corner, a figure sits shrouded in shadow.
You strain your eyes to see, but before you can make out who it is,
a shot pierces the air.

The sound reverberates through the room, followed by the smell of gunpowder.
Your senses heighten, and for a moment, time seems to stand still.
Then, a searing pain courses through you.

You stagger, trying to comprehend what just happened. You catch a glimpse
of the figure rising from the shadows, but it's too late. Darkness claims you.

The story comes to a sudden, tragic end. Your pursuit of the truth met
an untimely demise in the heart of Whodunit Manor. The secrets of the
manor, along with the identity of Mortimer's killer,
remain locked away forever.

  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
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

The story takes a tragic turn as your pursuit
of the truth ends in a sudden and violent demise.
The secrets of Whodunit Manor remain buried,
and the identity of Mortimer's killer remains a mystery.

  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
        """
    )


def branch_a1_1_2():
    print(
        """
You swiftly decide to follow the departing family members. Each takes
a different direction. The person closest to you, their silhouette
disappearing into the dimly lit chamber, catches your attention.

Without further hesitation, you choose to tail them. They walk briskly down
the corridor, the echo of their heels against the polished floor seems 
to reverberate through the silent mansion. Just as you round a corner,
you catch sight of them disappearing into the room. You quicken your pace,
determined not to lose them.

As you step into the room, the scene unfolds before you in an alarming tableau.
They stand with their back to you, their figure silhouetted against a
large ornate mirror. In their hand, you catch a glint of steel—a gun.

Before you can react, they turn to face you, their expression a chilling mix of
determination and desperation. Without a word, they raise the gun..

The world seems to slow for a heartbeat, and then everything happens at once.
The room fills with the echo of a gunshot. In a single, fatal shot, 
they hit their mark.

The room falls silent once more, the only sound the soft patter of
rain against the window. The truth of Mortimer's demise, along with
the answers you sought, remain locked within the walls of Whodunit Manor.

Your pursuit of the truth takes an unforeseen turn, culminating
in a deadly encounter. The enigma of Whodunit Manor remains unsolved.
  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
    """)


def branch_a1_2():
    print(
        """
 You decide to take a more diplomatic approach and engage in some small talk
 before delving into the heart of the matter. After exchanging pleasantries
 with the gathered family members, you ask about the events leading up to
 Mortimer's untimely demise.

Lady Genevieve takes a deep breath, her gaze distant. "It was a stormy
night, much like tonight. We were all gathered in the drawing room,
discussing family matters. Mortimer seemed... on edge."

Before she can continue, a voice from the other side of the room cuts in
sharply. "Nonsense, Genevieve! Mortimer was perfectly fine! He was in
high spirits, excited about an upcoming business venture."

The speaker, Uncle Reginald, a stern-looking man with a no-nonsense air,
stands tall, challenging Lady Genevieve's account. Tension fills the room
as the rest of the family looks on, divided.

Miss Penelope, with a glint of mischief in her eyes, interjects,
"Oh, come now! Let's not rehash old arguments. It won't do anyone any good."

With a gracious smile, she turns to you.
"Detective, might I trouble you for a glass of champagne? I believe
it's high time we toast to Mortimer's memory."

She leaves the room, her footsteps echoing down the hallway. The family
members exchange uneasy glances,
leaving an air of anticipation in her wake.

You now have two options:

A. Press Lady Genevieve to continue her account of the events.
B. Turn your attention to uncle Reginald and ask for his
   version of what happened.

How would you like to proceed, Detective?
        """
    )


def branch_a1_2_1():
    print(
        """
You turn your attention back to Lady Genevieve, encouraging her to
share more about the fateful night. She takes a deep breath and begins,
her voice steady yet tinged with sadness.

"As I said.. It was a stormy night, much like tonight. We were all gathered
in the drawing room, discussing family matters. Mortimer seemed... on edge."

Just as she's about to reveal the nature of the heated argument, a sudden
crash resounds through the mansion, followed by the sound of shattering glass.
The family members jump in their seats, their faces pale with shock.

You rush to the window and see a shattered vase, its remnants scattered across
the floor. Lady Genevieve gasps, clutching her chest."What in the world..."
she begins, her voice trembling.

Before anyone can react, the lights flicker and then go out entirely. The room
is plunged into darkness, and a collective gasp sweeps through the family.
In the chaos that follows, as everybody is trying to get the lights back on
from the shadows, a voice whispers in your ear.

"I know what happened that night, meet me in the basement.."
As you try to grab hold of whoever that whispered, you realise that they are
already gone..

You have two options:

A. Head to the basement to meet the mysterious informant.
B. Stay in the drawing room and try to restore order amidst the chaos.
   Ask the family who it was that whispered?

What will be your next move, Detective?
        """
    )


def branch_a1_2_1_1():
    print(
        """
With a sense of urgency, you make your way through the darkened mansion, guided
only by your flashlight. The air grows colder as you descend the narrow
staircase leading to the basement.

As you approach the bottom of the surprisingly steep stairs, just as you start
to make out that there are candles lit along the wall below the stairs, an
unseen force slams into your back. You lose your balance, tumbling forward into
the abyss.

Pain surges through your body as you collide with the ground, a searing agony
that leaves you breathless. In the dim light of your flashlight, you glimpse
strange symbols and eerie markings adorning the walls.

Gasping for air, you lay there, vision fading, the symbols etched into your
memory. You realize, too late, the sinister truth hidden within Whodunit Manor.

Your pursuit of the truth ends in a chilling and untimely demise.
The secrets of Whodunit Manor, particularly the sinister activities in the
basement, remain forever shrouded in mystery.
  _____ _            ____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)    
--------------------------------------------------------------------------------
        """
    )


def branch_a1_2_1_2():
    print(
        """
You choose to remain in the drawing room, determined to bring some semblance of
order to the chaos. Just as you're about to shout, "Who was it that just
whispered?" the lights flicker back on, bathing the room in a sudden, startling
brightness.Simultaneously, you've already begun to shout, creating a bizarre
contrast of noise and light.

The room falls into a stunned silence. The family members exchange concerned
looks, clearly taken aback by this unexpected turn of events. You can almost
feel their unease radiating from them.

Lady Genevieve clears her throat, breaking the silence.
"I think... perhaps we've all had enough excitement for one evening."

There's a murmur of agreement among the family members. It's clear that they're
nowconvinced that you've, for lack of a better term, lost it. They exchange
glances, and you catch snippets of conversation about hiring someone else,
perhaps that famous detective, Benoit Blanc.

You nod, feeling a strange mixture of embarrassment and bewilderment.
As you are make your way to the door, you can't help but wonder
how you ended up as the star of this peculiar show.

Your attempt at restoring order takes an unexpected turn,
leading to the family losing confidence in your ability to solve the case.
With the decision made to seek the assistance of another detective,
you make your exit from Whodunit Manor.
  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
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
excited about an upcoming business venture. There was no sign of
distress in him."

Before he can continue, a sudden crash resounds through the mansion,
followed by the sound of shattering glass. The family members jump in
their seats, their faces pale with shock.

You rush to the window and see a shattered vase, its remnants scattered
across the floor. Lady Genevieve gasps, clutching her chest. 
"What in the world..." she begins, her voice trembling.

Before anyone can react, the lights flicker and then go out entirely.
The room is plunged into darkness, and a collective gasp sweeps through
the family.

In the chaos that follows, as everybody is trying to get the lights back on
from the shadows, a voice whispers in your ear.

"I know what happened that night, meet me in the basement.."
As you try to grab hold of whoever that whispered, you realise that they are
already gone..

You now have two options:

A. Head to the basement to meet the informant.
B. Stay in the drawing room and try to restore order amidst the chaos. Ask the
   family who it was that whispered?

How would you like to proceed, Detective?
    """
    )


def branch_a2():
    print(
        """
Politely decline and explore the manor on your own.

You thank the butler for his offer but decide to take matters into your own
hands. The manor is vast, and you're eager to uncover any hidden secrets it
may hold.

As you venture further into the manor, you find yourself in a dimly lit
corridor lined with paintings of somber-faced ancestors. The air feels
cooler here, and a faint echo of distant voices reaches your ears.

You have two options:

A. Make your way to the basement, drawn by a strange and eerie sensation.
B. Follow the sound of the voices.

What will you choose?
    """
    )


def branch_a2_1():
    print(
        """
Make your way to the basement, drawn by a strange and eerie sensation.

You follow an inexplicable pull, leading you deeper into the manor.
The corridor seems to stretch endlessly, the air growing colder with each step.
Finally, you arrive at a sturdy wooden door, slightly ajar.

As you push it open, cold air washes over you, carrying with it a scent
of damp earth and something else, something... unnatural. The room beyond is
illuminated by a flickering light, revealing an unexpected sight.

Before you stands a makeshift altar, adorned with candles and strange symbols,
all arranged in the shape of a python snake. Against the far wall, you spot a
figure bound and gagged, their eyes wide with terror.

You watch in stunned silence, hidden in the shadows. It's clear that
this is no ordinary situation; something far more sinister is at play.

You have two options:

A. Attempt to rescue the bound figure.
B. Quietly retreat and call for backup

What will you choose, Detective?
        """
    )


def branch_a2_1_1():
    print(
        """
You step into the room, determined to free the captive. With swift motions,
you untie the knots, and the figure's gratitude is palpable.

Before you can exchange a word, a sudden,
sharp blow to the back of your head sends shockwaves of pain
radiating through your skull. Darkness engulfs you.

When you come to, you're bound to a chair. The room is dimly lit,
shadows dancing on the walls. Before you, the family members stand
in a semi-circle, their faces a mix of satisfaction and solemnity.

Lady Genevieve steps forward, her voice carrying purpose.
"We have a mission - to preserve Python's sanctity.
Mortimer strayed, delving into JavaScript. We couldn't allow that."

You realize the depth of their fanaticism, willing to commit murder
to protect their chosen language. The gravity of the situation settles
over you. You're an unwitting intruder in their midst.

As the minutes pass, their fervent discourse on Python's
virtues washes over you, a relentless tide of fanaticism.
In their eyes, diversity in programming languages holds little sway.

Time loses meaning, and the realisation that you will never
leave this chamber slowly hits you. You plead for your release to no avail.

In this shadowy realm, the fervor for Python eclipses all else.
Your attempt to navigate this treacherous path will leave an
indelible mark on the annals of Whodunit Manor, even if it remains
shrouded in secrecy.

  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
        """
    )


def branch_a2_1_2():
    print(
        """
You decide to quietly retreat, recognizing the gravity of the situation.
This is no ordinary family gathering - it's a clandestine cult,
bound by their extreme devotion to something related to.. a snake shaped
like a.. Python.

You navigate the winding halls, careful not to attract attention.
As you make your way back towards the manor's entrance, you take
out your phone and dial the authorities.

With a sense of urgency, you provide them with the location and
details of what you found in the basement.As you step outside to meet
the authorities, you're met with a squad of determined officers, 
ready to apprehend the family members.

Each member is taken into custody, their expressions ranging
from disbelief to defiant resignation. The truth of Mortimer's
murder, entangled with their fanatical devotion, will now be
scrutinized by the justice system.

You've brought an end to this dark chapter in Whodunit Manor's
history. As the investigation unfolds, the full extent of the cult's
fanaticism is revealed. It turns out, their extreme devotion
was centered around the Python programming language,
an obsession that ultimately led to Mortimer's demise.

Your actions have solved the mystery and have preserved the
diversity of programming languages for generations to come.

 __   _____  _   _    ____   ___  _ __     _______ ____     ___ _____ _ 
 \ \ / / _ \| | | |  / ___| / _ \| |\ \   / / ____|  _ \   |_ _|_   _| |
  \ V / | | | | | |  \___ \| | | | | \ \ / /|  _| | | | |   | |  | | | |
   | || |_| | |_| |   ___) | |_| | |__\ V / | |___| |_| |   | |  | | |_|
   |_| \___/ \___/   |____/ \___/|_____\_/  |_____|____/   |___| |_| (_)
 --------------------------------------------------------------------------------
    """
    )


def branch_a2_2():
    print(
        """
You decide to follow the sound of the voices, your curiosity piqued by the
hushed but intense conversation. The voices lead you down a dimly lit
corridor, their urgency growing more pronounced.

As you round a corner, you find yourself outside a partially closed door.
The voices inside are hushed but tinged with an unmistakable tension.

"You must ensure the detective doesn't discover what's in the basement,"
one voice says, the tone laced with urgency.

Another voice, slightly muffled, responds,
"We've gone to great lengths to keep it hidden. 
We can't afford any slip-ups now."

A chill runs down your spine as you listen, the gravity of their conversation
sinking in. Whatever is in the basement holds a secret so significant that the
family is willing to go to extreme lengths to protect it.

You make a mental note to find a way into the basement,
determined to uncover the truth that has been hidden away.

Your options are:

A. Attempt to find an entrance to the basement.
B. Go back out the main entrance and call for backup.
    """
    )


def branch_a2_2_1():
    print(
        """
You decide to search for an entrance to the basement.
The urgency in the voices you overheard only strengthens
your resolve to uncover the truth.

After a few twists and turns through the labyrinthine corridors,
you come across a seemingly inconspicuous door. There's a faint draft
emanating from beneath, hinting at a hidden passage.

As you descend the narrow staircase, the air grows colder,
and the echoes of your footsteps reverberate.
The flickering light of a lone bulb barely illuminates the space.

Your breath catches in your throat as you take in the sight
before you. The basement is adorned with eerie symbols, arranged
in the shape of a python snake. It's a startling revelation.

A sense of foreboding washes over you, realizing that
there's more to this family and this manor than
meets the eye. The secrets held within these walls
are darker and more twisted than you could have imagined.

Your eyes scan the dimly lit room, and to your horror,
you find a figure bound and gagged, their eyes wide with terror.

A. Attempt to rescue the bound figure.
B. Quietly retreat and continue your investigation elsewhere.

What will be your next move, Detective?
        """
    )


def branch_a2_2_2():
    print(
        """
You decide it's wiser to retreat and call for backup.
This situation has become far too perilous to handle alone.
You quietly make your way back through the dimly lit corridor,
your senses on high alert.

Just as you reach the main entrance, a voice behind you startles you.
"Leaving so soon, Detective?" It's the butler, his tone dripping with menace.

Turning slowly, you find the imposing figure of the butler blocking
your path. He eyes you with a mixture of steely determination
and grim satisfaction.

You have two options:

A. Attempt to reason with the butler, explaining the gravity of
   the situation and your need for assistance.
B. Prepare for a confrontation. Try to force your way past the butler.

What will be your next move, Detective?
        """
    )


def branch_a2_2_2_1():
    print(
        """
You decide to attempt to reason with the butler,
hoping he'll understand the gravity of the situation.

"Listen, I need to call for backup. There's something going on
in this manor that's far beyond my capabilities to handle alone.
Lives may be in danger."

As you speak, you see a flicker of consideration in the
butler's eyes. Perhaps he's weighing the options, you think.
But just as you start to feel a glimmer of hope, everything goes dark.

A sudden, searing pain explodes in your head, and then... nothing.

When you awaken, your surroundings are unfamiliar.
You're in the basement, tied to a chair. The dim light casts
eerie shadows on the walls, illuminating strange snake like symbols etched
into the stone. The air is heavy with an oppressive stillness.

It's clear now that this family is entangled in something
far more sinister than you could have imagined.
The cult-like atmosphere in the basement speaks volumes.

The secrets of Whodunit Manor, and the extent of their devotion to...
whatever this is, remain shrouded in darkness.

  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
        """
    )


def branch_a2_2_2_2():
    print(
        """
You steel yourself, preparing for a confrontation with the butler.
Despite his imposing presence, you manage to outmaneuver him with a swift,
calculated move. The butler, older and perhaps slower than he once was,
is taken by surprise.

Your decisive strike lands, and the butler stumbles back, 
a look of shock and pain contorting his face. It's clear that he's injured.

However, before you can react further, the commotion draws
the attention of the family members. They rush in, their faces a mix of
astonishment and outrage at the sight of their butler being attacked.

"You dare to harm one of us?" Lady Genevieve's voice drips with venom.
"You will pay dearly for this."

With the family united against you, there is no chance of escape.
They quickly subdue you, their combined strength too much for
you to resist. The room is charged with tension and anger.

As you're restrained, wrists bound tightly, Lady Genevieve
turns to one of the family members. "Call the authorities.
This intruder will face the full extent of the law."

In a short while, the police arrive and take you into custody.
The truth of Mortimer's demise, along with any other mysteries
the manor holds, will remain forever shrouded.
  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
        """
    )


def branch_b():
    print(
        """
Circumvent the manor and sneak in through a side entrance.

You decide to take a more discreet approach and circumvent
the grand front doors. After a bit of exploration, you discover
a side entrance that seems less conspicuous.

As you slip inside, you find yourself in a dimly lit corridor,
lined with family portraits that seem to watch your every move.
You move quietly, your senses on high alert.

After a short distance, you come across an unmarked door.
It seems out of place, as if deliberately hidden from casual view.
You can't shake the feeling that there's something significant behind it.

You have two options:

A. Continue exploring the house.
B. Open the door and see what lies beyond.
        """
    )


def branch_b1():
    print(
        """
You decide to continue exploring the house.

You meander through dimly lit hallways, tracing your fingers
along the elaborate wallpaper that seems to whisper ancient secrets.

The air grows colder as you find a door that seems to lead to a
basement, you creek it open silently and look down, there seems
to be some flickering lights down there.

At the same time you hear steps approaching..

You have two options

A. Run away from the approaching steps
B. Go down in the basement
        """
    )


def branch_b1_1():
    print(
        """
As the steps draw nearer, your heart races. Instinct takes over, and you
quietly slip away, retracing your steps through the dark hallways.

You find yourself in front of an imposing door, which, when opened, reveals a
richly furnished study. It's clear this is where Mortimer, the head of the
household, conducts his business.

Your eyes scan the room, searching for anything that might hold a clue. That's
when you spot it - a laptop, resting on an ornate desk. It flickers to life as
you approach, revealing a video file prominently displayed.

With a mix of trepidation and determination, you click play.

The screen comes to life, displaying a chilling scene of a darkened chamber,
adorned with arcane symbols. Figures cloaked in shadows move in deliberate
motions, their voices raised in an eerie chant. The ritual is unmistakable -
this is a cult, and it seems to be connected to some sort of snake..
Maybe a Python..?

What do you do next?

A. This is too wierd to handle on your own, call the authorities.
B. Leave the study and continue exploring the house, taking the laptop.
        """
    )


def branch_b1_1_1():
    print(
        """
You quickly pull out your phone and dial the emergency number. Within minutes,
the operator reassures you that help is on the way.

Soon, the manor is alive with the flashing lights of police cars and the murmur
of officers combing through every nook and cranny. The family members are taken
into custody, their expressions evidence of their shock and disbelief.

As the investigation deepens, it becomes clear that the strange cult revolved
around the programming language Python. Their motives remain shrouded in
mystery, but the danger they posed has been extinguished.

Watching from a distance, satisfied that your quick thinking and bravery led to
the unraveling of this bizarre case. With the manor now secured, you make your
exit, knowing that you've once again proven yourself as a true Detective
Extraordinaire.

 __   _____  _   _    ____   ___  _ __     _______ ____     ___ _____ _ 
 \ \ / / _ \| | | |  / ___| / _ \| |\ \   / / ____|  _ \   |_ _|_   _| |
  \ V / | | | | | |  \___ \| | | | | \ \ / /|  _| | | | |   | |  | | | |
   | || |_| | |_| |   ___) | |_| | |__\ V / | |___| |_| |   | |  | | |_|
   |_| \___/ \___/   |____/ \___/|_____\_/  |_____|____/   |___| |_| (_)
--------------------------------------------------------------------------------
        """
    )


def branch_b1_1_2():
    print(
        """
You carefully pick up the laptop, tucking it under your arm. Determined to
uncover the secrets of Whodunit Manor, you quietly exit the study, making your
way back into the dimly lit hallway.

Just as you turn the corner, a sharp voice cuts through the silence. "And where
do you think you're going with that?" It's the butler, his eyes narrow and
suspicious.

Caught off guard, you stammer for words, but before you can respond, he lunges
forward with surprising agility. In an instant, a heavy object connects with
your head, sending you spiraling into darkness.

When you finally regain consciousness, your head throbs with pain. Blinking
against the dim light, you realize you're in the basement. You're bound to
a chair, The laptop sits on a table, just out of reach. The dim light casts
eerie shadows on the walls, illuminating strange snake like symbols etched
into the stone.

It's clear now that this family is entangled in something
far more sinister than you could have imagined.
The cult-like atmosphere in the basement speaks volumes.

The secrets of Whodunit Manor, and the extent of their devotion to...
whatever this is, remain shrouded in darkness.

  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)   
--------------------------------------------------------------------------------
        """
    )


def branch_b1_2():
    print(
        """
You steel yourself and cautiously descend the stairs into the basement.

You reach the bottom, a chill washes over you. The room is filled with an eerie
stillness, broken only by the faint flickering lights that cast long, dancing
shadows on the walls.

Your eyes scan the surroundings, you notice strange markings etched into the
walls, their meaning eluding you. It's clear that this basement holds secrets
that defy easy explanation.

In the corner of the room, you spot another set of stairs,
seemingly there are multiple ways to descend to the basement.

As you take a step further, you notice a sturdy wooden door, slightly ajar,
catching your attention. It emanates an aura of mystery.

What will you do?

A. Explore the room behind the sturdy wooden door.
B. Explore the basement further
        """
    )


def branch_b1_2_1():
    print(
        """
As you push the wooden door open, a wave of cold air washes over you, carrying
with it a scent of damp earth and something else, something... unnatural.
The room is illuminated by a flickering light, revealing an unexpected sight.

Before you stands a makeshift altar, adorned with candles and strange symbols,
all arranged in the shape of a python snake. Against the far wall, you spot a
figure bound and gagged, their eyes wide with terror.

You watch in stunned silence, hidden in the shadows. It's clear that
this is no ordinary situation; something far more sinister is at play.

You have two options:

A. Attempt to rescue the bound figure.
B. Quietly retreat and call for backup
        """
    )


def branch_b1_2_2():
    print(
        """
You decide to explore the basement further.

The air grows heavier, the shadows
deeper, as you move deeper into the heart of the manor's secrets.

After what feels like an eternity, you stumble upon another door, this one even
more foreboding than the last. It groans as you push it open, revealing a room
that chills you to the bone.

Dim light filters in, casting eerie shapes across the floor. Suddenly you spot
it - a colossal python, coiled and poised, its unblinking eyes fixed on you.
The room seems almost tailor-made for the creature, with strange symbols
etched into the walls.

Panic surges through you, but it's too late. With lightning speed, the python
strikes, its powerful coils wrapping around you. The last thing you hear is the
hiss of the serpent before darkness claims you.

Your investigation at Whodunit Manor ends here. The secrets of Whodunit Manor,
and the extent of their devotion to... whatever this is, remain shrouded
in darkness.
  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)                                      
--------------------------------------------------------------------------------
        """
    )


def branch_b2():
    print(
        """
Open the door and see what lies beyond.

You can't resist the urge to uncover the mystery behind this hidden door.

With a determined push, it creaks open to reveal a small, dimly lit room
filled with an array of electronic equipment. It's unmistakably a server room.

Your eyes scan the room, and you notice a console with a blinking red button,
immediately drawing your attention. It's a curious sight in this old manor.

As you approach, a sense of unease washes over you. You press the button,
a low hum fills the room. Suddenly, a blinding light engulfs your vision, and
you feel an overwhelming sense of disorientation.

Moments later, you find yourself in a completely different place, a modern city
with skyscrapers that seem to touch the sky. The sights and sounds are
overwhelming, and you're surrounded by people in a rush.

You check your surroundings, only to realize that you have no memory of
how you got here or why you're here. All that lingers is an odd compulsion
to learn the programming language Python.

Your adventure at Whodunit Manor is but a distant memory, lost in the
recesses of your mind. The secrets and mysteries of the manor remain forever
concealed.

  _____ _            _____           _ _ 
 |_   _| |__   ___  | ____|_ __   __| | |
   | | | '_ \ / _ \ |  _| | '_ \ / _` | |
   | | | | | |  __/ | |___| | | | (_| |_|
   |_| |_| |_|\___| |_____|_| |_|\__,_(_)    
--------------------------------------------------------------------------------
        """
    )


def end_of_game_text():
    print(
        """
Thank you for joining us in the mysterious world of Whodunit Manor.
Your detective skills were truly extraordinary!

If you ever wish to return and unravel more mysteries, the manor's
gates will always be open for you.

Farewell, and may your adventures continue in the realm of the unknown.


'     ______                          __  __                          _  
'   .' ___  |                        |  ][  |                        | | 
'  / .'   \_|   .--.    .--.    .--. |  |  | |.--.   _   __  .---.   | | 
'  | |   ____ / .'`\ \/ .'`\ \/ /'`\ '  |  | '/'`\ \[ \ [  ]/ /__\ \ | | 
'  \ `.___]  || \__. || \__. || \__/    |  |  \__/ | \ '/ / | \__. , |_| 
'   `._____.'  '.__.'  '.__.'  '.__.; __][__;.__.'[\_:   /   '.__.'  (_) 
'                                                  \ __ .'              
--------------------------------------------------------------------------------
        """
    )


# Dictionary mapping relevant branches to user choices,
# to be used by user_choices function.
map_of_functions = {
    'a': branch_a,
    'aa': branch_a1,
    'aaa': branch_a1_1,
    'aab': branch_a1_2,
    'aaba': branch_a1_2_1,
    'aaab': branch_a1_1_2,
    'aaaa': branch_a1_1_1,
    'aabb': branch_a1_2_2,  # Leads to the same ending as branch_a1_2_1
    'aabba': branch_a1_2_1_1,
    'aabbb': branch_a1_2_1_2,
    'aabaa': branch_a1_2_1_1,
    'aabab': branch_a1_2_1_2,
    'aaaaa': branch_a1_1_1_1,
    'aaaab': branch_a1_1_1_2,
    'ab': branch_a2,
    'aba': branch_a2_1,
    'abaa': branch_a2_1_1,
    'abab': branch_a2_1_2,
    'abb': branch_a2_2,
    'abba': branch_a2_2_1,  # Leads to the same ending as branch_a2_1_1, a2_1_2
    'abbaa': branch_a2_1_1,
    'abbab': branch_a2_1_2,
    'abbb': branch_a2_2_2,
    'abbba': branch_a2_2_2_1,
    'abbbb': branch_a2_2_2_2,
    'b': branch_b,
    'ba': branch_b1,
    'baa': branch_b1_1,
    'baaa': branch_b1_1_1,
    'baab': branch_b1_1_2,
    'bab': branch_b1_2,
    'baba': branch_b1_2_1,  # Leads to the same ending as branch_a2_1_1, a2_1_2
    'babaa': branch_a2_1_1,
    'babab': branch_a2_1_2,
    'babb': branch_b1_2_2,
    'bb': branch_b2,
}
