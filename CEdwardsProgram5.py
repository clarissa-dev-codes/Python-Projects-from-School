# Program 5 -- File: CEdwardsProgram5.py
# Clarissa Edwards 11/15/2023
# This program asks for test grades before presenting how many grades were  
# read in, the average, median, highest and lowest of the grades before
# giving a histogram of the grades given.
##############################################################

givenGrade = 0
grades_list = []
# list order [A, B, C, D, F]
letterGrades_list = [0,0,0,0,0]
count = 0
total = 0



while givenGrade != -1:
    givenGrade = int(input("Please enter a test grade (-1 to quit): "))
    if givenGrade != -1:
        grades_list.append(givenGrade)   
        #counter values list
        if givenGrade >= 90:
            num = letterGrades_list[0]
            num = num + 1
            letterGrades_list.insert(0, num)
        elif givenGrade >= 80:
            num = letterGrades_list[1]
            num = num + 1
            letterGrades_list.insert(1, num)
        elif givenGrade >= 70:
            num = letterGrades_list[2]
            num = num + 1
            letterGrades_list.insert(2, num)
        elif givenGrade >= 60:
            num = letterGrades_list[3]
            num = num + 1
            letterGrades_list.insert(3, num)
        elif givenGrade < 60:
            num = letterGrades_list[4]
            num = num + 1
            letterGrades_list.insert(4, num)
        
    else:
        continue
    
    
    #appends the grade to the end
    


grades_list.sort()   
            
#Calculate the average 
for num in grades_list:
    total = total + grades_list[count]
    count = count + 1
    

average = float(total / count)

length = count - 1

#Calculate the median
if count%2 == 1:
    spot = int(length / 2)
    median = float(grades_list[spot])
elif count%2 == 0:
    spot1 = int(length / 2)
    spot2 = spot1 + 1
    median = float((grades_list[spot1] + grades_list[spot2]) / 2)
    
    

#Calculate the Highest
highNum = float(grades_list[length])

#Calculate the lowest
lowNum = float(grades_list[0])


#print the results
print("\n{} grades were read in.".format(count))
print("Average: {:.2f}".format(average))
print("Median: {:.2f}".format(median))
print("Highest: {:.2f}".format(highNum))
print("Lowest: {:.2f}".format(lowNum))

#Print the histogram
print("\n\nHISTOGRAM")
print("A: {}".format('*'*letterGrades_list[0]))
print("B: {}".format('*'*letterGrades_list[1]))
print("C: {}".format('*'*letterGrades_list[2]))
print("D: {}".format('*'*letterGrades_list[3]))
print("F: {}".format('*'*letterGrades_list[4]))