#! /usr/bin/python
# Homework No.  04
# Project No.   02
# File Name:    hw4project2.py
# Programmer:   Karina Elias
# Date:         Sep. 13, 2019
#
# Problem Statement:
# Write a program that creates a simple GUI for
# MyFirstProgram.py which calculates the percentage
# and sum of two numbers. GUI includes inputs of
# numbers and output of answers.
#
#
# Overall Plan:
# 1. Create graphics window
# 2. Print introduction
# 3. Prompt user for 1 number using Entry box
# 4. Prompt user for a 2nd number using Entry box
# 5. Create a Calculate button with Rectangle method
# 6. Display percentage w/ empty values
# 7. Display sum w/ empty values
# 8. Calculate percentage
# 9. Calculate sum
# 10. Change setText for percentage, sum, and button
#     after window is clicked
# 11. Click to close window
#
#
# import the necessary python libraries
# import everything defined in graphics.py
from graphics import *


def main():
    # Create graphics window
    win = GraphWin("MyFirstProgram.py GUI", 450, 300)
    win.setCoords(0.0, 0.0, 2.0, 6.0)  # 2 columns, 6 rows

    # Print introduction
    Text(Point(1, 5.75), "Hello!").draw(win)
    Text(Point(1, 5.25), "I can add two numbers for you").draw(win)

    # ---Window Layout--- #

    # Prompt user for 1st number using Entry text box
    Text(Point(0.6, 4.5), "Enter 1 whole number:").draw(win)
    num1_box = Entry(Point(1.5, 4.5), 15)
    num1_box.draw(win)

    # Prompt user for 2nd number using Entry text box
    Text(Point(0.5, 4), "Enter another whole number:").draw(win)
    num2_box = Entry(Point(1.5, 4), 15)
    num2_box.draw(win)

    # Create a Calculate rectangle button
    # Button does not work
    # User can click anywhere in window (except Entry input boxes)
    # to change button text
    Rectangle(Point(0.75, 2.75), Point(1.25, 3.25)).draw(win)
    button = Text(Point(1, 3), "Calculate")
    button.draw(win)

    # Display percentage label with empty output
    Text(Point(0.76, 2), "Percentage = ").draw(win)
    percent_output = Text(Point(1.5, 2), "")
    percent_output.draw(win)

    # Display sum label with empty output
    Text(Point(0.5, 1.5), "The sum of the two numbers is").draw(win)
    sum_output = Text(Point(1.5, 1.5), "")
    sum_output.draw(win)

    # ---Input--- #
    click_button = win.getMouse()  # User clicks inside window/Calculate button

    # Attempted to use while loop for button click
    # while 0.75 <= click_button.getX() <= 1.25 and 2.75 <= click_button.getY() <= 3.25:
    num1 = eval(num1_box.getText())  # Get num1 from Entry num1_box
    num2 = eval(num2_box.getText())  # Get num2 from Entry num2_box

    # ---Process--- #
    percentage = (float(num1) / float(num2)) * 100
    sum_2_numbers = num1 + num2

    # ---Output--- #
    percent_output.setText(percentage)  # Display calculated percentage
    sum_output.setText(sum_2_numbers)  # Display calculated sum
    button.setText("Close window")  # Change button text

    win.getMouse()  # pause for 2nd click in window
    win.close()  # closes window


main()
