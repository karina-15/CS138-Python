#! /usr/bin/python
#
# Homework No.  11
# Project No.   01
# File Name:    hw11project1.py
# Programmer:   Karina Elias
# Date:         Dec. 11, 2019
#
# Problem Statement: Programming Exercise #1 p.423
#   Modify the Dice Poker program from this chapter to include
#   any or all of the following features: (chose (a) splash screen)
#   (a) Splash Screen. When the program first fires up, have
#       it print a short introductory message about the program
#       and buttons for "Let's Play" and "Exit." The main interface
#       shouldn't appear unless the user selects "Let's Play."
#   (b) Add a help button that pops up another window displaying
#       the rules of the game (the payoffs table is the most
#       important part).
#   (c) Add a high score feature. The program should keep track
#       of the 10 best scores. When a user quits with a good
#       enough score, he/she is invited to type in a name for
#       the list. The list should be printed in the splash screen
#       when the program first runs. The high-scores list will
#       have to be stored in a file so that it persists between
#       program invocations.
#
#
# Overall Plan:
# 1. Create SplashScreen class
# 2. Create window of same style as guipoker window
# 3. Add "Let's Play" and "Exit" buttons
# 4. Add button functionality to continue to pokerapp window
#       or exit program
# 5. Initialize in main
#
#
# import the necessary python libraries and classes
# for this program guipoker, pokerapp, and button are used
# from the textbook
# adds splash screen
from guipoker import *
from pokerapp import *
from button import *
from graphics import *


class SplashScreen(GraphWin):
    def __init__(self, win):
        GraphWin.__init__(self, win, "Dice Poker", 600, 400)
        # self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")

        self.label1 = Text(Point(150, 40), "Welcome to Dice Poker")
        self.label1.draw(win)
        self.label2 = Text(Point(150, 80), "Play poker using five dice.")
        self.label2.draw(win)
        self.label3 = Text(Point(150, 100), "Up to two re-rolls are allowed.")
        self.label3.draw(win)

        self.button_play = Button(win, Point(95, 200 - 40), 75, 35, "Let's Play")
        self.button_exit = Button(win, Point(207, 200 - 40), 75, 35, "Exit")
        self.button_play.activate()
        self.button_exit.activate()


    def get_response(self, win):
        while True:
            p = self.win.checkMouse()
            if p and self.button_play.clicked(p):
                self.button_play.label.undraw()
                self.button_play.deactivate()
                self.button_play.rect.undraw()
                self.button_exit.label.undraw()
                self.button_exit.deactivate()
                self.button_exit.rect.undraw()
                self.label1.undraw()
                self.label2.undraw()
                self.label3.undraw()
                return True
            if p and self.button_exit.clicked(p):
                self.win.close()
                return False
