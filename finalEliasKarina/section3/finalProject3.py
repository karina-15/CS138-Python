#! /usr/bin/python
#
# Final
# Project No.   03
# File Name:    finalProject3.py
# Programmer:   Karina Elias
# Date:         Dec. 14, 2019
#
# Problem Statement:
#   This program will create a new Mira Costa Employee Management
#   system. There are 3 types of employees: Part-time Faculty,
#   Salary (include full time Faculty), and Hourly. You need to
#   create a generic employee which holds the employees first
#   and last name, and their id. The part-time faculty member
#   is paid a set amount(say 1000 per class) for each class they
#   teach. The salary employee is paid a monthly salary and the
#   hourly employee is paid based on the number of hours work
#   multiplied by their hourly rate.
#   The management system should allow you to enter a new employee,
#   remove an existing employee, save the existing employee
#   database to a file, load an existing employee database file,
#   and calculate the monthly paychecks for each employee. You
#   should use inheritance and polymorphism which is discussed
#   on page 419 (digital version of the book my vary slightly).
#
#
# Overall Plan:
# 1. Print introduction
# 2. Create Employee parent class
# 3. Create Parttime, Salary, Hourly child class
# 4. Create Management class with list of employee objects
# 5. Create file with employees information
# 6. Display employees information
#
#
# import the necessary python libraries and classes
# for this program None are used
from finalEliasKarina.section3.Management import Management
from finalEliasKarina.section3.Parttime import Parttime
from finalEliasKarina.section3.Salary import Salary
from finalEliasKarina.section3.Hourly import Hourly


# print introduction
def printIntro():
    print("\nThis program will find the rank and number of a\n"
          "popular name.\n")


# ---MAIN---
def main():
    printIntro()

    empList = []
    # create employees
    parttime = Parttime("Anakin", "Skywalker", "001", 5)
    salary = Salary("Han", "Solo", "002", 4000)
    hourly = Hourly("Leia", "Organa", "003", 40, 15)
    # add employees to list
    empList.append(parttime)
    empList.append(salary)
    empList.append(hourly)
    # create management list
    mccManagement = Management()
    mccManagement.addEmpList(empList)
    # write management to file
    mccManagement.writeFile("mccEmployees.txt")
    # display employees to console
    for emp in mccManagement.getEmpList():
        print(emp.printInfo())


if __name__ == '__main__':
    main()
