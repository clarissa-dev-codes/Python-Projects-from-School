# Lab 6 -- File: lab6.py
# Clarissa Edwards 9/20/2023
# This program has two parts. The first part computers factorials from
# a value given by the user. The second part reads in numbers until the user
# enters a 0 and prints whether the number is even or odd
##############################################################


# Lab 6 Part 1
# This program computes factorials from a value given by the user

# Step 1: Prompt the user for the N and read it in and convert to int
userNum = input("Please enter a number to compute it's factorial: ")
fNum = int(userNum)

# Step 2: Initialize factorial to a default before multiplying values
counter = fNum

# Step 3: Complete the loop below to compute factorial

    #Step a: While N > ; what is the condition to keep going
        
    #Step b: multiply N x factorial and save it to variable
    
    #Step c: decrement N by 1
while counter > 1:
    fNum = fNum*(counter-1)
    counter = counter -1

    
# Step 4: Print out the resulting factorial value
print("The factorial of ", userNum, " is ", fNum)



# Lab 6 Part 2
# Reads in numbers until the user stops it with a 0 and will tell if the
# number is even or odd

number = int(input("Enter a number. I will tell you if it is odd or even: "))
flag = 1

#Step 1: condition that allows the loop to continue

#Step 2: print whether number is even or odd

#Step 3: prompt for the next number

while flag != 0:
    temp = number % 2
    if temp == 1:
        print("The number", number, "is odd.")
        number = int(input("Please enter another number, 0 to stop: "))
        if number == 0:
            break
        else:
            continue
    else:
        print("The number", number, "is even")
        number = int(input("Please enter another number, 0 to stop: "))
        if number == 0:
            break
        else:
            continue
     
        
print("\nYou entered 0. Goodbye")