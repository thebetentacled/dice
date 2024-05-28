# dice game by thebetentacled
# (license info)

# imports
import random # for rolling dice

# variables
walletCash = int(20)
howManyDice = int(0)
howManySides = int(0)
minRoll = int(0)
maxRoll = int(0)
currentBet = int(0)
currentMoneyBet = int(0)
currentRoll = int(0)

# functions
def sayCash():
    print("You have $", walletCash, ".")

def getDiceInfo(): # gets the amount and type of dice
    howManyDice = int(input("How many dice do you want to use? -> "))
    howManySides = int(input("How many sides should the dice have? -> "))

def calculateMinMax(): # gets the minimum & maximum roll possible given the amount of die
    global howManyDice
    global howManySides
    global minRoll
    global maxRoll
    minRoll = howManyDice
    maxRoll = howManyDice * howManySides

def rollDice(): # rolls dice, duh
    global curentRoll
    currentRoll = random.randint(minRoll, MaxRoll)
    lossCheck()

def placeBet(): # place your bet on the next roll
    global currentBet
    global currentMoneyBet
    sayCash()
    currentBet = int(input("what will the next roll be? ->"))
    currentMoneyBet = int(input("how much will you bet on that? ->"))
    rollDice()

def changeMoney(): # take or add money to your wallet
    global walletCash
    global currentBet
    global currentMoneyBet
    global currentRoll
    if currentBet == currentRoll:
       walletCash = int(walletCash + currentMoneyBet)
    else: 
        walletCash = int(walletCash - currentMoneyBet)
    placeBet()

def lossCheck():
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
manual()
getDiceInfo()
calculateMinMax()
placeBet()