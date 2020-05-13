# Final Project 2
> Find rank and number of popular names using dictionary

## Screenshot
![screenshot](finalSection2.png)

## Instructions
> Two textfiles exist on canvas called [boynames.txt](boynames.txt) and [girlnames.txt](girlnames.txt).  
> They contain a list of the 1000 most popular boy and girl names in the  
> United States for the year 2003 as compiled by the Social Security Administration.  
> 
> These are blank-delimited files where the most popular name is listed first,  
> the second most popular second, and so on to the 1000th most popular name which  
> is listed last.  Each line consists of the first name followed by a blank space  
> and then the number of registered births using that name in the year.  
> For example the girlnames.txt file begins with:  
> 
> Emily 25494  
> Emma 22532  
> Madison 19986  
> 
> This indicate that Emily was the most popular name with 25494 registered  
> namings, Emma was the second most popular with 22532, and Madison was the  
> third most popular with 19986.  
> 
> Write a program that reads both the girl’s and boy’s files into memory using  
> a dictionary.  The key should be the name and value should be a user defined  
> object which is the count and rank of the name.  Allow the user to input a  
> name, the program should find the name in the dictionary and print out the  
> rank and the number of namings.  If the name isn’t a key in the dictionary  
> then the program should note this and say that no match exists.  
> 
> If the user enters the name “Walter”, then the program should output:  
> 
> Walter is not ranked among the top 1000 girl names.  
> Walter is ranked 356 in popularity among boys with 775 namings.