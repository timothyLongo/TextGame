# Timothy Longo

# the mystical cave adventure
# navigate through all crevasses of the cave to then duel the devil in an epic guitar battle

n_0 = 0  # variable to indicate whether the user has seen the screen for the first time or not.
i_n = 0  # variable to count the inventory items


# defining each room/prompt screen
# entry screen

def welcome_screen():
    global n_0
    while n_0 == 0:
        print("Enter 'exit' at any time to quit the game. \n"
              "Welcome! \n"
              "You've stumbled upon a small cave's entrance and kneel down inside. \n"
              "It's pitch black. Where will you head to first? Enter('forward', 'left', or 'right')\n")
        user_inv = input()
        if user_inv == 'forward':
            n_0 += 1
            hanuman()
        elif user_inv == 'left':
            print("Bunk! You'll feel that one tomorrow!")
            welcome_screen()
        elif user_inv == 'right':
            n_0 += 1
            jesus()
        else:
            print('Try again')
            welcome_screen()
    else:
        print("You've come back to the entrance of the cave. Where to now? Enter ('forward', 'left', or 'right')\n")
    n_0 += 1

    user = input()
    if user == 'forward':
        hanuman()
    if user == 'left':
        print("Bunk! You'll feel that one tomorrow!")
        welcome_screen()
    if user == 'right':
        jesus()
    if user == 'exit':
        quit()
    else:
        print('Try again')
        welcome_screen()


# defining room 1
n_1 = 0  # variable to indicate whether the user has seen the screen for the first time or not.


def hanuman():
    print('Inventory:', inventory)
    global n_1
    global i_n
    while n_1 == 0:
        print("You come face to face with Hanuman the monkey god while he's feasting on his stash of bananas. \n"
              "He throws one your way. Quick! Do you catch or dodge the banana? Enter 'c' to catch or 'd' to dodge\n")
        user_inv = input()
        if user_inv == 'c':
            inventory.append('banana')
            i_n += 1
            print('Good catch!')
            break
        elif user_inv == 'd':
            print('Close one!')
            break
        else:
            print('Try again')
            hanuman()
    else:
        print("You've come back across Hanuman's sanctuary, he smiles at you.")
    n_1 += 1
    print("Where are you headed now? Enter 'forward' 'left' 'right' or 'back'\n")
    user = input()
    if user == 'forward':
        cave_dweller()
    if user == 'left':
        print("Bunk! You'll feel that one tomorrow!")
        hanuman()
    if user == 'right':
        ram_dass()
    if user == 'back':
        welcome_screen()
    if user == 'exit':
        quit()
    else:
        print('Try again')
        hanuman()


# defining room 2
n_2 = 0  # variable to indicate whether the user has seen the screen for the first time or not.


def jesus():
    print('Inventory:', inventory)
    global i_n
    global n_2
    while n_2 == 0:
        print("An impoverished long-haired man in a long white robe is before you. \n"
              "Is that? - Is that you Jesus? The man turns \n"
              "to you with a glass of water. Moments later the clear liquid fills with dark hues of purple. \n"
              "He extends his glass toward you. Do you accept the mystical wine? Enter 'y' to accept and 'n' to pass\n")
        user_inv = input()
        if user_inv == 'y':
            inventory.append('wine')
            i_n += 1
            print('The grapey hues sit with your taste buds as you nerves are calmed and your body is relaxed.')
            break
        elif user_inv == 'n':
            print('Really? Wine from Jesus? No? Okay.')
            break
        else:
            print('Try again')
            jesus()
    else:
        print("You've come back across Jesus's sanctuary, he smiles at you.")
    n_2 += 1

    print("Where are you headed now? Enter('forward' 'left' 'right' or 'back') \n")
    user = input()
    if user == 'forward':
        ram_dass()
    if user == 'left':
        welcome_screen()
    if user == 'right':
        buddha()
    if user == 'back':
        print("Bunk! You'll feel that one tomorrow!")
        jesus()
    if user == 'exit':
        quit()
    else:
        print('Try again')
        jesus()


# defining room 3
n_3 = 0  # variable to indicate whether the user has seen the screen for the first time or not.


