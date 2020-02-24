#The adventure game
#a game where there's an adventure that is an adventure that is an adventure that is an adventure oob
#what kind of story dare I do???????
#define
#by koda
#
#
#Some non-ascii characters are in this code, please run it on a modern system from the last decade, thanks man. - Koda Koba
#
#
# -*- coding: cp1252 -*-

import random as ruben

hitpoints = 100
MP = 100
chara = ['attribute-main']
kit = 0
inventory = []
name = ""
ehp = 10
mhp = 1

def intro(scene):
    if scene == "begin":
        print "[turn CAPS LOCK on for this game, to make it easier]", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n", "\n"
        print "Welcome to l'arche de pain dans tus monde"
        print "A world beyond your wildest dreams, and deepest fantasies..."
        print "A place where only the sky is the limit, and everything goes."
        print "A traveler in the woods on the outskirt of a city is on their way"
        print "but who, oh who, may this entity be?"
        chara = []
        kit = 0
        inventory = []
        hitpoints = 100
        characterSelect()
        
    elif scene == "woods":
        print "Where the greyish horizon meets the ground, there is as far as they eye can see candy colored trees in all earthen colors."
        print "From the deepest reds, and brightest yellows, to the evergreens and browns of older trees. A heavy atmosphere surrounded from humidity."
        print "You awaken in a mysterious part of it, surrounded by none more than the wooded area around. You find you regular tools, and a meager item to eat."
        print "This is where it begins..."
        print "You find yourself in a small set of bushes, you basic materials with you."
        print "You have, standing up, two ways to go. One way goes to some moutains off in the distance\n", "while the other way goes towards a smaller set of moutains,\n and what appears to be a skyscraper off in the distance"
        print "The left goes off to the larger moutains, and the right goes to a city of sorts."
        #accidental shakespear much?
        story1()


def characterSelect():
    joos = raw_input("Would you like to Make your own character, or select a character? Press M for make ya own, or S for select: ")
    joos = joos.upper()
    if joos == "M":
        print "going to maker.........."
        makerN()
    elif joos == "S":
        print "Alrighty! I see you want to see my offerings. Here ya are!"
        juiceBox()
    else:
        print "That's not an option man!"
        characterSelect()

def juiceBox():
    print "Here's who there is:\n"
    print "Name: Jÿdra \n", "Type: Panther/Feline\n", "Perks: Jump Boost II, Feather Falling I.\n", "Weaknesses: Bodies of Water, The noise of pspspspspsps\n"
    print "-----------------------------------------------------------------", "\n", "\n", "\n"
    scrub = raw_input("See Next? Y/N: ")
    if scrub == "Y":
        print "Here's another", "\n", "\n", "\n"
        orangeBox()
    elif scrub == "N":
        print "Are you sure you want Jÿdra? Or would you like to go to the maker? Or how about the next one?"
        scoob = raw_input("Press J to select Jÿdra, Press N To see Next, or Press M to go to the Maker: ")
        if scoob == "J":
            chara.append('N-Jÿdra')    #adds attribute name()
            chara.append('T-Panther')  #adds attribute type.spec()
            chara.append('P-JumpII')   #adds an attribute to perk.local()
            chara.append('P-FeatherI') #adds an attribute to perk.local()
            chara.append('W-WaterIII') #adds an attribute to weakness.local()
            chara.append('W-pspsp')    #adds an attribute to weakness.local()
            name = "Jÿdra"
            print "You will start as Jÿdra the panther. You may now select your kit."
            camptime()
        elif scoob == "N":
            print "Here's the next character", "\n", "\n", "\n"
            orangeBox()
        elif scoob == "M":
            print "Sending you to the maker :>", "\n", "\n", "\n"
            makerN()
        else:
            print "what, no. Let me show you again...", "\n", "\n", "\n"
            juiceBox()
    else:
        juiceBox()
        
    
