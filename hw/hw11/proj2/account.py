#! /usr/bin/python
#
# Homework No.  11
# Project No.   02
# File Name:    account.py
# Programmer:   Karina Elias
# Date:         Dec. 11, 2019

# create account objects
class Account:
    def __init__(self, id, pin, checking, savings):
        self.id = id
        self.pin = pin
        self.checking = checking
        self.savings = savings

    # getters
    def get_id(self):
        return self.id

    def get_pin(self):
        return self.pin

    def get_checking(self):
        return self.checking

    def get_savings(self):
        return self.savings

    # withdraw from checking or savings
    def withdraw(self, amount, acct_type):
        # withdraw from checking
        if acct_type == 1:
            if self.checking < amount:
                return False
            else:
                self.checking -= amount
        # withdraw from savings
        elif acct_type == 2:
            if self.savings < amount:
                return False
            else:
                self.savings -= amount
        return True

    # transfer into checking or savings
    def transfer(self, amount, acct_type):
        if acct_type == 1:
            self.savings += amount
        elif acct_type == 2:
            self.checking += amount