def buddha():
    print('Inventory:', inventory)
    global i_n
    global n_3
    while n_3 == 0:
        print("You evade the creepy crawlers by your feet and find yourself in the presence of a man meditating. \n"
              "'Welcome traveler! My name is Siddhartha Gautama, but everyone calls me the Buddha. You look cold, \n"
              "would you like this robe?' Enter 'y' to accept and 'n' to pass \n")
        user_inv = input()
        if user_inv == 'y':
            inventory.append('robe')
            i_n += 1
            print('You wrap the warm robe around your emaciated skeleton of a body.')
            break
        elif user_inv == 'n':
            break
        else:
            print('Try again')
            buddha()
    else:
        print("You've come back across the Buddha's place of meditation, he smiles at you.")
    n_3 += 1

    print("Where are you headed now? Enter('forward' 'left' 'right' or 'back')\n")
    user = input()
    if user == 'forward':
        trevor_hall()
    if user == 'left':
        jesus()
    if user == 'right':
        print("Bunk! You'll feel that one tomorrow!")
        buddha()
    if user == 'back':
        print("Bunk! You'll feel that one tomorrow!")
        buddha()
    if user == 'exit':
        quit()
    else:
        print('Try again')
        buddha()


# defining room 4
n_4 = 0  # variable to indicate whether the user has seen the screen for the first time or not.


def ram_dass():
    print('Inventory:', inventory)
    global i_n
    global n_4
    while n_4 == 0:
        print("A bald-headed and burly bearded westerner is before you chanting to himself while rotating a beaded \n"
              "bracelet through his fingers. 'Ah I see you've come here to meditate, \n"
              "great minds think alike! Here, I have an extra mala bracelet if you wish to join me.' \n"
              "Ram Dass extends the bracelet out before you \n"
              "Enter 'y' to accept and 'n' to pass")
        user_inv = input()
        if user_inv == 'y':
            inventory.append('mala bracelet')
            i_n += 1
            print('Thank you Ram Dass!')
            break
        elif user_inv == 'n':
            break
        else:
            print('Try again')
            ram_dass()
    else:
        print("You've come back across Ram Dass's special place, he smiles at you.")
    n_4 += 1

    print("Where are you headed now? Enter('forward' 'left' 'right' or 'back')\n")
    user = input()
    if user == 'forward':
        print("Bunk! You'll feel that one tomorrow!")
        ram_dass()
    if user == 'left':
        hanuman()
    if user == 'right':
        trevor_hall()
    if user == 'back':
        jesus()
    if user == 'exit':
        quit()
    else:
        print('Try again')
        ram_dass()


# defining room 5
n_5 = 0  # variable to indicate whether the user has seen the screen for the first time or not.


def cave_dweller():
    print('Inventory:', inventory)
    global i_n
    global n_5
    while n_5 == 0:
        print("A man sits in silence before you, only following the sound of a stream of water nearly dripping down \n"
              "the side of the cave. Your foot steps break his concentration. 'Oh, greetings traveler! Oh here, \n"
              "I want you to have this, this is a necklace I received from an old wise man way up in the mountains, \n"
              "I was told "
              "it will bring about good fortune and protection to whoever wears it. Here you have it'  \n"
              "Enter 'y' to accept and 'n' to pass")
        user_inv = input()
        if user_inv == 'y':
            inventory.append('holy necklace')
            i_n += 1
            print('Thank you mister!')
            break
        elif user_inv == 'n':
            break
        else:
            print('Try again')
            cave_dweller()
    else:
        print("You've come back across the cave dweller's sanctuary, he smiles at you.")
    n_5 += 1

    print("Where are you headed now? Enter('forward' 'left' 'right' or 'back')\n")
    user = input()
    if user == 'forward':
        print("Bunk! You'll feel that one tomorrow!")
        cave_dweller()
    if user == 'left':
        print("Bunk! You'll feel that one tomorrow!")
        cave_dweller()
    if user == 'right':
        print("Bunk! You'll feel that one tomorrow!")
        cave_dweller()
    if user == 'back':
        hanuman()
    if user == 'exit':
        quit()
    else:
        print('Try again')
        cave_dweller()


