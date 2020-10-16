# Course: DSC510
# Assignment: 5.1
# Date: 4/6/20
# Name: Laura Hoffmann
# Description: Program to demonstrate loops

# This first function, once called, will allow the user to perform an operation of their choosing

def performCalculation(operation):
    # inp1 = input("Input a number: ") moved to the main body loop
    # inp2 = input("Input a second number: ") moved to the main body loop
    # moving these inputs to the while loop gives the user more context for each of the options they chose
    if operation == "+":
        print(int(inp1) + int(inp2))
    elif operation == "-":
        print(int(inp1) - int(inp2))
    elif operation == "*":
        print(int(inp1) * int(inp2))
    elif operation == "/":
        print(int(inp1) / int(inp2))

# The second function, once called, will allow the user to decide how many and what numbers are in the set to be averaged
# Using the for loop allows the user to input as many numbers as they want

def calculateAverage():
    intList = []
    number = int(input("How many numbers do you wish to input to calculate an average?: "))
    for x in range(number):
        integer = input("Please input number: ")
        integer = int(integer)
        intList.append(integer)
    print("The average is: ", int(sum(intList))/int(len(intList)))

# Below I give the context with the choices of operators

print("Welcome to the calculator!")
print("For addition type: +")
print("For subtraction type: -")
print("For multiplication type: *")
print("For division type: /")
print("Type 'q' to quit.")

# Here I begin the main body while loop
# The first function will be called and executed based on their choice in operator

looping = True
while looping == True:
    operation = input("Please choose an operation from the list above: ")
    if operation == "+":
        looping = True
        inp1 = input("Input your first number to add: ")
        inp2 = input("Input the second number you want to add: ")
        performCalculation(operation)
    elif operation == "-":
        looping = True
        inp1 = input("Input your base number: ")
        inp2 = input("Input the number you want to subtract from you base number: ")
        performCalculation(operation)
    elif operation == "*":
        looping = True
        inp1 = input("Input the first number you want to multiply: ")
        inp2 = input("Input your second number to multiply: ")
        performCalculation(operation)
    elif operation == "/":
        looping = True
        inp1 = input("Input your base number: ")
        inp2 = input("Input the number you want to divide your base number by: ")
        performCalculation(operation)
    elif operation == "q":
        looping = False
        print("Now we will move on to averages.")
    else:
        looping = True
        print("We did not understand, please be sure to choose from the list.")

# I created an averageLoop here that allows the user to calculate as many averages as they want
# Here I run the second function that allows the user to put in whatever numbers they want to average
# I also used enough elif statements to allow the user to type yes or no four different ways

averageLoop = True
while averageLoop == True:
    avginp = input("Would you like to calculate an average, yes or no?\n")
    if avginp == "yes":
        averageLoop = True
        calculateAverage()
    elif avginp == "Yes":
        averageLoop = True
        calculateAverage()
    elif avginp == "y":
        averageLoop = True
        calculateAverage()
    elif avginp == "Y":
        averageLoop = True
        calculateAverage()
    elif avginp == "no":
        averageLoop = False
        print("Thank you for using our calculator!")
    elif avginp == "No":
        averageLoop = False
        print("Thank you for using our calculator!")
    elif avginp == "n":
        averageLoop = False
        print("Thank you for using our calculator!")
    elif avginp == "N":
        averageLoop = False
        print("Thank you for using our calculator!")
    else:
        averageLoop = True
        print("I'm sorry we did not understand.")

