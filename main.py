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

def takeInput():
    print("you have $" + str(walletCash))
    userGuess = int(input("what will the dice roll? \n  -> "))
    userBet = int(input("how much are you willing to bet on that? \n  -> "))
    rollDice()
    changeMoney(diceRoll, userGuess, userBet)

def changeMoney(diceRoll, guess, bet):
    global walletCash
    if guess == diceRoll:
        walletCash = walletCash + bet
        print("right on the money! you guessed correctly.")
        takeInput()
    else:
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
# main code
takeInput()