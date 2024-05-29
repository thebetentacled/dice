# dice game by thebetentacled
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

# imports
import random # for rolling dice

# variables
walletCash = int(20)
minRoll = int(2)
maxRoll = int(12)
currentBet = int(0)
currentMoneyBet = int(0)
currentRoll = int(0)

# functions
def sayCash():
    print("You have $", walletCash, ".")

def rollDice(): # rolls dice, duh
    global curentRoll
    currentRoll = random.randint(minRoll, maxRoll)

def placeBet(): # place your bet on the next roll
    global currentBet
    global currentMoneyBet
    sayCash()
    currentBet = int(input("what will the next roll be? -> "))
    currentMoneyBet = int(input("how much will you bet on that? -> "))
    rollDice()
    changeMoney()

def changeMoney(): # take or add money to your wallet
    global walletCash
    global currentBet
    global currentMoneyBet
    global currentRoll
    if currentBet == currentRoll:
       walletCash = int(walletCash + currentMoneyBet)
    else: 
        walletCash = int(walletCash - currentMoneyBet)
    lossCheck()

def lossCheck(): # check if you lose or not
    global walletCash
    if walletCash <= 0:
        print("you lost. better luck next time.")
        exit()
    else:
        placeBet()

def manual():
    print("---MANUAL---")
    print("always place inputs as numbers - NO spaces or letters!")
    print("the game will guide you through the rest.")

# main code
placeBet()