#! /usr/bin/python
#
# Homework No.  10
# Project No.   02
# File Name:    hw10project2.py
# Programmer:   Karina Elias
# Date:         Nov. 22, 2019
#
# Problem Statement:
#   This program will create a GUI with a text box, button
#   and a picture. The user will type in the suit of a card
#   (spade, club, heart, diamond) and it will show the
#   corresponding suit. Use a dictionary as the storage mechanism.
#
#
# Overall Plan:
# 1. Create dictionary for suit
# 2. Create graphics window include:
#       Green background, banner text, instructions text,
#       entry textbox, display suit button, image placeholder
#       rectangle, quit button
# 3. Get suit entry when display suit button is clicked
# 4. Display image of corresponding suit
# 5. Close window when quit button is clicked
#
#
# import the necessary python libraries and classes
# for this program graphics and button is used
from graphics import *
from button import Button

class GraphicsInterface:
    # Create graphics window
    def __init__(self):
        # Dictionary for suit images
        self.suit = dict(club='club.ppm',
                         heart='heart.ppm',
                         diamond='diamond.ppm',
                         spade='spade.ppm')
        self.win = GraphWin("Suit Display", 600, 400)
        # Green background
        self.win.setBackground("green")
        # Banner text
        banner = Text(Point(300, 30), "Display a Suit")
        banner.setSize(24)
        banner.setFill("yellow")
        banner.setStyle("bold")
        banner.draw(self.win)
        # Instructions text
        instructions = Text(Point(300, 60), "(e.g. club, heart, diamond, spade)")
        instructions.setStyle("bold")
        instructions.draw(self.win)
        # Entry Textbox
        self.entryTextBox = Entry(Point(300, 85), 10)
        self.entryTextBox.draw(self.win)
        # Display suit button
        self.displaySuitButton = Button(self.win, Point(300, 115), 100, 20, "Display Suit")
        self.displaySuitButton.activate()
        # Image placeholder rectangle
        self.imageDisplayRect = Rectangle(Point(225, 150), Point(375, 350))
        self.imageDisplayRect.draw(self.win)
        # Quit button
        self.quitButton = Button(self.win, Point(300, 370), 100, 20, "Quit")
        self.quitButton.activate()
        # call function to display suit entered from user
        self.displaySuit()

    # ---FUNCTIONS---
    # function to display suit entered from user
    def displaySuit(self):
        # get mouse click point
        pt = self.win.getMouse()
        # if "Quit" button is clicked, close window
        while not self.quitButton.clicked(pt):
            # if the "Display Suit" button is clicked and
            # the entry textbox is not empty, display the
            # suit image
            if self.displaySuitButton.clicked(pt) \
                    and self.entryTextBox.getText() is not '':
                # image placeholder background turns white
                self.imageDisplayRect.setFill('white')
                inputText = self.entryTextBox.getText()
                # display suit image in center of
                # image placeholder rectangle
                suitImage = Image(Point(300, 250), self.suit[inputText])
                suitImage.draw(self.win)
            # get mouse click point again to check if the "Quit"
            # or "Display Suit" buttons were clicked
            pt = self.win.getMouse()
        # close window when "Quit" button is clicked
        self.win.close()


# ---MAIN---
def main():
    # Create GUI for suit display
    GraphicsInterface()


if __name__ == '__main__':
    main()
