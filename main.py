# dice game by thebetentacled
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

# imports
import random # for rolling dice

# variables
walletCash = float(20)
currentBet = float(0)
currentMoneyBet = float(0)
currentRoll = float(0)

# functions
def sayCash():
    print("You have $", walletCash, ".")

def rollDice(): # rolls dice, duh
    global curentRoll
    currentRoll = float(random.randint(2, 12))
    print(currentRoll)
    if currentRoll == float(2):
        printTwo()
    elif currentRoll == float(3):
        printThree()
    elif currentRoll == float(4):
        printFour()
    elif currentRoll == float(5):
        printFive()
    elif currentRoll == float(6):
        printSix()
    elif currentRoll == float(7):
        printSeven()
    elif currentRoll == float(8):
        printEight()
    elif currentRoll == float(9):
        printNine()
    elif currentRoll == float(10):
        printTen()
    elif currentRoll == float(11):
        printEleven()
    elif currentRoll == float(12):
        printTwelve()
    changeMoney()

def placeBet(): # place your bet on the next roll
    global currentBet
    global currentMoneyBet
    sayCash()
    currentBet = float(input("what will the next roll be? -> "))
    currentMoneyBet = float(input("how much will you bet on that? -> "))
    rollDice()

def changeMoney(): # take or add money to your wallet
    global walletCash
    global currentBet
    global currentMoneyBet
    global currentRoll
    if currentBet == currentRoll:
       walletCash = walletCash + currentMoneyBet
    elif currentBet > currentRoll:
        print("bet was greater than roll")
        walletCash = walletCash - currentMoneyBet
        lossCheck()
    elif currentBet < currentRoll:
        print("bet was less than roll")
        walletCash = walletCash - currentMoneyBet
        lossCheck()
    else: 
        print("what the fuck")

def lossCheck(): # check if you lose or not
    global walletCash
    if walletCash <= float(0):
        print("you lost. better luck next time.")
        exit()
    else:
        placeBet()

def printTwo():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("|         |  |         |")
    print("|    O    |  |    O    |")
    print("|         |  |         |")
    print("|_________|  |_________|")

def printThree():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("|         |  |     O   |")
    print("|    O    |  |         |")
    print("|         |  |   O     |")
    print("|_________|  |_________|")

def printFour():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("|   O     |  |         |")
    print("|    O    |  |    O    |")
    print("|     O   |  |         |")
    print("|_________|  |_________|")

def printFive():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("|     O   |  |     O   |")
    print("|         |  |    O    |")
    print("|   O     |  |   O     |")
    print("|_________|  |_________|")

def printSix():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("|     O   |  |     O   |")
    print("|    O    |  |    O    |")
    print("|   O     |  |   O     |")
    print("|_________|  |_________|")

def printSeven():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("| O     O |  |     O   |")
    print("|         |  |    O    |")
    print("| O     O |  |   O     |")
    print("|_________|  |_________|")

def printEight():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("|     O   |  | O     O |")
    print("|    O    |  |    O    |")
    print("|   O     |  | O     O |")
    print("|_________|  |_________|")

def printNine():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("| O     O |  | O     O |")
    print("|         |  |    O    |")
    print("| O     O |  | O     O |")
    print("|_________|  |_________|")

def printTen():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("| O     O |  | O     O |")
    print("|    O    |  |    O    |")
    print("| O     O |  | O     O |")
    print("|_________|  |_________|")

def printEleven():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("| O     O |  | O     O |")
    print("| O     O |  |    O    |")
    print("| O     O |  | O     O |")
    print("|_________|  |_________|")

def printTwelve():
    print("|‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾|")
    print("| O     O |  | O     O |")
    print("| O     O |  | O     O |")
    print("| O     O |  | O     O |")
    print("|_________|  |_________|")

# main code
placeBet()