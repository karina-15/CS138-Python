# Homework 03 Extra Credit
> Calculate the epact number given 4-digit year

## Screenshot
![screenshot](hw3extraCredit.gif)

## Instructions
> The Gregorian epact is the number of days between January 1st and the  
> previous new moon.  This value is used to figure out the date of Easter.  
> It is calculated by these formulas (using int arithmetic):  
> 
> C = year // 100  
> epact = (8+(C//4) - C + ((8C + 13)//25) + 11(year%19))%30  
> 
> Write a program that prompts the user for a 4-digit year and then outputs  
> the value of the epact. 
> (#8, pg. 77)