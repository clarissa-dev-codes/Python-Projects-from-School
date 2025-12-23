# Lab 3 -- File: lab5.py
# Clarissa Edwards 9/6/2023
# This program computers a person's car insurance based on their age and
# the number of tickets they have recieved using the info from the table in
# the lab assignment
##############################################################


# Step 1: Prompt the user for the person's age, read it in, convert to number
age = int(input("Please enter the Customer's age: "))
# Combined the two lines from the assignment for less lines


# Step 2: Prompt the user for the person's number of tickets and read in
tickets = int(input("Please enter the number of tickets: "))


# Step 3: Compute the insurance cost based on the table
if age < 21:
    insuranceCost = 1500 + 250*tickets
elif age > 21 and age < 24:
    insuranceCost = 1200 + 250*tickets
elif age >= 25:
    insuranceCost = 1000 + 200*tickets

# Step 4: Print out the resulting insurance cost message
print("The insurance cost for the customer is: $", insuranceCost)