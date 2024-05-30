# dice game by thebetentacled
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

# imports
import random # for rolling dice

# variables
walletCash = str(20)
currentBet = str(0)
currentMoneyBet = str(0)
currentRoll = str(0)

# functions
def sayCash():
    print("You have $", walletCash, ".")

def rollDice(): # rolls dice, duh
    global curentRoll
    currentRoll = str(random.randint(2, 12))
    print(currentRoll)
    if currentRoll is str(2):
        printTwo()
    elif currentRoll is str(3):
        printThree()
    elif currentRoll is str(4):
        printFour()
    elif currentRoll is str(5):
        printFive()
    elif currentRoll is str(6):
        printSix()
    elif currentRoll is str(7):
        printSeven()
    elif currentRoll is str(8):
        printEight()
    elif currentRoll is str(9):
        printNine()
    elif currentRoll is str(10):
        printTen()
    elif currentRoll is str(11):
        printEleven()
    elif currentRoll is str(12):
        printTwelve()
    changeMoney()

def placeBet(): # place your bet on the next roll
    global currentBet
    global currentMoneyBet
    sayCash()
    currentBet = input("what will the next roll be? -> ")
    currentMoneyBet = input("how much will you bet on that? -> ")
    rollDice()

def changeMoney(): # take or add money to your wallet
    global walletCash
    global currentBet
    global currentMoneyBet
    global currentRoll
    if currentBet is currentRoll:
       walletCash = walletCash + currentMoneyBet
    elif currentBet is not currentRoll:
        walletCash = walletCash + currentMoneyBet
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