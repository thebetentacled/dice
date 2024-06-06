#!/bin/bash

echo "making files executable. . ."
cd ~/Downloads/dice
sudo chmod +x dice

echo "making games directory. . ."
cd 
mkdir games
cd games
mkdir dice
cd ~/Downloads/dice

echo "copying files. . ."
cp main.py ~/games/dice
cp LICENSE.txt ~/games/dice
cp README.md ~/games/dice
sudo cp dice /bin

echo "process complete!"