#! /usr/bin/python
#
# userfile.py - pg.157
#   Program to create a file of usernames in batch mode.


def main():
    print("This program creates a file of usernames from a"
          "\nfile of names.")

    # get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the usernames go in? ")

    # open the files
    # multiple files can be opened & worked on at the same time
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the 1st & last names from line
        first, last = line.split()
        # create the username
        uname = (first[0] + last[:7].lower())   # uname is all lowercase
        # write it to the output file
        print(uname, file=outfile)  # doesn't need '\n' b/c at ea. print 1 is created

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)


main()