def orangeBox():
    print "this is the next character", "\n"
    print "Name: Wolf \n", "Type: Wolf/Canine \n", "Perks: Water Resistance I, Saturation II, Resistance I.\n", "Weaknesses: Heights, Hot Weather, his immobilizing fear of dragons...\n"
    print "-----------------------------------------------------------------", "\n", "\n", "\n"
    scrob = raw_input("See Next? Y/N: ")
    if scrob == "Y":
        print "Here's another", "\n", "\n", "\n"
        grapeBox()
    elif scrob == "N":
        print "Are you sure you want Wolf? Or would you like to go to the maker? Or how about the next one?"
        scoab = raw_input("Press W to select Wolf, Press N To see Next, or Press M to go to the Maker: ")
        if scoab == "W":
            chara.append('N-Wolf')         #adds attribute name()
            chara.append('T-Wolf')         #adds attribute type.spec()
            chara.append('P-WaterI')       #adds an attribute to perk.local()
            chara.append('P-SaturationII') #adds an attribute to perk.local()
            chara.append('P-ResistanceI')  #adds an attribute to perk.local()
            chara.append('W-HeightsI')     #adds an attribute to weakness.local()
            chara.append('W-HeatII')       #adds an attribute to weakness.local()
            chara.append('W-DragonsI')     #adds an attribute to weakness.local()
            print "You will start as Wolf the wolf. You may now select your kit."
            camptime()
        elif scoab == "N":
            print "Here's the next character", "\n", "\n", "\n"
            grapeBox()
        elif scoab == "M":
            print "Sending you to the maker :>", "\n", "\n", "\n"
            makerN()
        else:
            print "what, no. Let me show you again...", "\n", "\n", "\n"
            orangeBox()
    else:
        orangeBox()

def grapeBox():
    print "Here's the last one: \n"
    print "Name: Joe \n", "Type: Warrior/him-man\n", "Perks: Strength I\n", "Weaknesses: judymeme"
    print "-----------------------------------------------------------------", "\n", "\n", "\n"
    scrub = raw_input("See Next? Y/N: ")
    if scrub == "Y":
        print "Here's another", "\n", "\n", "\n"
        whatHaveyouDone()
    elif scrub == "N":
        print "Are you sure you want Joe? Or would you like to go to the maker? Or how about the next one?"
        scoob = raw_input("Press J to select Joe, Press N To see Next, or Press M to go to the Maker: ")
        if scoob == "J":
            chara.append('N-Joe')         #adds attribute name()
            chara.append('T-Warrior')     #adds attribute type.spec()
            chara.append('P-StrengthI')   #adds an attribute to perk.local()
            chara.append('judyMeme()')    #adds an attribute to weakness.local()
            print "You will start as Joe the warrior. You may now select your kit."
            camptime()
        elif scoob == "N":
            print "Here's the next character", "\n", "\n", "\n"
            whatHaveyouDone()
        elif scoob == "M":
            print "Sending you to the maker :>", "\n", "\n", "\n"
            makerN()
        else:
            print "what, no. Let me show you again...", "\n", "\n", "\n"
            grapeBox()
    else:
        grapeBox()


def whatHaveyouDone():
    print "WHAT ARE YOU DOING????????????????????? \n"
    print "Name: /dev/null \n", "Type: ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ \n", "Perks: INFINITY\n", "Weaknesses: ÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆÆ"
    print "-----------------------------------------------------------------", "\n", "\n", "\n"
    scrub = raw_input("See Next? Y/N: ")
    if scrub == "Y":
        print "Here's another", "\n", "\n", "\n"
        orangeBox()
    elif scrub == "N":
        print "Are you sure you want /dev/null? Or would you like to go to the maker? Or how about the next one?"
        scoob = raw_input("Press J to select /dev/null, Press N To see Next, or Press M to go to the Maker: ")
        if scoob == "J":
            chara.append('null') #define
            print "You will start as /dev/null the ÆÆÆÆÆÆÆÆÆÆÆÆÆ. You may now select your kit."
            camptime()
        elif scoob == "N":
            print "Here's the next character", "\n", "\n", "\n"
            juiceBox()
        elif scoob == "M":
            print "Sending you to the maker :>", "\n", "\n", "\n"
            makerN()
        else:
            print "what, no. Let me show you again...", "\n", "\n", "\n"
            whatHaveyouDone()
    else:
        whatHaveyouDone()

def makerN():
    print "i see, you want to try and make your own character! \n"
    print "So, there's a few things to be had here, for one you get random stats. Some stats may be a little more powerful than your allies, some may be more unfortuneate. \n"
    print "However, you get some more choices, and more fun to imagine. \n"
    naem = raw_input("First, lets give you a type. What type do you want? (Type refers to what your character is, it makes the game better): ")
    chara.append(naem)
    lion = raw_input("Next, give yourself a name: ")
    chara.append(lion)
    print "Now, im gonna randomly assign some stats for you. Rolling 20 for defence"
    for i in range(2):
        upstat = ruben.choice(['Strength', 'Resistance', 'Water', 'Saturation', 'Jump', 'Feather', 'Night', 'Smash'])
        modifier = ruben.randrange(4)
        chara.append(upstat)
    print "Rolling 20 for Weakness"
    for i in range(2):
        downstat = ruben.choice(['Weakness', 'fatigue', 'Water', 'Hunger', 'Heavy', 'nil', 'Blind'])
        modifier = ruben.randrange(4)
        chara.append(downstat)
    print chara
    print "Now your ready to get a kit"
    camptime()

