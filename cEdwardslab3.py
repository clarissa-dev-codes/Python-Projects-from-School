# Lab 3 -- File: lab3.py
# Clarissa Edwards 8/26/2023
# This program prompts the user for a temperature
# Fahrenheit and prints the equivalent Celsius value
##############################################################

tempF_str = input ('Enter the temperature in Fahrenheit: ')
tempF = float(tempF_str)


#Step 3 - Write arithmetic statement to compute Celsius
tempx = tempF - 32
tempC = float(5/9 * tempx)

#Step 4 - Print the Celsius tempertaure to the screen
print (tempF,'degrees F is equivalent to ', tempC, 'degrees C')


