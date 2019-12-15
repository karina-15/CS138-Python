#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Hourly.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from finalEliasKarina.section3.Employee import Employee


class Hourly(Employee):
    def __init__(self, firstName, lastName, employeeID, hours, hourlyRate):
        Employee.__init__(self, firstName, lastName, employeeID)
        self.hours = hours
        self.hourlyRate = hourlyRate

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmployeeID(self):
        return self.employeeID

    def getHours(self):
        return self.hours

    def getHourlyRate(self):
        return self.hourlyRate

    def getPay(self):
        return self.hours * self.hourlyRate

    def printInfo(self):
        return str("Name: {0} {1}\tID: {2}\tHours: {3}\tHourly Rate: {4}\tPay:${5}".
                   format(self.getFirstName(),
                          self.getLastName(),
                          self.getEmployeeID(),
                          self.getHours(),
                          self.getHourlyRate(),
                          self.getPay()))

