import sys
from time import sleep
spd = 0.02


def print_str(str):
    for character in str:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(spd)
    

def hallway():
    print_str('''We are now in the hallway, I hope we can get through the house safely!
    What should we do next? Have a look around or choose a door to go through?''')
    response = input("What would you like to do? [Look around/ Choose a door] \n")
    if response == "Look around":
        print_str("Ok I'll have a look around and see what I can find.")
        response = input("Which senses should I use? [Eyes/Nose] \n")
        if response == "Eyes":
            print_str("I can see two doors, the door to the bedroom and a strange marking on the wall")
            print_str("Should we go through Door A or Door B or stay in the hallway?")
            response = input("What should we do? [A/B/Hallway]  \n")
            if response == "A":
                print_str("OK! Here goes nothing.")
                #Door A
            elif response == "B":
                print_str("Alright into the unknown we go!")
                #Door B
            elif response == "Hallway":
                print_str("Good idea! Let's look about a bit more!")
                #NOTE:TODO:Something here
            else:
                print_str("I don't know what you mean!")
                #TODO: Wrong answer thing. 

        elif response == "Nose":
            print_str("I can smell food downstairs, a strange creature smell from one door and nothing special from the other door")
        else:
            print_str("I'm not sure what you meant!")
            ß
    elif response == "Choose a door":
        print_str("Ok! Door A or Door B?")
        response = input("[A/B] ")
        if response == "A":
            print_str('''The rest of the game is DLC :) ''')
            #Door(A)
        elif response == "B":
            print_str('''The rest of the game is DLC :) ''')
            #Door(B)
        else:
            print_str("I'm not sure what you mean!")
    else:
        print_str("I can't do that right now!")

def wrong_answer_bedroom():
    response = input("Shall we explore the hallway next? [Y/N] \n")
    if response == "Y":
        print_str_str("Ok, I'm on my way to the hallway!\n")
        
        hallway()
    elif response == "N":
        print_str("I can have another look if you want.\n")    
        bedroom()
    else:
        print_str("That wasn't an option, please try again!\n")
        
        wrong_answer_bedroom()

def bedroom():
    
    print_str("I can't see any food in here but I have found something that could be useful!\n")
    
    print_str("You have found *Dog Toy*\n")
    
    response = input("Shall we explore the hallway next? [Y/N] \n")
    if response == "Y":
        print_str("Ok, I'm on my way to the hallway!\n")
        
        hallway()
    elif response == "N":
        print_str("I can have another look if you want.\n")
        
        bedroom()
    else:
        print_str("That wasn't an option, please try again!\n")
        
        wrong_answer_bedroom()

def wrong_answer_first_room():
    
    response = input("What shall we do first? [Explore the bedroom/Go into the hallway] \n")
    if response == "Explore the bedroom":
        print_str("Ok, let's have a look aorund\n")
        
        bedroom()
    elif response == "Go into the hallway":
        print_str("Ok, let's go together!\n")
        hallway()
    else:
        print_str("That wasn't an option please try again!\n")
        
        wrong_answer_first_room()    

def first_room():
    
    print_str("We appear to be in the bedroom, I can smell food from the hallway.\n")
    
    print_str("I can't hear much noise at the moment, the dog must be asleep!\n")
    
    response = input("What shall we do first? [Explore the bedroom/Go into the hallway] \n")
    if response == "Explore the bedroom":
        print_str("Ok, let's have a look aorund\n")
        
        bedroom()
    elif response == "Go into the hallway":
        print_str("Ok, let's go together!\n")
        hallway()
    else:
        print_str("That wasn't an option please try again!\n")
        
        wrong_answer_first_room()


def game_intro_wrong():
    
    response = input("Will you help me find some food? [Y/N] \n")
    if response == "Y":
        print_str("Thank you! Let's have a look around!\n")
        first_room()
    elif response == "N":
        print_str("You will leave me to starve?\n")
        
        game_intro_wrong()
    else:
        print_str("That wasn't an option, please try again!\n")
        
        game_intro_wrong()      

def game_intro():
    print_str('''(=^-ω-^=) \n''')
    
    print_str("Hello! I am Cat, to start please give me a better name! \n")
    
    global cat
    cat = input("What is my name? \n")
    
    print_str(f"Thank you! My name is now {cat}.\n")
    
    print_str("I have just woken up and am very hungry!!\n")
    
    response = input("Will you help me find some food? [Y/N] \n")
    if response == "Y":
        print_str("Thank you! Let's have a look around!\n")
        first_room()
    elif response == "N":
        print_str("You will leave me to starve?\n")
        
        game_intro_wrong()
    else:
        print_str("That wasn't an option, please try again!\n")
        
        game_intro_wrong()
