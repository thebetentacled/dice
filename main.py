# dice game by thebetentacled
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

# imports
import random # for rolling dice

# variables
walletCash = 20
diceRoll = 0

# functions
def rollDice():
    global diceRoll
    diceRoll = random.randint(2, 12)
    printDice(diceRoll)

def takeInput():
    print("-------------------------------------------------------")
    print("you have $" + str(walletCash))
    print("input \"quit\" to quit.")
    userGuess = input("what will the dice roll? \n  -> ")
    if str(userGuess) == "quit":
        exit()
    else:
        userGuess = int(userGuess)
        pass
    userBet = int(input("how much are you willing to bet on that? \n  -> "))
    rollDice()
    changeMoney(diceRoll, userGuess, userBet)

def changeMoney(diceRoll, guess, bet):
    global walletCash
    if guess == diceRoll:
        walletCash = walletCash + bet
        print("right on the money! you guessed correctly.")
        takeInput()
    elif guess != diceRoll:
        walletCash = walletCash - bet
        if bet > diceRoll:
            print("you shot high. better luck next roll.")
            print("  (roll was " + str(diceRoll) + ", you guessed " + str(guess) + ".)")
        elif bet < diceRoll:
            print("you shot low. better luck next roll.")
            print("  (roll was " + str(diceRoll) + ", you guessed " + str(guess) + ".)")
        else:
            pass
        checkLoss()

def checkLoss():
    global walletCash
    if walletCash <= 0:
        print("you lost, better luck next time >:)")
        exit()
    else:
        takeInput()

# functions for ASCII graphics
def printDice(number):
    if number == 2:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|         | |         |")
        print("|    O    | |    O    |")
        print("|         | |         |")
        print("|_________| |_________|")
    elif number == 3:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|         | |     O   |")
        print("|    O    | |         |")
        print("|         | |   O     |")
        print("|_________| |_________|")
    elif number == 4:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|         | |     O   |")
        print("|    O    | |    O    |")
        print("|         | |   O     |")
        print("|_________| |_________|")
    elif number == 5:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|     O   | |     O   |")
        print("|    O    | |         |")
        print("|   O     | |   O     |")
        print("|_________| |_________|")
    elif number == 6:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|     O   | |     O   |")
        print("|    O    | |    O    |")
        print("|   O     | |   O     |")
        print("|_________| |_________|")
    elif number == 7:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|     O   | |  O   O  |")
        print("|    O    | |         |")
        print("|   O     | |  O   O  |")
        print("|_________| |_________|")
    elif number == 8:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|  O   O  | |  O   O  |")
        print("|         | |         |")
        print("|  O   O  | |  O   O  |")
        print("|_________| |_________|")
    elif number == 9:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|  O   O  | |  O   O  |")
        print("|    O    | |         |")
        print("|  O   O  | |  O   O  |")
        print("|_________| |_________|")
    elif number == 10:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|  O   O  | |  O   O  |")
        print("|    O    | |    O    |")
        print("|  O   O  | |  O   O  |")
        print("|_________| |_________|")
    elif number == 11:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|  O   O  | |  O   O  |")
        print("|    O    | |  O   O  |")
        print("|  O   O  | |  O   O  |")
        print("|_________| |_________|")
    elif number == 12:
        print("|‾‾‾‾‾‾‾‾‾| |‾‾‾‾‾‾‾‾‾|")
        print("|  O   O  | |  O   O  |")
        print("|  O   O  | |  O   O  |")
        print("|  O   O  | |  O   O  |")
        print("|_________| |_________|")

# main code
print("\"dice\" by thebetentacled")
print("This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.")
takeInput()