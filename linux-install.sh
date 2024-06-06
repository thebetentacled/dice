#!/bin/bash

echo "making files executable. . ."
sudo chmod +x dice

echo "making games directory. . ."
mkdir ~/games/dice

echo "copying files. . ."
cp main.py ~/games/dice
cp LICENSE.txt ~/games/dice
cp README.md ~/games/dice
sudo cp dice /bin

echo "process complete!"