# defining room 6


n_6 = 0  # variable to indicate whether the user has seen the screen for the first time or not.


def trevor_hall():
    print('Inventory:', inventory)
    global i_n
    global n_6
    while n_6 == 0:
        print("You start to hear something as you slowly step into this opening. It's something pleasant, almost \n"
              "soothing. As you step closer your eyes adjust as you begin to notice a man plucking strings from a \n"
              "stringed instrument. You recognize this beanie-headed hippy's sound as you step closer.\n"
              "Trevor Hall! Hey!\n"
              "'Oh hey I didn't see you there! Here's a guitar! Would you like to jam with me?'\n"
              "Enter 'y' to accept and 'n' to pass \n")
        user_inv = input()
        if user_inv == 'y':
            inventory.append('guitar')
            i_n += 1
            print("You guys jam out together, with the vibrations from the strings echoing down the cave's walls and \n"
                  "crevasses, creating a completely immersive and powerful experience.\n")
            break
        elif user_inv == 'n':
            break
        else:
            print('Try again')
            trevor_hall()
    else:
        print("You've come back across Trevor Hall's jamming session, he looks up and smiles at you.")
    n_6 += 1

    print("Where are you headed now? Enter('forward' 'left' 'right' or 'back')\n")
    user = input()
    if user == 'forward':
        satan()
    if user == 'left':
        ram_dass()
    if user == 'right':
        print("Bunk! You'll feel that one tomorrow!")
        trevor_hall()
    if user == 'back':
        buddha()
    if user == 'exit':
        quit()
    else:
        print('Try again')
        trevor_hall()


def satan():
    if i_n == 6:
        print("The devil jumped up on a rocky lil' stump \n"
              "And said, 'boy, let me tell you what' \n"
              "I guess you didn't know it but I'm a fiddle player too \n"
              "And if you'd care to take a dare, I'll make a bet with you\n "
              "Now you play a pretty good fiddle, boy \n"
              "But give the devil his due \n"
              "I'll bet a fiddle of gold against your soul \n"
              "'Cause I think I'm better than you!!")
        print("***")
        print("Well I've stumbled through this cave \n"
              "and it might be a sin \n"
              "But I'll take your bet, you're gonna regret \n"
              "'Cause I'm the best there's ever been!")
        print(" Johnny, rosin up your bow and play your fiddle hard \n"
              "Cause Hell's broke loose in the here cave, and the devil deals the cards \n"
              "And if you win, you get this shiny fiddle made of gold \n"
              "But if you lose, the devil gets your soul \n"
              "The devil opened up his case and he said, 'I'll start this show' \n"
              "And fire flew from his fingertips as he rosined up his bow \n"
              "And he pulled the bow across the strings \n"
              "And it made a evil hiss \n"
              "Then a band of demons joined in\n"
              "And it sounded something like this\n"
              "When the devil finished, Johnny said, 'well, you're pretty good, ol' son\n"
              "But sit down in that chair right there\n"
              "And let me show you how it's done!\n"
              "Fire on the Mountain run boys, run\n"
              "The devil's in the House of the Rising Sun\n"
              "Chicken in a bread pan pickin' out dough\n"
              "Granny, does your dog bite? No, child, no\n"
              "The devil bowed his head because he knew that he'd been beat\n"
              "And he laid that golden fiddle on the ground at Johnny's feet\n"
              "And I said, 'Devil, just come on back if you ever wanna try again\n"
              "I done told you once you son of a bitch, I'm the best that's ever been!!\n")
        quit()
    else:
        print("A faint shimmering angelic voice echos from within the cave's walls -- \n"
              "You need to explore further! -ther! -her! \n"
              "Don't go in there yet! -yet! -et! \n")
        print("Do you listen to the voice? Enter ('y' or 'n')")
        user = input()
        if user == 'y':
            trevor_hall()
        elif user == 'n':
            print("You bull-headed bastard, you trot on and fall into a pit of lava \n"
                  "Better luck next time !")
            quit()
        else:
            print('Try again')
            satan()

# after all functions are defined, we start the game here


inventory = []

welcome_screen()