def camptime():
    print "Now for you kit or class for your character, there are three types: \n", "Fighter Class, 100HP 100MP, standard equip set (An apple, sword, and a cape)"
    print "Heavy Class, 200HP 50MP, Heavy eqip set (2 apples, cape, and a sythe)\n", "Magic Class, 50HP 200MP, magic eqip set (apple, staff, and a ring)"
    noob = raw_input("Select a kit, type F for fighter, H for heavy, M for magic")
    if noob == "F":
        chara.append('apple')
        chara.append('sword-B')
        chara.append('cape')
        kit = 1
        print "Fighter Class Chosen!"
        print chara
        intro("woods")
    elif noob == "H":
        chara.append('apple')
        chara.append('apple')
        chara.append('sythe-B')
        chara.append('cape')
        hitpoints = 200
        MP = 50
        kit = 2
        print "Heavy class chosen!"
        print chara
        intro("woods")
    elif noob == "M":
        chara.append('apple')
        chara.append('staff-B')
        chara.append('ring')
        hitpoints = 50
        MP = 200
        kit = 3
        print "Magic class Chosen!"
        print chara
        intro("woods")
    else:
        camptime()


def story1():
    oof = raw_input("Which way do you choose to go? L for left, R for right: ")
    oof = oof.upper()
    if oof == "L":
        print "You chose to go left, going on to the snow capped moutains. It is oddly cloudy though... \n"
        print "A cool wind blows, you travel for the next while until the trees start to change from deciduous to taiga like."
        print "... but what is that strange shadow approaching?"
        firstbattle()
    elif oof == "R":
        print "You chose to go right, traveling until you reached a paved like area."
        print "It appeared that the area was deserted, though a soft light resonated from an oil lamp.", "\n", "However, a deeper shadow emerged, approaching at a high velocity"
        firstbattle()
    else:
        story1()

def firstbattle():
    print "Your first encounter! It's a monster lvl. 1, with 10HP!\n"
    print "First, let me explain how the battle system works\n"
    foo = raw_input("If you would like to skip, type an S: ")
    if foo == "S":
        print "All ready then, get ready to fight!"
    else:
        print "Battle in this ark bread game is pretty simple, just be mindful of things like HP and MP for attack.\n This game is fully turn based."
        print "Basically, your given a chance out of 20 for about everything, from an ability hurting you to simply going first in a battle."
        print "as you go on, more and more things will be at play, and battle logs might get a bit messy, but don't worry. Most of it is what stats effect and modify"
        print "different items, the enemy, or yourself. Later on, you'll find some weapons might by chance be much more powerful than some of the weapons you pick up along the way."
        print "Just remember the famous words: 'Roll 20 for defense'"
    print "\n", "\n", "\n", "\n", "\n", "\n"
    domath = ruben.randrange(20)
    print "Rolled a 20, got ", domath, " on roll"
    if domath > 9:
        print "Wowie! You go first!"
        print hitpoints, "HP       ", MP, "MP \n"
        himbo = raw_input("To attack with your main weapon, type A. To attack using magic, use D. To try to flee, press W.")
        himbo = himbo.upper()
        if himbo == "A": 
            if 'sword-B' in chara:
                ehp - 5
                print "Monster took 5 damage"
                print "Monster has", ehp, "HP left"
                bigtime()
            elif 'sythe-B' in chara:
                ehp - 10
                print "Monster took 10 damage"
                print "Monster has", ehp, "HP left"
                bigtime()
            elif 'staff-B' in chara:
                ehp - 3
                print "Monster took 3 damage"
                print "Monster has", ehp, "HP left"
                bigtime()
            else:
                print "F"
                firstbattle()
        elif himbo == "D":
            if 'T-Wolf' or 'Wolf' or 'wolf' or 'lion' or 'Lion' in chara:
                print "For magic, you can use Fire - uses 2MP, Ice - uses 3MP, or nutmeg - uses 1MP"
                print "To select use the first letter of the spell, in capitals. For instance, for fire use F."
            elif 'florida man' or 'Florida man' or 'Florida Man' or 'jimin' in chara:
                print "For magic, you can use Fire - uses 2MP, Ice - uses 3MP, or riding lawnmower - uses 1MP"
                print "To select use the first letter of the spell, in capitals. For instance, for fire use F."
            else:
                print "For magic, you can use Fire - uses 2MP, Ice - uses 3MP"
                print "To select use the first letter of the spell, in capitals. For instance, for fire use F."
            blyat = raw_input("Which magic attack would you like to use?")
            if blyat == "F":
                print "Summoning Fyre!"
            
    
    
    
        













    
    





    
