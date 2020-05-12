#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    Management.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019

from Employee import Employee
from Parttime import Parttime
from Salary import Salary
from Hourly import Hourly


class Management:
    def __init__(self):
        self.empList = []

    def getEmpList(self):
        return self.empList

    def addEmp(self, emp):
        self.getEmpList().append(emp)

    def addEmpList(self, employees):
        for emp in employees:
            self.getEmpList().append(emp)

    def removeEmp(self, emp):
        self.getEmpList().remove(emp)

    # write management list to file
    def writeFile(self, filename):
        with open(filename, 'w') as file:
            for emp in self.getEmpList():
                file.write(emp.printInfo())
                file.write("\n")

    # read management file
    def readFile(self, filename):
        empList = []
        hasNextLine = True

        # while there are still employees in file
        while hasNextLine:
            with open(filename, 'r') as file:
                # get firstName, lastName, and empID
                empNameLine = file.readline()
                empNameList = empNameLine.split()
                firstName = empNameList[1]
                lastName = empNameList[2]
                idLine = empNameList[2]
                idList = idLine.split()
                empID = idList[1]
                # get type of employee (language lookahead)
                checkEmpClass = file.read()
                checkEmpClassList = checkEmpClass.split()
                empType = checkEmpClassList[0]
                # part-time employee
                if empType == "Number":
                    numClasses = checkEmpClassList[2]
                    parttime = Parttime(firstName, lastName, empID, numClasses)
                    empList.append(parttime)
                # salary employee
                elif empType == "Salary":
                    salary = checkEmpClassList[1]
                    salaryEmp = Salary(firstName, lastName, empID, salary)
                    empList.append(salaryEmp)
                # hourly employee
                elif empType == "Hours":
                    hours = checkEmpClassList[2]
                    hourlyRate = file.readline()
                    hourlyRateList = hourlyRate.split()
                    hoursRate = hourlyRateList[2]
                    hourly = Hourly(firstName, lastName, empID, hours, hoursRate)
                    empList.append(hourly)
        return empList