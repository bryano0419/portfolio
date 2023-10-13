print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to the Island of treasure!')
print("You are a young adventurer waiting that has finally got your hands on a treasure map! \nThis map takes you to a mysterious unmarked island where each decision matters, \nbecause if you're not careful it could cost you your life... ")

choice1 = input("You reach the island and there are two paths one leads to a forest while the other leads to a cave which will you choose? \nChoice: FOREST, CAVE -> ").lower()
if choice1 == 'forest':
    choice2_main = input("As you walk into the forest you run into a jaguar! You can either run or hide, which will you choose?\nChoice: RUN, HIDE -> ").lower()
    if choice2_main == 'run':
        choice_run = input('As you run away you see the jaguar is chasing you! You can either continue to run or fight!\nChoice: RUN, FIGHT -> ').lower()
        if choice_run == 'run':
            choice_run2 = input('you trip and fall, the jaguar pounces on you and you die. You Lose.')
        elif choice_run == 'fight':
            choice_fight = input('You pick up a rock and attack the jaguar, after a rough struggle you manage to kill the jaguar\n you keep moving forward until you find a lake with an island in the center. You can either wait or try and swim across\n Choose: WAIT, SWIM -> ').lower()
            if choice_fight == 'wait':
                choice_wait = input('You look around and see a boat, you take a boat and make it to the small island there you find three doors a red, blue and yellow door.\n Choose: RED, BLUE, YELLOW -> ').lower()
                if choice_wait == 'red':
                    print('Congradulations you found the treasure. You Win!')
                elif choice_fight == 'blue':
                    print('You open the door and a blast of poisonous gas hits your face and you die. You Lose. -> ')
                elif choice_fight == 'yellow':
                    print('You open the door and a wild rat attacks you and you die. You Lose')
                else:
                    print('The decision drives you mad and you have a stroke. You Lose.')
            elif choice_fight == 'swim':
                print('You try to swim but are attacked by a rabid trout and die. You Lose.')
        else:
            print('A coconut falls out of nowwhere and hits your head and you die. You Lose.')

    elif choice2_main == 'hide':
        choice_hide = input('You hide and wait soon after the jaguar leaves.\nYou continue walking soon you come across a river which has line of rocks going across\nYou can either walk across the river or jump across the rocks.\nChoose: WALK, JUMP -> ').lower()
        if choice_hide == 'walk':
            choice_walk = input('As you walk the rushing river knocks you over and drags you down the river you drown. You Lose.')
        elif choice_hide == 'jump':
            choice_jump = input('You make it across the river and come across a shrine, you walk in and find three buttons\na red, blue, and yellow button which will you choose?\n RED, BLUE, YELLOW -> ').lower()
            if choice_jump == 'red':
                print('Out of nowhere poison darts shoot at you and you die. You Lose.')
            elif choice_jump == 'blue':
                print('The floor infront of you opens up and reveals the treasure!. You Win.')
            elif choice_jump == 'yellow':
                print('A trap door underneath you opens up and you fall and die. You Lose.')
            else: 
                print('You get so nervous you forget to breathe and die. You Lose.')

    else:
        print('You are suddenly attacked by a wild boar and die. You Lose')


elif choice1 == 'cave':
    choice2_alt = input('You have entered the cave but the entrance collapsed!\nLuckily you have a flashlight, you switch it on and you see two paths in the cave one goes up, one goes down what will you choose?\nChoice: UP, DOWN -> ').lower()
    if choice2_alt == 'up':
        choice_up = input('You move up and find another exit to the cave and find a a village, you instantly fall with the lifestyle and people but you have not forgotten the treasure\nChoose: STAY or LEAVE -> ').lower()
        if choice_up == 'stay':
            print('You decide to stay and are adopted by the village and spend the rest of your days happily. Happy Ending :)')
        elif choice_up == 'leave':
            choice_leave = input('You leave the village and come upon a large hill where you can see something at the top.\nWill you climb up the hill or go a differnet take a differnt path? Choose: CLIMB, PATH -> ').lower()
            if choice_leave == 'climb':
                choice_climb = input('You Find a house at the top, you go and explore the house and you find a skeloton gripping a key\n You grab the key and kep exploring, then you find a locked door, using the key you unlcok the door\nWill you go down or ignore the room Choose: DOWN, IGNORE -> ').lower()
                if choice_climb == 'down':
                    print('You go down and inside the room you find the treasure! You Win.')
                elif choice_climb == 'ignore':
                    print('You try to turn around but trip and fall down the stairs and die. You Lose.')
                else:
                    print('A fly flies into your mouth and you choke on it and die. You Lose.')
            elif choice_leave == 'path':
                print('You look for a differnt path but end up getting lost, you never find a way out. Bad Ending.')
        else:
            print('A meteor fall from the sky and crushes you. You Lose.')
    elif choice2_alt == 'down':
        choice_down = input('You go down the cave and fine an ancient ruin. In the ruins you find three levers\n a red, blue, and yellow lever.\nChoose: RED, BLUE, YELLOW -> ').lower()
        if choice_down == 'red':
            print('A giant stone rolls down crushes you. You Lose.')
        elif choice_down == 'blue':
            print('You pull the lever and the walls start closing in and crush you. You Lose.')
        elif choice_down == 'yellow':
            print('You pull the lever and a wall opens up revealing the treasure! You Win.')
        else:
            print('You stepped on a pressure plate which releases a swarm of bats that attaks you and you die. You Lose.')

else:
    print('You suddenly have a heart attack and die. You Lose')

