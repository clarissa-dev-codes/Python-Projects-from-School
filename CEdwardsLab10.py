# Lab 10 -- File: CEdwardsLab10.py
# Clarissa Edwards 11/6/2023
# This lab is to get a better understanding of how to work with lists
# that contain numeric data (numbers)
#  
##############################################################

#Lab 10 part 1

my_list = [7, 9, 11, 0, 1, 3, 4, 99]

#where the bread and butter goes for parts a-d

print(my_list[6], '\n')
my_list.insert(1, 3)
my_list.append(-1)


count = 0
for num in my_list:
    print(my_list[count])
    count = count + 1


#Lab 10 part 2

aList = [9, 10 , -1, 0, -3, 19, 24, 72, -98, 11, 24, 1, 1, 1, 15]
countPositive = 0

#meat and potatoes of part 2
#step 1, the loop that steps through the array of numbers to test for 
#positive and negative numbers

for num in aList:
    if num > 0:
        countPositive = countPositive + 1


#step 2: printing out how many positive numbers there are
print("\n\nThere were {} non-negative numbers in the list".format(countPositive))
