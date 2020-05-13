#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Employee.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019


class Employee:
    def __init__(self, firstName, lastName, employeeID):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = int(employeeID) + 1
        self.employeeID = '00' + str(self.employeeID)

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmployeeID(self):
        # print(self.employeeID)
        # self.employeeID = int(self.employeeID) + 1
        # print(self.employeeID)
        # self.employeeID = '00' + str(self.employeeID)
        # print(self.employeeID)

        # self.employeeID = int(self.employeeID) + 1
        # self.employeeID = '00' + str(self.employeeID)

        return self.employeeID

    def printInfo(self):
        return str("{0} {1} {2}".
                   format(self.getFirstName().ljust(7),
                          self.getLastName().ljust(13),
                          self.getEmployeeID().ljust(9)))
