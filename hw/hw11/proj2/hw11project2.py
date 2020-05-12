#! /usr/bin/python
#
# Homework No.  11
# Project No.   02
# File Name:    hw11project2.py
# Programmer:   Karina Elias
# Date:         Dec. 11, 2019
#
# Problem Statement: Programming Exercise #4 p.424
#   Write a program that simulates an Automatic Teller Machine
#   (ATM). Since you probably don't have access to a card reader,
#   have the initial screen ask for user id and a PIN. The user
#   is will be user to look up the info for the user's accounts
#   (including the PIN to see if it matches what the user types).
#   Each user will have access to a checking account and a savings
#   account. The user should be able to check balances, withdraw
#   cash, and transfer money between accounts. Design your interface
#   to be similar to what you see on your local ATM. The user
#   account information should be stored in a file when the
#   program terminates. This file will read in again when the
#   program restarts.
#
#
# Overall Plan:
# 1. Create Account class
# 2. Create list containing each accounts information
# 3. Read from accounts.txt file to create list
# 4. Prompt user for ID and PIN
# 5. If both user ID and PIN are valid display menu options
# 6. Get user choice to display balance, withdraw, or transfer
# 7. Continue to menu until user exits program
#
#
# import the necessary python libraries and classes
# for this program account is used
from hw11.hw11project2.account import *

def main():
    # initialize list to hold account info
    acct_list = []
    # open accounts.txt and add each to list
    with open("accounts.txt") as file:
        for line in file:
            num = line.split(' ')
            # num[0] = id, num[1] = pin,
            # num[2] = checking balance, num[3] = savings balance
            acct_list.append(Account(num[0],
                                     num[1],
                                     float(num[2]),
                                     float(num[3].replace('\n', ''))))
    # ask user for ID and PIN
    id = input("\nEnter ID: ")
    pin = input("Enter PIN: ")
    # goes through each account in list
    for acct in acct_list:
        # validates ID is in list
        if acct.get_id() == id:
            # validates PIN
            if acct.get_pin() == pin:
                choice = -1
                # display menu until user exits
                while choice != 0:
                    print("\n---Menu---\n"
                          "1. Check Balance\n"
                          "2. Withdraw\n"
                          "3. Transfer\n"
                          "0. Exit\n")
                    choice = eval(input("Choose from Menu (1-3): "))
                    # choose which account to check balance
                    if choice == 1:
                        print("---Check Balance---\n"
                              "1. Checking\n"
                              "2. Savings\n")
                        acct_type = eval(input("Choose an account (1-2): "))
                        if acct_type == 1:
                            print("Checking Balance: ", acct.get_checking())
                        else:
                            print("Savings Balance: ", acct.get_savings())
                    # choose which account to withdraw from
                    elif choice == 2:
                        print("---Withdraw---\n"
                              "1. Checking\n"
                              "2. Savings\n")
                        acct_type = eval(input("Choose an account (1-2): "))
                        amount = eval(input("Enter amount: "))
                        if acct.withdraw(amount, acct_type):
                            if acct_type == 1:
                                print("New Checking Balance: ", acct.get_checking())
                            else:
                                print("New Savings Balance: ", acct.get_savings())
                        else:
                            print("Insufficient funds.")
                    # choose which account to transfer to/from
                    elif choice == 3:
                        print("---Transfer---\n"
                              "1. From Checking to Savings\n"
                              "2. From Savings to Checking\n")
                        option = eval(input("Choose an option (1-2): "))
                        amount = eval(input("Enter amount:"))
                        if option == 1:
                            acct.withdraw(amount, option)
                            acct.transfer(amount, option)
                            print("New Checking Balance: ", acct.get_checking())
                            print("New Savings Balance: ", acct.get_savings())
                        else:
                            acct.withdraw(amount, option)
                            acct.transfer(amount, option)
                            print("New Savings Balance: ", acct.get_savings())
                            print("New Checking Balance: ", acct.get_checking())
                    # exit program
                    elif choice == 0:
                        break
                    else:
                        print("Invalid choice.")
            # pin does not match
            else:
                continue
        # id does not match current list account
        # check next account in list
        else:
            continue

    # save/write changes made to accounts.txt
    file = open("accounts.txt", 'w')
    for acct in acct_list:
        # checking and savings balance must be string
        file.write(acct.get_id() + ' ' +
                   acct.get_pin() + ' ' +
                   str(acct.get_checking()) + ' ' +
                   str(acct.get_savings()) + "\n")
    file.close()
    print("Goodbye")


if __name__ == '__main__':
    main()
