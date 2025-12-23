# Lab 8 -- File: CEdwardslab8.py
# Clarissa Edwards 9/20/2023
# This program takes the string given by the user and computes the 
# GC Ratio test before displaying the answer
##############################################################


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



# Main program to test the calculation
dnaFragment = input("Enter the DNA sequence: ")

gcratio = computeGCRatio(dnaFragment) # to test your function

print("For the sequence:",dnaFragment)
print("The GC-Ratio is {:6.3f}".format(gcratio))
#I changed the format to 6.3 so that there would be three decimal places 
# printed instead of just two places after the decimal point