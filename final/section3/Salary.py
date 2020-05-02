#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Salary.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from finalEliasKarina.section3.Employee import Employee

class Salary(Employee):
    def __init__(self, firstName, lastName, employeeID, salary):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.salary = salary

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmployeeID(self):
        return self.employeeID

    def getSalary(self):
        return self.salary

    def getPay(self):
        return self.salary

    def printInfo(self):
        return str("Name: {0} {1}\tID: {2}\tSalary: {3}\tPay:${4}".
                   format(self.getFirstName(),
                          self.getLastName(),
                          self.getEmployeeID(),
                          self.getSalary(),
                          self.getPay()))
