# dice game by thebetentacled
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

# imports
import random # for rolling dice

# variables
walletCash = 20
diceRoll = 0

# functions
def rollDice(minRoll, maxRoll):
    global diceRoll
    diceRoll = random.randint(minRoll, maxRoll)
    print("the dice rolled " + diceRoll + ".")

def takeInput():
    userGuess = int(input("what will the dice roll? -> "))
    userBet = int(input("how much are you willing to bet on that? -> "))
    rollDice(2, 12)
    changeMoney(userGuess, userBet)

def changeMoney(guess, bet):
    global diceRoll
    global walletCash
    if guess == diceRoll:
        walletCash = walletCash + bet
        takeInput()
    else:
        walletCash = walletCash - bet
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