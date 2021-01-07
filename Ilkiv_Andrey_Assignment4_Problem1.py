#Andrey Ilkiv Assignment 4 problem 1 section 01 10/12/2020

#variables
exitval = False
weight = 0
count = 0

#loop min = 1 loop max = 999
#asks to input weight for each consecutive day
#if user enters -1 then program ends and prints out results
print("Enter weight for each day, once you finished type -1 to end program and calculate")
for x in range(1, 999):
    #while exitval is not true
    if(exitval != True):
        #convert day to string
        day = str(x)
        #input weight
        enteredvalue = float(input("Enter your weight on day " + day + ": "))
        #checks if exit value is true or false for each input
        exitval = enteredvalue == -1
        #if user input = -1 finish program
        #else add to count and tota weight over x days
        #weight on last day entered
        if(enteredvalue != -1):
            count = count + 1
            weight = enteredvalue + weight
            finishedweight = enteredvalue
        else:
            day = str(x - 1)
    if(x == 1):
        startweight = enteredvalue
#calculates avg weight over x days and weight lost since the first day to the last
AvgWeight = format((weight/count), '.2f')
weightlost = format((startweight - finishedweight), '.2f')
#prints results
print('' , "Average Weight Over " + day + " Days: " + str(AvgWeight) , sep='\n')
print("Total Wight Loss Over " + day + " Days: " + str(weightlost))

