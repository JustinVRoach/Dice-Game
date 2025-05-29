import random
user_input = "y"

def RollD12():
    print("Rollin the dice...")
    value = random.randint(1, 12)
    print("You rolled a " + str(value))

def RollD6():
    print("Rollin the dice...")
    value = random.randint(1, 6)
    print("You rolled a " + str(value))

while user_input == "y":
    user_input = input("Enter 'y' to roll the dice, enter any other character to quit: ")
    if (user_input =="y"):
        dice_type = input("Press 1 for a D6, or 2 for a D12: ")
        print(dice_type)
        if (dice_type == "1"):
            RollD6() 
        elif (dice_type == "2"):
            RollD12()
        else:
           print("you chose poorly, rolling a d6")
           RollD6()
