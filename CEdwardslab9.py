# Lab 9 -- File: CEdwardslab9.py
# Clarissa Edwards 10/16/2023
# This program creates a new file and reads from it in a loop 
# and counts the numeric lines before closing the file
##############################################################

# STEP 1: open an input file named "input1.txt" 
inputFile = open("input1.txt", "r")
count = 0

# STEP 2: Add a loop to read each line of the file and print it to the screen
for line_str in inputFile:
    line_str = line_str.strip()
    if line_str.isnumeric() == True:
        count = count + 1 
    print(line_str)


print("\nThere were {} lines that contained numbers in this file".format(count))

# STEP 3: Close the file
inputFile.close()