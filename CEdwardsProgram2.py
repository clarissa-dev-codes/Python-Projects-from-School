# Program 2 -- File: CEdwardsProgram2.py
# Clarissa Edwards 9/9/2023
# This program asks the user for their blood type before printing
# a statememt that tells the user what they should donate
# as well as a error print statement
##############################################################


print("Maximize your donation.")
# First things first, ask the user for their blood type
userBloodType_str = input("Enter the Donor's Blood Type: ")

#added this so that the user doesn't HAVE to use the Caps lock when entering blood types
userBloodType = userBloodType_str.upper()

# Go through the if-elif-else statement to pick the right statement
if (userBloodType == "O+" or userBloodType == "O-"):
    print("A donor with", userBloodType, "should donate Whole Blood or Double Red Cells")
elif (userBloodType == "A+" or userBloodType == "B+" or userBloodType == "AB+" or userBloodType == "AB-"):
    print("A donor with", userBloodType, "should donate Plasma or plateletes")
elif (userBloodType == "A-" or userBloodType == "B-"):
    print("A donor with", userBloodType, "should donate Double Red Cells or Platelets")
else:
    print("I do not recognize the blood type of ", userBloodType)
    
# Print goodbye statement afterwards.
print("Thank you. Goodbye")