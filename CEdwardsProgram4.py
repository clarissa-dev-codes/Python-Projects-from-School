# Program 4 -- File: CEdwardsProgram4.py
# Clarissa Edwards 10/27/2023
# This program  will read in each fragment of DNA from a file and keep up with
# how many fragments there are in the file. As will as reporting results
# from the GCRatio Test that is tested on each DNA fragment. 
##############################################################

#def for the GCRatio test (taken from Lab 8)
def computeGCRatio(dnaString):
    """ Takes a tally of every single character in the string provided and 
        then computes the GC ratio provided in the lab instructions """
    numA = 0
    numT = 0
    numG = 0
    numC = 0
    
    #for loop to go through every single character in the string
    for char in dnaString:
        if char == "A":
            numA = numA + 1
        elif char == 'T':
            numT = numT + 1 
        elif char == 'G':
            numG = numG + 1 
        elif char == 'C':
            numC = numC + 1 
    gCRatio = (numG + numC)/(numA + numT + numG + numC)
    return(gCRatio)

def computeDNARange(ratioNum):
    """Takes the ratio found in the GCRatio and calculates if the fragment is
    within the range 35% to 65% """
    if ratioNum >= 0.35 and ratioNum <= 0.65:
        dnaRan = True
    else:
        dnaRan = False
    
    
    return(dnaRan)

###############################################################################
#Line is to split the main code from the functions.

#print welcome message on console
print("Welcome to the DNA profiler.")
print("This program will read a set of DNA fragments from an input data file.")
print("It will produce a report on the GC-ratios found in the file.")

#Ask for the input file name and call open function
inStrName = input("\nPlease enter the name of the input data file: ")
in_File = open(inStrName, "r")

#Ask for the ouput file name amd call open function
outStrName = input("\nPlease enter the name of the output data file: ")
out_File = open(outStrName, "w")

#variables that I need later
lineCount = 0
largestLine = 0
linesToShort = 0

#prints the first part of the stuff shown in the assignment doc
print("REPORT ON INPUT FILE: ", inStrName, file=out_File)

print("\n"+" "*15+"Fragment "+" "*33+"GCRatio"+"    "+"Other messages"+" "*29, file=out_File)
print("-"*110, file=out_File) #makes the single line of dashes at the top
#Take info from file and tests to see if fragment is more than 30 chars
#Use a for loop to call GC def if it is long enough
for line_str in in_File:
    line_str = line_str.strip()
    line_str = line_str.upper()
    length = len(line_str)
    if length >= 30:
        ratio = computeGCRatio(line_str)
        dnaRange = computeDNARange(ratio)
        if dnaRange == True:
            print(line_str.ljust(54)+" :   {:.2f}  Fragment within the range 35% - 65%".format(ratio), file=out_File)
        else:
            print(line_str.ljust(54)+" :   {:.2f}".format(ratio), file=out_File)
    else:
        linesToShort = linesToShort + 1
        print(line_str.ljust(54)+" :   Fragment is too short to process", file=out_File)
    lineCount = lineCount + 1 
    if length > largestLine:
        largestLine = length
    

print("-"*51 + "Summary" + "-"*52,file=out_File)
#need the variables at the end of each statement once they are made (10/22)
print("There were {} fragments found.".format(lineCount), file=out_File)
print("{} fragment was/were not long enough to process.".format(linesToShort), file=out_File)
print("The longest fragment found had {} values.".format(largestLine), file=out_File)

#close input file
in_File.close()

#close output file
out_File.close()

#prints the information on the console as shown in the assignment page
print("Report Complete - stored in file: {}".format(outStrName))
print("Exiting Program 4")