# dice game by thebetentacled
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.

# imports
import random # for rolling dice

# variables
walletCash = int(20)
currentBet = int(0)
currentMoneyBet = int(0)
currentRoll = int(0)

# functions
def sayCash():
    print("You have $", walletCash, ".")

def rollDice(): # rolls dice, duh
    global curentRoll
    currentRoll = random.randint(2, 12)
    if currentRoll == 2:
        printTwo()
    elif currentRoll == 3:
        printThree()
    elif currentRoll == 4:
        printFour()
    elif currentRoll == 5:
        printFive()
    elif currentRoll == 6:
        printSix()
    elif currentRoll == 7:
        printSeven()
    elif currentRoll == 8:
        printEight()
    elif currentRoll == 9:
        printNine()
    elif currentRoll == 10:
        printTen()
    elif currentRoll == 11:
        printEleven()
    elif currentRoll == 12:
        printTwelve()
    changeMoney()

def placeBet(): # place your bet on the next roll
    global currentBet
    global currentMoneyBet
    sayCash()
    currentBet = int(input("what will the next roll be? -> "))
    currentMoneyBet = int(input("how much will you bet on that? -> "))
    rollDice()

def changeMoney(): # take or add money to your wallet
    global walletCash
    global currentBet
    global currentMoneyBet
    global currentRoll
    if currentBet == currentRoll:
       walletCash = int(walletCash + currentMoneyBet)
    elif currentBet > currentRoll:
        print("bet was greater than roll")
        walletCash = int(walletCash - currentMoneyBet)
        lossCheck()
    elif currentBet < currentRoll:
        print("bet was less than roll")
        walletCash = int(walletCash - currentMoneyBet)
        lossCheck()
    else: 
        print("what the fuck")

def lossCheck(): # check if you lose or not
    global walletCash
    if walletCash <= 0:
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